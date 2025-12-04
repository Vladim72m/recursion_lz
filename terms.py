print('Введите число')
n = int(input())
def operation(a, n, k):
    if n:
        for i in range(n+1, 0, -1): # -1 - длина шага 
            if i <= k:
                operation(a+[i], n-i, i)
    else:
        print( a, end=' , ')
print('operation(',n,')=')  
operation([], n, n)

