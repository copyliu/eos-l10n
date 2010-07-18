#Item: Nighthawk [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteBonusCommandShipMissileKineticDamageCS1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "eliteBonusCommandShips1",
                      lambda skill: skill.name == "Missile Launcher Operation",
                      self.item, extraMult = level)