arr = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
ins = []

for i in range(1, len(arr)):
    if arr[i] - arr[i-1] > 1:
        ins.append(i)

if len(ins) == 0:
    print("Не найдено")
elif len(ins) == 1:
    print(ins[0])
else:
    print(ins)