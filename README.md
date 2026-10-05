# Appointment Availability Monitor

A Python automation tool that monitors appointment availability through the
Waitwhile API and sends real-time Discord notifications when new appointment
slots become available.

I built this project to automate the process of repeatedly checking for
limited appointment availability. Instead of manually refreshing a booking
page, the monitor polls Waitwhile for available time slots, detects newly
available appointments, and sends a notification containing the appointment
time, remaining availability, and booking link.

## Features

- Queries the Waitwhile API for appointment availability
- Searches a configurable rolling appointment window
- Polls automatically at a configurable interval
- Tracks previously observed appointment slots
- Detects newly available appointments
- Sends Discord notifications through a webhook
- Displays appointment time and number of available spots
- Includes error handling for failed API requests
- Uses timezone-aware date handling
- Supports environment-based configuration for webhook credentials

## How It Works

1. The application requests available appointment slots from Waitwhile.
2. Returned appointment dates are stored as the current availability state.
3. The current state is compared with the previous polling cycle.
4. Newly appearing appointment slots are identified.
5. When a new slot is detected, the application formats the appointment
   information and sends a Discord notification.
6. The monitor waits for the configured polling interval and repeats.

## Architecture

Waitwhile API → Python Monitor → Availability Comparison → Discord Webhook

## Tech Stack

- Python
- Waitwhile API
- REST APIs
- Requests
- Discord Webhooks
- python-dotenv
- ZoneInfo
- Pytest

## Project Structure

```text
appointment-availability-monitor/
├── src/
│   ├── config.py
│   ├── main.py
│   ├── notifier.py
│   └── waitwhile.py
├── tests/
├── requirements.txt
├── railpack.json
└── README.md

