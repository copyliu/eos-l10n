#Used by: Ship: Covert Ops
from customEffects import boostAmmoListByReq
def shipBonusSurveyProbeExplosionDelaySkillSurveyCovertOps3(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListByReq(fitting.modules, "explosionDelay", "eliteBonusCoverOps3",
                       lambda mod: mod.group.name == "Survey Probe",
                       self.item, extraMult = level)
