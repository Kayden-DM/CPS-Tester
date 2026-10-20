import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

score = 0
time_left = 0
start_time = 0


def add_point():
    global score
    score += 1
    score_label.configure(text=f"Score: {score}")


def start_game():
    global time_left, start_time
    try:
        time_left = int(entry.get())
    except ValueError:
        time_label.configure(text="Please enter a number!")
        return

    if time_left <= 0:
        time_label.configure(text="Enter a positive number!")
        return

    start_time = time_left
    entry.configure(state="disabled")
    start_btn.configure(state="disabled")
    click_btn.configure(state="normal")
    time_label.configure(text=f"Time: {time_left}")
    tick()


def tick():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.configure(text=f"Time: {time_left}")
        root.after(1000, tick)
    else:
        time_end()


def time_end():
    cps = score / start_time
    time_label.configure(text=f"Your CPS was {cps:.2f}")
    click_btn.configure(state="disabled")


root = ctk.CTk()
root.title("CPS Tester")
root.geometry("800x600")

time_label = ctk.CTkLabel(root, text="Time: -", font=("Arial", 20))
time_label.pack(pady=10)

score_label = ctk.CTkLabel(root, text=f"Score: {score}", font=("Arial", 20))
score_label.pack(pady=10)

entry = ctk.CTkEntry(root, font=("Arial", 16), justify="center", width=200,
                     placeholder_text="Time in seconds...")
entry.pack(pady=5)

start_btn = ctk.CTkButton(root, text="Start", font=("Arial", 14), width=120,
                          command=start_game)
start_btn.pack(pady=10)

click_btn = ctk.CTkButton(
    root,
    text="Click me",
    font=("Arial", 24, "bold"),
    width=400,
    height=200,
    state="disabled",
    command=add_point
)
click_btn.pack(pady=20)

root.mainloop()