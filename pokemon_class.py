# Goofy AHHH qn paper
# Your task is to implement a Pokedex super search engine that should be able to
# • display selected number of Pokemon with their types and statistics
# • display the first Pokemon of a Type of the trainer’s choice
# • display all Pokemon with Total Base stat of the trainer’s choice
# • display all Pokemon with a minimum set of stats
# • display all legendary Pokemon of Types of the trainer’s choice


import PIL.Image
import os.path
class Pokemon:
    def __init__(self,data):
        self.__dict__.update(data)
        self.photo=None
    def get_photo(self,folder):
        self.photo=PIL.Image.open(os.path.join(folder,self.Name+".png"))
    def __repr__(self):
        # gonna simplify
        return "".join(str(val).ljust(25) if isinstance(val,str) else str(val).ljust(8)  for key,val in self.__dict__.items() if key!="photo")

# class DB(Pokemon):
#     def __init__(self,L=[]):
#         self.L=L
#     def insert(self,item:Pokemon):
#         self.L.append(item)