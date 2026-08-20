import time
import requests
from datetime import datetime
from src.config import POLL_INTERVAL_SECONDS, BOOKING_URL
from src.waitwhile import get_available_slots
from src.notifier import send_discord_notification


def format_slot_date(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M")

    return date.strftime("%B %d at %I:%M %p").replace(" 0", " ")

def get_new_slots(current_slots, previous_slots):
    return current_slots - previous_slots


def main():
    previous_slots = set()
    try:
        while True:
            try:
                slots = get_available_slots()
            except requests.RequestException as error:
                print(f"Waitwhile request failed: {error}")
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            current_slots = {slot["date"] for slot in slots}

            new_slots = get_new_slots(current_slots, previous_slots)
            
            if new_slots:
                print("New appointment(s) found!")
                message_lines = ["🚨 **New appointment(s) found!**"]

                for slot in slots:
                    if slot["date"] in new_slots:
                        formatted_date = format_slot_date(slot['date'])
                        available = slot['numAvailableSpots']
                        spot_word = "spot" if available == 1 else "spots"
                        line = (
                            f"**{formatted_date}**\n"
                            f"{available} {spot_word} available"
                        )
                        print(line)
                        message_lines.append(line)
                message_lines.append(f"🔗 **BOOK NOW:** {BOOKING_URL}")
                send_discord_notification("\n\n".join(message_lines))
            else:
                print("No new appointments.")

            previous_slots = current_slots

            time.sleep(POLL_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\nMonitor stopped.")

if __name__ == "__main__":
    main()