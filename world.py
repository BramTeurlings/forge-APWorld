import string
from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as forgeap_options

class ForgeAPWorld(World):
    """
    Forge is an unofficial rules engine for the world's greatest card game.
    This world allows you to play the adventure mode with archipelago support.
    """

    game = "ForgeAP"

    web = web_world.ForgeAPWebWorld()

    options_dataclass = forgeap_options.ForgeAPOptions
    options: forgeap_options.ForgeAPOptions

    location_name_to_id = locations.give_all_locations()
    item_name_to_id = items.item_table

    origin_region_name = "Colorless"

    set_unlocks = 0

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
        # if self.options.color_sanity:
        #     for name, data in items.item_table_colors.items():
        #         if self.should_ignore_color(name):
        #             continue
        #         pool.append(self.create_item(name))

        remaining_slots = len(local_location_table) - len(pool)

        weights = {
            "set_unlock": self.options.set_unlocks_percentage,
            "gold": self.options.gold_percentage,
            "mana": self.options.mana_shard_percentage,
            "coin": self.options.challenge_coin_percentage,
            "life": self.options.life_upgrade_percentage,
            "equipment": self.options.equipment_percentage,
        }

        total_weight = sum(weights.values())
        if total_weight <= 0:
            return # should be impossible

        norm = {k: v / total_weight for k, v in weights.items()}

        possible_equipment = items.give_possible_equipment(self.options)
        max_equipment = len(possible_equipment)

        desired_equipment = int(remaining_slots * norm["equipment"])
        equipment_to_place = min(desired_equipment, max_equipment)
        equipment_used_as_fixed = False

        if self.options.try_include_all_equipment:
            # MUST fit ALL equipment or we ignore this mode completely
            if remaining_slots - len(possible_equipment) >= 1:
                for name in possible_equipment:
                    pool.append(self.create_item(name))

                equipment_used_as_fixed = True
                equipment_to_place = 0
                remaining_slots -= len(possible_equipment)

        remaining_after_equipment = remaining_slots - equipment_to_place

        alloc_weights = {
            "set_unlock": norm["set_unlock"],
            "gold": norm["gold"],
            "mana": norm["mana"],
            "coin": norm["coin"],
            "life": norm["life"],
        }

        total_alloc_weight = sum(alloc_weights.values())
        alloc_weights = {k: v / total_alloc_weight for k, v in alloc_weights.items()}

        allocation = {
            k: int(remaining_after_equipment * w)
            for k, w in alloc_weights.items()
        }

        allocated = sum(allocation.values())
        drift = remaining_after_equipment - allocated

        priority = ["set_unlock", "gold", "mana", "coin", "life"]

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
            "life": [
                ("Life +1", 50),
                ("Life +2", 50),
            ]
        }

        pool.extend(self.create_item("Set Unlock") for _ in range(allocation["set_unlock"]))
        self.set_unlocks = allocation["set_unlock"]
        for _ in range(allocation["gold"]):
            pool.append(self.create_item(self.weighted_choice(variants["gold"])))

        for _ in range(allocation["mana"]):
            pool.append(self.create_item(self.weighted_choice(variants["mana"])))

        for _ in range(allocation["coin"]):
            pool.append(self.create_item(self.weighted_choice(variants["coin"])))

        for _ in range(allocation["life"]):
            pool.append(self.create_item(self.weighted_choice(variants["life"])))

        if not equipment_used_as_fixed:
            equipment_pool = self.random.sample(list(possible_equipment), equipment_to_place)
            for name in equipment_pool:
                pool.append(self.create_item(name))

        self.multiworld.itempool += pool

    def weighted_choice(self, options):
        total = sum(w for _, w in options)
        roll = self.random.randint(1, total)

        current = 0
        for item, weight in options:
            current += weight
            if roll <= current:
                return item

        return options[-1][0]

    def create_item(self, name: str) -> items.ForgeAPItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
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
            "life": [
                ("Life +1", 50),
                ("Life +2", 50),
            ]
        }
        category = self.random.choice(list(variants.keys()))

        return self.weighted_choice(variants[category])

    def should_ignore_color(self, name : str) -> bool:
        if self.options.starting_color == 0 and name == "Unlock White":
            return True
        if self.options.starting_color == 1 and name == "Unlock Blue":
            return True
        if self.options.starting_color == 2 and name == "Unlock Black":
            return True
        if self.options.starting_color == 3 and name == "Unlock Red":
            return True
        if self.options.starting_color == 4 and name == "Unlock Green":
            return True
        return False

    def fill_slot_data(self) -> dict:
        slot_data = self.options.as_dict("castles_required",
                                         # "color_sanity",
                                         # "starting_color",
                                         "fight_locations",
                                         "fight_amount_per_location",
                                         "quest_locations",
                                         "event_locations",
                                         "include_miniboss_locations",
                                         "common_card_locations",
                                         "common_cards_per_location",
                                         "uncommon_card_locations",
                                         "uncommon_cards_per_location",
                                         "rare_card_locations",
                                         "rare_cards_per_location",
                                         "mythic_rare_card_locations",
                                         "mythic_rare_cards_per_location",
                                         "include_power",
                                         "include_cheat",
                                         "set_unlocks_percentage",
                                         "gift_pack",
                                         "gold_percentage",
                                         "mana_shard_percentage",
                                         "life_upgrade_percentage",
                                         "equipment_percentage",
                                         "try_include_all_equipment",
                                         "min_shop_price",
                                         "max_shop_price",
                                         "gold_multiplier_percentage",)
                                         # "death_link",
        slot_data["set_unlock_count"] = self.set_unlocks
        slot_data['seed'] = "".join(self.random.choice(string.ascii_letters) for i in range(16))
        return slot_data
