from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ForgeAPWorld

item_table_progression = {
    "White Rune": 1,
    "Blue Rune": 2,
    "Black Rune": 3,
    "Red Rune": 4,
    "Green Rune": 5,
}

item_table_filler = {
    "Gold (S)": 1000,
    "Gold (M)": 1001,
    "Gold (L)": 1002,
    "Mana Shards (S)": 1003,
    "Mana Shards (M)": 1004,
    "Mana Shards (L)": 1005,
    "Bronze Challenge Coin": 1006,
    "Silver Challenge Coin": 1007,
    "Gold Challenge Coin": 1008,
    "Set Unlock": 1009,
    "Life +1": 1010,
    "Life +2": 1011,
}

item_table_colors = {
    "Unlock White": 2000,
    "Unlock Blue": 2001,
    "Unlock Black": 2002,
    "Unlock Red": 2003,
    "Unlock Green": 2004,
}

item_table_equipment_default = {
    "Chandra's Tome": 3000,
    "Phoenix Charm": 3001,
    "Demonic Contract": 3002,
    "Piper's Charm": 3003,
    "Sleep Wand": 3004,
    "Hill Giant Club": 3005,
    "Cursed Treasure": 3006,
    "Farmer's Tools": 3007,
    "Battle Standard": 3008,
    "Hivestone": 3009,
    "Life Amulet": 3010,
    "Axt": 3011,
    "Bronze Sword": 3012,
    "Iron Boots": 3013,
    "Iron Shield": 3014,
    "Iron Armor": 3015,
    "Steel Sword": 3016,
    "Steel Boots": 3017,
    "Steel Shield": 3018,
    "Steel Armor": 3019,
    "Armor of the Hivelord": 3020,
    "Leather Boots": 3021,
    "Jungle Shield": 3022,
    "Sorin's Amulet": 3023,
    "Dagger": 3024,
    "Aladdin's Ring": 3025,
    "Spell Book": 3026,
    "Cursed Ring": 3027,
    "Mithril Boots": 3028,
    "Mithril Shield": 3029,
    "Mithril Armor": 3030,
    "Presence of the Hydra": 3031,
    "Death Ring": 3032,
    "Flame Sword": 3033,
    "Mirror Shield": 3034,
    "Dungeon Map": 3035,
    "Aladdin's Lamp": 3036,
    "Heart-Piercer": 3037,
    "Wood Bow": 3038,
    "Sandals": 3039,
    "Gold Boots": 3040,
    "Gold Shield": 3041,
    "Gold Armor": 3042,
    "Dark Boots": 3043,
    "Dark Shield": 3044,
    "Dark Armor": 3045,
    "Blood Vial": 3046,
    "Charm": 3047,
    "Snack": 3048,
    "Change": 3049,
    "Treasure": 3050,
    "Magic Shard": 3051,
    "Mad Staff": 3052,
    "Dark Amulet": 3053,
    "Pandora's Box": 3054,
    "Disrupting Scepter": 3055,
    "Entrancing Lyre": 3056,
    "Heavy Arbalest": 3057,
    "Ring of Three Wishes": 3058,
    "The Blackstaff of Waterdeep": 3059,
    "Unerring Sling": 3060,
    "Jeweled Amulet": 3061,
    "Traveler's Amulet": 3062,
    "Relic Amulet": 3063,
    "Amulet of Kroog": 3064,
    "Amulet of Vigor": 3065,
    "Veilstone Amulet": 3066,
    "Jandor's Ring": 3067,
    "Jinxed Ring": 3068,
    "Nine-Ringed Bo": 3069,
    "Ring of Immortals": 3070,
    "Prism Ring": 3071,
    "Ring of Renewal": 3072,
    "Kite Shield": 3073,
    "Shell Wand": 3074,
    "Manasight Amulet": 3075,
    "Lightbringers Boots": 3076,
    "Fortune Coin": 3077,
    "White Staff": 3078,
    "Black Staff": 3079,
    "Blue Staff": 3080,
    "Red Staff": 3081,
    "Green Staff": 3082,
    "Slimefoot's Slimy Staff": 3083,
    "Kiora's Bident": 3084,
    "Slime-Covered Boots": 3085,
    "Amulet of the Deceiver": 3086,
    "Jace's Signature Hoodie": 3087,
    "Teferi's Staff": 3088,
    "Garruk's Mighty Axe": 3089,
    "Nahiri's Armory": 3090,
    "Giant Scythe": 3091,
    "Chicken Egg": 3092,
    "Tibalt's Bag of Tricks": 3093,
    "Xira's Fancy Hat": 3094,
    "The Underworld Cookbook": 3095,
    "Mantle of Ancient Lore": 3096,
    "Zedruu's Lantern": 3097,
    "Grolnok's Skin": 3098,
    "Slobad's Iron Boots": 3099,
    "Hallowed Sigil": 3100,
    "Unhallowed Sigil": 3101,
    "Basilisk Collar": 3102,
    "Evil Ankh": 3103,
    "Staff of the Demoncaller": 3104,
    "Concordant Boots": 3105,
    "Crown of Growth": 3106,
    "Raptor Bondband": 3107,
    "Mantle of Denial": 3108,
    "Golden Egg": 3109,
    "Amulet of Telepathy": 3110,
    "Warren Tender's Baton": 3111,
    "Prayerbook of Ire": 3112,
    "Robes of Omniscience": 3113,
    "Angelic Armaments": 3114,
    "Angelic Greaves": 3115,
}

