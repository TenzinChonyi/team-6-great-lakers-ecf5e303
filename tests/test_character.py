from unittest import TestCase
from levelup.character import Character
from levelup.position import Position


class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_default_name_assignment(self):
        testobj = Character("")
        self.assertEqual("Character", testobj.name)

    def test_getPosition_returns_a_value(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertIsNotNone(testobj.getPosition)
        

        