#Variations of item: Large Particle Dispersion Projector I (2 of 2)
#Variations of item: Medium Particle Dispersion Projector I (2 of 2)
#Variations of item: Small Particle Dispersion Projector I (2 of 2)
#Item: Long Distance Jamming
from customEffects import boostModListByReq
def ewSkillTpMaxRangeBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, extraMult = level)