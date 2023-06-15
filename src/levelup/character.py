class Character:
    name = ""
    DEFUALT_NAME = "Character"
    def __init__(self, character_name):
        if character_name:
            self.name = character_name
        else:
            self.name = self.DEFUALT_NAME

    def getPosition():
        return 1;