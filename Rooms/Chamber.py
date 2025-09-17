########################################################################################


#           ░█████╗░██╗░░██╗░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
#           ██╔══██╗██║░░██║██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
#           ██║░░╚═╝███████║███████║██╔████╔██║██████╦╝█████╗░░██████╔╝
#           ██║░░██╗██╔══██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
#           ╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██████╦╝███████╗██║░░██║
#           ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝


########################################################################################

import os
import sys
import inventory

########################################################################################

# Clears CMD screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\n[Press Enter]")

def pedestal(): # Pedestal Interaction
    while True:
        clear()
        print(r""" 
          .------.
          `------`
          || | |||
          || | |||
          ||   |||
          ||   |||
          || | |||
          || --||-
          --   -- 
You step slowly across the chamber floor, shards of pottery crunching beneath your boots.
...
    1) Place your hand firmly on the surface.
    2) Run your fingers lightly around the edges.
    3) Kick the pedestal sharply.
    4) Walk away.
""")
        choice = input("Enter Selection: ").strip().lower()

        if choice == "1":
            print("\nThe stone sinks under your palm. A grinding roar erupts as the trap unleashes fully. A storm of darts blasts from the walls in every direction.")
            pause()
            clear()
            from Rooms.Death import Death
            Death().start()
            return False  

        elif choice == "2":
            print("\nA quiet click sounds... You recover a Stone Tablet Fragment.")
            print("\n\033[91mYou can no longer examine the pedestal.\033[0m")
            pause()
            inventory.set_item("stone_tablet_fragment", True) 
            return True # Locks the room

        elif choice == "3":
            print("\nThe brittle stone shatters... the pedestal’s secret is destroyed.")
            print("\n\033[91mYou can no longer examine the pedestal.\033[0m")
            pause()
            return True  # Locks the room

        elif choice == "4":
            print("\nYou walk away from the pedestal.")
            pause()
            clear()
            return False

        elif choice in ("q", "quit"):
            sys.exit(0)

        elif choice in ("inv", "inventory"):
            inventory.show_inventory()
            pause()
            continue

        else:
            print("\nNothing happens. Choose a valid option.")
            pause()
            continue

class Chamber:
    def __init__(self):
        self.pedestal_locked = False

    def start(self):
        while True:
            clear()
            print(r"""
The corridor slopes downward, the air turning colder with every step. At last it opens into
a wide stone chamber. The walls are rough-hewn, as though carved in haste, and the ceiling
rises into darkness. At the center of the room stands a broken pedestal, its surface cracked
and scarred. Shards of pottery and splintered wood litter the floor, remnants of something
once kept here. A faint dripping sound echoes from somewhere unseen. The stillness feels
unnatural, as if the room itself is waiting.
                  
    How do you wish to continue?
          
    1) Take the archway lined with faded runes.
    2) Examine the cracks in the walls.
    3) Look up into the darkness above.
    4) Walk up to the broken pedestal.
    5) Step through the doorway reinforced with rusted iron.
""")
            
            choice = input("Enter Selection: ").strip().lower()

            if choice == "1":
                print("\nThe symbols glow faintly as you pass beneath, and the air shifts from stale stone to the dry scent of old parchment.")
                pause()
                clear()
                from .Library import Library
                Library().start()
                continue
            elif choice == "2":
                print("\nYou trace your hand along the stone. Thin fissures run through the chamber as though the walls themselves are straining. From one crack seeps a faint cold draft. You sense there may be another passage hidden deeper within the fortress, but not here.")
                pause()
                continue
            elif choice == "3":
                print("\nDust falls onto your face. You glimpse chains hanging from the ceiling, their ends snapped. Whatever they once held has long since broken free.")
                pause()
                continue
            elif choice == "4":
                if self.pedestal_locked:
                    print("\nThe pedestal is ruined. There is nothing left to examine.")
                    pause()
                    continue
                clear()
                became_locked = pedestal()
                if became_locked:
                    self.pedestal_locked = True
                    continue
            elif choice == "5":
                print("\nThe heavy frame bears deep gouges, as if weapons were tested against it long ago. Beyond lies the metallic tang of oil and steel.")
                pause()
                clear()
                from .Armoury import Armoury
                Armoury().start()
                continue
            elif choice in ("q", "quit"):
                sys.exit(0)
            elif choice in ("inv", "inventory"):
                inventory.show_inventory()
                pause()
                continue
            else:
                print("\nNothing happens. Choose a valid option.")
                pause()
                continue
