import main
import signal,sys,base64


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
    print("Hi There!ヾ(≧▽≦*)o \t Welcome to Pokemon Super Search Engine!")
    while True:
        print('''Here are the operations available:
              PRESS CTRL+C to exit! (In case you dont know it force-exit any command line programme.)
              Key In the Operation No. to execute them:
              1. Print first N row of CSV
              2. Display the first pokemon of type S, full type name, case sensitive
              3. Display all pokemon with total stat exactly N
              4. display all pokemon with Special attack, special defense, and speed all greater or equal to the user's input.
              5. input two types, letter for letter, and find legerndary pokemon
              There's A Hidden Suprise await your discovery!''')

        USER=input("Enter Operation!:")
        # print(base64.b64encode(USER.lower().encode("utf-8")))
        if base64.b64encode(USER.lower().encode("utf-8"))==b"Z3Vlc3MgbXkgbmFtZQ==":
            print("You found the Hidden Option!")
            # TODO
            continue
        if USER=='1':
            pass
        elif USER=='2':
            pass
        elif USER=='3':
            pass
        elif USER=='4':
            pass
        elif USER=='5':
            pass

