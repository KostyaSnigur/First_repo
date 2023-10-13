def lookup_key(data, value):
    keys = []
    for key, val in data.items():
        if val == value:
            keys.append(key)
    return keys

        