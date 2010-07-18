#Variations of item: Large Particle Dispersion Projector I (2 of 2)
#Variations of item: Medium Particle Dispersion Projector I (2 of 2)
#Variations of item: Small Particle Dispersion Projector I (2 of 2)
#Item: Long Distance Jamming
from customEffects import boostModListByReq
def ewSkillEcmBurstRangeBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "ecmBurstRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "ECM Burst",
                      self.item, extraMult = level)