def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    # return max(len(word) for word in list_words)  # TODO записать выражение-генератор
    return min(len(word) for word in list_words)

if __name__ == "__main__":
    print(task())
