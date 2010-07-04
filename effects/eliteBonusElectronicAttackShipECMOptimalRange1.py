#Used by: Ship: Kitsune
from customEffects import boostModListByReq
def eliteBonusElectronicAttackShipECMOptimalRange1(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusElectronicAttackShip1",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)