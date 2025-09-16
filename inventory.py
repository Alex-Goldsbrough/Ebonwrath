import json
import os

FILE = os.path.join(os.path.dirname(__file__), "inventory.json")

# Default starting items
DEFAULT_INVENTORY = {
  "small_silver_key": False,
  "iron_key": False,
  "rusted_lever_handle": False,
  "stone_tablet_fragment": False,
  "rope": False,
  "brass_medallion": False,
  "empty_flask": False,
  "hammer": False,
  "obsidian_shard": False,
  "ancient_coin": False
}

# Internal key -> display name
ITEM_NAMES = {
  "small_silver_key": "A Silver Key",
  "iron_key": "An Iron Key",
  "rusted_lever_handle": "A Rusted Lever Handle",
  "stone_tablet_fragment": "A Stone Tablet Fragment",
  "rope": "Some Rope",
  "brass_medallion": "A Brass Medallion",
  "empty_flask": "An Empty Flask",
  "hammer": "A Hammer",
  "obsidian_shard": "An Obsidian Shard",
  "ancient_coin": "An Ancient Coin"
}

def load_inventory():
    with open(FILE, "r") as f:
        return json.load(f)

def save_inventory(inv):
    with open(FILE, "w") as f:
        json.dump(inv, f, indent=2)

def reset_inventory():
    """Wipe and restore to defaults."""
    save_inventory(DEFAULT_INVENTORY.copy())

def set_item(item, value=True):
    inv = load_inventory()
    inv[item] = value
    save_inventory(inv)

def has_item(item):
    inv = load_inventory()
    return inv.get(item, False)

def show_inventory():
    inv = load_inventory()
    owned = [ITEM_NAMES.get(k, k.replace("_", " ").title()) for k, v in inv.items() if v]

    if not owned:
        print("\nYou open your satchel. It is empty.")
        return

    print("\nYou open your satchel. Inside you have:")
    for name in owned:
        print(f"  {name}")
