def fizzbuzz():
    for i in range(1, 100+1):
        print(i)
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")



if __name__ == "__main__":
    fizzbuzz()
