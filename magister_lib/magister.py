from datetime import datetime, timedelta

class FakeHomework:
    def __init__(self):
        self.course = type("Course", (), {"name": "Wiskunde"})
        self.description = "Maak opgave 3 t/m 7"
        self.deadline = datetime.now() + timedelta(days=3)

class FakeHomeworkInterface:
    async def get(self, start, end):
        return [FakeHomework()]

class FakeStudent:
    def __init__(self):
        self.homework = FakeHomeworkInterface()

class Magister:
    @classmethod
    async def login(cls, school_url, username, password):
        instance = cls()
        instance.current_student = FakeStudent()
        return instance
