def get_grade(key):
    grades = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    return grades.get(key, None)

def get_description(key):
    descriptions = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    return descriptions.get(key, None)