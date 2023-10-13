def format_ingredients(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        formatted = ", ".join(items[:3]) + " and " + items[-1]
        return formatted