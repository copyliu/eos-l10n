#Items from group: Mechanic (9 of 32) [Skill]
from customEffects import boostModListByReq
def rigDrawbackBonusEffect(self, fitting, level):
    boostModListByReq(fitting.modules, "drawback", "rigDrawbackBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)