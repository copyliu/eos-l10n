#Items from group: Cyberimplant (6 of 138)
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusSisters(self, fitting):
    boostImplantListByReq(fitting.implants, "scanStrengthBonus", "implantSetSisters",
                          lambda implant: "scanStrengthBonus" in implant.attributes and \
                          "implantSetSisters" in implant.attributes,
                          self.item, helper = multiply)