points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if not coordinates:
        return 0
    total_distance = 0
    for i in range(len(coordinates) - 1):
        point1 = min(coordinates[i], coordinates[i + 1])
        point2 = max(coordinates[i], coordinates[i + 1])
        distance = points[(point1, point2)]
        total_distance += distance

    return total_distance