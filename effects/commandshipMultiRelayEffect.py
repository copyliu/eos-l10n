#Used by: Ship: Command ships
from customEffects import boostModListByReq, increase
def commandshipMultiRelayEffect(self, fitting):
    boostModListByReq(fitting.modules, "maxGroupActive", "maxGangModules",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase)
