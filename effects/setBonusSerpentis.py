#Used by: Item: Snake Implant Set
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusSerpentis(self, fitting):
    boostImplantListByReq(fitting.implants, "velocityBonus", "implantSetSerpentis",
                          lambda implant: "velocityBonus" in implant.attributes and \
                          "implantSetSerpentis" in implant.attributes,
                          self.item, helper = multiply)