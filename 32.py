try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ValueError as a:
    print(a)
    print('Enter only number')

except ZeroDivisionError as a:
    print(a)
    print("you can't divide by zero")

except Exception as a:
    print(a)
    print('somthing went wrong')

else:
    print(result)

finally:
    print('Happy')