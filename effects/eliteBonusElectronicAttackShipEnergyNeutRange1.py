#Item: Sentinel
from customEffects import boostModListByReq
def eliteBonusElectronicAttackShipEnergyNeutRange1(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boostModListByReq(fitting.modules, "energyDestabilizationRange", "eliteBonusElectronicAttackShip1",
                      lambda mod: mod.group.name == "Energy Destabilizer",
                      self.item, extraMult = level)