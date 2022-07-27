""" Pomodoro
    Coded by TechGYQ
    www.MythosWorks.com
    2022.07.26-1840 """


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
CHECK_MARK = '✔'
# TODO Add in for break & long break at some point.
# SHORT_BREAK = '☕'
# LONG_BREAK = '😴'
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    global timer
    display.after_cancel(timer)
    reps = 0
    status_label.config(text='Timer', fg=GREEN)
    backdrop.itemconfig(timer_text, text='00:00')
    podo_label.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        status_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        status_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        status_label.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    backdrop.itemconfig(timer_text, text=f'{count_minutes}:{count_seconds}')
    if count > 0:
        timer = display.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_count = math.floor(reps/2)
        for _ in range(work_count):
            mark += CHECK_MARK
        podo_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
display = Tk()
display.title('Pomodoro')
display.config(padx=100, pady=50, bg=YELLOW)

status_label = Label(text='Timer', font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=GREEN)
status_label.grid(column=1, row=0)

backdrop = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
backdrop.create_image(100, 112, image=tomato_img)
timer_text = backdrop.create_text(110, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
backdrop.grid(column=1, row=1)

start_button = Button(text='Start', fg='black', bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

podo_label = Label(font=(FONT_NAME, 20, 'bold'), bg=YELLOW, fg=GREEN)
podo_label.grid(column=1, row=3)

reset_button = Button(text='Reset', fg='black', bg=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

display.mainloop()
