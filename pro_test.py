# cards = {'A': 1, 'B': 2, 'C': 4}

# def answer(cards):
#     print(list(cards.values()))
#     if set(cards.values()) > {1, 2}:
#         for key, value in cards.items():
#             if value != 1 and value != 2:
#                 print(f"{key}=>MAX")
#     if set(cards.values()) > {4, 5}:
#         for key, value in cards.items():
#             if value != 4 and value != 5:
#                 print(f"{key}=>MIN")


# answer(cards)

chara_exp = (2, 1, 1.3)
exp = 1
print(len(chara_exp), exp)

def check_chara_exp(chara_exp):
    for chara in chara_exp:
        if chara > 1000.0:
            return False
    return True

if check_chara_exp(chara_exp):
    for chara in chara_exp:
        print(chara)
else:
    print("キャラクターの必要経験値は0から1000.0の範囲で設定してください")

count = 1
total_exp = 0
while True:
    total_exp += exp
    if total_exp >= sum(chara_exp):
        print(count)
        break
    count += 1
    
