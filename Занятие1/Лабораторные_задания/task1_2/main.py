def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return max(map(len,list_words)) # TODO найти длину самого длинного слова
    # return len(map(max,list_words))

if __name__ == "__main__":
    print(task())
