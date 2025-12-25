class EventManager():
    def __init__(self):
        self.registrations = []

    def register(self, user: str) -> bool:
        self.user = user

        if self.user in self.registrations:
            return False    

        self.registrations.append(self.user)
        return True

    def deregister(self, user: str) -> bool:
        self.user = user

        if self.user not in self.registrations:
            return False
        
        self.registrations.remove(self.user)
        return True

    def get_num_registrations(self) -> int:
        return len(self.registrations)
    
#
# Task 10: Limited Event Manager
#

class LimitedEventManager(EventManager):
    def __init__(self, registration_limit):
        super().__init__()
        self.registration_limit = registration_limit

    def register(self, user: str) -> bool:
        self.user = user

        if len(self.registrations) >= self.registration_limit:
            return False

        if self.user in self.registrations:
            return False    

        self.registrations.append(self.user)
        return True