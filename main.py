from pokemon_class import *
from nicegui import ui,app
import PIL.Image,csv,asyncio
import UI
DATA=[]
TYPE_LIST=[ANY_TYPE,'Water', 'Grass', 'Poison', 'Ice', 'Fighting', 'Normal', 'Fire', 'Ghost', 'Flying', 'Ground', 'Psychic', 'Dragon', 'Fairy', 'Dark', 'Steel', 'Rock', 'Bug', 'Electric']
NAME_LIST=[]
SEARCH=Query()

@ui.page("/")
def SearchPage():
    ui.row.default_classes("justify-between w-full")
    # ui.label("Filter Manual").classes("text-2xl")
    with ui.expansion('Filter', icon='filter_alt').classes('w-full'):
        # Type Dropdown
        binding.bind_from
        with ui.row():

            ui.select(options=TYPE_LIST,with_input=True)\
                .classes("w-1/3")\
                .bind_value(SEARCH,"type_1")
            
            ui.select(options=TYPE_LIST,with_input=True)\
                .classes("w-1/3")\
                .bind_value(SEARCH,"type_2")
            
            ui.switch("Legendary Only")\
                .style("width:50px, padding:1px")\
                .bind_value(SEARCH,"is_legendary")
        # Base Stat Range Slider
        ui.label("Total Base Stat").classes("text-lg")
        with ui.row():
            # ui.label("Min:").style("flex:1")
            ui.range(min=0, max=800, value={"min":0,"max":800})\
                .classes("w-full")\
                .props("label")\
                .bind_value(SEARCH,"base_stat")
            # ui.label("Max:").style("flex:1")
        
        # Min specific stats is kinda goofy like nobdy wanna use it?
        # ui.label("Advanced Query").classes("text-sm")
        # ui.input("Min. Specific Stats").classes("w-full p-2")

        # Clear button (it was not implimented)
        # ui.button("Clear", on_click=lambda: ui.notify("Filters cleared")).classes("ml-auto")

    # Name Search Bar
    # with ui.row().classes("justify-between w-full"):
    ui.select(options=NAME_LIST+["(Use Filter)"],value="(Use Filter)",with_input=True)\
        .classes("w-full")\
        .bind_value(SEARCH,"Name")
    submit_search=ui.button("Search").classes('ml-auto bg-blue-500 text-white')
    results_container=ui.row()
    submit_search.on_click(lambda:show_result(results_container))
        # name_input.on('input', lambda e: GMN().launch() if name_input.value == "Guess My Name" else None)

def search_filter(cur):
    if SEARCH.Name:
        return cur.Name==SEARCH.Name
    else:
        return (cur.Total>=SEARCH.base_stat["min"] and cur.Total<=SEARCH.base_stat["max"])\
        and (cur.Type_1==SEARCH.type_1 or cur.Type_2==SEARCH.type_1 or SEARCH.type_1==ANY_TYPE)\
        and (cur.Type_1==SEARCH.type_2 or cur.Type_2==SEARCH.type_2 or SEARCH.type_2==ANY_TYPE)\
        and (cur.Legendary==SEARCH.is_legendary)
async def show_result(par:ui.row):
    RESULTS=list(filter(search_filter,DATA))
    par.clear()
    with par:
        if not RESULTS:
            # print("lifestyle")
            ui.notify("No Pokemon satisfy these constrains!",type="negative")
            
        else:
            for pokemon in RESULTS:
                # print(f"Loading {pokemon.Name}")
                with ui.card().classes("justify-center w-[320px] px-[0px]"):
                    ui.label(pokemon.Name)
                    loading_img=ui.skeleton(type="QSlider")
                    await asyncio.sleep(0.5)
                    loading_img.delete()
                    ui.image(pokemon.get_image()).style("height:300px,width:auto")
                    ui.echart(pokemon.graph())
                    

def robust_int(qn: str):
    response=input(qn)
    while not response.isnumeric():
        print("Please input integers!")
        response=input(qn)
    return int(response)

def get_data(path):
    DATA=[]
    with open(path) as f:
        RAW=list(csv.DictReader(f))
    for row in RAW:
        row= {key.replace(" ","_").replace(".",""): (int(value) if value.isdigit() else value) for key, value in row.items()} 
        row["Legendary"]=row["Legendary"]=="TRUE"
        # print(row)
        row=Pokemon(row)
        # row.get_photo()
        DATA+=[ row]
    return DATA


if __name__ in {"__main__", "__mp_main__"}:
    DATA=get_data("ASSETS\\Pokemon.csv")
    NAME_LIST=[""]+[i.Name for i in DATA]
    # SearchPage()
    # ui.page("/search")(SEARCH.results)
    # ui.page("/")(SEARCH.build)
    app.native.window_args['resizable'] = False
    ui.run(favicon="ASSETS\\favicon.png",
           title="Pokemon Super Search Engine",
           native=True,
           window_size=(1080, 720))