DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #all_python_dev = [Worker["name"] for Worker in DATA if Worker["language"] == "python"]
    #all_Platzi_workers = [Worker["name"] for Worker in DATA if Worker["organization"] == "Platzi"]
    #adults =  list(filter(lambda x: x["age"] > 18, DATA))
    #adults = map(lambda worker: worker['name'],adults)
    #old_people = list(map(lambda worker: worker | {"old": worker['age'] > 70}, DATA))
    all_python_dev = list(filter(lambda worker: worker["language"] == "python",DATA))
    all_python_dev = map(lambda worker: worker["name"],all_python_dev)
    all_Platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi",DATA))
    all_Platzi_workers = map(lambda worker: worker["name"],all_Platzi_workers)
    adults =  [Worker["name"] for Worker in DATA if Worker["age"] > 18]
    old_people =  [worker | {'old': worker['age'] > 70} for worker in DATA]
    

    for worker in all_python_dev:
       print(worker)
    print("----------------------------")

    for worker in all_Platzi_workers:
       print(worker)
    print("----------------------------")

    for worker in adults:
        print(worker)
    print("----------------------------")

    for worker in old_people:
       print(worker)

if __name__ == '__main__':
    run()