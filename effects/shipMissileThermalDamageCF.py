#Used by: Ship: Kestrel
#               Caldari Navy Hookbill
from customEffects import boostAmmoListBySkillReq
def shipMissileThermalDamageCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "shipBonusCF2",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
