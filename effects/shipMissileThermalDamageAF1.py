#Item: Inquisitor [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileThermalDamageAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "shipBonusAF",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)