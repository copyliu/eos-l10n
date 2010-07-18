#Item: Imicus
from customEffects import boostAmmoListByReq
def shipBonusSurveyProbeExplosionDelay3GF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostAmmoListByReq(fitting.modules, "explosionDelay", "shipBonus3GF",
                       lambda mod: mod.group.name == "Survey Probe",
                       self.item, extraMult = level)
