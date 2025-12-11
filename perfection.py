def operation1(a, b):
    if b == sum(a):  # Если число сравнимо с суммой его делителей, оно совершенное
         return "Число совершенное"
    else:
          return "Число несовершенное"

def operation2(n, i=1, a=[]):
    if i == 1:
        a = []
    if i == n:
        return a
    if n % i == 0:   # Если i делитель n, добавляем его к сумме
        a.append(i)
    return operation2(n, i+1, a)

def main():
    b = int(input("Введите число: "))
    print(operation2(b))
    print(operation1(operation2(b), b))

if __name__ == "__main__":  
    main()
