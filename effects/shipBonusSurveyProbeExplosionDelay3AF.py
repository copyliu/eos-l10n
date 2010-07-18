#Item: Magnate
from customEffects import boostAmmoListByReq
def shipBonusSurveyProbeExplosionDelay3AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListByReq(fitting.modules, "explosionDelay", "shipBonus3AF",
                       lambda mod: mod.group.name == "Survey Probe",
                       self.item, extraMult = level)
