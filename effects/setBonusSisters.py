#Item: Low-grade Virtue Alpha [Implant]
#Item: Low-grade Virtue Beta [Implant]
#Item: Low-grade Virtue Delta [Implant]
#Item: Low-grade Virtue Epsilon [Implant]
#Item: Low-grade Virtue Gamma [Implant]
#Item: Low-grade Virtue Omega [Implant]
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusSisters(self, fitting):
    boostImplantListByReq(fitting.implants, "scanStrengthBonus", "implantSetSisters",
                          lambda implant: "scanStrengthBonus" in implant.attributes and \
                          "implantSetSisters" in implant.attributes,
                          self.item, helper = multiply)