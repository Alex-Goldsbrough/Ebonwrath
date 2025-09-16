# Designed and created by Alex Goldsbrough

########################################################################################

# Code Imports
import Rooms.Altar
import Rooms.Armory
import Rooms.Barracks
import Rooms.Boss
import Rooms.Catacombs
import Rooms.Cells
import Rooms.Chapel
import Rooms.Crypt
import Rooms.DeathScreen
import Rooms.Dining
from Rooms.Entrance import Entrance
from Rooms.Gate import Gate
import Rooms.Guard_Post
import Rooms.Kitchen
import Rooms.Library
import Rooms.Pantry
import Rooms.Rune
import Rooms.Shrine
import Rooms.Storage
import Rooms.Torture
import Rooms.Trap
import Rooms.WinScreen
import os

########################################################################################


#███████╗██████╗░░█████╗░███╗░░██╗░██╗░░░░░░░██╗██████╗░░█████╗░████████╗██╗░░██╗
#██╔════╝██╔══██╗██╔══██╗████╗░██║░██║░░██╗░░██║██╔══██╗██╔══██╗╚══██╔══╝██║░░██║
#█████╗░░██████╦╝██║░░██║██╔██╗██║░╚██╗████╗██╔╝██████╔╝███████║░░░██║░░░███████║
#██╔══╝░░██╔══██╗██║░░██║██║╚████║░░████╔═████║░██╔══██╗██╔══██║░░░██║░░░██╔══██║
#███████╗██████╦╝╚█████╔╝██║░╚███║░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░██║░░██║
#╚══════╝╚═════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝


########################################################################################

# Displaying starting screen/menu
def prompt() -> str:
            print(r"""
                                                           ____________
                                     (`-..________....---''  ____..._.-`
                                      \\`._______.._,.---'''     ,'
                                      ; )`.      __..-'`-.      /
                                     / /     _.-' _,.;;._ `-._,'
                                    / /   ,-' _.-'  //   ``--._``._
                                  ,','_.-' ,-' _.- (( =-    -. `-._`-._____
                                ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
                 _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
      _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
    ,',)---' /|)          `     `      ``-.   `     /     /     `     `-.
    \_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
     \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
               `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
                       ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   
                                                          ``--------..._``--.__
                  
Long ago, an ancient fortress sank into the earth, its halls claimed by darkness and creatures of stone.
Legends speak of three sacred gems hidden within, each bound by puzzles and forgotten guardians.
Only those who claim them may face the final horror that stirs in the deepest chamber.
                  
                            Do you wish to challenge this dunegon?

                     1) Play              2) Help            3) Quit

""")
    
            return input("Enter Selection: ").strip().lower()


# Clears CMD screen
def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear()
        choice = prompt()
        if choice == "1":
               clear()
               Entrance().start() # Starts the game
        elif choice == "2":
                clear()
                print("""
A strange light flickers in the darkness…  
From the glow steps an old mage, his voice echoing in your mind:  

Adventurer, heed my words!  
- To choose your path, press 1, 2, 3, or 4 when making your choice.
- To see what treasures you bear, type INV or INVENTORY.
- To cast aside your journey, type Q or Quit.

The road is yours to shape, but beware… every choice bends destiny itself. 
                    """)
                input("\n[Press Enter]")
        elif choice == "3" or "q" or "quit":
               break
        else:
            print("Invalid Selection")
            input("\n[Press Enter]")

if __name__ == "__main__":
    main()