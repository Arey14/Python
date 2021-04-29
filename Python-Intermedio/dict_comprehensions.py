def dict2():
    dict = {}
    for i in range(0,101):
        dict[i] = i**3

    print(dict)
def notdiv3():
    dict2 = {}
    for i in range(0,101):
        if i % 3 !=0:
            dict2[i] = i**3
    print(dict2)

my_dict = {i: i**3 for i in range(1,101) if i % 3 !=0}

my_dict2 = {i: i**0.5 for i in range(1,1001)}


if __name__ == '__main__':
    dict2()
    notdiv3()
    print(my_dict)
    print(my_dict2)