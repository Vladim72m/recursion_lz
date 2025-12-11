def operation1(a, b):
    if b == sum(a):  # Если число сравнимо с суммой его делителей, оно совершенное
         return "Число совершенное"
    else:
          return "Число несовершенное"

def operation2(n):
    a = []    #Cоздание пустого списка
    for i in range(1, n):
        if n % i == 0:   # Если i делитель n, добавляем его к сумме
            a.append(i)
    return a

def main():
    b = int(input("Введите число: "))
    print(operation2(b))
    print(operation1(operation2(b), b))

if __name__ == "__main__":  
    main()
