#Used by: Ship: Golem
from customEffects import boostAmmoListBySkillReq
def shipBonusAoeVelocityCruiseMissileCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "shipBonus2CB",
                            lambda skill: skill.name == "Cruise Missile",
                            self.item, extraMult = level)