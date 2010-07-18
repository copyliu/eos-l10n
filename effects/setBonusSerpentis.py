#Items from group: Cyberimplant (12 of 138) [Implant]
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusSerpentis(self, fitting):
    boostImplantListByReq(fitting.implants, "velocityBonus", "implantSetSerpentis",
                          lambda implant: "velocityBonus" in implant.attributes and \
                          "implantSetSerpentis" in implant.attributes,
                          self.item, helper = multiply)