# librerie
import random
import time
from collections import Counter     # importo la classe Counter


# legge la lista di parole
with open("words.txt", "r") as word_pool:
    words = [line.strip() for line in word_pool]
# FONTE della lista di acronimi: https://itools.subhashbose.com/wordfind/common-anagrams/


# VARIABILI
width = 150     # variabile per type specifier (centrare il testo)
title_line = "*********************************************"
title = "*       WRITE THE ACRONYM: THE GAME!        *"

command = ""    # comando di start

in_game = True  # flag del ciclo while
question_number = 0
score = 0


# FUNZIONI
# 1. countdown prima di ogni round
def countdown():
    print("------")
    for t in reversed(range(1, 4)):
        print(t, end=" ")
        time.sleep(1)
    print()
    print("------")

# 2. istruzioni e inizio gioco
def is_ready(com):
    welcome = "Welcome to 'WRITE THE ACRONYM: THE GAME!'"
    print(f"{welcome:^{width}}")
    print("In this game, you need to create an acronym from the word shown.")
    print("Be careful:")
    print("1. The acronym must be different from the original word.")
    print("2. It must contain exactly the same number of each letter as the original word.")
    print("If you make a mistake, the game is over!")
    print("Try to get the highest score by correctly forming as many acronyms in a row as you can.")
    print()
    while com != "START":
        com = input("Type START to begin the game: ").upper()

# 3. controlla se l'acronimo inserito è nella lista
def is_in_list(acr):
    if acr in words:
        return True
    else:
        print("Not in the list")
        return False

# 4. controlla che l'acronimo sia diverso dalla parola iniziale
def is_different(ch_w, acr):
    if acr != ch_w:
        return True
    else:
        print("You typed the same word")
        return False

# 5. controlla che tutte le lettere dell'acronimo appaiano nella parola iniziale
def is_acronym(ch_w, acr):
    for letter in acr:
        if letter not in ch_w:
            print("Not a valid acronym")
            return False
    return True

# 6. controlla che tutte le lettere appaiano LO STESSO NUMERO DI VOLTE nelle due parole
def same_letter_counts(ch_w, acr):
    if Counter(ch_w) == Counter(acr):
        return True
    else:
        print("Wrong number of letters")
        return False

# MAIN
# titolo
print(f"{title_line:^{width}}")
print(f"{title:^{width}}")
print(f"{title_line:^{width}}")

print()

# istruzioni
is_ready(command)

# inizio gioco
while in_game:
    countdown()
    print()

    question_number += 1

    # seleziono la parola e la rimuovo dalla lista
    chosen_word = random.choice(words)
    words.remove(chosen_word)
    print(f"QUESTION {question_number}: your word is {chosen_word.upper()}")

    # inserisco l'acronimo
    acronym = input("Please, type your acronym: ").lower()
    in_game = (is_in_list(acronym)
               and is_different(chosen_word, acronym)
               and is_acronym(chosen_word, acronym)
               and same_letter_counts(chosen_word, acronym))
    if in_game:
        score += 1
        print("Correct!")

# fine gioco
print()

game_over ="GAME OVER!"
print(f"{title_line:^{width}}")
print(f"{game_over:^{width}}")
print(f"{title_line:^{width}}")


if score < 2:
    final_message = "Better luck next time!"
elif score < 5:
    final_message = "Good job!"
else:
    final_message = "You're a real champion!"

print(f"Your final score is {score}.")
print(f"{final_message}")