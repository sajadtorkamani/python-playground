from typing import List


def freed_prisoners(prison_cells: List[bool]) -> int:
    if prison_cells[0] is False:
        return 0

    num_prisoners_freed = 0
    current_cell_index = 0

    while True in prison_cells[current_cell_index::]:
        current_cell_index = unlock_prisoner(prison_cells, current_cell_index)
        num_prisoners_freed += 1

    return num_prisoners_freed


def unlock_prisoner(prison_cells: List[bool], current_cell_index: int) -> int | None:
    for cell_index, is_cell_unlocked in enumerate(prison_cells):
        # Skip cells we've already visited
        if cell_index < current_cell_index:
            continue

        # Free prison cell
        if is_cell_unlocked:
            flip_cell_locks(prison_cells)
            return cell_index + 1


def flip_cell_locks(prison_cells: List[bool]) -> List[bool]:
    for cell_index, is_cell_unlocked in enumerate(prison_cells):
        prison_cells[cell_index] = not is_cell_unlocked

    return prison_cells
