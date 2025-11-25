study-timer-kishan

Simple Python study timer that runs in the terminal. Enter your study minutes, let it block until time is up, then take a break.

Usage
- Requires Python 3 (built-in `time` module only).
- From the repo root: `python timer.py`
- Enter a positive number of minutes, or Q to quit.
- When the timer finishes, it prints a completion message and triggers the terminal bell (if supported).

Notes
- KeyboardInterrupt (Ctrl+C) cleanly cancels the timer.
- Future ideas: session tracking, richer sounds, simple stats per day.
