#Items from group: Cyberimplant (6 of 138) [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def imperialsetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanRadarStrengthModifier", "implantSetLGImperialNavy",
                          lambda implant: "implantSetLGImperialNavy" in implant.attributes \
                          and "scanRadarStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)