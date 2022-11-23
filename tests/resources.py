import json

SAMPLE_MESSAGE = {
    "checksum": "e6cd69605e0fa4a46439f2e87ebcc757",
    "client": "a79cefed0b7076cf3998ef7578a18bf0",
    "e": json.dumps([
        {
            "device_id": "6rPzaVUwYHquzptdsrrKff",
            "user_id": "test_user",
            "timestamp": 1667130434980,
            "event_id": 7,
            "session_id": 1667130434980,
            "event_type": "Dart Click",
            "version_name": None,
            "platform": "Web",
            "os_name": "Chrome",
            "os_version": "106",
            "device_model": "Windows",
            "device_manufacturer": None,
            "language": "en-US",
            "api_properties": {},
            "event_properties": {},
            "user_properties": {},
            "uuid": "52c0306f-f972-45e8-8055-9d05c940e809",
            "library": {"name": "amplitude-flutter", "version": "3.10.0"},
            "sequence_number": 9,
            "groups": {},
            "group_properties": {},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        }
    ]),
    "upload_time": "1667130434980",
    "v": "2",
}


SAMPLE_MESSAGE_THREE_EVENTS = {
    "checksum": "e6cd69605e0fa4a46439f2e87ebcc757",
    "client": "a79cefed0b7076cf3998ef7578a18bf0",
    "e": json.dumps([
        {
            "device_id": "6rPzaVUwYHquzptdsrrKff",
            "user_id": "test_user",
            "timestamp": 1667130434980,
            "event_id": 7,
            "session_id": 1667130434980,
            "event_type": "Dart Click",
            "version_name": None,
            "platform": "Web",
            "os_name": "Chrome",
            "os_version": "106",
            "device_model": "Windows",
            "device_manufacturer": None,
            "language": "en-US",
            "api_properties": {},
            "event_properties": {},
            "user_properties": {},
            "uuid": "52c0306f-f972-45e8-8055-9d05c940e809",
            "library": {"name": "amplitude-flutter", "version": "3.10.0"},
            "sequence_number": 9,
            "groups": {},
            "group_properties": {},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        },
        {
            "device_id": "6rPzaVUwYHquzptdsrrKff",
            "user_id": "test_user",
            "timestamp": 1667130434980,
            "event_id": 7,
            "session_id": 1667130434980,
            "event_type": "Dart Click",
            "version_name": None,
            "platform": "Web",
            "os_name": "Chrome",
            "os_version": "106",
            "device_model": "Windows",
            "device_manufacturer": None,
            "language": "en-US",
            "api_properties": {},
            "event_properties": {},
            "user_properties": {},
            "uuid": "52c0306f-f972-45e8-8055-9d05c940e809",
            "library": {"name": "amplitude-flutter", "version": "3.10.0"},
            "sequence_number": 9,
            "groups": {},
            "group_properties": {},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        },
        {
            "device_id": "6rPzaVUwYHquzptdsrrKff",
            "user_id": "test_user",
            "timestamp": 1667130434980,
            "event_id": 7,
            "session_id": 1667130434980,
            "event_type": "Dart Click",
            "version_name": None,
            "platform": "Web",
            "os_name": "Chrome",
            "os_version": "106",
            "device_model": "Windows",
            "device_manufacturer": None,
            "language": "en-US",
            "api_properties": {},
            "event_properties": {},
            "user_properties": {},
            "uuid": "52c0306f-f972-45e8-8055-9d05c940e809",
            "library": {"name": "amplitude-flutter", "version": "3.10.0"},
            "sequence_number": 9,
            "groups": {},
            "group_properties": {},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        }
    ]),
    "upload_time": "1667130434980",
    "v": "2",
}