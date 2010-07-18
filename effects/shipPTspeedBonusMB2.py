#Variations of item: Tempest (4 of 4) [Ship]
#Variations of item: Typhoon (3 of 3) [Ship]
#Item: Maelstrom [Ship]
from customEffects import boostModListBySkillReq
def shipPTspeedBonusMB2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusMB2",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
