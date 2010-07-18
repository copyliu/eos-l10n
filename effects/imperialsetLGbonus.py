#Item: Low-grade Grail Alpha [Implant]
#Item: Low-grade Grail Beta [Implant]
#Item: Low-grade Grail Delta [Implant]
#Item: Low-grade Grail Epsilon [Implant]
#Item: Low-grade Grail Gamma [Implant]
#Item: Low-grade Grail Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def imperialsetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanRadarStrengthModifier", "implantSetLGImperialNavy",
                          lambda implant: "implantSetLGImperialNavy" in implant.attributes \
                          and "scanRadarStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)