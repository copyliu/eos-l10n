#Item: Harbinger
from customEffects import boostModListByReq
def shipLaserDamageBonusBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "damageMultiplier", "shipBonusBC2",
                      lambda mod: mod.group.name == "Energy Weapon", self.item,
                      extraMult = level)