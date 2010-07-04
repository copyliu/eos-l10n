#Used by: Item: Projectile Locus Coordinator
from customEffects import boostModListByReq
def maxRangeBonusEffectProjectiles(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Projectile Weapon",
                      self.item, useStackingPenalty = True)