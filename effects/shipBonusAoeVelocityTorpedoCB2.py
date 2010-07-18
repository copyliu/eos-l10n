#Item: Golem [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusAoeVelocityTorpedoCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "shipBonus2CB",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)