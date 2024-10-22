# TODO  Напишите функцию count_letters

def count_letters(txt):
    l_count = {}
    txt = txt.lower()
    for char in txt:
        if char.isalpha():
            char_lower = char.lower()
            if char in l_count:
                l_count[char_lower] += 1
            else:
                l_count[char_lower] = 1
    return {key: value for key, value in l_count.items() if key.islower()}


# TODO Напишите функцию calculate_frequency

def calculate_frequency(l_count):
    letters = sum(l_count.values()) # общее количество букв
    frequency = {key: round(value / letters, 2) for key, value in l_count.items()}
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

# TODO Распечатайте в столбик букву и её частоту в тексте

l_count = count_letters(main_str)
frequency = calculate_frequency(l_count)

for key, value in frequency.items():
    print(f"{key}: {value:.2f}")