#Item: Low-grade Talon Alpha [Implant]
#Item: Low-grade Talon Beta [Implant]
#Item: Low-grade Talon Delta [Implant]
#Item: Low-grade Talon Epsilon [Implant]
#Item: Low-grade Talon Gamma [Implant]
#Item: Low-grade Talon Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def caldarisetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanGravimetricStrengthModifier", "implantSetLGCaldariNavy",
                          lambda implant: "implantSetLGCaldariNavy" in implant.attributes \
                          and "scanGravimetricStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)