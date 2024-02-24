import random

from time import sleep

from colorama import Fore, Back, Style

from termcolor import colored



def show_menu():
    print(Fore.BLACK + Back.BLUE + ('1.Грати в "Поле-Чудес"  😎  ') + Style.RESET_ALL)
    sleep(1)
    print()
    print(Fore.BLACK + Back.BLUE + ('2. Вихід ⛔️ ') + Style.RESET_ALL)
    sleep(1)
    print()

def wheel_of_fortune_game():
    print()
    sleep(1)
    print(Fore.CYAN + Back.BLACK + "Грати у Поле-Чудес:" + Style.RESET_ALL)
    words = ["Python", "Програмування", "Розважальний", "Чат-бот", "Штучний інтелект"]
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 10

    while attempts > 0:
        display_word = "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        print()
        sleep(1)
        print(Fore.CYAN + Back.BLACK + f"Загадане слово: {display_word}" + Style.RESET_ALL)
        sleep(1)
        user_guess = input(colored(Fore.CYAN + Back.BLACK + "Введіть літеру або повне слово: " + Style.RESET_ALL)).lower()

        if len(user_guess) == 1:
            if not user_guess.isalpha():
                print()
                sleep(1)
                print(Fore.CYAN + Back.BLACK + "Невірний ввід. Будь ласка, введіть одну літеру або повне слово." + Style.RESET_ALL)
                continue
            elif user_guess in guessed_letters:
                print()
                sleep(1)
                print(Fore.CYAN + Back.BLACK + "Ви вже вводили цю літеру. Спробуйте іншу." + Style.RESET_ALL)
                continue
            else:
                guessed_letters.add(user_guess)
                if user_guess not in secret_word:
                    attempts -= 1
                    print()
                    sleep(1)
                    print(Fore.CYAN + Back.BLACK + f"Невірно! Залишилося спроб: {attempts}" + Style.RESET_ALL)
                    print()
                else:
                    if set(secret_word) <= guessed_letters:
                        print()
                        sleep(1)
                        print(Fore.CYAN + Back.BLACK + f"Вітаємо! Ви вгадали слово '{secret_word}'. " + Style.RESET_ALL)
                        print()
                        break
        elif len(user_guess) > 1:
            if user_guess == secret_word:
                print()
                sleep(1)
                print(Fore.CYAN + Back.BLACK + f"Вітаємо! Ви вгадали слово '{secret_word}'. " + Style.RESET_ALL)
                print()
                break
            else:
                attempts -= 1
                print()
                sleep(1)
                print(Fore.CYAN + Back.BLACK + f"Невірно! Залишилося спроб: {attempts}" + Style.RESET_ALL)
                print()

    else:
        print()
        sleep(1)
        print(Fore.CYAN + Back.BLACK + f"Ви програли! Загадане слово було: '{secret_word}'. " + Style.RESET_ALL)
        print()

def main():
    print(Fore.CYAN + Back.BLACK +
          f'Привіт, це програма розважальний чат-бот!\nОбери один пункт з меню: '
          + Style.RESET_ALL)
    sleep(1)
    print()

    while True:
        show_menu()
        print()
        sleep(1)
        option = input(colored(Fore.CYAN + Back.BLACK + "Ваш вибір🔎: " + Style.RESET_ALL))

        if option == '1':
            wheel_of_fortune_game()
            sleep(1)
        elif option == '2':
            print()
            sleep(1)
            print(Fore.CYAN + Back.BLACK + "До нової зустрічі.✌😉🤞" + Style.RESET_ALL)
            break
        else:
            print()
            sleep(1)
            print(Fore.CYAN + Back.BLACK + ("Невірний вибір.Спробуйте ще раз 🤨") + Style.RESET_ALL)

if __name__ == '__main__':
    main()
    