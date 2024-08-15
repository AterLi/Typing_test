import tkinter.messagebox
from tkinter import *
import random


def choose_content():
    all_data = ["content1.txt", "content2.txt", "content3.txt"]
    return random.choice(all_data)


def show_data():
    chosen_file = choose_content()
    with open(file=chosen_file) as content:
        text = content.read()
    return text


def compare_data():
    # Message that shows user score
    def pop_up(score):
        click_ok = tkinter.messagebox.showinfo("Times up", message=f"Your score is: {score} WPM-words per minute.\n"
                                                                   f"The average typing speed is roughly 40 WPM.\n"
                                                                   f"Practice makes perfection!")
        # Close the window
        if click_ok:
            window.destroy()

    # Calcul score:
    original_data = data
    # Store typed data.
    typed_data = input_text.get("1.0", END)

    # Calcul words that matches.
    total_score = 0
    text = original_data.split(" ")
    user_data = typed_data.split(" ")
    # Removing '\n' that automatically is created when using get().
    user_data = [i.strip() for i in user_data]
    for i in range(len(user_data)):
        if user_data[i] == text[i]:
            total_score += 1
    print(total_score)
    # Call pop_up function.
    pop_up(score=total_score)
    return total_score


data = show_data()

window = Tk()
window.title("Ready for a typing test")
window.config(pady=20, padx=36)

canvas = Canvas(width=730, height=320, bg="#37B7C3")
canvas_text = canvas.create_text(365, 160, text=data, width=700, font=("Arial", 14, "bold"), fill="white")
canvas.grid(row=1, column=0, pady=10)

input_text = Text(height=10, width=52)
input_text.focus_set()
input_text.grid(row=2, column=0, pady=10)

button1 = Button(text="Stop test", command=compare_data)
button1.grid(row=3, column=0)

# After methode that will trigger to stop user to type and show the score.
window.after(60000, func=compare_data)


window.mainloop()