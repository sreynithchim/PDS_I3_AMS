import pandas as pd
from pathlib import Path
import pandas as pd
DATA = Path(__file__).parent

df = pd.read_csv(DATA/ "students.csv")
out_dir = DATA /"output"
out_dir.mkdir(exist_ok=True)

df.to_csv(out_dir / "students_copy.csv", index=False)
back = pd.read_csv(out_dir / "students_copy.csv")
print("CSV identical  :", back.equals(df))


by_major = df.groupby("major")["gpa"].mean().round(2)
with pd.ExcelWriter(out_dir / "students.xlsx") as writer:
    df.to_excel(writer, sheet_name="all", index=False)
    by_major.to_excel(writer, sheet_name="by_major")
sheets = pd.read_excel(out_dir / "students.xlsx", sheet_name=None)
print("Sheets         :", list(sheets))
print("Excel identical:", sheets["all"].equals(df))

# Step 4
honours = df[df["gpa"] >= 3.7]
honours.to_json(out_dir / "honours.json", orient="records", indent=2)
print("From JSON:", pd.read_json(out_dir / "honours.json")["name"].tolist())

# Step 5
df.to_csv(out_dir / "with_index.csv")
print(pd.read_csv(out_dir / "with_index.csv").columns.tolist()[:3])