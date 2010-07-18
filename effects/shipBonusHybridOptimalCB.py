#Item: Rokh
from customEffects import boostModListBySkillReq
def shipBonusHybridOptimalCB(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusCB",
                      lambda skill: skill.name == "Large Hybrid Turret",
                      self.item, extraMult = level)