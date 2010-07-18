#Item: Low-grade Edge Alpha [Implant]
#Item: Low-grade Edge Beta [Implant]
#Item: Low-grade Edge Delta [Implant]
#Item: Low-grade Edge Epsilon [Implant]
#Item: Low-grade Edge Gamma [Implant]
#Item: Low-grade Edge Omega [Implant]
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusSyndicate(self, fitting):
    boostImplantListByReq(fitting.implants, "boosterAttributeModifier", "implantSetSyndicate",
                          lambda implant: "boosterAttributeModifier" in implant.attributes and \
                          "implantSetSyndicate" in implant.attributes,
                          self.item, helper = multiply)