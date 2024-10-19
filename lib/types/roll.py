import random

def roll_d8():
    return random.randint(1,8)

element_table = {
    1: "light",
    2: "pyro",
    3: "cryo",
    4: "electro",
    5: "dendro",
    6: "hydro",
    7: "anemo",
    8: "geo"
}

def convert_id(id_number):
    return element_table.get(id_number, "ID not found")
