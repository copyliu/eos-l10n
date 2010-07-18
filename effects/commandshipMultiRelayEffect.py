#Items from market group: Ships > Capital Industrial Ships (2 of 2)
#Items from market group: Ships > Command Ships (8 of 8)
from customEffects import boostModListByReq, increase
def commandshipMultiRelayEffect(self, fitting):
    boostModListByReq(fitting.modules, "maxGroupActive", "maxGangModules",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase)
