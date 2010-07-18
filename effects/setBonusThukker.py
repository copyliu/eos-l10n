#Items from group: Cyberimplant (6 of 138)
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusThukker(self, fitting):
    boostImplantListByReq(fitting.implants, "agilityBonus", "implantSetThukker",
                          lambda implant: "agilityBonus" in implant.attributes and \
                          "implantSetThukker" in implant.attributes,
                          self.item, helper = multiply)