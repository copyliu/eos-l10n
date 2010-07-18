#Item: Kinetic Armor Compensation
from customEffects import boostModListByReq
def kineticArmorCompensationHardeningBonusGroupArmorCoating(self, fitting, level):
    boostModListByReq(fitting.modules, "kineticDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Coating",
                      self.item, extraMult = level)