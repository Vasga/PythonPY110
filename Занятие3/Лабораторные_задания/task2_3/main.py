import json


def task():
    filename = "input.json"
    with open(filename) as f:# TODO считать содержимое JSON файла
        json.data = json.load(f)
    return max(json.data, key = lambda item: item["score"],)  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
