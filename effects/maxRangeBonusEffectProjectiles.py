#Items from group: Rig Projectile Weapon (6 of 30)
from customEffects import boostModListByReq
def maxRangeBonusEffectProjectiles(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Projectile Weapon",
                      self.item, useStackingPenalty = True)