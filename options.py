from dataclasses import dataclass
from random import choice

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

# -----------------------Settings for Gameplay options ---------------

class CastlesRequired(Range):
    """
    The amount of Castles required for your goal.
    Setting this to 6 will require you to beat all colored castle bosses and then Emrakul.
    Otherwise, it will require the set number of colored castle bosses.
    """
    range_start = 1
    range_end = 6
    default = 3
    display_name = "Castles Required"

# class ColorSanity(Toggle):
#     """
#     Shuffles colors into the item pool, allowing decks to only be built form unlocked colors.
#     Colorless will always be available.
#     NOT CURRENTLY IMPLEMENTED IN-GAME
#     """
#     display_name = "ColorSanity"
#
# class StartingColor(Choice):
#     """
#     Chooses your starting color if Colorsanity is enabled.
#     NOT CURRENTLY IMPLEMENTED IN-GAME
#     """
#     display_name = "Starting Color"
#     option_White = 0
#     option_Blue = 1
#     option_Black = 2
#     option_Red = 3
#     option_Green = 4
#
# class DeathLink(Toggle):
#     """
#     Send DeathLinks.
#     NOT CURRENTLY IMPLEMENTED IN-GAME
#     """
#     display_name = "DeathLink"

# -----------------------Settings for Location amount control ---------------

class FightLocations(Range):
    """
    The amount of fight win locations per region.
    Adds 6 locations per.
    """
    display_name = "Fight Locations"
    range_start = 0
    range_end = 100
    default = 15

class FightAmountPerLocation(Range):
    """
    The amount of wins required to count as a fight location check.
    """
    display_name = "Fight wins per Location"
    range_start = 1
    range_end = 100
    default = 1

class QuestLocations(Range):
    """
    The amount of quest locations per region.
    Adds 6 locations per.
    """
    display_name = "Quest Locations"
    range_start = 0
    range_end = 10
    default = 3

class EventLocations(Range):
    """
    The amount of event locations per region.
    Adds 6 locations per.
    """
    display_name = "Event Locations"
    range_start = 0
    range_end = 10
    default = 3

class IncludeMinibossLocations(DefaultOnToggle):
    """
    Includes Minibosses as locations.
    Adds 24 locations.
    """
    display_name = "Dungeon Locations"

class CommonCardLocations(Range):
    """
    The amount of locations for collecting common cards.
    """
    display_name = "Common card Locations"
    range_start = 0
    range_end = 100
    default = 10

class CommonCardsPerLocation(Range):
    """
    The amount of common cards that have to be collected to send a common card location check.
    """
    display_name = "Common cards per Location"
    range_start = 1
    range_end = 100
    default = 50

class UncommonCardLocations(Range):
    """
    The amount of locations for collecting uncommon cards.
    """
    display_name = "Uncommon card Locations"
    range_start = 0
    range_end = 100
    default = 10

class UncommonCardsPerLocation(Range):
    """
    The amount of uncommon cards that have to be collected to send an uncommon card location check.
    """
    display_name = "Uncommon cards per Location"
    range_start = 1
    range_end = 100
    default = 25

class RareCardLocations(Range):
    """
    The amount of locations for collecting rare cards.
    """
    display_name = "Rare card Locations"
    range_start = 0
    range_end = 100
    default = 10

class RareCardsPerLocation(Range):
    """
    The amount of rare cards that have to be collected to send a rare card location check.
    """
    display_name = "Rare cards per Location"
    range_start = 1
    range_end = 100
    default = 10

class MythicRareCardLocations(Range):
    """
    The amount of locations for collecting mythic rare cards.
    """
    display_name = "Mythic Rare card Locations"
    range_start = 0
    range_end = 100
    default = 10

class MythicRareCardsPerLocation(Range):
    """
    The amount of rare cards that have to be collected to send a mythic rare card location check.
    """
    display_name = "Mythic Rare cards per Location"
    range_start = 1
    range_end = 100
    default = 5

# -----------------------Settings for Equipment items ---------------

class IncludePower(Toggle):
    """
    Expand the standard equipment pool with Power equipment.
    Power equipment lets you start with a sol ring/mox/black lotus in play.
    """
    display_name = "Include Power"

class IncludeCheat(Toggle):
    """
    Expand the standard equipment pool with the Cheat equipment.
    The Cheat equipment is effectively an instant win combo on game start.
    """
    display_name = "Include Cheat"

# -----------------------Settings for Filler items ---------------

class SetUnlockPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Set Unlocks.
    Sets will be spread equally over all available Set Unlock items.
    Collecting all Set Unlock items will unlock every set in the game.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Set Unlock Percentage"
    range_start = 1
    range_end = 1000
    default = 25

class GiftPack(DefaultOnToggle):
    """
    Gives you a free matching booster pack when unlocking a new set.
    This only works on sets that booster packs can be generated for.
    """
    display_name = "Enable Gift Packs"

class GoldPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Gold filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Gold Percentage"
    range_start = 0
    range_end = 1000
    default = 15

class ManaShardPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Mana Shard filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Mana Shard Percentage"
    range_start = 0
    range_end = 1000
    default = 15

class ChallengeCoinPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Challenge Coin filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Challenge Coin Percentage"
    range_start = 0
    range_end = 1000
    default = 10

class LifeUpgradePercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Health filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Health Upgrade Percentage"
    range_start = 0
    range_end = 1000
    default = 5

class EquipmentPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Mana Shard filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Equipment Percentage"
    range_start = 0
    range_end = 1000
    default = 30

class TryIncludeAllEquipment(Toggle):
    """
    When possible the system will try to include all equipment pieces instead of randomly filling filler locations with a certain amount of equipment.
    Randomization with this on will require at least: amount of included equipment + 6 (5 runes + 1 set unlock item) + 4 (if color sanity is enabled) locations.
    At the time of writing: Default equipment contains 102 items, Power equipment contains 7 items, Cheat equipment contains 1 item.
    """
    display_name = "Try Include All Equipment"

