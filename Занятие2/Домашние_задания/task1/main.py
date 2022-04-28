i = int(input("Введи знаменатель прогрессии"))
def gp():
    b =  1
    while True:
        b = b *i
        yield b

gp_gen = gp()
# print(next(gp_gen))
# print(next(gp_gen))
# print(next(gp_gen))
# print(next(gp_gen))
for num in gp_gen:
    print(num)
    if num > 10000:
        break