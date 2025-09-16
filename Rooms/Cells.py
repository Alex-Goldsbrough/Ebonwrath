########################################################################################


#                       ░█████╗░███████╗██╗░░░░░██╗░░░░░░██████╗
#                       ██╔══██╗██╔════╝██║░░░░░██║░░░░░██╔════╝
#                       ██║░░╚═╝█████╗░░██║░░░░░██║░░░░░╚█████╗░
#                       ██║░░██╗██╔══╝░░██║░░░░░██║░░░░░░╚═══██╗
#                       ╚█████╔╝███████╗███████╗███████╗██████╔╝
#                       ░╚════╝░╚══════╝╚══════╝╚══════╝╚═════╝░

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

class Cells:
    def start(self):
        while True:
            clear()
            print(r"""
The iron door groans shut behind you, sealing you inside the next chamber. A corridor stretches forward,
lined with rusted barred cells. The stench of damp stone clings to the air, and rotten straw litters the
floor. Scratches and carvings scar the walls, faint echoes of the prisoners who once lingered here. The
silence presses down like a weight.

    How do you wish to continue?
          
    1) Peer into one of the cells.
    2) Search the straw on the floor.
    3) Call out.
    4) Continue forward down the corridor.
""")
            
            choice = input("Enter Selection: ").strip().lower()

            if choice == "1":
                print("""
 ---.----.__..----.----| _|_||___||___||___||___||___||___||_|_ |
    |        |    |    | -.-..---..---..---..---..---..---..-.- |--.-
 ---'--.-----'----'--.-|  | ||   ||   ||   ||   ||   ||   || |  | `|
       |:           (| |  | ||   ||   ||   ||   ||   ||   || |  |--'-
       |:.           | | _|_||___||___||___||___||___||___||_|_ |
 ------'----.-.,----.'-| -.-..---..---..---..---..---..---..-.- |-.--
        ,/) |       |  |  | ||   ||   ||   ||   ||   ||   || |  | |`
 ----.---8--'--.----'--|  | ||   ||   ||   ||   ||   ||   || |  | |
     |   8     |:      | _|_||___||___||___||___||___||___||_|_ |-'--
     | ,)//    |:.     | -.-..---..---..---..---..---..---..-.- |:.
 ----'-`=;'--.-'-.----.|  | ||   ||   ||   ||   ||   ||   || |  |--.-
       //   /_ _( \    |  | ||   ||   ||   ||   ||   ||   || |  | /|
 ---.-//----)/\,'_/----| _|_||___||___||___||___||___||___||_|_ | `|
    |/|     `;=.(      | -.-..---..---..---..---..---..---..-.- |--'-
 (  |`.`.   |`,-/      |,-'-||---||---||---||---||---||---||-'-.|
 -`-'-.`.`-.';'=`.-..--'-.--------.-------------.--.-------.----'--.-
      |  `-./.}{-'\.)    |        )             |   `)     |       \
      |    :`-}{-''||    |:.      |   ,_        |          |:.     |
 ---'`'-.--|`-}{-'||)----'-.------'--'.,`--.----'--------.-'-------'-
        |  :`-`'-'/)|      |               |:.           |
 -.-----'--;`.}{,`.||----,-'--------.------'---.--------,'--.,-------
  |:     ,'/.`..'_(/(    |:         |          |             \
  |:.  ,',' |`--`.('))   |:.        |          |             |:
 -'--,' <.._|__,. >`,----'----------'--------.,'-------------'-------
     ``----....(','
            _,'>'
            )/
            `'

You press your face to the bars and peer inside. In the dim light you make out a skeleton slumped against the wall, a shackle still clasped around its wrist. Its jaw hangs open as though it died mid-scream.
                      """)
                pause()
                continue
            elif choice == "2":
                if not inventory.has_item("brass_medallion"):
                    print("\nBeneath the rotting straw in one cell, your hand closes around something solid. You lift it free: a Brass Medallion, tarnished but intact. Its surface bears the image of a serpent coiled around a crown.")
                    print("\n\033[92mYou pocket the brass medallion into your satchel.\033[0m")
                    inventory.set_item("brass_medallion", True)
                    pause()
                    continue
                else:
                    print("\nYou sift through the rotting straw once more, but find nothing else. Only dust, bones, and the smell of decay remain.")
                    pause()
                    continue
            elif choice == "3":
                print("\nYour voice bounces between the stone walls. For a moment it almost sounds like someone answers, but when you listen again the corridor is empty.")
                pause()
                continue
            elif choice == "4":
                print("\nThe passage narrows and descends steeply. A faint smell of earth and decay fills the air. You emerge into the Catacombs, where rows of stone coffins stretch into the dark.")
                pause()
                clear()
                from .Chamber import Chamber
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
