class DataBase:
    def __init__(self,file_path:str):
        self.file_path = file_path

    def save_student(self, student):
        pass

    def get_student(self, student_id):
        pass

    def save_roster(self, roster):
        pass

    def get_roster(self, class_id):
        pass

    def save_session(self, session):
        pass

    def get_session_by_token(self, token):
        pass

    def update_session(self, session):
        pass

    def has_checked_in(self, student_id, session_id):
        pass

    def save_attendance(self, record):
        pass

    def get_attendance(self, session_id):
        pass

    def get_sessions(self, class_id, start_date, end_date):
        pass