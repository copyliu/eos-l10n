#Item: Abaddon
from customEffects import boostModListBySkillReq
def shipBonusLargeEnergyWeaponDamageAB2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusAB2",
                      lambda skill: skill.name == "Large Energy Turret",
                      self.item, extraMult = level)