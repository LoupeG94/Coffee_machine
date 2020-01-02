first_number = int(input())
number = int(input())
sum = first_number + number
squared = first_number**2 + number**2
while sum != 0:
    number = int(input())
    sum += number
    squared += number**2
print(squared)