class Character:
    name = ""

    def __init__(self, character_name):
        if character_name:
            self.name = character_name
        else:
            self.name = "Character"
