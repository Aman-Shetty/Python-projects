import math
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
reps = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(TIMER)
    canvas.itemconfig(Text_timer, text="00:00")
    timer["text"] = "Timer"
    timer["fg"] = GREEN
    check["text"] = ''
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(work_sec)
        timer["text"] = "Work"
        timer["fg"] = GREEN
        reps += 1
    elif reps == 7:
        count_down(long_sec)
        timer["text"] = "Long-Break"
        timer["fg"] = RED
        reps = 0
    else:
        count_down(short_sec)
        timer["text"] = "Short-Break"
        timer["fg"] = PINK
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(Text_timer, text=f"{count_min}:{count_sec}")

    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark = check["text"]
            check["text"] = checkmark + "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
Text_timer = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 38, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)
start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()
