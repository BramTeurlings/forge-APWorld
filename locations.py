from __future__ import annotations

from pickle import REDUCE
from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ForgeAPWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
boss_locations = {
    "White Boss Defeated": 1,
    "Blue Boss Defeated": 2,
    "Black Boss Defeated": 3,
    "Red Boss Defeated": 4,
    "Green Boss Defeated": 5,
    "Colorless Boss Defeated": 6,
    "WUBRG Boss Defeated": 7,
}

colorless_equipment_shop_locations = {
    "Colorless Equipment Shop - 1": 100,
    "Colorless Equipment Shop - 2": 101,
    "Colorless Equipment Shop - 3": 102,
    "Colorless Equipment Shop - 4": 103,
    "Colorless Equipment Shop - 5": 104,
    "Colorless Equipment Shop - 6": 105,
}

white_equipment_shop_locations = {
    "White Equipment Shop - 1": 200,
    "White Equipment Shop - 2": 201,
    "White Equipment Shop - 3": 202,
    "White Equipment Shop - 4": 203,
    "White Equipment Shop - 5": 204,
    "White Equipment Shop - 6": 205,
}

white_item_shop_locations = {
    "White Item Shop - 1": 206,
    "White Item Shop - 2": 207,
    "White Item Shop - 3": 208,
    "White Item Shop - 4": 209,
    "White Item Shop - 5": 210,
    "White Item Shop - 6": 211,
    "White Item Shop - 7": 212,
    "White Item Shop - 8": 213,
}

blue_equipment_shop_locations = {
    "Blue Equipment Shop - 1": 300,
    "Blue Equipment Shop - 2": 301,
    "Blue Equipment Shop - 3": 302,
    "Blue Equipment Shop - 4": 303,
    "Blue Equipment Shop - 5": 304,
    "Blue Equipment Shop - 6": 305,
}

blue_item_shop_locations = {
    "Blue Item Shop - 1": 306,
    "Blue Item Shop - 2": 307,
    "Blue Item Shop - 3": 308,
    "Blue Item Shop - 4": 309,
    "Blue Item Shop - 5": 310,
    "Blue Item Shop - 6": 311,
    "Blue Item Shop - 7": 312,
    "Blue Item Shop - 8": 313,
}

black_equipment_shop_locations = {
    "Black Equipment Shop - 1": 400,
    "Black Equipment Shop - 2": 401,
    "Black Equipment Shop - 3": 402,
    "Black Equipment Shop - 4": 403,
    "Black Equipment Shop - 5": 404,
    "Black Equipment Shop - 6": 405,
}

black_item_shop_locations = {
    "Black Item Shop - 1": 406,
    "Black Item Shop - 2": 407,
    "Black Item Shop - 3": 408,
    "Black Item Shop - 4": 409,
    "Black Item Shop - 5": 410,
    "Black Item Shop - 6": 411,
    "Black Item Shop - 7": 412,
    "Black Item Shop - 8": 413,
}

red_equipment_shop_locations = {
    "Red Equipment Shop - 1": 500,
    "Red Equipment Shop - 2": 501,
    "Red Equipment Shop - 3": 502,
    "Red Equipment Shop - 4": 503,
    "Red Equipment Shop - 5": 504,
    "Red Equipment Shop - 6": 505,
}

red_item_shop_locations = {
    "Red Item Shop - 1": 506,
    "Red Item Shop - 2": 507,
    "Red Item Shop - 3": 508,
    "Red Item Shop - 4": 509,
    "Red Item Shop - 5": 510,
    "Red Item Shop - 6": 511,
    "Red Item Shop - 7": 512,
    "Red Item Shop - 8": 513,
}

green_equipment_shop_locations = {
    "Green Equipment Shop - 1": 600,
    "Green Equipment Shop - 2": 601,
    "Green Equipment Shop - 3": 602,
    "Green Equipment Shop - 4": 603,
    "Green Equipment Shop - 5": 604,
    "Green Equipment Shop - 6": 605,
}

green_item_shop_locations = {
    "Green Item Shop - 1": 606,
    "Green Item Shop - 2": 607,
    "Green Item Shop - 3": 608,
    "Green Item Shop - 4": 609,
    "Green Item Shop - 5": 610,
    "Green Item Shop - 6": 611,
    "Green Item Shop - 7": 612,
    "Green Item Shop - 8": 613,
}


# colorless 6 shop locations
# colors 6 equipment shop locations 8 item shop locations

# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ForgeAPLocation(Location):
    game = "ForgeAP"

def give_all_locations() -> dict:
    battle_locations = give_default_battle_locations(100)
    event_locations = give_default_event_locations(10)
    quest_locations = give_default_quest_locations(10)
    dungeon_locations = give_default_dungeon_locations(10)

    return {
        **battle_locations,
        **event_locations,
        **quest_locations,
        **dungeon_locations,
        **give_predefined_locations()
    }

def give_predefined_locations() -> dict:
    return {
        **boss_locations,
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
        "Colorless": 1000,
        "White": 1100,
        "Blue": 1200,
        "Black": 1300,
        "Red": 1400,
        "Green": 1500,
    }

    for color, start_id in colors.items():
        for i in range(locations):
            key = f"{color} battle win - {i + 1}"
            location_table[key] = start_id + i
    return location_table

