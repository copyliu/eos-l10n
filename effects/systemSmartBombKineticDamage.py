#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemSmartBombKineticDamage(self, fitting, state):
    boostModListByReq(fitting.modules, "kineticDamage ", "smartbombDamageMultiplier",
                      lambda mod: mod.group.name == "Smart Bomb",
                      self.item, helper = multiply)