import random
import time

# Списък с думи за играта
words = [
    # Плодове
    "ябълка", "банан", "череша", "фурма", "смокиня", "грозде", "киви", "лимон", "лайм", "манго",
    "диня", "портокал", "праскова", "круша", "слива", "ананас", "нар", "малина", "ягода", "диня",
    "кайсия", "боровинка", "кокос", "личи", "нектарина", "папая", "пасифлора", "мандарина",

    # Зеленчуци
    "морков", "картоф", "домат", "лук", "краставица", "чушка", "спанак", "броколи", "зеле", "карфиол",
    "целина", "царевица", "патладжан", "чесън", "джинджифил", "маруля", "гъба", "грах", "ряпа", "тиквичка",
    "артишок", "аспержи", "цвекло", "чили","праз", "магданоз", "тиква", "ряпа",

    # Животни
    "котка", "куче", "кравa", "кон", "овца", "коза", "петел", "патица", "свиня", "зайче",
    "мечка", "сърна", "лисица", "вълк", "тигър", "лъв", "слон", "зебра", "жираф", "кенгуру",
    "панда", "маймуна", "катерица", "прилеп", "кит", "делфин", "акула", "октопод", "раци", "тюлен",
    "мравка", "пчела", "пеперуда", "паяк", "комар", "жаба", "гущер", "игуана", "костенурка",
    "алпака", "бизон", "гепард", "кон", "ему", "фламинго", "гекон", "лисица", "панда","динозавър",

    # Риби
    "сьомга", "тон", "пъстърва", "херинга", "треска", "сардина", "аншоа","щука", "сом", "распер",
    "пъстърва", "халибут", "баракудa", "скат", "морско конче", "рак", "скарида","омар", "мъздруга"

    # Превозни средства
    "кола", "автобус", "камион", "паровоз", "велосипед", "мотор", "скутер", "самолет", "хеликоптер", "лодка",
    "кораб", "подводница", "яхта", "кану", "каяк", "трамвай", "тролейбус", "ван", "джип", "булдозер", "кран",
    "трактор", "снегоход", "ракета", "амфибия", "скейтборд", "ролери", "парапланер", "джет", "картинг", "ферибот",
    "параход", "колело", "тротинетка",

]

# Структура на обесването
HANGMAN_STRUCTURE = [
    (1, 4, "+-----"),  # Горна част на стойката
    (2, 4, "|"),  # Въже над главата
    (3, 4, "O"),  # Глава
    (4, 4, "|"),  # Тяло
    (4, 3, "/"),  # Лява ръка
    (4, 5, "\\"),  # Дясна ръка
    (5, 3, "/"),  # Ляв крак
    (5, 5, "\\"),  # Десен крак
]

BOARD_WIDTH = 7
BOARD_HEIGHT = 6


def draw_board(missed_count):
    board = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    for i in range(missed_count):
        x, y, char = HANGMAN_STRUCTURE[i]
        board[x][y] = char

    for row in board:
        print("".join(row))
    print("===")

def get_random_word():
    return random.choice(words).upper()


def display_game(missed_letters, correct_letters, secret_word):
    print("\033c", end="")
    draw_board(len(missed_letters))
    print("\nПропуснати букви:", " ".join(missed_letters))

    blanks = ["_" if letter not in correct_letters else letter for letter in secret_word]
    print("Търсена дума:", " ".join(blanks))
    print()


def main():
    print(r"""
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                            __/ |                       
                           |___/        
    =============Добре дошъл в играта Hangman!=============""")

    secret_word = get_random_word()
    missed_letters = []
    correct_letters = []
    game_is_done = False

    while not game_is_done:
        display_game(missed_letters, correct_letters, secret_word)

        guess = input("Познай буква: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Моля, въведи само една буква!")
            time.sleep(1)
            continue

        if guess in missed_letters or guess in correct_letters:
            print("Вече си опитал тази буква.")
            time.sleep(1)
            continue

        if guess in secret_word:
            correct_letters.append(guess)


            if all(letter in correct_letters for letter in secret_word):
                display_game(missed_letters, correct_letters, secret_word)
                print(f"Браво! Позна думата '{secret_word}'")
                game_is_done = True
        else:
            missed_letters.append(guess)


            if len(missed_letters) == len(HANGMAN_STRUCTURE):
                display_game(missed_letters, correct_letters, secret_word)
                print(f"Ти не позна! Думата беше: {secret_word}")
                game_is_done = True

        if game_is_done:
            if input("Искаш ли да играеш пак? (да/не): ").lower().startswith("д"):
                secret_word = get_random_word()
                missed_letters = []
                correct_letters = []
                game_is_done = False

if __name__ == "__main__":
    main()
