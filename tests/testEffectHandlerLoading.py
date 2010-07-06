import unittest
from model import db
import types

class TestEffectHandlerLoading(unittest.TestCase):        
    def test_loadEffect(self):
        i = db.getItem("Rifter")
        self.assertEqual(type(i.effects["shipPDmgBonusMF"].handler), types.FunctionType)