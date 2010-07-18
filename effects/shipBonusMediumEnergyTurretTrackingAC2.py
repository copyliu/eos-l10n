#Item: Phantasm
from customEffects import boostModListBySkillReq
def shipBonusMediumEnergyTurretTrackingAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusAC2",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)