# -----------------------Settings for Helpers ---------------

class MinShopPrice(Range):
    """
    Minimum gold price for shop items.
    """
    display_name = "Minimum Shop Price"
    range_start = 1
    range_end = 100000
    default = 500

class MaxShopPrice(Range):
    """
    Maximum gold price for shop items.
    """
    display_name = "Maximum Shop Price"
    range_start = 1
    range_end = 100000
    default = 1000

class GoldMultiplierPercentage(Range):
    """
    A percentage multiplier on gold gain. Only affects combat rewards.
    200 would be double, 50 would be half.
    """
    display_name = "Gold Multiplier Percentage"
    range_start = 1
    range_end = 10000
    default = 100

@dataclass
class ForgeAPOptions(PerGameCommonOptions):
    castles_required: CastlesRequired
    # color_sanity: ColorSanity
    # starting_color: StartingColor
    fight_locations: FightLocations
    fight_amount_per_location: FightAmountPerLocation
    quest_locations: QuestLocations
    event_locations: EventLocations
    include_miniboss_locations: IncludeMinibossLocations
    common_card_locations: CommonCardLocations
    common_cards_per_location: CommonCardsPerLocation
    uncommon_card_locations: UncommonCardLocations
    uncommon_cards_per_location: UncommonCardsPerLocation
    rare_card_locations: RareCardLocations
    rare_cards_per_location: RareCardsPerLocation
    mythic_rare_card_locations: MythicRareCardLocations
    mythic_rare_cards_per_location: MythicRareCardsPerLocation
    include_power: IncludePower
    include_cheat: IncludeCheat
    set_unlocks_percentage: SetUnlockPercentage
    gift_pack: GiftPack
    gold_percentage: GoldPercentage
    mana_shard_percentage: ManaShardPercentage
    challenge_coin_percentage: ChallengeCoinPercentage
    life_upgrade_percentage: LifeUpgradePercentage
    equipment_percentage: EquipmentPercentage
    try_include_all_equipment: TryIncludeAllEquipment
    min_shop_price: MinShopPrice
    max_shop_price: MaxShopPrice
    gold_multiplier_percentage: GoldMultiplierPercentage
    # death_link: DeathLink

option_groups = [
    OptionGroup("Game Options", [
        CastlesRequired,
        # ColorSanity,
        # StartingColor,
        # DeathLink,
    ]),
    OptionGroup("Location Options", [
        FightLocations,
        FightAmountPerLocation,
        QuestLocations,
        EventLocations,
        IncludeMinibossLocations,
        CommonCardLocations,
        CommonCardsPerLocation,
        UncommonCardLocations,
        UncommonCardsPerLocation,
        RareCardLocations,
        RareCardsPerLocation,
        MythicRareCardLocations,
        MythicRareCardsPerLocation
    ]),
    OptionGroup("Equipment Options", [
        IncludePower,
        IncludeCheat,
    ]),
    OptionGroup("Filler Options", [
        SetUnlockPercentage,
        GiftPack,
        GoldPercentage,
        ManaShardPercentage,
        ChallengeCoinPercentage,
        LifeUpgradePercentage,
        EquipmentPercentage,
        TryIncludeAllEquipment,
    ]),
    OptionGroup("Helper Options", [
        MinShopPrice,
        MaxShopPrice,
        GoldMultiplierPercentage,
    ])
]

option_presets = {
    "Standard": {
        "castles_required": 3,
        # "color_sanity": False,
        # "starting_color": 0,
        "fight_locations": 15,
        "fight_amount_per_location": 1,
        "quest_locations": 3,
        "event_locations": 3,
        "include_miniboss_locations": True,
        "common_card_locations": 10,
        "common_cards_per_location": 50,
        "uncommon_card_locations": 10,
        "uncommon_cards_per_location": 25,
        "rare_card_locations": 10,
        "rare_cards_per_location": 10,
        "mythic_rare_card_locations": 10,
        "mythic_rare_cards_per_location": 5,
        "include_power": True,
        "include_cheat": False,
        "set_unlocks_percentage": 30,
        "gift_pack": True,
        "gold_percentage": 25,
        "mana_shard_percentage": 20,
        "challenge_coin_percentage": 15,
        "life_upgrade_percentage": 10,
        "equipment_percentage": 0,
        "try_include_all_equipment": True,
        "min_shop_price": 500,
        "max_shop_price": 1000,
        "gold_multiplier_percentage": 100,
        # "death_link": False,
    },
    "Short": {
        "castles_required": 1,
        # "color_sanity": False,
        # "starting_color": 0,
        "fight_locations": 5,
        "fight_amount_per_location": 1,
        "quest_locations": 1,
        "event_locations": 1,
        "miniboss_locations": False,
        "common_card_locations": 4,
        "common_cards_per_location": 50,
        "uncommon_card_locations": 4,
        "uncommon_cards_per_location": 25,
        "rare_card_locations": 4,
        "rare_cards_per_location": 10,
        "mythic_rare_card_locations": 4,
        "mythic_rare_cards_per_location": 5,
        "include_power": True,
        "include_cheat": False,
        "set_unlocks_percentage": 25,
        "gift_pack": True,
        "gold_percentage": 15,
        "mana_shard_percentage": 15,
        "challenge_coin_percentage": 10,
        "life_upgrade_percentage": 5,
        "equipment_percentage": 30,
        "try_include_all_equipment": False,
        "min_shop_price": 500,
        "max_shop_price": 1000,
        "gold_multiplier_percentage": 200,
        # "death_link": False,
    },
}
