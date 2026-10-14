This README is made with AI

🖱️ Python CPS (Clicks Per Second) Tester
A modern desktop application built with Python and CustomTkinter that measures how many times you can click a button in a given number of seconds. It calculates your CPS (Clicks Per Second) and displays the result at the end of the timer. It's a great beginner project for learning about modern GUI programming, timers, global variables, and event-driven design in Python.

📖 Python CPS Tester
The Python CPS Tester is a graphical application built with CustomTkinter — a modern, themeable wrapper around Tkinter. The app launches in dark mode with a blue color theme, giving it a sleek, contemporary look.

The user enters a number of seconds into a text field, presses Start, and then clicks a large button as many times as possible before the timer runs out. The score label updates instantly with each click, and the time label counts down every second.

When time expires, the click button is disabled, and the program displays the user's CPS — calculated as the total score divided by the chosen time. The CPS is formatted to two decimal places for clarity.

The interface is built entirely with CustomTkinter widgets, so the only external dependency is the customtkinter library. It's a fun, quick, and useful tool for anyone curious about their clicking speed.

✨ Features
Dark mode by default – Uses CustomTkinter's built-in appearance mode.

Blue color theme – Applied globally for a modern, cohesive look.

Custom timer length – Enter any positive number of seconds via a placeholder-labeled entry field.

Live countdown – The time label updates every second while the timer runs.

Live score display – The score label updates instantly with each click.

Start button – Begins the countdown and enables the click button.

Click button – A large, easy-to-hit button for scoring points.

CPS calculation – Automatically computes score / start_time when the timer ends.

Two-decimal precision – CPS is displayed as e.g. 5.42.

Input validation – Rejects non-numeric entries and non-positive values with helpful messages.

Button state management – Prevents interaction before the game starts and after it ends.

Disabled entry after start – The time entry locks once the game begins, preventing mid-game changes.

Clean, spacious layout – 800×600 window with a large clickable area.

🛠️ What It Uses
Language & Library
Python 3

CustomTkinter – A modern, themeable wrapper for Tkinter.

Install with: pip install customtkinter

Key Variables
Variable	Purpose
score	Tracks the number of clicks the user has made.
time_left	Counts down the remaining seconds.
start_time	Stores the original timer length, used to calculate CPS.
Key Functions
Function	Purpose
add_point()	Increments the score by 1 and updates the score label.
start_game()	Validates the timer input, resets state, enables the click button, and starts the countdown.
tick()	The main countdown loop. Decrements time_left by 1 every second using root.after(1000, tick).
time_end()	Calculates CPS, displays the final result, and disables the click button.
CustomTkinter Widgets & Methods Used
ctk.set_appearance_mode("dark") – Sets the global theme to dark mode.

ctk.set_default_color_theme("blue") – Applies the blue color scheme.

ctk.CTk() – Main application window.

ctk.CTkLabel – Displays the timer and score.

ctk.CTkButton – The Start button and the big Click button.

ctk.CTkEntry – Accepts the timer duration from the user, with a placeholder.

.pack() – Geometry manager for laying out widgets.

.configure() – Dynamically updates label text and button states.

.get() – Reads the current text from the entry field.

root.after() – Schedules the next countdown tick without blocking the GUI.

root.mainloop() – Starts the CustomTkinter event loop.

Python Concepts Demonstrated
Global variables – Shared across functions for score, time_left, and start_time.

Exception handling – try/except ValueError for safe numeric input.

Conditional logic – Validating inputs and checking timer state.

Event-driven programming – Buttons trigger functions on click.

F-strings – Formatted output for score, time, and CPS.

Float formatting – :.2f to round CPS to two decimal places.

Widget state management – Enabling/disabling buttons and entries based on game state.

Built-in Functions Used
int() – Converts the entry text into a whole number.

f"{...}" – String formatting for labels.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
cps_tester.py
Then install the required library:

bash
pip install customtkinter
▶️ How to Run
Make sure you have Python 3 installed (python.org).

Install CustomTkinter:

bash
pip install customtkinter
Save the code as cps_tester.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python cps_tester.py
Enter the number of seconds you want, press Start, and click the big button as fast as you can!

🐍 Made with Python
This project is written in Python 3 and uses CustomTkinter to give the interface a modern, polished look. It's a fun and practical example of how CustomTkinter's widgets and timing methods can be combined to build a small interactive application.

Whether you're a beginner exploring GUI development or someone who just wants to test their clicking speed, this project is a great starting point.

💡 Possible Future Improvements
Allow multiple rounds – Reset the score and time without restarting the app.

Add a "Reset" button – Re-enable the entry and Start button after a game ends.

High score tracking – Save the best CPS across sessions to a file.

Visual feedback on click – Flash the button or play a click sound.

Progress bar – Add a CustomTkinter progress bar to visually show time remaining.

Countdown before start – A "3, 2, 1, Go!" intro for fairness.

CPS graph – Track clicks over time and plot them at the end.

Theme switcher – Add a toggle between light and dark modes at runtime.

Leaderboard – Let multiple players compete and rank their CPS scores.

Adjustable window size – Use a smaller default size for smaller screens.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.
