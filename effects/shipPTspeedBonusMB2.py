#Used by: Ship: Typhoon
#               Typhoon Fleet Issue
#               Tempest
#               Tempest Fleet Issue
#               Tempest Tribal Issue
#               Maelstrom
#               Panther
#               Vargur
from customEffects import boostModListBySkillReq
def shipPTspeedBonusMB2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusMB2",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
