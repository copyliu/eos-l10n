#Item: Kinetic Armor Compensation [Skill]
from customEffects import boostModListByReq
def kineticArmorCompensationHardeningBonusGroupEnergized(self, fitting, level):
    boostModListByReq(fitting.modules, "kineticDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Plating Energized",
                      self.item, extraMult = level)