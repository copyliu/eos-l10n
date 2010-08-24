import unittest
from eos import db
from eos.types import Item

class TestGameDataQueries(unittest.TestCase):
    def test_unicode(self):
        #Deliberatly request something with unicode in it. Will crash if the dump isn't encoded correctly
        a = db.getAttributeInfo(384)
