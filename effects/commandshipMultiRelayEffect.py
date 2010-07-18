#Items from group: Command Ship (8 of 8) [Ship]
#Items from market group: Ships > Capital Industrial Ships (2 of 2)
from customEffects import boostModListByReq, increase
def commandshipMultiRelayEffect(self, fitting):
    boostModListByReq(fitting.modules, "maxGroupActive", "maxGangModules",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase)
