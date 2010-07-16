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
            
    def test_requiresSkill(self):
        i = db.getItem("Shield Boost Amplifier II")
        self.assertTrue(i.requiresSkill("Shield Management"))
        self.assertTrue(i.requiresSkill("Shield Management", 5))
        self.assertFalse(i.requiresSkill("Moo Management"), 9000)