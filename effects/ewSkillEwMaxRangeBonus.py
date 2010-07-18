#Items from group: Cyberimplant (5 of 138) [Implant]
#Items from group: Rig Electronics Superiority (6 of 48) [Module]
#Variations of item: Medium Particle Dispersion Projector I (2 of 2) [Module]
#Variations of item: Small Particle Dispersion Projector I (2 of 2) [Module]
#Item: Long Distance Jamming [Skill]
from customEffects import boostModListByReq
def ewSkillEwMaxRangeBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill" or self.item.group.category.name == "Implant":
        penalized = False
    else:
        penalized = True
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "ECM", self.item,
                      useStackingPenalty = penalized, extraMult = level)
