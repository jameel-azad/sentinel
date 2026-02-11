from datetime import datetime, timezone
import time
import json

def create_event(event_type,confidence=1.0,severity='LOW'):
    event = {
        "sensor_id":"WEBCAM",
        "location":"TEST_LAB",
        "event_type":event_type,
        "confidence":confidence,
        "severity":severity,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    return event

while True:
    try:
        event = create_event('HEARTBEAT')
        print(json.dumps(event), flush=True)
        time.sleep(2)
    except KeyboardInterrupt:
        break