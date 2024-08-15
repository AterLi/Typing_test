# Typing test without GUI
import time
import threading
import random


def press_key_timer(delay):
    time.sleep(delay)
    print("\nTimes up")


def choose_content():
    all_data = ["content1.txt", "content2.txt", "content3.txt"]
    return random.choice(all_data)


def show_data():
    chosen_file = choose_content()
    with open(file=chosen_file) as content:
        text = content.read()
    return text


def compare_data(to_type_data):
    # After 60 seconds key enter is triggered.
    delay = 60
    enter_thread = threading.Thread(target=press_key_timer, args=(delay,))
    enter_thread.start()

    # Calcul words that matches.
    total_point = 0
    text = to_type_data.split(" ")
    user_input = input("Challenge started:\n")
    user_data = user_input.split(" ")
    for i in range(len(user_data)):
        if user_data[i] == text[i]:
            total_point += 1
    return total_point


data = show_data()
print(data)
calcul = compare_data(data)
print(f"Score: {calcul}")
