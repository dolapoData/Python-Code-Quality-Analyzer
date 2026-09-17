def calculate(x, y):
    result = x * y
    print("The result is", result)
    return result

def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

price = 500
quantity = 3
calculate(price, quantity)
check_age(20)
