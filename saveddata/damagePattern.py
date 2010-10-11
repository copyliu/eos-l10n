#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
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

class DamagePattern(object):
    DAMAGE_TYPES = ("em", "thermal", "kinetic", "explosive")

    def __init__(self, emAmount = 25, thermalAmount = 25, kineticAmount = 25, explosiveAmount = 25):
        self.emAmount = emAmount
        self.thermalAmount = thermalAmount
        self.kineticAmount = kineticAmount
        self.explosiveAmount = explosiveAmount

    def calculateEhp(self, fit):
        ehp = {}
        totalDamage = sum((self.emAmount, self.thermalAmount, self.kineticAmount, self.explosiveAmount))
        for (type, attr) in (('shield', 'shieldCapacity'), ('armor', 'armorHP'), ('hull', 'hp')):
            rawCapacity = fit.ship.getModifiedItemAttr(attr)
            ehp[type] = self.effectivify(fit, rawCapacity, type)

        return ehp

    def calculateEffectiveTank(self, fit, tankInfo):
        ehps = {}
        passiveShield = fit.calculateShieldRecharge()
        ehps["passiveShield"] = self.effectivify(fit, passiveShield, "shield")
        for type in ("shield", "armor", "hull"):
            ehps["%sRepair" % type] = self.effectivify(fit, tankInfo["%sRepair" % type], type)

        return ehps

    def effectivify(self, fit, amount, type):
        type = type if type != "hull" else ""
        totalDamage = sum((self.emAmount, self.thermalAmount, self.kineticAmount, self.explosiveAmount))
        specificDivider = 0
        for damageType in self.DAMAGE_TYPES:
            #Compose an attribute name, then make sure the first letter is NOT capitalized
            attrName = "%s%sDamageResonance" % (type, damageType.capitalize())
            attrName = attrName[0].lower() + attrName[1:]

            resonance = fit.ship.getModifiedItemAttr(attrName)
            damage = getattr(self, "%sAmount" % damageType)

            specificDivider += damage / float(totalDamage) * resonance

        return amount / (specificDivider or 1)

    def __deepcopy__(self, memo):
        p = DamagePattern(self.emAmount, self.thermalAmount, self.kineticAmount, self.explosiveAmount)
        p.name = "%s copy" % self.name
        return p
