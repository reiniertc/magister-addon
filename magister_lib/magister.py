# Minimale mock-up van de magister.py client
import asyncio

class FakeHomework:
    def __init__(self):
        self.course = type("Course", (), {"name": "Wiskunde"})
        self.description = "Maak opgave 3 t/m 7"
        self.deadline = asyncio.get_event_loop().time()

class FakeStudent:
    async def homework(self, start, end):
        return [FakeHomework()]

class Magister:
    @classmethod
    async def login(cls, school_url, username, password):
        instance = cls()
        instance.current_student = type("Student", (), {"homework": FakeStudent()})()
        return instance
