#Used by: Ship: Sentinel
from customEffects import boostModListByReq
def eliteBonusElectronicAttackShipEnergyVampireRange1(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boostModListByReq(fitting.modules, "powerTransferRange", "eliteBonusElectronicAttackShip1",
                      lambda mod: mod.group.name == "Energy Vampire",
                      self.item, extraMult = level)