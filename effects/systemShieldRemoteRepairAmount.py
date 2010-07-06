#Used by: Item: Cataclysmic Variable Effect Beacon
from customEffects import boostModListByReq, multiply
type = "projected"
def systemShieldRemoteRepairAmount(self, fitting, state):
    boostModListByReq(fitting.modules, "shieldBonus", "shieldBonusMultiplier",
                      lambda mod: mod.group.name == "Shield Booster",
                      self.item, helper = multiply)