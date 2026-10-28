
"""(a). Compute hours, minutes and seconds, then print the sentence shown below."""
def transform_seconds(total_second):
    total_hour=total_second//3600
    hold=total_second%3600
    total_minute=hold//60
    total_second=hold%60
    return total_hour, total_minute, total_second
total_second=9875
total_hour, total_minute, total_second = transform_seconds(total_second)
print(f"{total_second} = {total_hour} hours {total_minute} minutes {total_second} seconds")


"""(b). Check your answer: rebuild the total from the three parts and print whether it equals."""
check=total_hour*3600+total_minute*60+total_second
if check==9875:
    print("The calculation is correct.")
else:
    print("The calculation is incorrect.")
    
    
"""(c). Test your code with 3600, 59 and 86399 seconds."""
for test_seconds in [3600, 59, 86399]:
    total_hour, total_minute, total_second = transform_seconds(test_seconds)
    print(f"{test_seconds} seconds = {total_hour} hours {total_minute} minutes {total_second} seconds")
  
