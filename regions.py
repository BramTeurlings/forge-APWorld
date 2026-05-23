from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ForgeAPWorld

def create_and_connect_regions(world: ForgeAPWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ForgeAPWorld) -> None:
    colorless = Region("Colorless", world.player, world.multiworld)
    white = Region("White", world.player, world.multiworld)
    blue = Region("Blue", world.player, world.multiworld)
    black = Region("Black", world.player, world.multiworld)
    red = Region("Red", world.player, world.multiworld)
    green = Region("Green", world.player, world.multiworld)

    regions = [colorless, white, blue, black, red, green]

    world.multiworld.regions += regions

def connect_regions(world: ForgeAPWorld) -> None:
    colorless = world.get_region("Colorless")
    white = world.get_region("White")
    blue = world.get_region("Blue")
    black = world.get_region("Black")
    red = world.get_region("Red")
    green = world.get_region("Green")

    colorless_to_white = Entrance(world.player, "Colorless to White", parent=colorless)
    colorless.exits.append(colorless_to_white)
    colorless_to_blue = Entrance(world.player, "Colorless to Blue", parent=colorless)
    colorless.exits.append(colorless_to_blue)
    colorless_to_black = Entrance(world.player, "Colorless to Black", parent=colorless)
    colorless.exits.append(colorless_to_black)
    colorless_to_red = Entrance(world.player, "Colorless to Red", parent=colorless)
    colorless.exits.append(colorless_to_red)
    colorless_to_green = Entrance(world.player, "Colorless to Green", parent=colorless)
    colorless.exits.append(colorless_to_green)

    colorless_to_white.connect(white)
    colorless_to_blue.connect(blue)
    colorless_to_black.connect(black)
    colorless_to_red.connect(red)
    colorless_to_green.connect(green)
