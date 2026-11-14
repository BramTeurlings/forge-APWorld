from dataclasses import dataclass
from random import choice

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, DeathLink, OptionCounter, OptionSet

from .items import item_table_equipment_default, item_table_equipment_power, item_table_equipment_cheat

# -----------------------Settings for Gameplay options ---------------

class CastlesRequired(Range):
    """
    The amount of Castles required for your goal.
    Setting this to 7 will require you to beat all colored castle bosses, then Emrakul and finally Arzakon.
    Setting this to 6 will require you to beat all colored castle bosses and then Emrakul.
    Otherwise, it will require the set number of colored castle bosses.
    """
    range_start = 1
    range_end = 7
    default = 3
    display_name = "Castles Required"

class SetUnlocksBeforeBosses(Range):
    """
    The amount of Set Unlocks logic expects you to have before you fight any boss or miniboss.
    This makes sure no boss is required before you could build a decent deck.
    The pool will always contain at least this many Set Unlocks.
    If a seed has too few locations for the chosen amount, it is lowered automatically.
    Set this to 0 to disable it.
    """
    range_start = 0
    range_end = 30
    default = 5
    display_name = "Set Unlocks Before Bosses"

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
class ForgeDeathLink(DeathLink):
    """
    When you lose a battle, everyone who enabled death link dies.
    When someone else dies, you suffer a regular battle loss: you lose gold and life as if you lost a battle.
    If you are in a battle when it happens, a Death Link trigger goes on the stack that makes you lose your current life
    total. You can respond to it, for example by gaining life.
    """

class NoStartingDeck(Toggle):
    """
    You don't get a starting deck, you only get the Starting Cards (if any), which become your starting deck.
    If you don't set any starting cards, you will start the game with an empty collection.
    """
    display_name = "No Starting Deck"

class AutoSellDeck(Toggle):
    """
    Automatically sells every card in your active deck when you defeat a castle boss.
    You get the normal sell price for the cards and have to build a new deck from your collection.
    """
    display_name = "Auto-sell Deck on Castle Boss Defeat"

class EventMinibossChecks(Toggle):
    """
    When enabled, beating a miniboss in an inn event, tournament or arena battle also sends that miniboss's check.
    Castle bosses only ever count when you beat them in their castle.
    """
    display_name = "Event Miniboss Checks"

# -----------------------Settings for Starting inventory ---------------

class StartingCards(OptionCounter):
    """
    Cards you start the run with, as <card name: amount>.
    Starting cards are always unlocked, even if their set is still locked.
    If the "No Starting Deck" option is enabled, these cards make up your starting deck.
    Card names are checked in-game, unknown names are skipped.
    When editing the .yaml file manually, Put each name in quotes, for example:
      starting_cards: {"Lightning Bolt": 4, "Preston, the Vanisher": 1}
    or one card per line:
      starting_cards:
        "Lightning Bolt": 4
        "Preston, the Vanisher": 1
    """
    display_name = "Starting Cards"
    min = 1
    max = 99
    default = {}

class StartingSets(OptionSet):
    """
    Codes of the sets that start unlocked.
    The set codes are the ones Forge uses, they are checked in-game and unknown codes are skipped.
    When editing the .yaml file manually, put each code in quotes, for example:
      starting_sets: ["M20", "FRA"]
    or one code per line:
      starting_sets:
        - "M20"
        - "FRA"
    """
    display_name = "Starting Sets"
    default = frozenset()

class StartingBoosters(OptionCounter):
    """
    Booster packs you start the run with, as <set code: amount>.
    The set codes are the ones Forge uses, sets that have no booster packs are skipped in-game.
    Starting boosters don't unlock their set.
    When editing the .yaml file manually, put each code in quotes, for example:
      starting_boosters: {"M20": 3, "FRA": 1}
    or one set per line:
      starting_boosters:
        "M20": 3
        "FRA": 1
    """
    display_name = "Starting Boosters"
    min = 1
    max = 99
    default = {}

class StartingEquipment(OptionSet):
    """
    Equipment you start the run with, using the equipment names from the item pool.
    Starting equipment is removed from the item pool.
    Names are case-sensitive. The Archipelago launcher suggests the correctly spelled names once you type the first
    three letters.
    For example:
      starting_equipment: ["Sol Ring", "Hill Giant Club"]
    or one item per line:
      starting_equipment:
        - "Sol Ring"
        - "Hill Giant Club"
    """
    display_name = "Starting Equipment"
    valid_keys = sorted({**item_table_equipment_default, **item_table_equipment_power, **item_table_equipment_cheat})
    default = frozenset()

