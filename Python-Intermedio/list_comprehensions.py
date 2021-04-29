def nat_cuadrados():

    cuadrados = []
    x = 0

    for i in range(0,101):
     x = i**2
     cuadrados.append(x)

    return cuadrados

def no_div3():   
    no_div = []
    for i in nat_cuadrados():
        if not i%3 == 0:
            no_div.append(i)
    return no_div

multiplos469 = [i for i in range(0,10000) if i % 36 == 0]

if __name__ == '__main__':
    print(nat_cuadrados())
    print(no_div3())
    print(multiplos469)