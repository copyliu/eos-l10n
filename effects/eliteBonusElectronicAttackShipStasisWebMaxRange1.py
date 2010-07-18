#Item: Hyena
from customEffects import boostModListByReq
def eliteBonusElectronicAttackShipStasisWebMaxRange1(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusElectronicAttackShip1",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)