# -----------------------Settings for Location amount control ---------------

class FightLocations(Range):
    """
    The amount of fight win locations per region.
    Adds 6 locations per.
    """
    display_name = "Fight Locations"
    range_start = 0
    range_end = 100
    default = 6

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
    default = 2

class EventLocations(Range):
    """
    The amount of event locations per region.
    Adds 6 locations per.
    """
    display_name = "Event Locations"
    range_start = 0
    range_end = 10
    default = 2

class IncludeMinibossLocations(DefaultOnToggle):
    """
    Includes Minibosses as locations.
    Adds 24 locations.
    """
    display_name = "Include Miniboss Locations"

class CommonCardLocations(Range):
    """
    The amount of locations for collecting common cards.
    """
    display_name = "Common card Locations"
    range_start = 0
    range_end = 100
    default = 15

class CommonCardsPerLocation(Range):
    """
    The amount of common cards that have to be collected to send a common card location check.
    """
    display_name = "Common cards per Location"
    range_start = 1
    range_end = 100
    default = 30

class UncommonCardLocations(Range):
    """
    The amount of locations for collecting uncommon cards.
    """
    display_name = "Uncommon card Locations"
    range_start = 0
    range_end = 100
    default = 15

class UncommonCardsPerLocation(Range):
    """
    The amount of uncommon cards that have to be collected to send an uncommon card location check.
    """
    display_name = "Uncommon cards per Location"
    range_start = 1
    range_end = 100
    default = 18

class RareCardLocations(Range):
    """
    The amount of locations for collecting rare cards.
    """
    display_name = "Rare card Locations"
    range_start = 0
    range_end = 100
    default = 15

class RareCardsPerLocation(Range):
    """
    The amount of rare cards that have to be collected to send a rare card location check.
    """
    display_name = "Rare cards per Location"
    range_start = 1
    range_end = 100
    default = 6

class MythicRareCardLocations(Range):
    """
    The amount of locations for collecting mythic rare cards.
    """
    display_name = "Mythic Rare card Locations"
    range_start = 0
    range_end = 100
    default = 20

class MythicRareCardsPerLocation(Range):
    """
    The amount of rare cards that have to be collected to send a mythic rare card location check.
    """
    display_name = "Mythic Rare cards per Location"
    range_start = 1
    range_end = 100
    default = 1

class ScaleCardChecks(DefaultOnToggle):
    """
    Spreads the card collection checks of each rarity over your progress through the regions in logic.
    This keeps important items from being placed on card checks that take a long time to get early on.
    It only affects logic, card checks can still be sent at any time in-game.
    """
    display_name = "Scale Card Checks with Progress"

# -----------------------Settings for Equipment items ---------------

class IncludePower(DefaultOnToggle):
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
    default = 30

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
    default = 5

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
    Choose the percentage of filler items in the pool that will be Equipment items.
    Note if filler percentage doesn't sum up exactly to 100 the system will treat them as proportions.
    """
    display_name = "Equipment Percentage"
    range_start = 0
    range_end = 1000
    default = 30

class TryIncludeAllEquipment(Toggle):
    """
    When possible archipelago will try to include all possible equipment pieces instead of using the provided equipment percentage.
    If not enough space can be allocated it will use equipment percentage as a fallback, so make sure it's not 0 unless you know what you are doing!

    Randomization with this on will require at least: amount of included equipment + 6 (5 runes + 1 set unlock item) locations.
    At the time of writing: Default equipment contains 116 items, Power equipment contains 7 items, Cheat equipment contains 1 item.
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
    set_unlocks_before_bosses: SetUnlocksBeforeBosses
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
    scale_card_checks: ScaleCardChecks
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
    death_link: ForgeDeathLink
    no_starting_deck: NoStartingDeck
    auto_sell_deck: AutoSellDeck
    event_miniboss_checks: EventMinibossChecks
    starting_cards: StartingCards
    starting_sets: StartingSets
    starting_boosters: StartingBoosters
    starting_equipment: StartingEquipment

