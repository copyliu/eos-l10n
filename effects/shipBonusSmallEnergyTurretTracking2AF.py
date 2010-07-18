#Item: Succubus
from customEffects import boostModListBySkillReq
def shipBonusSmallEnergyTurretTracking2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonus2AF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)