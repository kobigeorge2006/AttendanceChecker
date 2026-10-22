from datetime import datetime
class AttendanceRecord:
    def __init__(self,record_id:str, student_id: str, session_id:str, check_in_time: datetime):
        self.record_id = record_id
        self.student_id = student_id
        self.session_id = session_id
        self.check_in_time = check_in_time

        