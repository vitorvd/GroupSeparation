from participant import Participant


class Group:
    participantsLimit = 6

    def __init__(self, tag):
        self.tag = tag
        self.participants = []

    def addParticipant(self, name, contact, experience):
        nonlocal participantsLimit
        if len(self.participants) < participantsLimit:
            self.participants.append(Participant(name, contact, experience))
            return True
        return False
