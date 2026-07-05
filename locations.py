from __future__ import annotations

from pickle import REDUCE
from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ForgeAPWorld

boss_locations = {
    "Emrakul Victory": 1,
    "Akroma Victory": 2,
    "Lorthos Victory": 3,
    "Griselbrand Victory": 4,
    "Lathliss Victory": 5,
    "Ghalta Victory": 6,
}

boss_loot_locations = {
    "Akroma Defeated": 12,
    "Lorthos Defeated": 13,
    "Griselbrand Defeated": 14,
    "Lathliss Defeated": 15,
    "Ghalta Defeated": 16,
}

miniboss_locations = {
    "Slime Mother Defeated": 100,
    "Slobad Defeated": 101,
    "Xira Defeated": 102,
    "Nahiri Defeated": 200,
    "Valyx Defeated": 201,
    "Jace Defeated": 300,
    "Kiora Defeated": 301,
    "Myr Superion Defeated": 302,
    "Sliver Queen Defeated": 303,
    "Teferi Defeated": 304,
    "Grolnok Defeated": 400,
    "Guardian Angel Defeated": 401,
    "Liliana Defeated": 402,
    "Slimefoot Defeated": 403,
    "Sorin Defeated": 404,
    "Chandra Defeated": 500,
    "Tibalt's Torturer Defeated": 501,
    "Tibalt Defeated": 502,
    "Zedruu's Cook Defeated": 503,
    "Conjurer Defeated": 504,
    "Zedruu Defeated": 505,
    "Garruk Defeated": 600,
    "Hydra of Shandalaar Defeated": 601,
    "Scarecrow Captain Defeated": 602
}

colorless_equipment_shop_locations = {
    "Colorless Equipment Shop - 1": 1000,
    "Colorless Equipment Shop - 2": 1001,
    "Colorless Equipment Shop - 3": 1002,
    "Colorless Equipment Shop - 4": 1003,
    "Colorless Equipment Shop - 5": 1004,
    "Colorless Equipment Shop - 6": 1005,
}

white_equipment_shop_locations = {
    "White Equipment Shop - 1": 1100,
    "White Equipment Shop - 2": 1101,
    "White Equipment Shop - 3": 1102,
    "White Equipment Shop - 4": 1103,
    "White Equipment Shop - 5": 1104,
    "White Equipment Shop - 6": 1105,
}

white_item_shop_locations = {
    "White Item Shop - 1": 1200,
    "White Item Shop - 2": 1201,
    "White Item Shop - 3": 1202,
    "White Item Shop - 4": 1203,
    "White Item Shop - 5": 1204,
    "White Item Shop - 6": 1205,
    "White Item Shop - 7": 1206,
    "White Item Shop - 8": 1207,
}

blue_equipment_shop_locations = {
    "Blue Equipment Shop - 1": 1300,
    "Blue Equipment Shop - 2": 1301,
    "Blue Equipment Shop - 3": 1302,
    "Blue Equipment Shop - 4": 1303,
    "Blue Equipment Shop - 5": 1304,
    "Blue Equipment Shop - 6": 1305,
}

blue_item_shop_locations = {
    "Blue Item Shop - 1": 1400,
    "Blue Item Shop - 2": 1401,
    "Blue Item Shop - 3": 1402,
    "Blue Item Shop - 4": 1403,
    "Blue Item Shop - 5": 1404,
    "Blue Item Shop - 6": 1405,
    "Blue Item Shop - 7": 1406,
    "Blue Item Shop - 8": 1407,
}

black_equipment_shop_locations = {
    "Black Equipment Shop - 1": 1500,
    "Black Equipment Shop - 2": 1501,
    "Black Equipment Shop - 3": 1502,
    "Black Equipment Shop - 4": 1503,
    "Black Equipment Shop - 5": 1504,
    "Black Equipment Shop - 6": 1505,
}

black_item_shop_locations = {
    "Black Item Shop - 1": 1600,
    "Black Item Shop - 2": 1601,
    "Black Item Shop - 3": 1602,
    "Black Item Shop - 4": 1603,
    "Black Item Shop - 5": 1604,
    "Black Item Shop - 6": 1605,
    "Black Item Shop - 7": 1606,
    "Black Item Shop - 8": 1607,
}

