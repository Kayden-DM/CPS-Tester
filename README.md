## CPS Tester
A desktop click-speed tester built with CustomTkinter. It lets the user set a time limit, click as fast as possible for that duration, and calculates their clicks per second (CPS) at the end.

## Features
Custom Time Limit — Enter any positive number of seconds to set the game length.

Start Button — Begins the countdown and enables the click button while locking the input fields.

Click Counter — Adds a point to the score each time the click button is pressed.

Live Countdown — Updates the time label every second using root.after().

CPS Result — Divides the final score by the starting time and displays it to 2 decimal places.

Input Validation — Rejects non-numeric and non-positive time values with a clear message.

Dark Mode UI — CustomTkinter dark appearance with a blue accent theme.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Desktop GUI |
| `CTk`, `CTkLabel`, `CTkEntry`, `CTkButton` | Widgets for the interface |
| `root.after()` | Schedules the countdown ticks |
| `global` | Updates `score`, `time_left`, and `start_time` |
| `try / except` | Handles invalid time input |
| f-strings | Formats the score, time, and CPS labels |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install CustomTkinter by running pip install customtkinter.

Save the code as cps_tester.py.

Open a terminal in the folder containing the file.

Run python cps_tester.py.

Enter a time in seconds, click Start, and press the big button as many times as you can before the timer runs out.

## Improvements
Add a restart button — once the timer ends, the click button stays disabled and the entry stays locked, so the only way to play again is to restart the program; a reset function would let the user try again without relaunching.

Handle division by zero — cps = score / start_time would crash if start_time were 0, which can happen if the timing logic ever changes; guarding against that case would make it safer.