item_table_equipment_power = {
    "Sol Ring": 4000,
    "Black Lotus": 4001,
    "Mox Pearl": 4002,
    "Mox Sapphire": 4003,
    "Mox Jet": 4004,
    "Mox Ruby": 4005,
    "Mox Emerald": 4006,
}

item_table_equipment_cheat = {
    "Cheat": 5000,
}

# CUSTOM_EQUIPMENT = {
#     "Custom item 1": 10000
# }

item_table = {
    **item_table_progression,
    **item_table_filler,
    **item_table_colors,
    **item_table_equipment_default,
    **item_table_equipment_power,
    **item_table_equipment_cheat,
}

item_classifications_progression = {
    "White Rune": ItemClassification.progression,
    "Blue Rune": ItemClassification.progression,
    "Black Rune": ItemClassification.progression,
    "Red Rune": ItemClassification.progression,
    "Green Rune": ItemClassification.progression,
}

item_classifications_filler = {
    "Gold (S)": ItemClassification.filler,
    "Gold (M)": ItemClassification.filler,
    "Gold (L)": ItemClassification.filler,
    "Mana Shards (S)": ItemClassification.filler,
    "Mana Shards (M)": ItemClassification.filler,
    "Mana Shards (L)": ItemClassification.filler,
    "Bronze Challenge Coin": ItemClassification.filler,
    "Silver Challenge Coin": ItemClassification.filler,
    "Gold Challenge Coin": ItemClassification.filler,
    "Set Unlock": ItemClassification.useful,
    "Life +1": ItemClassification.useful,
    "Life +2": ItemClassification.useful,
}

item_classifications_colorsanity = {
    "Unlock White": ItemClassification.progression,
    "Unlock Blue": ItemClassification.progression,
    "Unlock Black": ItemClassification.progression,
    "Unlock Red": ItemClassification.progression,
    "Unlock Green": ItemClassification.progression,
}

