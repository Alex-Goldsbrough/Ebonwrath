########################################################################################


#           ██╗░░██╗░█████╗░██╗░░░░░██╗░░░░░░██╗░░░░░░░██╗░█████╗░██╗░░░██╗
#           ██║░░██║██╔══██╗██║░░░░░██║░░░░░░██║░░██╗░░██║██╔══██╗╚██╗░██╔╝
#           ███████║███████║██║░░░░░██║░░░░░░╚██╗████╗██╔╝███████║░╚████╔╝░
#           ██╔══██║██╔══██║██║░░░░░██║░░░░░░░████╔═████║░██╔══██║░░╚██╔╝░░
#           ██║░░██║██║░░██║███████╗███████╗░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░
#           ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░

########################################################################################

import os
import inventory

########################################################################################

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
        88888888888888888888888888888888888888888888888888888888888888888888888
        88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
        88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
        88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
        88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
        88   |``"..__ |    |`";.| A|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
        88   |      |``--..|_ | `;!|e|MMoMMMMoMMM|w|.'E   |_..!-'|     |     88
        88   |      |    |   |`-,!_|_|MMMMPYYMMMM|_||.!-;'  |    |     |     88
        88___|______|____!.,.!,.!,!|b|MPYMoMMMMoM|r|,!,.!.,.!..__|_____|_____88
        88      |     |    |  |  | |_|MMMMbodMMMM|_|| |   |   |    |      |  88
        88      |     |    |..!-;'L|o|MPYMoMMMMoM|a| |`-..|   |    |      |  88
        88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `X-!.._ |      |  88
        88     _!.-'|    | _."|  !;|n|MbdMMoMMMMM|t|`.| `-._|    |``-.._  |  88
        88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
        88   |      |.|    |.|  !| |%|MoMMMMoMMMM|h||`. |`!   | `".    |     88
        88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
        88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
        88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
        88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
        88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
        88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
        88888888888888888888888888888888888888888888888888888888888888888888888

You step inside. The heavy door closes behind you with a dull thud. The only light comes faintly
from behind, slipping through cracks in the old door. Ahead, the hallway stretches into shadow, its
stone walls cracked and damp. The air is heavy, and every step forward feels likemoving deeper into 
a place long forgotten.

    How do you wish to continue?
          
    1) Inspect the broken stones along the wall.
    2) Walk carefully down the hallway.
    3) Call out into the hallway.
    4) Sit still and listen.
""")
            
            choice = input("Enter Selection: ").strip().lower()

            if choice == "1":
                if not inventory.has_item("iron_key"):
                    print("\nYou pry at loose stone near the floor. Beneath it, you uncover a small iron key, cold to the touch. Its purpose is unclear.")
                    print("\n\033[92mYou pocket the iron key into your satchel.\033[0m")
                    inventory.set_item("iron_key", True)
                    pause()
                    continue
                else:
                    print("\nYou have already done that.")
                    pause()
                    continue
            elif choice == "2":
                print("\nThe floor groans but holds beneath your weight. A faint draft guides you toward a distant archway. You move forward without incident.")
                pause()
                from .Foyer import Foyer
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
                break
            elif choice in ("inv", "inventory"):
                inventory.show_inventory()
                pause()
                continue
            else:
                print("\nNothing happens. Choose a valid option.")
                pause()
                continue
