def divisors(num):
    divisors = []
    for i in range(1,num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingrese un numero:  "))
        if num < 0:
            raise ValueError
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un numero mayor a cero")
        run()
        
if __name__ == '__main__':
    run()