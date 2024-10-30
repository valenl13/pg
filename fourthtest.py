# Simplified implementation of `je_tah_mozny` for clarity and readability
def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Check if target position is within board limits and not occupied
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8) or cilova_pozice in obsazene_pozice:
        return False

    typ = figurka['typ']
    start_pos = figurka['pozice']
    row_diff, col_diff = cilova_pozice[0] - start_pos[0], cilova_pozice[1] - start_pos[1]

    # Rules for each chess piece
    if typ == 'pěšec':
        if start_pos[0] == 2 and row_diff == 2 and col_diff == 0:
            return (start_pos[0] + 1, start_pos[1]) not in obsazene_pozice and cilova_pozice not in obsazene_pozice
        return row_diff == 1 and col_diff == 0 and cilova_pozice not in obsazene_pozice

    elif typ == 'jezdec':
        return (abs(row_diff), abs(col_diff)) in {(2, 1), (1, 2)}

    elif typ == 'věž':
        if row_diff == 0:  # Horizontal move
            step = 1 if col_diff > 0 else -1
            return all((start_pos[0], start_pos[1] + i) not in obsazene_pozice for i in range(step, col_diff, step))
        elif col_diff == 0:  # Vertical move
            step = 1 if row_diff > 0 else -1
            return all((start_pos[0] + i, start_pos[1]) not in obsazene_pozice for i in range(step, row_diff, step))

    elif typ == 'střelec':
        if abs(row_diff) == abs(col_diff):  # Diagonal move
            step_row = 1 if row_diff > 0 else -1
            step_col = 1 if col_diff > 0 else -1
            return all((start_pos[0] + i * step_row, start_pos[1] + i * step_col) not in obsazene_pozice
                       for i in range(1, abs(row_diff)))

    elif typ == 'dáma':
        if row_diff == 0:  # Horizontal move
            step = 1 if col_diff > 0 else -1
            return all((start_pos[0], start_pos[1] + i) not in obsazene_pozice for i in range(step, col_diff, step))
        elif col_diff == 0:  # Vertical move
            step = 1 if row_diff > 0 else -1
            return all((start_pos[0] + i, start_pos[1]) not in obsazene_pozice for i in range(step, row_diff, step))
        elif abs(row_diff) == abs(col_diff):  # Diagonal move
            step_row = 1 if row_diff > 0 else -1
            step_col = 1 if col_diff > 0 else -1
            return all((start_pos[0] + i * step_row, start_pos[1] + i * step_col) not in obsazene_pozice
                       for i in range(1, abs(row_diff)))

    elif typ == 'král':
        return max(abs(row_diff), abs(col_diff)) == 1

    return False  # If no conditions are met, return False

# This simplified function should fulfill the requirements with a more direct approach to each piece's movement logic.
