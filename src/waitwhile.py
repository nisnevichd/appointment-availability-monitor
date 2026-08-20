from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import requests

from src.config import (
    WAITWHILE_BASE_URL,
    SERVICE_ID,
    SEARCH_DAYS,
)


def get_available_slots():
    now = datetime.now(ZoneInfo("America/New_York"))
    search_end = now + timedelta(days=SEARCH_DAYS)

    params = {
        "fromDate": now.strftime("%Y-%m-%dT%H:%M"),
        "toDate": search_end.strftime("%Y-%m-%dT%H:%M"),
        "maxNumSlots": 10,
        "serviceDuration": 1800,
        "partySize": 1,
        "serviceIds": SERVICE_ID,
    }

    response = requests.get(
        WAITWHILE_BASE_URL,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()