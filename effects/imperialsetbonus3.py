#Item: Grail Alpha [Implant]
#Item: Grail Beta [Implant]
#Item: Grail Delta [Implant]
#Item: Grail Epsilon [Implant]
#Item: Grail Gamma [Implant]
#Item: Grail Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def imperialsetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanRadarStrengthPercent",
                          "implantSetImperialNavy",
                          lambda implant: "scanRadarStrengthPercent" in implant.attributes and\
                          "implantSetImperialNavy" in implant.attributes,
                          self.item, helper = multiply)