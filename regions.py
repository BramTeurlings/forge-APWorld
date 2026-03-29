from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import APQuestWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: APQuestWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: APQuestWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    colorless = Region("Colorless", world.player, world.multiworld)
    white = Region("White", world.player, world.multiworld)
    blue = Region("Blue", world.player, world.multiworld)
    black = Region("Black", world.player, world.multiworld)
    red = Region("Red", world.player, world.multiworld)
    green = Region("Green", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [colorless, white, blue, black, red, green]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # if world.options.hammer:
    #     top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #     regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: APQuestWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    colorless = world.get_region("Colorless")
    white = world.get_region("White")
    blue = world.get_region("Blue")
    black = world.get_region("Black")
    red = world.get_region("Red")
    green = world.get_region("Green")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
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

    # You can then connect the Entrance to the target region.
    colorless_to_white.connect(white)
    colorless_to_blue.connect(blue)
    colorless_to_black.connect(black)
    colorless_to_red.connect(red)
    colorless_to_green.connect(green)

    # An even easier way is to use the region.connect helper.
    # colorless.connect(right_room, "Overworld to Right Room")
    # right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    # colorless.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     colorless.connect(top_middle_room, "Overworld to Top Middle Room")
