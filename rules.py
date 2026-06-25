from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import ForgeAPWorld


def set_all_rules(world: ForgeAPWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ForgeAPWorld) -> None:
    if not world.options.sequential_regions:
        colorless_to_white = world.get_entrance("Colorless to White")
        colorless_to_blue = world.get_entrance("Colorless to Blue")
        colorless_to_black = world.get_entrance("Colorless to Black")
        colorless_to_red = world.get_entrance("Colorless to Red")
        colorless_to_green = world.get_entrance("Colorless to Green")

        world.set_rule(colorless_to_white, lambda state: state.has("White Rune", world.player))
        world.set_rule(colorless_to_blue, lambda state: state.has("Blue Rune", world.player))
        world.set_rule(colorless_to_black, lambda state: state.has("Black Rune", world.player))
        world.set_rule(colorless_to_red, lambda state: state.has("Red Rune", world.player))
        world.set_rule(colorless_to_green, lambda state: state.has("Green Rune", world.player))

def set_all_location_rules(world: ForgeAPWorld) -> None:
    final_boss = world.get_location("Emrakul Defeated")
    world.set_rule(final_boss, lambda state: state.has_all(("White Rune", "Blue Rune", "Black Rune", "Red Rune", "Green Rune"), world.player))

def set_completion_condition(world: ForgeAPWorld) -> None:
    world.set_completion_rule(Has("Victory"))