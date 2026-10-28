"""(a) Write is_leap(year) that returns True or False using one boolean expression with and / or."""
def is_leap(year):
    return (year%4==0 and year%100!=0) or (year%400==0)


"""(b) Write days_in_month(month, year) that returns 28, 29, 30 or 31, or None if the month is not
between 1 and 12. Use in to test the 30-day months (4, 6, 9, 11)."""
def day_in_month(month,year):
    if month<1 or month>12:
        return None
    if month==2:
        return 29 if is_leap(year) else 28
    if month in [4,6,9,11]:
        return 30
    return 31


"""(c) Print whether 1900, 2000, 2024 and 2026 are leap years."""
for y in[1900,2000,2024,2026]:
    print(y,"leap" if is_leap(y) else "not_leap")

print("Feb 2024:", day_in_month(2, 2024), "|",
      "Feb 2026:", day_in_month(2, 2026), "|",
      "Apr:", day_in_month(4, 2026), "|",
      "month 13:", day_in_month(13, 2026))
    
    
"""(d) Count the leap years from 2000 to 2100 (both included) with a loop."""
count=0
for y in range(2000,2101):
    if is_leap(y):
        count+=1
print("Leap years from 2000 to 2100 is ",count)


