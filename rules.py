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
    final_boss = world.get_location("Emrakul Victory")
    world.set_rule(final_boss, lambda state: state.has_all(("White Rune", "Blue Rune", "Black Rune", "Red Rune", "Green Rune"), world.player))
    if world.options.castles_required == world.options.castles_required.range_end:
        # Emrakul is a regular check here, so it needs the same runes as Emrakul's victory
        world.set_rule(world.get_location("Emrakul Defeated"), lambda state: state.has_all(("White Rune", "Blue Rune", "Black Rune", "Red Rune", "Green Rune"), world.player))
        # Arzakon's castle is revealed after defeating Emrakul
        world.set_rule(world.get_location("Arzakon Victory"), lambda state: state.has("Emrakul Victory", world.player))

def set_completion_condition(world: ForgeAPWorld) -> None:
    castle_bosses = [
        "Emrakul",
        "Akroma",
        "Lorthos",
        "Griselbrand",
        "Lathliss",
        "Ghalta",
    ]
    if world.options.castles_required == world.options.castles_required.range_end:
        castle_bosses.append("Arzakon")

    world.multiworld.completion_condition[world.player] = (
        lambda state: sum(
            state.has(f"{boss} Victory", world.player)
            for boss in castle_bosses
        ) >= world.options.castles_required
    )
