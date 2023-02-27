import tkinter as tk

# Constants for the dialog box
PINK = "#e2979c"
FONT = ("Courier", 50, "bold")

# Set up global variables: initial timer count and timer id
timer = 5
timer_id = "5_sec"


# Start writing: start button and instruction label disappear, text field activates, timer starts
def start_writing():
    name_label.pack_forget()
    start_button.pack_forget()
    timer_label.pack(pady=20)
    text_field.pack(pady=20)
    text_field.config(state="normal")
    count_down(timer)


# Reset and restart timer if a key is pressed or if the time ran out
def reset_timer():
    global timer
    timer = 5
    count_down(timer)


# Stop count down if a key is pressed
def cancel_count(event):
    global timer_id
    window.after_cancel(timer_id)
    reset_timer()


def count_down(count):
    timer_label.config(text=f"{count} seconds", fg=PINK)
    if count > 0:
        # Count down to 0 seconds or reset timer on a keystroke
        global timer_id
        timer_id = window.after(1000, count_down, count - 1)
        window.bind("<Key>", cancel_count)
    else:
        # Clear the text field and reset the timer
        text_field.delete("1.0", 'end-1c')
        reset_timer()


# App window
window = tk.Tk()
window.title("Disappearing Text")
window.config(pady=20, padx=20)
window.state("zoomed")

name_label = tk.Label(text="Keep writing!\nIf you stop typing for 5 seconds,\nyour progress will be lost",
                      fg=PINK,
                      font=FONT)
name_label.pack(pady=50)

timer_label = tk.Label(text=f"{timer} seconds", fg=PINK, font=FONT)

start_button = tk.Button(text="Start writing", font=FONT, padx=3, pady=3, command=start_writing, fg="black")
start_button.pack(pady=20)

text_field = tk.Text(height=100, width=200, font=("Courier", 20, "normal"), padx=5, pady=5, spacing3=5)

window.mainloop()