def give_default_event_locations(locations: int) -> dict:
    location_table = {}

    colors = {
        "Colorless": 2000,
        "White": 2100,
        "Blue": 2200,
        "Black": 2300,
        "Red": 2400,
        "Green": 2500,
    }

    for color, start_id in colors.items():
        for i in range(locations):
            key = f"{color} event win - {i + 1}"
            location_table[key] = start_id + i
    return location_table

def give_default_quest_locations(locations: int) -> dict:
    location_table = {}

    colors = {
        "Colorless": 3000,
        "White": 3100,
        "Blue": 3200,
        "Black": 3300,
        "Red": 3400,
        "Green": 3500,
    }

    for color, start_id in colors.items():
        for i in range(locations):
            key = f"{color} quest completion - {i + 1}"
            location_table[key] = start_id + i
    return location_table

def give_default_dungeon_locations(locations: int) -> dict:
    location_table = {}

    colors = {
        "Colorless": 4000,
        "White": 4100,
        "Blue": 4200,
        "Black": 4300,
        "Red": 4400,
        "Green": 4500,
    }

    for color, start_id in colors.items():
        for i in range(locations):
            key = f"{color} dungeon clear - {i + 1}"
            location_table[key] = start_id + i
    return location_table

def setup_locations_with_settings(options) -> None:
    total_locations = {}

    total_locations.update(give_predefined_locations())
    total_locations.update(give_default_battle_locations(options.fightLocations))
    total_locations.update(give_default_event_locations(options.questLocations))
    total_locations.update(give_default_quest_locations(options.eventLocations))
    total_locations.update(give_default_dungeon_locations(options.dungeonLocations))

    return total_locations

# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: give_all_locations()[location_name] for location_name in location_names}


def create_all_locations(world: ForgeAPWorld, location_database : dict) -> None:
    create_regular_locations(world, location_database)
    # create_events(world)


def create_regular_locations(world: ForgeAPWorld, location_database : dict) -> None:
    regions = {
        "Colorless": world.get_region("Colorless"),
        "White": world.get_region("White"),
        "Blue": world.get_region("Blue"),
        "Black": world.get_region("Black"),
        "Red": world.get_region("Red"),
        "Green": world.get_region("Green"),
    }

    # Assign every location automatically
    for location_name, location_id in location_database.items():
        region_name = get_region_name(location_name)

        if region_name is None:
            continue

        regions[region_name].add_locations(
            {location_name: location_id},
            ForgeAPLocation
        )

def get_region_name(location_name: str) -> str | None:
    if location_name.startswith("Colorless"):
        return "Colorless"

    if location_name.startswith("White"):
        return "White"

    # Special case
    if location_name.startswith("WUBRG"):
        return "Blue"

    if location_name.startswith("Blue"):
        return "Blue"

    if location_name.startswith("Black"):
        return "Black"

    if location_name.startswith("Red"):
        return "Red"

    if location_name.startswith("Green"):
        return "Green"

    return None

    # colorless = world.get_region("Colorless")
    # white = world.get_region("White")
    # blue = world.get_region("Blue")
    # black = world.get_region("Black")
    # red = world.get_region("Red")
    # green = world.get_region("Green")
    #
    # colorless.add_locations(colorless_equipment_shop_locations, ForgeAPLocation)
    # colorless.add_locations(get_location_names_with_ids(["Colorless Boss Defeated"]))
    # white.add_locations(white_equipment_shop_locations, ForgeAPLocation)
    # white.add_locations(white_item_shop_locations, ForgeAPLocation)
    # white.add_locations(get_location_names_with_ids(["White Boss Defeated"]))
    # blue.add_locations(blue_equipment_shop_locations, ForgeAPLocation)
    # blue.add_locations(blue_item_shop_locations, ForgeAPLocation)
    # blue.add_locations(get_location_names_with_ids(["Blue Boss Defeated"]))
    # black.add_locations(black_equipment_shop_locations, ForgeAPLocation)
    # black.add_locations(black_item_shop_locations, ForgeAPLocation)
    # black.add_locations(get_location_names_with_ids(["Black Boss Defeated"]))
    # red.add_locations(red_equipment_shop_locations, ForgeAPLocation)
    # red.add_locations(red_item_shop_locations, ForgeAPLocation)
    # red.add_locations(get_location_names_with_ids(["Red Boss Defeated"]))
    # green.add_locations(green_equipment_shop_locations, ForgeAPLocation)
    # green.add_locations(green_item_shop_locations, ForgeAPLocation)
    # green.add_locations(get_location_names_with_ids(["Green Boss Defeated"]))





# def create_events(world: ForgeAPWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    # top_left_room = world.get_region("Top Left Room")
    # final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    # button_in_top_left_room = ForgeAPLocation(world.player, "Top Left Room Button", None, top_left_room)
    # top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    # button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    # button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    # final_boss_room.add_event(
    #     "Final Boss Defeated", "Victory", location_type=ForgeAPLocation, item_type=items.APQuestItem
    # )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
