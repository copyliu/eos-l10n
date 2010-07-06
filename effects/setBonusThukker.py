#Used by: Item: Nomad Implant Set
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusThukker(self, fitting):
    boostImplantListByReq(fitting.implants, "agilityBonus", "implantSetThukker",
                          lambda implant: "agilityBonus" in implant.attributes and \
                          "implantSetThukker" in implant.attributes,
                          self.item, helper = multiply)