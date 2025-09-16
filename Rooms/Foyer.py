########################################################################################


#                      ███████╗░█████╗░██╗░░░██╗███████╗██████╗░
#                      ██╔════╝██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
#                      █████╗░░██║░░██║░╚████╔╝░█████╗░░██████╔╝
#                      ██╔══╝░░██║░░██║░░╚██╔╝░░██╔══╝░░██╔══██╗
#                      ██║░░░░░╚█████╔╝░░░██║░░░███████╗██║░░██║
#                      ╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

########################################################################################

import os
import inventory

########################################################################################

# Clears CMD screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\n[Press Enter]")

class Foyer:
    def start(self):
        while True:
            clear()
            print(r"""
The hallway ends in a wide chamber, its ceiling arching high above. Cracked pillars
line the walls, and scraps of broken furniture lie scattered across the floor. At the
far side of the room stands a massive oak door bound in black iron. Its lock is large
and unyielding, carved with unfamiliar runes. The air here feels heavier, as though the
fortress itself is watching.
                  
    How do you wish to continue?
          
    1) Try to force the iron door.
    2) Search the broken furniture.
    3) Return to the hallway
    4) Examine the lock on the door.
""")
            
            choice = input("Enter Selection: ").strip().lower()

            if choice == "1":
                print("\nThe lock does not move. The more you push, the louder the runes hum. Without the Iron Key, there is no way forward.")
                pause()
                continue
            elif choice == "2":
                print("\nDust and splinters. Nothing of value remains. Just the emptiness of a place abandoned.")
                pause()
                continue
            elif choice == "3":
                print("\nYou step back into the long, cold passage you came from.")      
                pause()
                clear()
                from .Hallway import Hallway
                Hallway().start()
                continue
            elif choice == "4":
                if inventory.has_item("iron_key"):
                    print("\nThe key slides in as though it has always belonged there. With a low groan, the lock gives way and the door swings open, revealing the path ahead.")
                    print("\n\033[91mYou no longer have the iron key.\033[0m")
                    pause()
                    clear()
                    inventory.set_item("iron_key", False)
                    from .Cells import Cells
                    Cells().start()
                else:
                    print("\nIt seems like you'll need a key.")
                    pause()
                    continue
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