option_groups = [
    OptionGroup("Game Options", [
        CastlesRequired,
        SetUnlocksBeforeBosses,
        # ColorSanity,
        # StartingColor,
        ForgeDeathLink,
        AutoSellDeck,
        EventMinibossChecks,
    ]),
    OptionGroup("Starting Options", [
        NoStartingDeck,
        StartingCards,
        StartingSets,
        StartingBoosters,
        StartingEquipment,
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
        MythicRareCardsPerLocation,
        ScaleCardChecks,
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
    "Short": {
        "castles_required": 1,
        "set_unlocks_before_bosses": 5,
        # "color_sanity": False,
        # "starting_color": 0,
        "fight_locations": 5,
        "fight_amount_per_location": 1,
        "quest_locations": 1,
        "event_locations": 1,
        "include_miniboss_locations": False,
        "common_card_locations": 8,
        "common_cards_per_location": 30,
        "uncommon_card_locations": 8,
        "uncommon_cards_per_location": 18,
        "rare_card_locations": 8,
        "rare_cards_per_location": 6,
        "mythic_rare_card_locations": 8,
        "mythic_rare_cards_per_location": 1,
        "scale_card_checks": True,
        "include_power": True,
        "include_cheat": False,
        "set_unlocks_percentage": 30,
        "gift_pack": True,
        "gold_percentage": 15,
        "mana_shard_percentage": 15,
        "challenge_coin_percentage": 5,
        "life_upgrade_percentage": 5,
        "equipment_percentage": 30,
        "try_include_all_equipment": False,
        "min_shop_price": 500,
        "max_shop_price": 1000,
        "gold_multiplier_percentage": 300,
        "death_link": False,
        "no_starting_deck": False,
        "auto_sell_deck": False,
        "event_miniboss_checks": False,
    },
    "Medium": {
        "castles_required": 3,
        "set_unlocks_before_bosses": 5,
        # "color_sanity": False,
        # "starting_color": 0,
        "fight_locations": 6,
        "fight_amount_per_location": 1,
        "quest_locations": 1,
        "event_locations": 1,
        "include_miniboss_locations": False,
        "common_card_locations": 15,
        "common_cards_per_location": 30,
        "uncommon_card_locations": 15,
        "uncommon_cards_per_location": 18,
        "rare_card_locations": 15,
        "rare_cards_per_location": 6,
        "mythic_rare_card_locations": 20,
        "mythic_rare_cards_per_location": 1,
        "scale_card_checks": True,
        "include_power": True,
        "include_cheat": False,
        "set_unlocks_percentage": 30,
        "gift_pack": True,
        "gold_percentage": 15,
        "mana_shard_percentage": 15,
        "challenge_coin_percentage": 5,
        "life_upgrade_percentage": 5,
        "equipment_percentage": 30,
        "try_include_all_equipment": False,
        "min_shop_price": 500,
        "max_shop_price": 1000,
        "gold_multiplier_percentage": 150,
        "death_link": False,
        "no_starting_deck": False,
        "auto_sell_deck": False,
        "event_miniboss_checks": False,
    },
    "Long": {
        "castles_required": 7,
        "set_unlocks_before_bosses": 5,
        # "color_sanity": False,
        # "starting_color": 0,
        "fight_locations": 25,
        "fight_amount_per_location": 1,
        "quest_locations": 5,
        "event_locations": 5,
        "include_miniboss_locations": True,
        "common_card_locations": 40,
        "common_cards_per_location": 30,
        "uncommon_card_locations": 40,
        "uncommon_cards_per_location": 18,
        "rare_card_locations": 40,
        "rare_cards_per_location": 6,
        "mythic_rare_card_locations": 40,
        "mythic_rare_cards_per_location": 1,
        "scale_card_checks": True,
        "include_power": True,
        "include_cheat": False,
        "set_unlocks_percentage": 25,
        "gift_pack": True,
        "gold_percentage": 15,
        "mana_shard_percentage": 15,
        "challenge_coin_percentage": 10,
        "life_upgrade_percentage": 5,
        "equipment_percentage": 30,
        "try_include_all_equipment": True,
        "min_shop_price": 500,
        "max_shop_price": 1000,
        "gold_multiplier_percentage": 100,
        "death_link": False,
        "no_starting_deck": False,
        "auto_sell_deck": False,
        "event_miniboss_checks": False,
    },
}
