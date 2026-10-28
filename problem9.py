
"""(a) Write electricity_bill(kwh) that returns the bill in riel, rounded to a whole number, or None
for negative input."""
service_free=100
vat=0.10
RIEL_PER_USD = 4100

def electricity_bill(kwh):
    if kwh<0:
        return None
    tier1 = min(kwh, 50)                  # first 50 kWh
    tier2 = min(max(kwh - 50, 0), 150)    # next 150 kWh
    tier3 = max(kwh - 200, 0)
    energy_cost = tier1 * 480 + tier2 * 610 + tier3 * 730
    total = (energy_cost + service_free) * (1 + vat)
    return round(total)

"""(b) Print a table for 0, 35, 50, 120, 200 and 350 kWh, with thousands separators (f"{bill:,}") and
the value in USD (1 USD = 4,100 riel)."""
for kwh in (0, 35, 50, 120, 200, 350):
    bill = electricity_bill(kwh)
    usd = bill / RIEL_PER_USD
    print(f"{kwh:>3} kWh -> {bill:>9,} riel (≈ {usd:>6.2f} USD)")
    
    
"""(c) Ask the user for their monthly consumption and print their bill."""
kwh = float(input("Enter your monthly consumption (kWh): "))
bill = electricity_bill(kwh)
if bill is None:
    print("Invalid Value")
else:
    print(f"Your bill is {bill:,} riel (≈ {bill / RIEL_PER_USD:.2f} USD)")
    
    