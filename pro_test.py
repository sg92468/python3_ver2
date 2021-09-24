cards = {'A': 1, 'B': 2, 'C': 4}

def answer(cards):
    print(list(cards.values()))
    if set(cards.values()) > {1, 2}:
        for key, value in cards.items():
            if value != 1 and value != 2:
                print(f"{key}=>MAX")
    if set(cards.values()) > {4, 5}:
        for key, value in cards.items():
            if value != 4 and value != 5:
                print(f"{key}=>MIN")


answer(cards)