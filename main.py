from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 2 != 0:
        count_down(work_time)
        timer_label.config(text="Work", fg=GREEN)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = "{:02d}".format(math.floor(count / 60))
    count_sec = "{:02d}".format(count % 60)
    # print(f"{count_min} : {count_sec}")

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"

        checkmarks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(150, 130, image=tomato_img)
timer_text = canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


# TIMER LABEL
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

# CHECKMARK LABELS
checkmarks_label = Label(font=(FONT_NAME, 20, "normal"), bg=YELLOW, fg=GREEN)
checkmarks_label.grid(column=2, row=4)

# START BUTTON
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=lambda: start_timer())
start_button.grid(column=1, row=3)

# RESET BUTTON
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=lambda: reset_timer())
reset_button.grid(column=3, row=3)


window.mainloop()
