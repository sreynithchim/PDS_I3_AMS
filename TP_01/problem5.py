def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


"""(a) Test your function with the list [99, 90, 85.5, 72, 60, 59.9, -5, 101] and print the results
aligned as below."""
print(letter_grade(99))
print(letter_grade(90))
print(letter_grade(85.5))
print(letter_grade(72))
print(letter_grade(60))
print(letter_grade(59.9))
print(letter_grade(-5))
print(letter_grade(101))

"""(b) Why must the test for A+ come before the test for A? What happens if you swap them?"""
""" If i swap the test A+ come before the test for A , Grade would never hit A+ beacuse 99 greater than 90 already 
so even the student got hight score will never get A+
"""