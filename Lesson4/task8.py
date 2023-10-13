def game(terra, power):
    for sublist in terra:
        for value in sublist:
            if value <= power:
                power += value
            else:
                break
    return power