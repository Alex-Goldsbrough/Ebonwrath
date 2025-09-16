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

class Pedestal:
    def start(self):
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
The cracked pedestal rises before you, its stone surface coated in dust. As you draw closer,
you notice a faint groove circling the top like a scar, and small holes pockmarking the surrounding
walls. The air feels tense, as if the chamber itself is waiting for you to make a mistake.


    How do you wish to continue?
          
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
                continue
            elif choice == "2":
                print("\nA quiet click sounds, and the pressure in the room lifts. The pedestal cracks suddenly, splitting down the middle. Stone crumbles away as the mechanism inside seizes and tears itself apart." \
                " Amid the rubble, you recover a Stone Tablet Fragment—the only thing spared from destruction.")
                print("\n\033[91mYou can no longer examine the pedestal.\033[0m")
                pause()
                inventory.set_item("stone_tablet_fragment", True)
                inventory.set_item("pedestal_locked", True)
                return
            elif choice == "3":
                print("\nThe brittle stone shatters, collapsing into rubble. Dust floods the air as the trap discharges harmlessly into the ruins. You survive, but the pedestal’s secret is destroyed.")
                print("\n\033[91mYou can no longer examine the pedestal.\033[0m")
                inventory.set_item("pedestal_locked", True)
                pause()
                return
            elif choice == "4":
                print("\nYou walk away from the pedestal.")
                pause()
                clear()
                from Rooms.Chamber import Chamber
                Chamber().start()
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
