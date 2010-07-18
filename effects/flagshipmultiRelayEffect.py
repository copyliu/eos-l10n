#Item: Command Processor I
from customEffects import boostModListByReq, increase
def flagshipmultiRelayEffect(self, fitting, state):
    #Need to enable two more, one for itself, one for an extra gang module
    boostModListByReq(fitting.modules, "maxGroupActive", 2,
                         lambda mod: mod.group.name == "Gang Coordinator" and \
                         "maxGroupActive" in mod.attributes,
                         self.item, helper = increase)