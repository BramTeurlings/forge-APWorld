from dataclasses import dataclass
from random import choice

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.

# -----------------------Settings for Gameplay options ---------------

class ColorSanity(Toggle):
    """
    Shuffles colors into the item pool.
    Colorless will always be available.
    """
    display_name = "ColorSanity"

class StartingColor(Choice):
    """
    Chooses your starting color if Colorsanity is enabled.
    """
    display_name = "Starting Color"
    option_White = 0
    option_Blue = 1
    option_Black = 2
    option_Red = 3
    option_Green = 4

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

class DungeonLocations(Range):
    """
    The amount of dungeon locations per region.
    Adds 6 locations per.
    """
    display_name = "Dungeon Locations"
    range_start = 0
    range_end = 10
    default = 3

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
    range_end = 100
    default = 30

class GiftPack(DefaultOnToggle):
    """
    Should you recieve a free giftpack when unlocking a new set.
    """
    display_name = "Enable Gift Packs"

class GoldPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Gold filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Gold Percentage"
    range_start = 0
    range_end = 100
    default = 15

class ManaShardPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Mana Shard filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Mana Shard Percentage"
    range_start = 0
    range_end = 100
    default = 15

class ChallengeCoinPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Challenge Coin filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Challenge Coin Percentage"
    range_start = 0
    range_end = 100
    default = 10


class EquipmentPercentage(Range):
    """
    Choose the percentage of filler items in the pool that will be Mana Shard filler items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Equipment Percentage"
    range_start = 0
    range_end = 100
    default = 30

class TryIncludeAllEquipment(Toggle):
    """
    When possible the system will try to include all equipment pieces instead of randomly filling filler locations with a certain amount of equipment.
    Randomization with this on will require at least: amount of included equipment + 6 (5 runes + 1 set unlock item) + 4 (if color sanity is enabled) locations.
    Default equipment contains 102 items. Power equipment contains 7 items. Cheat equipment contains 1 item.
    """
    display_name = "Try Include All Equipment"

# -----------------------Settings for Helpers ---------------

class MinShopPrice(Range):
    """
    Minimum gold price for shop items.
    """
    display_name = "Minimum Shop Price"
    range_start = 1
    range_end = 10000
    default = 500

class MaxShopPrice(Range):
    """
    Maximum gold price for shop items.
    """
    display_name = "Maximum Shop Price"
    range_start = 1
    range_end = 10000
    default = 1000

class GoldMultiplierPercentage(Range):
    """
    A percentage multiplier on gold gain.
    100 would be equivalent to base game.
    """
    display_name = "Gold Multiplier Percentage"
    range_start = 10
    range_end = 1000
    default = 100

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class ForgeAPOptions(PerGameCommonOptions):
    colorSanity: ColorSanity
    startingColor: StartingColor
    fightLocations: FightLocations
    fightAmountPerLocation: FightAmountPerLocation
    questLocations: QuestLocations
    eventLocations: EventLocations
    dungeonLocations: DungeonLocations
    includePower: IncludePower
    includeCheat: IncludeCheat
    setUnlocksPercentage: SetUnlockPercentage
    giftPack: GiftPack
    goldPercentage: GoldPercentage
    manaShardPercentage: ManaShardPercentage
    challengeCoinPercentage: ChallengeCoinPercentage
    equipmentPercentage: EquipmentPercentage
    tryIncludeAllEquipment: TryIncludeAllEquipment
    minShopPrice: MinShopPrice
    maxShopPrice: MaxShopPrice
    goldMultiplierPercentage: GoldMultiplierPercentage

# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup("Gameplay Options", [
        ColorSanity,
        StartingColor,
        GiftPack,
    ]),
    OptionGroup("Location Options", [
        FightLocations,
        FightAmountPerLocation,
        QuestLocations,
        EventLocations,
        DungeonLocations,
    ]),
    OptionGroup("Equipment Options", [
        IncludePower,
        IncludeCheat,
    ]),
    OptionGroup("Filler Options", [
        SetUnlockPercentage,
        GoldPercentage,
        ManaShardPercentage,
        ChallengeCoinPercentage,
        EquipmentPercentage,
        TryIncludeAllEquipment,
    ]),
    OptionGroup("Helper Options", [
        MinShopPrice,
        MaxShopPrice,
        GoldMultiplierPercentage,
    ])
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "Standard": { # 227 total checks.
        "colorSanity": False,
        "startingColor": 0,
        "fightLocations": 15,
        "fightAmountPerLocation": 1,
        "questLocations": 3,
        "eventLocations": 3,
        "dungeonLocations": 3,
        "includePower": True,
        "includeCheat": False,
        "setUnlocksPercentage": 30,
        "giftPack": True,
        "goldPercentage": 15,
        "manaShardPercentage": 15,
        "equipmentPercentage": 30,
        "tryIncludeAllEquipment": True,
        "minShopPrice": 500,
        "maxShopPrice": 1000,
        "goldMultiplierPercentage": 100,
    },
    "Short": { # 131 total checks.
        "colorSanity": False,
        "startingColor": 0,
        "fightLocations": 5,
        "fightAmountPerLocation": 1,
        "questLocations": 1,
        "eventLocations": 1,
        "dungeonLocations": 1,
        "includePower": True,
        "includeCheat": False,
        "setUnlocksPercentage": 30,
        "giftPack": True,
        "goldPercentage": 15,
        "manaShardPercentage": 15,
        "equipmentPercentage": 30,
        "tryIncludeAllEquipment": False,
        "minShopPrice": 500,
        "maxShopPrice": 1000,
        "goldMultiplierPercentage": 200,
    },
}
