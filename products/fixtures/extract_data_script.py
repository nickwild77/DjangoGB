from json import load


def extract_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = load(f)
    return data
