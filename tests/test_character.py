from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_default_name_assignment(self):
        testobj = Character("")
        self.assertEqual("Character", testobj.name)


#         variable = None

# if variable is not None:
#     print("Variable is not null")
# else:
#     print("Variable is null")
