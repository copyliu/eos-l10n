#Used by: Item: Talon Implant Set
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def caldarisetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanGravimetricStrengthPercent",
                          "implantSetCaldariNavy",
                          lambda implant: "implantSetCaldariNavy" in implant.attributes and\
                          "scanGravimetricStrengthPercent" in implant.attributes,
                          self.item, helper = multiply)