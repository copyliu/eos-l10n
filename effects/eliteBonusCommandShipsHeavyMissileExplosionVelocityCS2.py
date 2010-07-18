#Item: Nighthawk
from customEffects import boostAmmoListBySkillReq
def eliteBonusCommandShipsHeavyMissileExplosionVelocityCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "eliteBonusCommandShips2",
                       lambda skill: skill.name == "Heavy Missiles",
                       self.item, extraMult = level)