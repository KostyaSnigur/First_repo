from pathlib import Path

path = Path('')

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        if i.is_file():
            files.append(i.name)
    return files, folders


