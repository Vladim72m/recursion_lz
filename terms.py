def partitions(n, min = 1): # создаем функцию 
    if n == 0:
        return [[]]  # возвращаем пустое разбиение
    list = []
    for i in range(min, n + 1):  
        for j in partitions(n - i, i):  
            list.append([i] + j)  # Добавляем  число к каждому разбиению
    return list

def b(c): # создаем функцию
    parts = partitions(c) # список всех разложений
    for a in parts:
        print(a)
        
def main():
    c = int(input("Введите число, которое хотите разложить на сумму целых чисел: "))
    print(b(c)) 
if __name__ == "__main__":
    main()
