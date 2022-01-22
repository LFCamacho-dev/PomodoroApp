from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(150, 130, image=tomato_img)
canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
# TIMER LABEL
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

# CHECKMARK LABELS
checkmarks_label = Label(text="✔✔✔✔", font=(FONT_NAME, 20, "normal"), bg=YELLOW, fg=GREEN)
checkmarks_label.grid(column=2, row=4)

# START BUTTON
start_button = Button(text="Start", bg=YELLOW, highlightthickness= 0)
start_button.grid(column=1, row=3)
# RESET BUTTON
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness= 0)
reset_button.grid(column=3, row=3)


window.mainloop()
