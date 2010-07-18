#Item: Low-grade Harvest Alpha [Implant]
#Item: Low-grade Harvest Beta [Implant]
#Item: Low-grade Harvest Delta [Implant]
#Item: Low-grade Harvest Epsilon [Implant]
#Item: Low-grade Harvest Gamma [Implant]
#Item: Low-grade Harvest Omega [Implant]
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusOre(self, fitting):
    boostImplantListByReq(fitting.implants, "maxRangeBonus", "implantSetORE",
                          lambda implant: "maxRangeBonus" in implant.attributes and \
                          "implantSetORE" in implant.attributes,
                          self.item, helper = multiply)