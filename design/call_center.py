"""

"""
from typing import List

class Role(Enum):
    NONE = 0
    RESPONDENT = 1,
    MANAGER = 2,
    DIRECTOR = 3

class Employee:
    def __init__(self, role: Role):
        self.role = role

    def can_handle(self, call):
        #subclass specific logic

class Manager(Employee):
    def __init__(self):
        super.__init__(Role.MANAGER)
    def can_handle(self, call):
        pass

class Respondent(Employee):
    def __init__(self, role: Role):
        super().__init__(Role.RESPONDENT)

    def can_handle(self, call):
        super().can_handle(call)


class Director(Employee):
    pass

class Call:
    def __init__(self):
        self.id: int = 0
        self.handler: Employee = None

class CallManager:
    def __init__(self):
        """
        """
        self.manager_pool = List[Manager]
        self.respondent_pool = List[Respondent]
        self.director_pool = List[Director]

    def dispatch_call(self, call: Call):
        if self.respondent_pool:
            respondent: Respondent = self.respondent_pool.pop(0)
            if not respondent.can_handle(call):



