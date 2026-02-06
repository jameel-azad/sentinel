from datetime import datetime, timezone
import json

event = {
    "sensor_id":"WEBCAM",
    "location":"TEST_LAB",
    "event_type":"FIRE",
    "confidence":0.0,
    "severity":"HIGH",
    "timestamp": datetime.now(timezone.utc).isoformat()
}

print(json.dumps(event, default=str))