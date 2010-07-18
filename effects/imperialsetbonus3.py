#Items from group: Cyberimplant (6 of 138)
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def imperialsetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanRadarStrengthPercent",
                          "implantSetImperialNavy",
                          lambda implant: "scanRadarStrengthPercent" in implant.attributes and\
                          "implantSetImperialNavy" in implant.attributes,
                          self.item, helper = multiply)