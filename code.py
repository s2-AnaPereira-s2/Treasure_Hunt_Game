
print("Welcome to Berlin Island")
print("")
print("!!!Be aware!!!\n--This is a DANGEROUS hunt--")
print("")
username = input("What is your pirate name?\n")
print("")
start = input(f"{username} are you ready for the hunt?(Y/N)\n")
print("")


class Game():
    def __init__(self, username):
        self.username = username
    
    def First_phase(self):
        question = input("It's a treasure hunt. What is need? type the word and you may proceed.\n")
        question1 = question.lower()
        if question1 == "map":
            print(f"Congratulations {self.username}! You have the map\n")
            print('''
            #####################################################################
            |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
            |  _   ~~ ~~ __,---'_   xxxx"xxxxx    `. ~~~ _,--.  ~~~~ __,---.  ~~|
            | | \___ ~~ /      ( )  x" xx    x  "   `-.,' (') \~~ ~ (  / _\ \~~ |
            |  \    \__/_   __(( _)_ x    (  x "   "     (_\_) \___~ `-.___,'  ~|
            |~~ \     (  )_(__)_|( ))x "   )) xx       "   |    "  \ ~~ ~~~ _ ~~|
            |  ~ \__ (( _( (  ))  ) _)x   ((   \ \ / /   " |   "    \_____,' | ~|
            |             FOREST    xxx    ))    (X)                            |
            |~~ ~   \  ( ))(_)(_)_)|x "   ((   / / \ \ " _,---._  "  "   "  /~~~|
            |    ~~~ |(_ _)| | | xx|x  "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
            | ~~     |  |  | xx|xx _,--- ,--. _  "  (~~  LAKE  ~~~ ) /___\ \~~ ~|
            |  ~ ~~ /   | xxxx _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
            |~~    / " xxxx_,-' / `\ ,' / _'  \`.---.._          __        " \~ |
            | ~~~ / / x .-' , / ' _,'_ _VOLCANO _`._ `.`-._    _/- `--.   " " \~|
            |  ~ / / _xxxxxxxx .-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
            | ~ | | -- _    /x/  `-_- _  _,' '  \ \_`-._,-'  /MOUNTAIN \ \_   / |
            |~~ | \ -      /~x| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
            | ~~\  \_ /   /x~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
            |~   \      ,'x~|  "  (o o)  "         " " |~~~ \_,-' ~ `.     ,'~~ |
            | ~~ ~|__,-'~~x~~\    \ "/  LAVA "  "  "   /~ ~~   O ~ ~~`-.__/~ ~~~|
            |~~~ ~~~  ~~~~x~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
            |____~    ~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
            #####################################################################''')
            print("")
            game.Second_phase()
        else:
            print(f"{self.username} if what is need is not what is need. Come back when the word you perceive!!!")

    def Second_phase(self):
        question = input("One look one see. What you should follow, so the prize you receive?\n")
        question2 = question.lower()
        if question2 == "x":
            print(f"{self.username} congratulations!!! You found the spot")
            print("")
            game.Final_phase()
        else:
            print(f"{self.username} if you look you see, find your guide and come back to receive!!!")
    
    def Final_phase(self):
        print("You are almost there. Now it's time to dig")
        print("")
        dig = input("To get the shovel you need to speak. Ask the local for a shovel, just type the word. Remember: it's Berlin Island.\n")
        dig1 = dig.lower()
        if dig1 == "schaufel":
            print("")
            print(f"Aye captain {self.username}, splendid work. Here is your treasure!!!")
            print("")
            print('''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/
            *******************************************************************************''')
        else:
            print("")
            print("OWWW NOOOO...you got it wrong. The locals are mad..NEIN NEIN, JETZT MUSST DU STERBEN...shout the locals.\nYou were killed by the locals!!!")
            print("")
            print('''       
                _____
              /~/~   ~\ 
             | |       \ 
             \ \ GAME   \ 
              \ \  OVER  \ 
             --\ \       .\ ''
            --==\ \     ,,i!!i,
                ''"'',,}{,,''')

     
game = Game(username)

while True:
    ready = start.lower()
    if ready == "y":
        print("Aye Captain")
        game.First_phase()
        break
    elif ready == "n":
        print('''
          /))   _   _________________       ((\ 
         / / _ / ` |_______SEE_______|  ,- _ \ \ 
        / / / / /`_|____YOU__________|,-\ \ \ \ \ 
        | |/ / / / |______SOON_______| \ \ \ \| |
        | / / / / /|_____PIRATE_____ |\ \ \ \ \ |
        | | | `'  (|/(|___________|)\|    ' | | |
        |          `\  \         /  /,          |
        \           |  |         |  |          /
         \             |         |            /
          \           /          \           /
           \         /            \         /
        ''')
        break
    else:
        print(f"{username} please type Y or N")
        ready = input("Are you ready for the hunt?(Y/N)\n")




