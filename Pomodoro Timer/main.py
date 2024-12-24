#Pomodoro Timer

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
RED = "red"
GREEN = "green"
WHITE = "white"
BLACK = "black"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counter = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(counter)
    canvas.itemconfig(timer, text = "00:00")
    label.config(text = "Timer", fg = WHITE)
    tick.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text = "Break", fg = WHITE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text = "Break", fg = WHITE)
    else:
        count_down(work_sec)
        label.config(text = "Work", fg = RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer, text = f"{count_min}:{count_sec}")
    if count > 0:
        global counter
        counter = window.after(1000, count_down, count - 1)
    else:
        start_timer() 
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        tick.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 100, bg = BLACK)

canvas = Canvas(width = 200, height = 224, bg = BLACK, highlightthickness = 0)
tomato_img = PhotoImage(file = "./tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer = canvas.create_text(100, 130, text = "00:00", fill = WHITE, font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

label = Label(text = "Timer", bg = BLACK, fg = WHITE, font = (FONT_NAME, 35, "bold"))
label.grid(row = 0, column = 1)

start = Button(text = "Start", bg = BLACK, fg = WHITE, font = (FONT_NAME, 20, "bold"), command = start_timer)
start.grid(row = 2, column = 0)

reset = Button(text = "Reset", bg = BLACK, fg = WHITE, font = (FONT_NAME, 20, "bold"), command = reset_timer)
reset.grid(row = 2, column = 2)

tick = Label(bg = BLACK, fg = GREEN, font = (FONT_NAME, 20, "bold"))
tick.grid(row = 3, column = 1)


window.mainloop()
