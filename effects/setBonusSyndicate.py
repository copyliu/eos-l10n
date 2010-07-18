#Items from group: Cyberimplant (6 of 138)
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusSyndicate(self, fitting):
    boostImplantListByReq(fitting.implants, "boosterAttributeModifier", "implantSetSyndicate",
                          lambda implant: "boosterAttributeModifier" in implant.attributes and \
                          "implantSetSyndicate" in implant.attributes,
                          self.item, helper = multiply)