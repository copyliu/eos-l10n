#Variations of item: Large Particle Dispersion Projector I (2 of 2)
#Variations of item: Medium Particle Dispersion Projector I (2 of 2)
#Variations of item: Small Particle Dispersion Projector I (2 of 2)
#Item: Long Distance Jamming
from customEffects import boostModListByReq
def ewSkillTdMaxRangeBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill":
        penalized = False
    else:
        penalized = True
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, useStackingPenalty = penalized, extraMult = level)
