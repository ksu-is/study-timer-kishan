import time


def ask_minutes():
    """Prompt for study minutes until the user quits or provides a valid number."""
    while True:
        entry = input("Enter study minutes (or Q to quit): ").strip()
        if entry.upper().startswith("Q"):
            return None
        if entry.isdigit() and int(entry) > 0:
            return int(entry)
        print("Please enter a positive whole number of minutes, or Q to quit.")


def main():
    """Entry point for the study timer."""
    try:
        minutes = ask_minutes()
        if minutes is None:
            print("Goodbye.")
            return
        start_timer(minutes)
    except KeyboardInterrupt:
        print("\nTimer cancelled.")


def start_timer(minutes):
    """Run a blocking timer for the requested number of minutes."""
    total_seconds = minutes * 60
    print(f"Starting timer for {minutes} minute(s)...")
    start = time.monotonic()
    time.sleep(total_seconds)
    elapsed = round(time.monotonic() - start)
    print(f"Time's up! You studied for {elapsed} seconds. Take a break.")
    alert_complete()


def alert_complete():
    """Signal completion with a terminal bell when supported."""
    try:
        print("\a", end="")  # terminal bell (may beep in some terminals)
    except Exception:
        pass


if __name__ == "__main__":
    main()
