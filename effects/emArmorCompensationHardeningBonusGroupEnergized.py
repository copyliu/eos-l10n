#Item: EM Armor Compensation [Skill]
from customEffects import boostModListByReq
def emArmorCompensationHardeningBonusGroupEnergized(self, fitting, level):
    boostModListByReq(fitting.modules, "emDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Plating Energized",
                      self.item, extraMult = level)