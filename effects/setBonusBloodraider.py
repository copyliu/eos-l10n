#Used by: Item: Talisman Implant Set
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusBloodraider(self, fitting):
    boostImplantListByReq(fitting.implants, "durationBonus", "implantSetBloodraider",
                          lambda implant: "durationBonus" in implant.attributes and \
                          "implantSetBloodraider" in implant.attributes,
                          self.item, helper = multiply)