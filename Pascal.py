def Pascal(n):         # Функция, которая выводит строку из треугольника Паскаля
    if n == 0:
        return [1]
    else:
        row = [1]
        row2 = Pascal(n - 1)
        for i in range(len(row2) - 1):
            row.append(row2[i] + row2[i + 1])    
        row.append(1)
        return row
def main():           # Главная функция вызова
    n = int(input('Введите число: '))
    for i in range(n):
        print(Pascal(i))

if __name__ == "__main__":    #Выполнение кода, если он запущен как самостоятельный файл
    main()