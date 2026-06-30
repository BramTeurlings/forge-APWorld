from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import ForgeAPWorld


def set_all_rules(world: ForgeAPWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: ForgeAPWorld) -> None:
    final_boss = world.get_location("Emrakul Defeated")
    world.set_rule(final_boss, lambda state: state.has_all(("White Rune", "Blue Rune", "Black Rune", "Red Rune", "Green Rune"), world.player))

def set_completion_condition(world: ForgeAPWorld) -> None:
    world.set_completion_rule(Has("Victory"))
