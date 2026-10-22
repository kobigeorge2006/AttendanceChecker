from datetime import datetime

class AttendanceSession:
    def __init__(self, session_id: str, class_id: str, start_time: datetime, is_open: bool, session_token: str):
        self.session_id = session_id
        self.class_id = class_id
        self.start_time = start_time
        self.is_open = is_open
        self.session_token = session_token

    def get_check_in_URL(self) -> str: 
        pass