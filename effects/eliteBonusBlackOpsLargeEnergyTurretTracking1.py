#Item: Redeemer
from customEffects import boostModListBySkillReq
def eliteBonusBlackOpsLargeEnergyTurretTracking1(self, fitting):
    skill, level = fitting.getCharSkill("Black Ops")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusBlackOps1",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)