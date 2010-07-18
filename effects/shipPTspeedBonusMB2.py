#Items from category: Ship (8 of 245)
from customEffects import boostModListBySkillReq
def shipPTspeedBonusMB2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusMB2",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
