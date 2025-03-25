import main
from pokemon_class import Pokemon
import signal,sys,base64,time

# print(Pokemon.num_print_length)
lengths=[Pokemon.num_print_length,
        Pokemon.string_print_length,
        Pokemon.string_print_length,
        Pokemon.string_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length,
        Pokemon.num_print_length]
HEADINGS="".join(string.ljust(l) for l,string in zip(lengths,"No,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary".split(',')))

def robust_int(qn: str):
    response=input(qn)
    while not response.isnumeric():
        print("Please input integers!")
        response=input(qn)
    return int(response)

# I asked chatgpt for this chunck of code
# Ngl even if i dont ask ChatGPT ill just ask google, its the same
def handle_sigint(signal_received, frame):
    print("\nGoodbye! Thanks for using Pokemon Super Search Engine!")
    sys.exit(0)  # Ensure the program exits cleanly

# Register signal handler
signal.signal(signal.SIGINT, handle_sigint)


DATA=[]
if __name__=="__main__":
    DATA=main.get_data("ASSETS\Pokemon.csv")
    USER=""
    print("Hi There!ヾ(≧▽≦*)o \nWelcome to Pokemon Super Search Engine!")

    while True:
        print('''Here are the operations available:
    PRESS CTRL+C to exit! (In case you dont know it force-exit any command line programme.)
    Key In the Operation No. to execute them:
    1. Print first N row of CSV
    2. Display the first pokemon of type S, full type name, case sensitive
    3. Display all pokemon with total stat exactly N
    4. Display all pokemon with Special attack, special defense, and speed all greater or equal to the user's input.
    5. Input two types, letter for letter, and find legerndary pokemon
    There's A Hidden Suprise await your discovery!''')

        USER=input("Enter Operation!:")
        print()
        if base64.b64encode(USER.lower().encode("utf-8"))==b"Z3Vlc3MgbXkgbmFtZQ==":
            print("You found the Hidden Option!")
            print("But... There's really not much here ╮（╯＿╰）╭")
            # TODO
            continue

        if USER=='1':
            lines=robust_int("How many lines you want: ")
            print(HEADINGS)
            for cur in DATA[:lines]:
                print(cur)

        elif USER=='2':
            typename=input("Input type name: ")
            index=0
            while DATA[index].Type_1!=typename and DATA[index].Type_2!=typename:
                index+=1
                if index==len(DATA): break
            print(HEADINGS)
            print("No Pokemon of this type!" if index==len(DATA) else DATA[index])

        elif USER=='3':
            stat=robust_int("Input The base stat you want: ")
            # now... better!
            results=filter(lambda cur: cur.Total==stat,DATA)
            if not any(True for _ in results):
                print("No such pokemon with this stat!")
                break
            print(HEADINGS)
            for result in results:
                print(result)

        elif USER=='4':
            # skibidi tiolet
            spatk=robust_int("Input special Atk: ")
            spdef=robust_int("Input special Def:")
            spd=robust_int("Input Speed: ")
            results=filter(lambda cur: cur.Sp_Atk>=spatk and cur.Sp_Def>=spdef and cur.Speed>=spd,DATA)
            if not any(True for _ in results):
                print("No such pokemon with this stat!")
                break
            print(HEADINGS)
            for result in results:
                print(result)

        elif USER=='5':
            type1=input("Input First type: ")
            type2=input("Input Second type: ")
            results=filter(lambda cur: cur.Type_1==type1 and cur.Type_2==type2 and cur.Legendary,DATA)
            if not any(True for _ in results):
                print("No Legendary pokemon with these types! ")
                break
            print(HEADINGS)
            for result in results:
                print(result)

        print()

