# import math
# a = math.floor(78.34)
# print(a % 3 == 0)
# a = input().split('.')
# print(int(a[1]) >= 50)
# a = float(input())
# print( 0 <= a <= 2 or  10 <= a <= 20)
# f ="panda"
# print(f[:4])
# a, b =input().split()
# print(a[1:len(b):2] == b[1::2])
# print(a[1:len(b):2], b[1::2])
# a = [input(),input(), int(input()), float(input())]
#
# del a[2]
# print(a)
#
# help(sorted)
#a,b,c = map(int,input().split())

#print(['НЕТ','ДА'][c**2 == a**2 + b**2])
#st =list(input().split())
#if 'Москва' in lst:
 #   lst.d
 #   print(*lst)
# a= int(input())
# gen = (abs(x) for x in range(-a, a + 1))
# gen1 =((x**3) for x in gen)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

# from string import ascii_lowercase
# gen =(i+j for i in ascii_lowercase for j in ascii_lowercase)
# for i in range(51):
#     print(next(gen), end=' ')
# a, b = map(int,input().split())
#
# gen = (0.5 * pow(i/100,2) - 2 for i in range(a*100,b*100))
# for i in range(20):
#     print(round(next(gen), 2), end = ' ')

N = int(input())

# здесь продолжайте программу
def get_sum():
    for n in range(N+1):
        sum = N +2
        yield sum
        sum +=1
a = get_sum()
for x in a:
    print((x))