num = 1
while num <=1000:
        if num % 15 == 0:
            print("Fizzbuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num = num + 1
