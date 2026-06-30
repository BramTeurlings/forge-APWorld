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
    regions = {
        "Colorless": world.get_region("Colorless"),
        "White": world.get_region("White"),
        "Blue": world.get_region("Blue"),
        "Black": world.get_region("Black"),
        "Red": world.get_region("Red"),
        "Green": world.get_region("Green"),
    }

    colored_regions = [
        regions["White"],
        regions["Blue"],
        regions["Black"],
        regions["Red"],
        regions["Green"],
    ]

    world.random.shuffle(colored_regions)

    previous = regions["Colorless"]

    for region in colored_regions:
        entrance = Entrance(
            world.player,
            f"{previous.name} to {region.name}",
            parent=previous
        )
        previous.exits.append(entrance)
        entrance.connect(region)

        world.set_rule(
            entrance,
            lambda state, rune=f"{region.name} Rune": state.has(rune, world.player)
        )

        previous = region
