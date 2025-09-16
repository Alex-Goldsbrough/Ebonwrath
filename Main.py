# Code Imports
import os
from Rooms.Entrance import Entrance
from Rooms.flow import GoToMainMenu
import inventory

########################################################################################

# Displaying starting screen/menu
def prompt() -> str:
            print(r"""                                                                                                                                                                
           ███████╗██████╗░░█████╗░███╗░░██╗░██╗░░░░░░░██╗██████╗░░█████╗░████████╗██╗░░██╗   
           ██╔════╝██╔══██╗██╔══██╗████╗░██║░██║░░██╗░░██║██╔══██╗██╔══██╗╚══██╔══╝██║░░██║   
           █████╗░░██████╦╝██║░░██║██╔██╗██║░╚██╗████╗██╔╝██████╔╝███████║░░░██║░░░███████║   
           ██╔══╝░░██╔══██╗██║░░██║██║╚████║░░████╔═████║░██╔══██╗██╔══██║░░░██║░░░██╔══██║   
           ███████╗██████╦╝╚█████╔╝██║░╚███║░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░██║░░██║   
           ╚══════╝╚═════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝   
                                                                                     
                            Designed and created by Alex Goldsbrough                        
                                                                                     
Long ago, an ancient fortress sank into the earth, its halls claimed by darkness and creatures of stone.
 Legends speak of three sacred gems hidden within, each bound by puzzles and forgotten guardians. Only 
        those who claim them may face the final horror that stirs in the deepest chamber.
                  
                         Do you wish to challenge this dunegon?

                    1) Play              2) Help            3) Quit

""")
    
            return input("Enter Selection: ").strip().lower()


########################################################################################

# Clears CMD screen
def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

########################################################################################

def main():
    while True:
        clear()
        choice = prompt()
        if choice in ("1", "play", "start"):
               clear()
               inventory.reset_inventory()
               try:
                Entrance().start()
               except GoToMainMenu:
                     pass
        elif choice in ("2", "help"):
                clear()
                print(r"""       
              _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/       
                      
A strange light flickers in the darkness…  
From the glow steps an old mage, his voice echoing in your mind:  

Adventurer, heed my words!  
- To choose your path, press 1, 2, 3, or 4 when making your choice.
- To see what treasures you bear, type INV or INVENTORY.
- To cast aside your journey, type Q or Quit.

The road is yours to shape, but beware… every choice bends destiny itself. 
                    """)
                input("\n[Press Enter]")
        elif choice in ("3", "q", "quit"):
               break
        else:
            print("Invalid Selection")
            input("\n[Press Enter]")

if __name__ == "__main__":
    main()

########################################################################################