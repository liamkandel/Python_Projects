def fib():
    count = 0
    n1, n2, = 0,1

    while True:
        num_of_terms = int(input("How many terms would you like to generate? "))
        if num_of_terms > 1:
            break

    while count < num_of_terms:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1
    print("Fibonacci sequence completed")
fib()



