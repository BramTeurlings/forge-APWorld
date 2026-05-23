import string
from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as forgeap_options  # rename due to a name conflict with World.options

# APQuest will go through all the parts of the world api one step at a time,
# with many examples and comments across multiple files.
# If you'd rather read one continuous document, or just like reading multiple sources,
# we also have this document specifying the entire world api:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md


# The world class is the heart and soul of an apworld implementation.
# It holds all the data and functions required to build the world and submit it to the multiworld generator.
# You could have all your world code in just this one class, but for readability and better structure,
# it is common to split up world functionality into multiple files.
# This implementation in particular has the following additional files, each covering one topic:
# regions.py, locations.py, rules.py, items.py, options.py and web_world.py.
# It is recommended that you read these in that specific order, then come back to the world class.
class ForgeAPWorld(World):
    """
    APQuest is a minimal 8bit-era inspired adventure game with grid-like movement.
    Good games don't need more than six checks.
    """

    # The docstring should contain a description of the game, to be displayed on the WebHost.

    # You must override the "game" field to say the name of the game.
    game = "ForgeAP"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.ForgeAPWebWorld()

    # This is how we associate the options defined in our options.py with our world.
    # (Note: options.py has been imported as "apquest_options" at the top of this file to avoid a name conflict)
    options_dataclass = forgeap_options.ForgeAPOptions
    options: forgeap_options.ForgeAPOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = locations.give_all_locations()
    item_name_to_id = items.item_table

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Colorless"

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        local_location_table = locations.setup_locations_with_settings(self.options).copy()
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self, local_location_table)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        local_location_table = locations.setup_locations_with_settings(self.options)
        pool = []

        # Progression Items
        for name, data in items.item_table_progression.items():
            pool.append(self.create_item(name))

        # Optional sanity
        if self.options.colorSanity:
            for name, data in items.item_table_colors.items():
                if self.should_ignore_color(name):
                    continue
                pool.append(self.create_item(name))

        remaining_slots = len(local_location_table) - len(pool)

        # -------------------------
        # Raw weights
        # -------------------------
        weights = {
            "set_unlock": self.options.setUnlocksPercentage,
            "gold": self.options.goldPercentage,
            "mana": self.options.manaShardPercentage,
            "coin": self.options.challengeCoinPercentage,
            "equipment": self.options.equipmentPercentage,
        }

        total_weight = sum(weights.values())
        if total_weight <= 0:
            return # should be impossible

        norm = {k: v / total_weight for k, v in weights.items()}

        possible_equipment = items.give_possible_equipment(self.options)
        max_equipment = len(possible_equipment)

        # -------------------------
        # STEP 1: determine equipment demand
        # -------------------------

        desired_equipment = int(remaining_slots * norm["equipment"])
        equipment_to_place = min(desired_equipment, max_equipment)
        equipment_used_as_fixed = False

        if self.options.tryIncludeAllEquipment:
            # MUST fit ALL equipment or we ignore this mode completely
            if remaining_slots - len(possible_equipment) >= 1:
                for name, data in possible_equipment:
                    pool.append(self.create_item(name))

                equipment_used_as_fixed = True
                equipment_to_place = 0
                remaining_slots -= len(possible_equipment)

        remaining_after_equipment = remaining_slots - equipment_to_place

        # -------------------------
        # STEP 2: redistribute weights if equipment is capped
        # -------------------------

        alloc_weights = {
            "set_unlock": norm["set_unlock"],
            "gold": norm["gold"],
            "mana": norm["mana"],
            "coin": norm["coin"],
        }

        total_alloc_weight = sum(alloc_weights.values())
        alloc_weights = {k: v / total_alloc_weight for k, v in alloc_weights.items()}

        # Initial allocation
        allocation = {
            k: int(remaining_after_equipment * w)
            for k, w in alloc_weights.items()
        }

        allocated = sum(allocation.values())
        drift = remaining_after_equipment - allocated

        # ensure deterministic distribution of drift
        priority = ["set_unlock", "gold", "mana", "coin"]

        # IMPORTANT: guarantee at least 1 set unlock
        if allocation["set_unlock"] == 0:
            allocation["set_unlock"] = 1
            drift -= 1

        i = 0
        while drift > 0:
            allocation[priority[i % len(priority)]] += 1
            drift -= 1
            i += 1

        variants = {
            "gold": [
                ("Gold (S)", 55),
                ("Gold (M)", 30),
                ("Gold (L)", 15),
            ],
            "mana": [
                ("Mana Shards (S)", 55),
                ("Mana Shards (M)", 30),
                ("Mana Shards (L)", 15),
            ],
            "coin": [
                ("Bronze Challenge Coin", 55),
                ("Silver Challenge Coin", 30),
                ("Gold Challenge Coin", 15),
            ],
        }

        pool.extend(self.create_item("Set Unlock") for _ in range(allocation["set_unlock"]))
        for _ in range(allocation["gold"]):
            pool.append(self.create_item(self.weighted_choice(variants["gold"])))

        for _ in range(allocation["mana"]):
            pool.append(self.create_item(self.weighted_choice(variants["mana"])))

        for _ in range(allocation["coin"]):
            pool.append(self.create_item(self.weighted_choice(variants["coin"])))

        if not equipment_used_as_fixed:
            equipment_pool = self.random.sample(list(possible_equipment), equipment_to_place)
            for name in equipment_pool:
                pool.append(self.create_item(name))

        self.multiworld.itempool += pool

    def weighted_choice(self, options):
        # options = [(item, weight), ...]
        total = sum(w for _, w in options)
        roll = self.random.randint(1, total)

        current = 0
        for item, weight in options:
            current += weight
            if roll <= current:
                return item

        return options[-1][0]  # fallback safety

        # set_unlock_percentage = self.setUnlocksPercentage
        # gold_percentage = self.goldPercentage
        # mana_shard_percentage = self.manaShardPercentage
        # challenge_coin_percentage = self.challengePercentage
        # equipment_percentage = self.equipmentPercentage
        #
        # total_percentage = set_unlock_percentage + gold_percentage + mana_shard_percentage + challenge_coin_percentage + equipment_percentage
        # total_percentage_no_equipment = set_unlock_percentage + gold_percentage + mana_shard_percentage + challenge_coin_percentage
        #
        # correction = 100/total_percentage
        # correction_no_equipment = 100/total_percentage_no_equipment
        #
        # possible_equipment = items.give_possible_equipment(self.options)
        #
        # if self.options.tryIncludeAllEquipment and len(local_location_table) - len(possible_equipment) - len(pool) >= 1:
        #     for name, data in possible_equipment.items():
        #         pool.append(self.create_item(name))
        #
        # total_fillers_needed = len(local_location_table) - len(pool)
        #
        # set_unlocks_needed = int(total_fillers_needed * set_unlock_percentage * correction / 100)
        # gold_needed = int(total_fillers_needed * gold_percentage * correction / 100)
        # mana_shard_needed = int(total_fillers_needed * mana_shard_percentage * correction / 100)
        # challenge_coin_needed = int(total_fillers_needed * challenge_coin_percentage * correction / 100)
        # equipment_needed = int(total_fillers_needed * equipment_percentage * correction / 100)
        # error_range = total_fillers_needed - set_unlocks_needed - gold_needed - mana_shard_needed - challenge_coin_needed - equipment_needed
        #
        # equipment_needed += error_range
        #
        # for amount in range(0, set_unlocks_needed):
        #     pool.append(self.create_item("Set Unlock"))
        #
        # for amount in range(0, gold_needed):
        #     pool.append(self.create_item("Gold (M)"))
        #
        # for amount in range(0, mana_shard_needed):
        #     pool.append(self.create_item("Mana Shards (M)"))
        #
        # for amount in range(0, challenge_coin_needed):
        #     pool.append(self.create_item("Silver Challenge Coin"))
        #
        # for amount in range(0, equipment_needed):
        #     pool.append(self.create_item("Some Equipment"))
        #
        # items.create_all_items(self)

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.
    def create_item(self, name: str) -> items.ForgeAPItem:
        return items.create_item_with_correct_classification(self, name)

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    # def fill_slot_data(self) -> Mapping[str, Any]:
    #     # If you need access to the player's chosen options on the client side, there is a helper for that.
    #     return self.options.as_dict(
    #         "set_unlocks"
    #     )

    def should_ignore_color(self, name : str) -> bool:
        if self.options.startingColor == 0 and name == "Unlock White":
            return True
        if self.options.startingColor == 1 and name == "Unlock Blue":
            return True
        if self.options.startingColor == 2 and name == "Unlock Black":
            return True
        if self.options.startingColor == 3 and name == "Unlock Red":
            return True
        if self.options.startingColor == 4 and name == "Unlock Green":
            return True
        return False

    def fill_slot_data(self) -> dict:
        slot_data = self.options.as_dict("colorSanity",
                                         "startingColor",
                                         "fightLocations",
                                         "fightAmountPerLocation",
                                         "questLocations",
                                         "eventLocations",
                                         "dungeonLocations",
                                         "includePower",
                                         "includeCheat",
                                         "setUnlocksPercentage",
                                         "giftPack",
                                         "goldPercentage",
                                         "manaShardPercentage",
                                         "equipmentPercentage",
                                         "tryIncludeAllEquipment",
                                         "minShopPrice",
                                         "maxShopPrice",
                                         "goldMultiplierPercentage")
        slot_data['seed'] = "".join(self.random.choice(string.ascii_letters) for i in range(16))
        return slot_data