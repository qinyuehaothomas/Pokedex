from pokemon_class import Pokemon
import PIL.Image
import csv
DATA=[]

def robust_int(qn: str):
    response=input(qn)
    while not response.isnumeric():
        print("Please input integers!")
        response=input(qn)
    return int(response)

def guess_my_name():
    # TODO
    pass

def get_data(path):
    DATA=[]
    with open(path) as f:
        RAW=list(csv.DictReader(f))
    for row in RAW:
        row= {key.replace(" ","_"): (int(value) if value.isdigit() else value) for key, value in row.items()} 
        row["Legendary"]=row["Legendary"]=="TRUE"
        # print(row)
        row=Pokemon(row)
        row.get_photo(r"ASSETS\\Pokemon Image")
        DATA+=[ row]
    return DATA

if __name__=="__main__":
    get_data("ASSETS\\Pokemon.csv")