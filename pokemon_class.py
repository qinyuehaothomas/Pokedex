# Goofy AHHH qn paper
# Your task is to implement a Pokedex super search engine that should be able to
# • display selected number of Pokemon with their types and statistics
# • display the first Pokemon of a Type of the trainer’s choice
# • display all Pokemon with Total Base stat of the trainer’s choice
# • display all Pokemon with a minimum set of stats
# • display all legendary Pokemon of Types of the trainer’s choice


import PIL.Image
import os.path
import base64
from dataclasses import field
from nicegui import ui,binding

ENCODE=lambda x: base64.b64encode(x.encode("utf-8"))

ANY_TYPE="(Any Type)"


@binding.bindable_dataclass
class Query:
    type_1: str = ANY_TYPE
    type_2: str = ANY_TYPE
    Name: str = ""
    is_legendary: bool = False
    base_stat: dict = field(default_factory=lambda:{"min": 10, "max": 900})

@binding.bindable_dataclass
class GMN_User: # binder for Guess My Name User Input
    user_input: str = ""

class Pokemon:
    string_print_length=25
    num_print_length=8
    type_list=['Water', 'Grass', 'Poison', 'Ice', 'Fighting', 'Normal', 'Fire', 'Ghost', 'Flying', 'Ground', 'Psychic', 'Dragon', 'Fairy', 'Dark', 'Steel', 'Rock', 'Bug', 'Electric']
    def __init__(self,data):
        self.__dict__.update(data)
        self.photo=None
    def graph(self):
        # HP,Attack,Defense,Sp. Atk,Sp. Def,Speed
        return {
            "radar": {
                "indicator": [
                {"name": "HP", "max": 180},
                {"name": "Attack", "max": 180},
                {"name": "Defense", "max": 180},
                {"name": "Special Atk", "max": 180},
                {"name": "Special Def", "max": 180},
                {"name": "Speed", "max": 180},
                ],
                "shape": "circle"
            },
            'axisName': {  
                'color': 'grey',   # Indicator label color
                'fontSize': 12,    # Indicator font size
                "inside":True,
                'fontWeight': 'bold',
            },
            "series": [{
                "type": "radar",
                "data": [
                {
                    "value": [self.HP,self.Attack,self.Defense,self.Sp_Atk,self.Sp_Def,self.Speed]
                }
                ],
                "lineStyle": {
                "color": "rgba(220, 20, 60, 1)"  # 🔴 Red Lines
                },
                "symbol": "circle",  # 🔴 Red Dots (Make it a circle)
                "symbolSize": 8,
                "itemStyle": {
                "color": "rgba(220, 20, 60, 1)"  # 🔴 Red Dots (Fix the color)
                },
                "areaStyle": {
                "color": "rgba(220, 20, 60, 0.8)" 
                },
                "label": {
                "show": True,
                "color": "#222",
                "fontSize": 12
                }
            }]
        }
    def masked(self):
        r, g, b, a = self.get_image().split()

        # Create a new black image with the same alpha channel
        black_img = PIL.Image.merge("RGBA", (r.point(lambda _: 0), g.point(lambda _: 0), b.point(lambda _: 0), a))

        # Show or save the modified image
        # black_img.show()
        return black_img
        pass
    def get_image(self):
        folder=r"ASSETS\\Pokemon Image"
        if self.photo==None:
            self.photo=PIL.Image.open(os.path.join(folder,self.Name+".png")).convert("RGBA")
        return self.photo
        
    def __repr__(self):
        return "".join(str(val).ljust(self.string_print_length) if isinstance(val,str) else str(val).ljust(self.num_print_length)  for key,val in self.__dict__.items() if key!="photo")

# class DB(Pokemon):
#     def __init__(self,L=[]):
#         self.L=L
#     def insert(self,item:Pokemon):
#         self.L.append(item)