red_equipment_shop_locations = {
    "Red Equipment Shop - 1": 1700,
    "Red Equipment Shop - 2": 1701,
    "Red Equipment Shop - 3": 1702,
    "Red Equipment Shop - 4": 1703,
    "Red Equipment Shop - 5": 1704,
    "Red Equipment Shop - 6": 1705,
}

red_item_shop_locations = {
    "Red Item Shop - 1": 1800,
    "Red Item Shop - 2": 1801,
    "Red Item Shop - 3": 1802,
    "Red Item Shop - 4": 1803,
    "Red Item Shop - 5": 1804,
    "Red Item Shop - 6": 1805,
    "Red Item Shop - 7": 1806,
    "Red Item Shop - 8": 1807,
}

green_equipment_shop_locations = {
    "Green Equipment Shop - 1": 1900,
    "Green Equipment Shop - 2": 1901,
    "Green Equipment Shop - 3": 1902,
    "Green Equipment Shop - 4": 1903,
    "Green Equipment Shop - 5": 1904,
    "Green Equipment Shop - 6": 1905,
}

green_item_shop_locations = {
    "Green Item Shop - 1": 2000,
    "Green Item Shop - 2": 2001,
    "Green Item Shop - 3": 2002,
    "Green Item Shop - 4": 2003,
    "Green Item Shop - 5": 2004,
    "Green Item Shop - 6": 2005,
    "Green Item Shop - 7": 2006,
    "Green Item Shop - 8": 2007,
}

class ForgeAPLocation(Location):
    game = "ForgeAP"

def give_all_locations() -> dict:
    battle_locations = give_default_battle_locations(100)
    event_locations = give_default_event_locations(10)
    quest_locations = give_default_quest_locations(10)
    common_locations = give_default_common_card_locations(10)
    uncommon_locations = give_default_uncommon_card_locations(10)
    rare_locations = give_default_rare_card_locations(10)
    mythic_rare_locations = give_default_mythic_rare_card_locations(10)

    return {
        **give_predefined_locations(),
        **battle_locations,
        **event_locations,
        **quest_locations,
        **common_locations,
        **uncommon_locations,
        **rare_locations,
        **mythic_rare_locations,
        **miniboss_locations,
    }

def give_predefined_locations() -> dict:
    return {
        **boss_locations,
        **boss_loot_locations,
        **colorless_equipment_shop_locations,
        **white_equipment_shop_locations,
        **white_item_shop_locations,
        **blue_equipment_shop_locations,
        **blue_item_shop_locations,
        **black_equipment_shop_locations,
        **black_item_shop_locations,
        **red_equipment_shop_locations,
        **red_item_shop_locations,
        **green_equipment_shop_locations,
        **green_item_shop_locations,
    }

def give_default_battle_locations(locations: int) -> dict:
    location_table = {}

    colors = {
        "Colorless": 10000,
        "White": 20000,
        "Blue": 30000,
        "Black": 40000,
        "Red": 50000,
        "Green": 60000,
    }

    for color, start_id in colors.items():
        for i in range(locations):
            key = f"{color} battle win - {i + 1}"
            location_table[key] = start_id + i
    return location_table

def give_default_event_locations(locations: int) -> dict:
    location_table = {}

    colors = {
        "Colorless": 11000,
        "White": 21000,
        "Blue": 31000,
        "Black": 41000,
        "Red": 51000,
        "Green": 61000,
    }

    for color, start_id in colors.items():
        for i in range(locations):
            key = f"{color} event completion - {i + 1}"
            location_table[key] = start_id + i
    return location_table

def give_default_quest_locations(locations: int) -> dict:
    location_table = {}

    colors = {
        "Colorless": 12000,
        "White": 22000,
        "Blue": 32000,
        "Black": 42000,
        "Red": 52000,
        "Green": 62000,
    }

    for color, start_id in colors.items():
        for i in range(locations):
            key = f"{color} quest completion - {i + 1}"
            location_table[key] = start_id + i
    return location_table

