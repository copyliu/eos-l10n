#Item: Vargur
from customEffects import boostModListBySkillReq
def shipBonusPTFalloffMB1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusMB",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)