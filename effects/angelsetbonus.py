#Used by: Item: Halo Implant Set
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def angelsetbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "signatureRadiusBonus", "implantSetAngel",
                          lambda implant: "signatureRadiusBonus" in implant.attributes and \
                          "implantSetAngel" in implant.attributes,
                          self.item, helper = multiply)
