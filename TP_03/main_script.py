from pathlib import Path
import sales_utils as su

DATA = Path(__file__).parent        # folder that holds sales.csv

sales = su.load_sales(DATA / "sales.csv")
print(sales)
print(su.total_by_product(sales))
print("Best seller:", su.best_seller(sales))