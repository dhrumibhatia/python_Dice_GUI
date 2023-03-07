import tkinter as tk
import random

root = tk.Tk()
root.title("Dice Roller")

def roll_dice():
    dice_value = random.randint(1,6)
    label_result["text"] = (f"You rolled a {dice_value}!")

label_title = tk.Label(root, text="Roll your fortunate dice!", font=("Arial", 18))
label_title.pack(pady=10)

button_roll = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=roll_dice)
button_roll.pack(pady=20)

label_result = tk.Label(root, text="", font=("Arial", 18))
label_result.pack(pady=10)

root.mainloop()


if __name__== "__main__":
  main()
