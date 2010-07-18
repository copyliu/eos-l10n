#Item: Low-grade Nomad Alpha [Implant]
#Item: Low-grade Nomad Beta [Implant]
#Item: Low-grade Nomad Delta [Implant]
#Item: Low-grade Nomad Epsilon [Implant]
#Item: Low-grade Nomad Gamma [Implant]
#Item: Low-grade Nomad Omega [Implant]
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusThukker(self, fitting):
    boostImplantListByReq(fitting.implants, "agilityBonus", "implantSetThukker",
                          lambda implant: "agilityBonus" in implant.attributes and \
                          "implantSetThukker" in implant.attributes,
                          self.item, helper = multiply)