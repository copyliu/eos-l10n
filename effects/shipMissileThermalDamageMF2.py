#Item: Breacher [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileThermalDamageMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "shipBonusMF2",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)