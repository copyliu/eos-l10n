#Used by: Item: Jackal Implant Set
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def republicsetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanLadarStrengthPercent",
                          "implantSetRepublicFleet",
                          lambda implant: "implantSetRepublicFleet" in implant.attributes and\
                          "scanLadarStrengthPercent" in implant.attributes,
                          self.item, helper = multiply)