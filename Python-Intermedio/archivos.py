archivo = "/home/augusto/Escritorio/Python/Python-Intermedio/Archivos/numbers.txt"
namestxt ="/home/augusto/Escritorio/Python/Python-Intermedio/Archivos/names.txt"


def read():
    numbers = []
    with open(archivo, "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)

def write():
    names = ["Augusto", "Miguel", "Pepe", "Catalina"]
    with open(namestxt, "w", encoding="utf-8") as f:
        for i in names:
            f.write(i)
            f.write("\n")

def append():
    names = ["Nancy", "Sole", "Beni", "Mely"]
    with open(namestxt, "a", encoding="utf-8") as f:
        for i in names:
            f.write(i)
            f.write("\n")

def run():
    read()
    write()
    append()

if __name__ == '__main__':
    run()

    