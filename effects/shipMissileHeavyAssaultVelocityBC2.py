#Item: Damnation [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileHeavyAssaultVelocityBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusBC2",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item, extraMult = level)