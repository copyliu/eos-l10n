#Item: Jackal Alpha [Implant]
#Item: Jackal Beta [Implant]
#Item: Jackal Delta [Implant]
#Item: Jackal Epsilon [Implant]
#Item: Jackal Gamma [Implant]
#Item: Jackal Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def republicsetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanLadarStrengthPercent",
                          "implantSetRepublicFleet",
                          lambda implant: "implantSetRepublicFleet" in implant.attributes and\
                          "scanLadarStrengthPercent" in implant.attributes,
                          self.item, helper = multiply)