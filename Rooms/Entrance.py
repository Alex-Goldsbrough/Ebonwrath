from .Hallway import Hallway
import os

# Clears CMD screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\n[Press Enter]")

class Entrance:
    def start(self):
        while True:
            clear()
            print(r"""
You stand before the crumbling gates of Ebonwrath, a fortress swallowed by stone and silence. 
The air is heavy with dust and the faint stench of decay. Moss creeps along broken walls, and 
an ancient wooden door looms ahead, its iron hinges rusted but intact.


    How do you wish to continue?
          
    1) Push the door open with force.
    2) Examine the door carefully.
    3) Wait in silence before the gate.
    4) Knock on the door.
""")
            
            choice = input("Enter Selection: ").strip().lower()

            if choice == "1":
                print("\nYou throw your weight at the ancient wood. It doesn’t budge. Dust falls on your head, and your shoulder aches. Congratulations, you’ve achieved nothing but looking like a fool in front of a door.")
                pause()
                continue
            elif choice == "2":
                print("\nThe runes carved into the wood flicker faintly when touched. You feel the door resisting you, as though it judges your intent. The path remains closed.")
                pause()
                continue
            elif choice == "3":
                print("\nThe longer you stand still, the colder the air becomes. A distant sound, like chains dragging on stone, stirs within the fortress. The atmosphere grows oppressive, pressing you to act.")
                pause()
                continue
            elif choice == "4":
                print("\nAgainst all logic, the door slowly opens on its own. An eerie voice whispers your name. A chill lingers in your bones, lowering your morale slightly, but the fortress welcomes you inside.")
                pause()
                clear()
                Hallway().start()
                continue
            elif choice in ("q", "quit"):
                return
            else:
                print("\nNothing happens. Choose a valid option.")
                pause()
                continue
