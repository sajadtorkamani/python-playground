from typing import List, Optional


# Determine max number of stone picks you can make from the materials.
# To make a stone pick, you need 3 Cobblestones and 2 Sticks.
# Wood can be converted into 4 Sticks.

def stone_pick(materials: Optional[List[str]] = None) -> int:
    if materials is None:
        return 0

    num_stone_picks = 0
    usable_materials = []

    # Iterate through materials
    for material in materials:
        print(material)

        # If it's a Cobblestone or Stick, add it to the usable materials list
        if material in ['Cobblestone', 'Sticks']:
            usable_materials.append(material)

        # If it's a Wood, add 4 Sticks to the usable materials list
        if material == 'Wood':
            usable_materials += ['Sticks'] * 4

    while usable_materials.count('Cobblestone') >= 3 and usable_materials.count(
            'Sticks') >= 2:
        num_stone_picks += 1

        # Remove material from usable_materials
        usable_materials.remove('Cobblestone')
        usable_materials.remove('Cobblestone')
        usable_materials.remove('Cobblestone')
        usable_materials.remove('Sticks')
        usable_materials.remove('Sticks')

    # If we do have enough materials, increment the num_stone_picks
    # When we don't have enough, return num_stone_picks
    return num_stone_picks
