def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    # return min(map(len, list_words))  # используй ключевую у функции min, по которой она долна определять минимальный элемент
    return min(list_words, key= len)

if __name__ == "__main__":
    print(task())
