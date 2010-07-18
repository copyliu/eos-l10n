#Item: Heron [Ship]
from customEffects import boostAmmoListByReq
def shipBonusSurveyProbeExplosionDelay3CF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListByReq(fitting.modules, "explosionDelay", "shipBonus3CF",
                       lambda mod: mod.group.name == "Survey Probe",
                       self.item, extraMult = level)
