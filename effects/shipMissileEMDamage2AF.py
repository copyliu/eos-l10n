#Item: Inquisitor [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileEMDamage2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "shipBonus2AF",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)