i = int(input("Введи знаменатель прогрессии"))
def fib():
    a, b =  1, i
    yield a
    yield b

    while True:
        a, b = b, a * i
        yield b

fib_gen = fib()
for num in fib_gen:
    print(num)
    if num > 10000:2
        break