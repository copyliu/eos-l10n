import unittest
from model import db

class TestItem(unittest.TestCase):
    def test_Race(self):
        i = db.getItem("Dramiel")
        self.assertEqual(i.race, "angel")
        
    def test_RequiredSkills(self):
        i = db.getItem("Dramiel")
        self.assertEquals(len(i.requiredSkills), 2)
        skills = ("Minmatar Frigate", "Gallente Frigate")
        for skill, level in i.requiredSkills.iteritems():
            self.assertTrue(skill.name in skills)
            self.assertEquals(level, 3)