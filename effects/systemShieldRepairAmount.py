#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostModListByReq, multiply
type = "projected"
def systemShieldRepairAmount(self, fitting, state):
    boostModListByReq(fitting.modules, "shieldBonus", "shieldBonusMultiplier",
                      lambda mod: mod.group.name == "Shield Booster",
                      self.item, helper = multiply)