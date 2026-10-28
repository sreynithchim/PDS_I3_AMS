"""Without converting numbers to strings, write three functions that work digit by digit with a while
loop:"""
def digit_sum(n):
    total=0
    while(n>0):
        total+=n%10
        n//=10
    return total
    
def reverse_number(n):
    reversed_num=0
    while(n>0):
        reversed_num=reversed_num*10+n%10
        n//=10
    return reversed_num
    
def is_palindrome(n):
    return n==reverse_number(n)

"""(a) Test the three functions with 2026, 12321 and 9875"""
for number in (2026, 12321, 98789):
    print("Number:", number)
    print("Digit Sum:", digit_sum(number))
    print("Reversed Number:", reverse_number(number))
    print("Is Palindrome:", is_palindrome(number))
    print("-----------------------------")
    
"""(b) Count how many palindromes there are from 10 to 999."""
count=0
for number in range(10,1000):
    if is_palindrome(number):
        count+=1
print("Total Palindrome numbers between 10 and 1000:", count)

