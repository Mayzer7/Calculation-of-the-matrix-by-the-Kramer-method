# Расчет матрицы методомом Крамера
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']        # Расширенная матрица
columns = 3

x1 = int(input("Введите значение x1 для первой строки = "))
x2 = int(input("Введите значение x2 для первой строки = "))
x3 = int(input("Введите значение x3 для первой строки = "))
x4 = int(input("Введите значение x1 для второй строки = "))
x5 = int(input("Введите значение x2 для второй строки = "))
x6 = int(input("Введите значение x3 для второй строки = "))
x7 = int(input("Введите значение x1 для третьей строки = "))
x8 = int(input("Введите значение x2 для третьей строки = "))
x9 = int(input("Введите значение x3 для третьей строки = "))

my_list[0] = x1
my_list[1] = x2
my_list[2] = x3
my_list[3] = x4
my_list[4] = x5
my_list[5] = x6
my_list[6] = x7
my_list[7] = x8
my_list[8] = x9


for first, second, third in zip(
    my_list[::columns], my_list[1::columns], my_list[2::columns]
):
    print(f'{first: <5}{second: <5}{third}')

definerMain = x1 * x5 * x9 + x4 * x8 * x3 + x2 * x6 * x7 - x7 * x5 * x3 - x2 * x4 * x9 - x8 * x6 * x1   # Определитель матрицы
print ("Определитель матрицы = ", definerMain)

x10 = int(input("Введите значение чему равно 1 уравнение = "))
x11 = int(input("Введите значение чему равно 2 уравнение = "))
x12 = int(input("Введите значение чему равно 3 уравнение = "))

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']          # Определитель x1 
columns = 3

my_list[0] = x10
my_list[1] = x2
my_list[2] = x3
my_list[3] = x11
my_list[4] = x5
my_list[5] = x6
my_list[6] = x12
my_list[7] = x8
my_list[8] = x9


for first, second, third in zip(
    my_list[::columns], my_list[1::columns], my_list[2::columns]
):
    print(f'{first: <5}{second: <5}{third}')

definerx1 = x10 * x5 * x9 + x11 * x8 * x3 + x2 * x6 * x12 - x12 * x5 * x3 - x8 * x6 * x10 - x11 * x2 * x9
print ("Определитель матрицы x1 =", definerx1)



my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']          # Определитель x2 
columns = 3

my_list[0] = x1
my_list[1] = x10
my_list[2] = x3
my_list[3] = x4
my_list[4] = x11
my_list[5] = x6
my_list[6] = x7
my_list[7] = x12
my_list[8] = x9


for first, second, third in zip(
    my_list[::columns], my_list[1::columns], my_list[2::columns]
):
    print(f'{first: <5}{second: <5}{third}')

definerx2 = x1 * x11 * x9 + x4 * x12 * x3 + x10 * x6 * x7 - x7 * x11 * x3 - x10 * x4 * x9 - x12 * x6 * x1
print ("Определитель матрицы x2 =", definerx2)



my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']          # Определитель x3
columns = 3

my_list[0] = x1
my_list[1] = x2
my_list[2] = x10
my_list[3] = x4
my_list[4] = x5
my_list[5] = x11
my_list[6] = x7
my_list[7] = x8
my_list[8] = x12


for first, second, third in zip(
    my_list[::columns], my_list[1::columns], my_list[2::columns]
):
    print(f'{first: <5}{second: <5}{third}')

definerx3 = x1 * x5 * x12 + x4 * x8 * x10 + x2 * x11 * x7 - x7 * x5 * x10 - x8 * x11 * x1 - x4 * x2 * x12
print ("Определитель матрицы x3 =", definerx3)

mainx1 = definerx1 // definerMain
mainx2 = definerx2 // definerMain
mainx3 = definerx3 // definerMain
print("x1 = ", mainx1)
print("x2 = ", mainx2)
print("x3 = ", mainx3)