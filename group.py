from participant import Participant


class Group:
    def __init__(self, tag):
        self.tag = tag
        self.participants = []

    def addParticipant(self, name, contact, experience):
        if len(self.participants) < 6:
            self.participants.append(Participant(name, contact, experience))
            # print(f'**ADICIONADO** {nome} adicionado ao Grupo {self.tag}')
            return True
        # print(f'**ERRO** ao cadastrar {nome} no Grupo {self.tag} que possui {len(self.participantes)} participantes')
        return False
