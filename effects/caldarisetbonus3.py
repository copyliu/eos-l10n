#Item: Talon Alpha [Implant]
#Item: Talon Beta [Implant]
#Item: Talon Delta [Implant]
#Item: Talon Epsilon [Implant]
#Item: Talon Gamma [Implant]
#Item: Talon Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def caldarisetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanGravimetricStrengthPercent",
                          "implantSetCaldariNavy",
                          lambda implant: "implantSetCaldariNavy" in implant.attributes and\
                          "scanGravimetricStrengthPercent" in implant.attributes,
                          self.item, helper = multiply)