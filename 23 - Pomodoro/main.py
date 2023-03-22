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
def start_timer():
    countdown(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(column=0, row=3)

btn_end = Button(text="Reset", highlightthickness=0)
btn_end.grid(column=2, row=3)

lbl_check = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
lbl_check.grid(column=1, row=3)

lbl_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
lbl_timer.grid(column=1, row=0)

window.mainloop()
