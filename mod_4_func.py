# def hello(name):
#     print(f'Hello {name}!')
#
# hello('Vasya')
# def hello():
#     print('hello')
#
# hello()

# def multiplier(num_n,num_a):
#     if num_n % num_a == 0:
#         print(f'{num_a} делитель {num_n}')
#     else:
#         print('пошол в жопу')
#
# multiplier(1332,5)
#
# def stairway(num):
#     # while num !=0: --- мое решение
#     #     num = num - 1
#     for i in range(num, 0, -1):  ---сф решение
#         print('*' * i)
#
# stairway(4)

# def quant_mult(num):
#     c = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             c += 1
#     return c
#
# print(quant_mult(10000))

# def check_p(text):
#     if text[::] == text[::-1]:
#         print (f'{text} палиндром')
#     else:
#         print('fuck off')
#
# check_p('хуййух')
#
# def mult(*nums):
#     res = 1
#     for n in nums:
#         res *= n
#     return res
#
# print(mult(1,0,5,6))
#
# def summa(n):
#     if n == 1:
#         return 1
#     return n + (summa(n-1))
#
# print(summa(900))
#
# def turnover(n):
#     if len(n) == 0:
#         return ""
#     return n[-1] + (turnover(n[:-1]))
#
# print(turnover('n'))
# a = 'string'
# print(a[-1] +" " + a[:-1])

# def sumfun(num):
#     if num < 10:
#         return num
#     else:
#         return num % 10 + sumfun(num//10)
#
# def fib():
#     a, b = 0, 1
#     yield a
#     yield b
#
#     while True:
#         a, b = b, a + b
#         yield b
#
# for num in fib():
#    print(num)

# def seq(start = 1, step = 1):
#
#     sequence = start
#     while True:
#         yield sequence
#         sequence = sequence + step
#
# for num in seq(1,1):

#     print(num)


# def infinit(lst):
#
#     while lst:
#         for i in lst:
#             yield i
#
# a = [1, 2, 3]
#
# for num in infinit(a):
#     print(num)

# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

# import time
#
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921
#
# in_build_pow()
# # Запустилась функция <function in_build_pow at 0x7f938401b620>
# # Функция выполнилась. Время: 0.0000021458

for i in range(-1, 10, -1):
    print(i)