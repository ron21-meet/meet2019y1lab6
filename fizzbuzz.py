def fizzbuzz(n):
    lst = []
      for i in range(1,n):
          if i % 3 == 0:
          lst.append("Fizz")
        elif i % 5 == 0:
          lst.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
          lst.append("FizzBuzz")
        else:
          lst.append(n)
    print(lst)


fizzbuzz(50)

