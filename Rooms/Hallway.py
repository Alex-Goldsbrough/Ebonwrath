from .Foyer import Foyer
import os

# Clears CMD screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\n[Press Enter]")

class Hallway:
    def start(self):
        while True:
            clear()
            print(r"""
You step inside. The heavy door closes behind you with a dull thud. The air is colder here, thick with dust. 
A long stone hallway stretches forward, its walls cracked and damp.Faint torch brackets line the passage, though
no flames burn in them. Shadows gather in every corner, waiting.


    How do you wish to continue?
          
    1) Inspect the broken stones along the wall.
    2) Walk carefully down the hallway.
    3) Call out into the hallway.
    4) Sit still and listen.
""")
            
            choice = input("Enter Selection: ").strip().lower()

            if choice == "1":
                print("\nYou pry at loose stone near the floor. Beneath it, you uncover a small silver key, cold to the touch. Its purpose is unclear, but you pocket it.")
                pause()
                continue
            elif choice == "2":
                print("\nThe floor groans but holds beneath your weight. A faint draft guides you toward a distant archway. You move forward without incident.")
                pause()
                Foyer().start()
                continue
            elif choice == "3":
                print("\nYour voice bounces back unnaturally, echoing until it fades into silence. The weight of the fortress presses heavier on you. Nothing answers.")
                pause()
                continue
            elif choice == "4":
                print("\nAt first you hear nothing. Then, faintly, something like footsteps above you, moving slowly. The sound vanishes as quickly as it began.")
                pause()
                clear()
                continue
            elif choice in ("q", "quit"):
                return
            else:
                print("\nNothing happens. Choose a valid option.")
                pause()
                continue
