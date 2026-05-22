from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ForgeAPWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.

# TODO: Build this list dynamically based on the yaml options
PROGRESSION = {
    "White Rune": 1,
    "Blue Rune": 2,
    "Black Rune": 3,
    "Red Rune": 4,
    "Green Rune": 5,
}

FILLER = {
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
}

COLORSANITY = {
    "Unlock White": 2000,
    "Unlock Blue": 2001,
    "Unlock Black": 2002,
    "Unlock Red": 2003,
    "Unlock Green": 2004,
}

EQUIPMENT = {
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
}

POWER_EQUIPMENT = {
    "Sol Ring": 4000,
    "Black Lotus": 4001,
    "Mox Pearl": 4002,
    "Mox Sapphire": 4003,
    "Mox Jet": 4004,
    "Mox Ruby": 4005,
    "Mox Emerald": 4006,
}

CHEAT_EQUIPMENT = {
    "Cheat": 5000,
}

# CUSTOM_EQUIPMENT = {
#     "Custom item 1": 10000
# }

ITEM_TABLE = {
    **PROGRESSION,
    **FILLER,
    **COLORSANITY,
    **EQUIPMENT,
    **POWER_EQUIPMENT,
    **CHEAT_EQUIPMENT,
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.

PROGRESSION_ITEM_CLASSIFICATIONS = {
    "White Rune": ItemClassification.progression,
    "Blue Rune": ItemClassification.progression,
    "Black Rune": ItemClassification.progression,
    "Red Rune": ItemClassification.progression,
    "Green Rune": ItemClassification.progression,
}

FILLER_ITEM_CLASSIFICATIONS = {
    "Mana Crystals": ItemClassification.filler,
    "Gold": ItemClassification.filler,
    "Gold Challenge Coin": ItemClassification.filler,
    "Silver Challenge Coin": ItemClassification.filler,
    "Bronze Challenge Coin": ItemClassification.filler,
    "Set Unlock": ItemClassification.useful,
}

COLORSANITY_ITEM_CLASSIFICATIONS = {
    "Unlock White": ItemClassification.progression,
    "Unlock Blue": ItemClassification.progression,
    "Unlock Black": ItemClassification.progression,
    "Unlock Red": ItemClassification.progression,
    "Unlock Green": ItemClassification.progression,
}

EQUIPMENT_ITEM_CLASSIFICATIONS = {
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
}

POWER_EQUIPMENT_ITEM_CLASSIFICATIONS = {
    "Sol Ring": ItemClassification.useful,
    "Mox Emerald": ItemClassification.useful,
    "Black Lotus": ItemClassification.useful,
    "Mox Jet": ItemClassification.useful,
    "Mox Pearl": ItemClassification.useful,
    "Mox Ruby": ItemClassification.useful,
    "Mox Sapphire": ItemClassification.useful,
}

CHEAT_EQUIPMENT_ITEM_CLASSIFICATIONS = {
    "Cheat": ItemClassification.useful,
}

ITEM_CLASSIFICATION_TABLE = {
    **PROGRESSION_ITEM_CLASSIFICATIONS,
    **FILLER_ITEM_CLASSIFICATIONS,
    **COLORSANITY_ITEM_CLASSIFICATIONS,
    **EQUIPMENT_ITEM_CLASSIFICATIONS,
    **POWER_EQUIPMENT_ITEM_CLASSIFICATIONS,
    **CHEAT_EQUIPMENT_ITEM_CLASSIFICATIONS,
}

    # "Sword": ItemClassification.progression | ItemClassification.useful,  # Items can have multiple classifications.
    # "Shield": ItemClassification.progression,
    # "Hammer": ItemClassification.progression,
    # "Health Upgrade": ItemClassification.useful,
    # "Confetti Cannon": ItemClassification.filler,
    # "Math Trap": ItemClassification.trap,

# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class ForgeAPItem(Item):
    game = "ForgeAP"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: ForgeAPWorld) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    # if world.random.randint(0, 99) < world.options.trap_chance:
    #     return "Math Trap"
    return "Set Unlock"


def create_item_with_correct_classification(world: ForgeAPWorld, name: str) -> ForgeAPItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = ITEM_CLASSIFICATION_TABLE[name]

    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    # if name == "Health Upgrade" and world.options.hard_mode:
    #     classification = ItemClassification.progression

    return ForgeAPItem(name, classification, ITEM_TABLE[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: ForgeAPWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
        world.create_item("White Rune"),
        world.create_item("Blue Rune"),
        world.create_item("Black Rune"),
        world.create_item("Red Rune"),
        world.create_item("Green Rune"),
    ]

    # Some items may only exist if the player enables certain options.
    # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # Otherwise, we add a filler Confetti Cannon.
    # if world.options.hammer:
        # Once again, it is important to stress that even though the Hammer doesn't always exist,
        # it must be present in the worlds item_name_to_id.
        # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
        # itempool.append(world.create_item("Hammer"))

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    # TODO: Filler pool creation. Be able to provide a set quantity of filler items. (for ex. set unlocks)
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().

    # TODO: Define starting options
    # if world.options.start_with_one_confetti_cannon:
    #     # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
    #     starting_confetti_cannon = world.create_item("Confetti Cannon")
    #     world.push_precollected(starting_confetti_cannon)
