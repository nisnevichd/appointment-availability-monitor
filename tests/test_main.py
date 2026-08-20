
from src.main import format_slot_date, get_new_slots

def  test_format_slot_date():
    result = format_slot_date("2026-08-30T17:30")

    assert result == "August 30 at 5:30 PM"

def test_format_slot_date_morning():
    result = format_slot_date("2026-09-01T09:00")

    assert result == "September 1 at 9:00 AM"

def test_get_new_slots():
    previous = {
        "2026-08-30T17:00"
    }

    current = {
        "2026-08-30T17:00",
        "2026-08-30T17:30"
    }

    result = get_new_slots(current, previous)

    assert result == {"2026-08-30T17:30"}


def test_get_new_slots_none():
    previous = {
        "2026-08-30T17:00"
    }

    current = {
        "2026-08-30T17:00"
    }

    result = get_new_slots(current, previous)

    assert result == set()