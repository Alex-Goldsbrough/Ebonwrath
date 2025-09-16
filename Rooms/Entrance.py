from Rooms.Gate import Gate
import os

# Clears CMD screen
def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

class Entrance():
    def start(self):
        print(r"""
You stand before the crumbling gates of Ebonwrath, a fortress swallowed by stone and silence. 
The air is heavy with dust and the faint stench of decay. Moss creeps along broken walls, and 
an ancient wooden door looms ahead, its iron hinges rusted but intact.


    How do you wish to continue?
          
    1) Push the door open with force.
    2) Examine the door carefully.
    3) Look around the ruins outside.
    4) Knock on the door.
          
          """)
        
        choice = input("Enter Selection: ").strip()

        if choice == "1":
            print("\nYou throw your weight against the door. It groans loudly but begins to budge, dust raining down.")
        elif choice == "2":
            print("\nYou trace your fingers over the wood and iron. Scratches mark the surface, and you spot a faint carving—runes long forgotten.")
        elif choice == "3":
            print("\nYou step back and scan the ruins. Fallen stones form jagged silhouettes, and in the distance you hear the faint rustle of movement.")
        elif choice == "4":
            print("\nYou knock firmly on the wood. The sound echoes unnaturally. After a pause, the door creaks open...")
            clear()
            Gate().start()  # move to Gate room
        else:
            print("\nNothing happens. Perhaps choose a valid option.")