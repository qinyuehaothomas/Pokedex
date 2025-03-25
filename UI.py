
from nicegui import ui,binding,app
from random import choice
from dataclasses import field
# Documentation says using bindable property is more efficent

@binding.bindable_dataclass
class Query:
    type_1: str = "Fire"
    type_2: str = ""
    Name: str = "Pikachu"
    is_legendary: bool = False
    base_stat: dict = field(default_factory=lambda:{"min": 10, "max": 900})

class SearchPage(): # Search Page
    
    type_list=['Water', 'Grass', 'Poison', 'Ice', 'Fighting', 'Normal', 'Fire', 'Ghost', 'Flying', 'Ground', 'Psychic', 'Dragon', 'Fairy', 'Dark', 'Steel', 'Rock', 'Bug', 'Electric']
    
    def __init__(self,DATA):
        self.DATA=DATA
        self.name_list=[i.Name for i in self.DATA if " " not in i.Name]
        self.current_search=Query()
    
    def build(self):
        ui.row.default_classes("justify-between w-full")
        # ui.label("Filter Manual").classes("text-2xl")
        with ui.expansion('Filter', icon='filter_alt').classes('w-full'):
            # Type Dropdown
            binding.bind_from
            with ui.row():

                ui.select(options=self.type_list,with_input=True)\
                    .style("width:200px")\
                    .bind_value(self.current_search,"type_1")
                
                ui.select(options=self.type_list+[""],with_input=True)\
                    .style("width:200px")\
                    .bind_value(self.current_search,"type_2")
                
                ui.switch("Legendary Only")\
                    .style("width:50px, padding:1px")\
                    .bind_value(self.current_search,"is_legendary")
            # Base Stat Range Slider
            ui.label("Total Base Stat").classes("text-lg")
            with ui.row():
                # ui.label("Min:").style("flex:1")
                ui.range(min=0, max=800, value={"min":0,"max":800})\
                    .classes("w-full")\
                    .props("label")\
                    .bind_value(self.current_search,"base_stat")
                # ui.label("Max:").style("flex:1")
            
            # Min specific stats is kinda goofy like nobdy wanna use it?
            # ui.label("Advanced Query").classes("text-sm")
            # ui.input("Min. Specific Stats").classes("w-full p-2")

            # Clear button (it was not implimented)
            # ui.button("Clear", on_click=lambda: ui.notify("Filters cleared")).classes("ml-auto")

        # Name Search Bar
        # with ui.row().classes("justify-between w-full"):
        ui.select(options=self.name_list+["(Use Filter)"],value="(Use Filter)",with_input=True)\
            .classes("w-full")\
            .bind_value(self.current_search,"Name")
        ui.button("Search",on_click=self.results).classes('ml-auto bg-blue-500 text-white')

            # name_input.on('input', lambda e: GMN().launch() if name_input.value == "Guess My Name" else None)
    def results(self):
        ui.label().bind_text_from(self.current_search,"type_1")
        ui.link("Back","/")

