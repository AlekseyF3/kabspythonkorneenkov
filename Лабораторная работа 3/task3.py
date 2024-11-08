def count_letters(txt):
    letter_count = {}
    txt = txt.lower()
    for char in txt:
        if char.isalpha():
            char_lower = char.lower()
            if char in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    return {key: value for key, value in letter_count.items() if key.islower()}


def calculate_frequency(letter_count):
    letters = sum(letter_count.values())  # общее количество букв
    frequency = {key: value / letters for key, value in letter_count.items()}
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_count = count_letters(main_str)
frequency = calculate_frequency(letter_count)

for key, value in frequency.items():
    print(f"{key}: {value: .2f}")

