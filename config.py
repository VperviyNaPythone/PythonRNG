import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


RARITIES = [
    "Common",
    "Uncommon",
    "Rare",
    "Epic",
    "Arcane",
    "Lily",
    "Overture",
    "BREAKTHROUGH",
]

RARITY_COLORS = {
    "Common": "gray",
    "Uncommon": "green",
    "Rare": "blue",
    "Epic": "#ee00ff",
    "Arcane": "lightcyan",
    "Lily": "#e3ffeb",
    "Overture": "#000a36",
    "BREAKTHROUGH": "white",
}

CHANCES = [50.0, 25.0, 15.0, 6.0, 2.5, 1.0, 0.4, 0.1]
FREE_GLOVE_CHANCES = [47.98, 23.99, 14.39, 8.18, 3.41, 1.36, 0.55, 0.14]
LUCKY_GLOVE_CHANCES = [46.47, 23.23, 13.94, 9.81, 4.09, 1.64, 0.65, 0.17]
