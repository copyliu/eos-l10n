#===============================================================================
# Copyright (C) 2010 Diego Duclos
#               2010 Anton Vorobyov
#
# This file and all other files in this folder (and its subfolders) are part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

import unittest

from eos import db
from eos.types import Fit, Character, Skill, Ship, Drone

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        db.saveddata_meta.create_all()

    @classmethod
    def tearDownClass(self):
        db.saveddata_meta.drop_all()

    @classmethod
    def skillTestGetItemAttr(self, skillname, lvl, itemname, attr):
        fit = Fit()
        char = Character("test")
        skill = db.getItem(skillname)
        char.addSkill(Skill(skill, lvl))
        fit.character = char
        # Use any ship to just make items which have
        # influence on ship attributes work
        fit.ship = Ship(db.getItem("Rifter"))
        item = db.getItem(itemname)
        cat = item.category.name.lower()
        if cat == "drone":
            from eos.types import Drone
            itemInst = Drone(item)
            fit.drones.append(itemInst)
        elif cat == "module":
            from eos.types import Module
            itemInst = Module(item)
            fit.modules.append(itemInst)
        else:
            return None
        fit.calculateModifiedAttributes()
        result = itemInst.getModifiedItemAttr(attr)
        return result
