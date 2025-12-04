def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def main():
    a=int(input('Введите первое4 число:'))
    b=int (input('Введите второе число:'))
    print('НОД:',gcd(a,b))
if __name__ == "__main__":
    main()