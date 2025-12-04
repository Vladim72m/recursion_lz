def operation1(a, b):
    if b == sum(a):
        print("Число совершенное")
    else:
        print("Число несовершенное")

def operation2(n):
    a = []
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
    return a

def main():
    b = int(input("Введите число: "))
    print(operation2(b))
    operation1(operation2(b), b)

if __name__ == "__main__":  
    main()
