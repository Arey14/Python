def fibo(n):
    """Calcula el n numero de fibonacci

    n int => 0
    returns fibo(n)
    """
    if n == 0 or n==1:
        return 1
    return (fibo(n-1)+fibo(n-2))
n = int(input("Escriba un numero: "))    
print(fibo(n))