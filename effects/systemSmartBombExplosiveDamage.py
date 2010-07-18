#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import boostModListByReq, multiply
def systemSmartBombExplosiveDamage(self, fitting, state):
    boostModListByReq(fitting.modules, "explosiveDamage ", "smartbombDamageMultiplier",
                      lambda mod: mod.group.name == "Smart Bomb",
                      self.item, helper = multiply)