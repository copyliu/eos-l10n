#Item: Probe [Ship]
from customEffects import boostAmmoListByReq
def shipBonusSurveyProbeExplosionDelay3MF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListByReq(fitting.modules, "explosionDelay", "shipBonus3MF",
                       lambda mod: mod.group.name == "Survey Probe",
                       self.item, extraMult = level)
