#Item: Inquisitor
from customEffects import boostAmmoListBySkillReq
def shipMissileExplosiveDamageAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "shipBonusAF",
                       lambda skill: skill.name == "Missile Launcher Operation",
                       self.item, extraMult = level)