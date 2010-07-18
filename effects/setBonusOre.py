#Items from group: Cyberimplant (6 of 138) [Implant]
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusOre(self, fitting):
    boostImplantListByReq(fitting.implants, "maxRangeBonus", "implantSetORE",
                          lambda implant: "maxRangeBonus" in implant.attributes and \
                          "implantSetORE" in implant.attributes,
                          self.item, helper = multiply)