def give_default_common_card_locations(locations: int) -> dict:
    location_table = {}
    start_id = 5000

    for i in range(locations):
        key = f"Common cards collected - {(i + 1)}"
        location_table[key] = start_id + i

    return location_table

def give_default_uncommon_card_locations(locations: int) -> dict:
    location_table = {}
    start_id = 5100

    for i in range(locations):
        key = f"Uncommon cards collected - {(i + 1)}"
        location_table[key] = start_id + i

    return location_table

def give_default_rare_card_locations(locations: int) -> dict:
    location_table = {}
    start_id = 5200

    for i in range(locations):
        key = f"Rare cards collected - {(i + 1)}"
        location_table[key] = start_id + i

    return location_table

def give_default_mythic_rare_card_locations(locations: int) -> dict:
    location_table = {}
    start_id = 5300

    for i in range(locations):
        key = f"Mythic Rare cards collected - {(i + 1)}"
        location_table[key] = start_id + i

    return location_table

def setup_locations_with_settings(options) -> None:
    total_locations = {}

    total_locations.update(give_predefined_locations())
    total_locations.update(give_default_battle_locations(options.fight_locations))
    total_locations.update(give_default_event_locations(options.quest_locations))
    total_locations.update(give_default_quest_locations(options.event_locations))
    total_locations.update(give_default_common_card_locations(options.common_card_locations))
    total_locations.update(give_default_uncommon_card_locations(options.uncommon_card_locations))
    total_locations.update(give_default_rare_card_locations(options.rare_card_locations))
    total_locations.update(give_default_mythic_rare_card_locations(options.mythic_rare_card_locations))

    if options.include_miniboss_locations:
        total_locations.update(miniboss_locations)

    return total_locations

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: give_all_locations()[location_name] for location_name in location_names}

def create_all_locations(world: ForgeAPWorld, location_database : dict) -> None:
    create_regular_locations(world, location_database)
    create_events(world)

def create_regular_locations(world: ForgeAPWorld, location_database : dict) -> None:
    colorless = world.get_region("Colorless")
    white = world.get_region("White")
    blue = world.get_region("Blue")
    black = world.get_region("Black")
    red = world.get_region("Red")
    green = world.get_region("Green")

    for location_name, location_id in location_database.items():
        if location_id == 1 or 100 <= location_id < 200 or 1000 <= location_id < 1100 or 5000 <= location_id < 5400 or 10000 <= location_id < 20000:
            colorless.add_locations({location_name: location_id}, ForgeAPLocation)
        if location_id == 2 or location_id == 12 or 200 <= location_id < 300 or 1100 <= location_id < 1300 or 20000 <= location_id < 30000:
            white.add_locations({location_name: location_id}, ForgeAPLocation)
        if location_id == 3 or location_id == 13 or 300 <= location_id < 400 or 1300 <= location_id < 1500 or 30000 <= location_id < 40000:
            blue.add_locations({location_name: location_id}, ForgeAPLocation)
        if location_id == 4 or location_id == 14 or 400 <= location_id < 500 or 1500 <= location_id < 1700 or 40000 <= location_id < 50000:
            black.add_locations({location_name: location_id}, ForgeAPLocation)
        if location_id == 5 or location_id == 15 or 500 <= location_id < 600 or 1700 <= location_id < 1900 or 50000 <= location_id < 60000:
            red.add_locations({location_name: location_id}, ForgeAPLocation)
        if location_id == 6 or location_id == 16 or 600 <= location_id < 700 or 1900 <= location_id < 2100 or 60000 <= location_id < 70000:
            green.add_locations({location_name: location_id}, ForgeAPLocation)
    return None

def create_events(world: ForgeAPWorld) -> None:
    castle_bosses = [
        ("Colorless", "Emrakul"),
        ("White", "Akroma"),
        ("Blue", "Lorthos"),
        ("Black", "Griselbrand"),
        ("Red", "Lathliss"),
        ("Green", "Ghalta"),
    ]

    for region_name, boss_name in castle_bosses:
        world.get_region(region_name).add_event(
            f"{boss_name} Victory",
            f"{boss_name} Victory",
            location_type=ForgeAPLocation,
            item_type=items.ForgeAPItem,
        )
