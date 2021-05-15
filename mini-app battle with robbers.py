import random

# constants
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("СТРЕЛА","КОШЕЛЁК","САПОГИ","БЕДНОСТЬ","ГРАБЁЖ","ЧЕСТЬ","СИЛА","СМЕКАЛКА","ХИТРОСТЬ","ДОБЫЧА")

word = random.choice(WORDS)  # слово, которое нужно угадать
so_far = "-" * len(word)  # тире для каждой буквы из угадываемого слова
wrong = 0  # количество ошибок
used = []  # буквы,которые уже угаданы

print("Добро пожаловать в виселицу.Удачи!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы использовали буквы:\n", used)
    print("\nЭто слово:\n", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()

    while guess in used:
        print("Вы уже использовал букву", guess)
        guess = input("Введите букву: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nДа!", guess, "есть в этом слове!")
        
        # интеграция буквы на место пропуска
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nК сожалению,", guess, "нет в этом слове.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nТы проиграл(")
else:
    print("\nТы угадал!")

print("\nЭто слово", word)

input("\n\nНажми на ENTER,чтобы выйти.")
