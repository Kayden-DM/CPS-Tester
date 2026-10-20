CPS Tester
A GUI Python app built with CustomTkinter that measures how many times you can click per second within a chosen time limit.

Concepts Used
CustomTkinter GUI — builds labels, an entry, and buttons with a dark theme.

root.after() — schedules the tick() countdown every 1000ms without blocking the UI.

Global Variables — score, time_left, and start_time are shared and updated across functions.

Features
Custom Time Limit — the user enters how many seconds the test runs, with validation for numbers and positive values.

Live Countdown — time_label updates each second while the click button counts taps.

CPS Calculation — on time-up, displays clicks-per-second to two decimals and disables the button.

Improvements
Prevent Repeat Starts — starting a game twice or clicking before the timer ends isn't guarded; a running flag would block re-entry.

Fix Division Edge Case — score / start_time in time_end() is fine, but if start_time somehow resets to 0 it errors; guard it or store the initial duration separately.

Reset & Replay — after a round the score and entry stay locked; add a reset button so users can run multiple tests without restarting the app.

