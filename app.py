import sys
import random
from hangman_ascii import hangman_ascii_list


def make_word() -> str:
    rand_line = random.randint(0, 100)
    try:
        with open('summary.txt', encoding='utf-8') as file:
            i = 0
            while i != rand_line:
                file.readline()
                i += 1
            return file.readline().strip().lower()
    except FileNotFoundError:
        print('Error: Файл summary.txt не найден.')
        sys.exit(1)
    except IOError:
        print('Error: Ошибка чтения файла summary.txt')
        sys.exit(1)


def stage_start() -> int:
    while True:
        enter = input(f'1) Начать новую игру\n0) Выйти из приложения\n> ')
        try:
            enter_move = int(enter)
            if enter_move not in (0, 1):
                raise ValueError
            return enter_move
        except ValueError:
            print(f'Неизвествная команда {enter}.\nТребуется ввести 0 или 1\n> ')


def enter_complexity() -> int:
    while True:
        enter = input(f'Введите сложность партий:\n1 - Легкая\n2 - Средняя\n3 - Сложная\n> ')
        try:
            enter_move = int(enter)
            if enter_move not in (1, 2, 3):
                raise ValueError
            return enter_move
        except ValueError:
            print(f'Неизвествная команда {enter}.')


def enter_char(entered_chars: list) -> str:
    while True:
        char = input('Введите букву> ').strip()
        if len(char) == 1 and ord('а') <= ord(char.lower()) <= ord('я'):
            if char.lower() not in entered_chars:
                return char.lower()
            else:
                print(f'Буква {char} уже была введена ранее')
        else:
            print(f'Некоректная введенная буква - {char}. Требуется ввести букву от А до Я')


def complexity_hangman_ascii_list(complexity: int):
    match complexity:
        case 1:
            return list(x for x in range(6))
        case 2:
            return 0, 1, 3, 4, 5
        case 3:
            return 0, 1, 3, 5


def start_game(complexity: int):
    dict_complexity = {1: 5, 2: 4, 3: 3}  # сложность: кол-во ошибок
    entered_chars = []
    errors = 0
    shadow_word = make_word()
    list_complexity_hangman_ascii = complexity_hangman_ascii_list(complexity)
    print(hangman_ascii_list[list_complexity_hangman_ascii[errors]])
    first_open_chars = random.sample(list([ch for ch in shadow_word]), k=(3, 2, 1)[complexity - 1])
    dict_chars = {key: True if key in first_open_chars else False for key in shadow_word}
    while True:
        print("".join([ch if dict_chars.get(ch) else '_' for ch in shadow_word]))
        print(f'Ошибок - {errors}')
        char = enter_char(entered_chars)
        entered_chars.append(char)
        check = dict_chars.get(char, None)
        if check is None:
            print(f'Введенной буквы - \'{char}\' нет в загаданном слове')
            errors += 1
        elif check:
            print(f'Введенная буква \'{char}\' уже разгадана')
        else:
            dict_chars[char] = True
            print(f'Угадана буква - \'{char}\'')

        print(hangman_ascii_list[list_complexity_hangman_ascii[errors]])

        if errors == dict_complexity.get(complexity):
            print(f'Вы проиграли.\nЗагаданное слово - {shadow_word}\n')
            return

        if len(set(dict_chars.values())) == 1:
            print(f'Вы победили.\nЗагаданное слово - {shadow_word}\n')
            return


if __name__ == '__main__':
    move = stage_start()
    while move:
        start_game(enter_complexity())
        move = stage_start()