item_classifications_equipment_standard = {
    "Chandra's Tome": ItemClassification.useful,
    "Phoenix Charm": ItemClassification.useful,
    "Demonic Contract": ItemClassification.useful,
    "Piper's Charm": ItemClassification.useful,
    "Sleep Wand": ItemClassification.useful,
    "Hill Giant Club": ItemClassification.useful,
    "Cursed Treasure": ItemClassification.useful,
    "Farmer's Tools": ItemClassification.useful,
    "Battle Standard": ItemClassification.useful,
    "Hivestone": ItemClassification.useful,
    "Life Amulet": ItemClassification.useful,
    "Axt": ItemClassification.useful,
    "Bronze Sword": ItemClassification.useful,
    "Iron Boots": ItemClassification.useful,
    "Iron Shield": ItemClassification.useful,
    "Iron Armor": ItemClassification.useful,
    "Steel Sword": ItemClassification.useful,
    "Steel Boots": ItemClassification.useful,
    "Steel Shield": ItemClassification.useful,
    "Steel Armor": ItemClassification.useful,
    "Armor of the Hivelord": ItemClassification.useful,
    "Leather Boots": ItemClassification.useful,
    "Jungle Shield": ItemClassification.useful,
    "Sorin's Amulet": ItemClassification.useful,
    "Dagger": ItemClassification.useful,
    "Aladdin's Ring": ItemClassification.useful,
    "Spell Book": ItemClassification.useful,
    "Cursed Ring": ItemClassification.useful,
    "Mithril Boots": ItemClassification.useful,
    "Mithril Shield": ItemClassification.useful,
    "Mithril Armor": ItemClassification.useful,
    "Presence of the Hydra": ItemClassification.useful,
    "Death Ring": ItemClassification.useful,
    "Flame Sword": ItemClassification.useful,
    "Mirror Shield": ItemClassification.useful,
    "Dungeon Map": ItemClassification.useful,
    "Aladdin's Lamp": ItemClassification.useful,
    "Heart-Piercer": ItemClassification.useful,
    "Wood Bow": ItemClassification.useful,
    "Sandals": ItemClassification.useful,
    "Gold Boots": ItemClassification.useful,
    "Gold Shield": ItemClassification.useful,
    "Gold Armor": ItemClassification.useful,
    "Dark Boots": ItemClassification.useful,
    "Dark Shield": ItemClassification.useful,
    "Dark Armor": ItemClassification.useful,
    "Blood Vial": ItemClassification.useful,
    "Charm": ItemClassification.useful,
    "Snack": ItemClassification.useful,
    "Change": ItemClassification.useful,
    "Treasure": ItemClassification.useful,
    "Magic Shard": ItemClassification.useful,
    "Mad Staff": ItemClassification.useful,
    "Dark Amulet": ItemClassification.useful,
    "Pandora's Box": ItemClassification.useful,
    "Disrupting Scepter": ItemClassification.useful,
    "Entrancing Lyre": ItemClassification.useful,
    "Heavy Arbalest": ItemClassification.useful,
    "Ring of Three Wishes": ItemClassification.useful,
    "The Blackstaff of Waterdeep": ItemClassification.useful,
    "Unerring Sling": ItemClassification.useful,
    "Jeweled Amulet": ItemClassification.useful,
    "Traveler's Amulet": ItemClassification.useful,
    "Relic Amulet": ItemClassification.useful,
    "Amulet of Kroog": ItemClassification.useful,
    "Amulet of Vigor": ItemClassification.useful,
    "Veilstone Amulet": ItemClassification.useful,
    "Jandor's Ring": ItemClassification.useful,
    "Jinxed Ring": ItemClassification.useful,
    "Nine-Ringed Bo": ItemClassification.useful,
    "Ring of Immortals": ItemClassification.useful,
    "Prism Ring": ItemClassification.useful,
    "Ring of Renewal": ItemClassification.useful,
    "Kite Shield": ItemClassification.useful,
    "Shell Wand": ItemClassification.useful,
    "Manasight Amulet": ItemClassification.useful,
    "Lightbringers Boots": ItemClassification.useful,
    "Fortune Coin": ItemClassification.useful,
    "White Staff": ItemClassification.useful,
    "Black Staff": ItemClassification.useful,
    "Blue Staff": ItemClassification.useful,
    "Red Staff": ItemClassification.useful,
    "Green Staff": ItemClassification.useful,
    "Slimefoot's Slimy Staff": ItemClassification.useful,
    "Kiora's Bident": ItemClassification.useful,
    "Slime-Covered Boots": ItemClassification.useful,
    "Amulet of the Deceiver": ItemClassification.useful,
    "Jace's Signature Hoodie": ItemClassification.useful,
    "Teferi's Staff": ItemClassification.useful,
    "Garruk's Mighty Axe": ItemClassification.useful,
    "Nahiri's Armory": ItemClassification.useful,
    "Giant Scythe": ItemClassification.useful,
    "Chicken Egg": ItemClassification.useful,
    "Tibalt's Bag of Tricks": ItemClassification.useful,
    "Xira's Fancy Hat": ItemClassification.useful,
    "The Underworld Cookbook": ItemClassification.useful,
    "Mantle of Ancient Lore": ItemClassification.useful,
    "Zedruu's Lantern": ItemClassification.useful,
    "Grolnok's Skin": ItemClassification.useful,
    "Slobad's Iron Boots": ItemClassification.useful,
    "Hallowed Sigil": ItemClassification.useful,
    "Unhallowed Sigil": ItemClassification.useful,
    "Basilisk Collar": ItemClassification.useful,
    "Evil Ankh": ItemClassification.useful,
    "Staff of the Demoncaller": ItemClassification.useful,
    "Concordant Boots": ItemClassification.useful,
    "Crown of Growth": ItemClassification.useful,
    "Raptor Bondband": ItemClassification.useful,
    "Mantle of Denial": ItemClassification.useful,
    "Golden Egg": ItemClassification.useful,
    "Amulet of Telepathy": ItemClassification.useful,
    "Warren Tender's Baton": ItemClassification.useful,
    "Prayerbook of Ire": ItemClassification.useful,
    "Robes of Omniscience": ItemClassification.useful,
    "Angelic Armaments": ItemClassification.useful,
    "Angelic Greaves": ItemClassification.useful,
}

item_classifications_equipment_power = {
    "Sol Ring": ItemClassification.useful,
    "Mox Emerald": ItemClassification.useful,
    "Black Lotus": ItemClassification.useful,
    "Mox Jet": ItemClassification.useful,
    "Mox Pearl": ItemClassification.useful,
    "Mox Ruby": ItemClassification.useful,
    "Mox Sapphire": ItemClassification.useful,
}

item_classifications_equipment_cheat = {
    "Cheat": ItemClassification.useful,
}

item_classification_table = {
    **item_classifications_progression,
    **item_classifications_filler,
    **item_classifications_colorsanity,
    **item_classifications_equipment_standard,
    **item_classifications_equipment_power,
    **item_classifications_equipment_cheat,
}

class ForgeAPItem(Item):
    game = "ForgeAP"

def give_possible_equipment(options) -> dict:
    possible_equipment = dict(item_table_equipment_default)
    if options.include_power:
        possible_equipment.update(item_table_equipment_power)
    if options.include_cheat:
        possible_equipment.update(item_table_equipment_cheat)

    return possible_equipment

def create_item_with_correct_classification(world: ForgeAPWorld, name: str) -> ForgeAPItem:
    classification = item_classification_table[name]

    return ForgeAPItem(name, classification, item_table[name], world.player)


def create_all_items(world: ForgeAPWorld) -> None:
    itempool: list[Item] = [
        world.create_item("White Rune"),
        world.create_item("Blue Rune"),
        world.create_item("Black Rune"),
        world.create_item("Red Rune"),
        world.create_item("Green Rune"),
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
