#Used by: Item: Centurion Implant Set
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusMordus(self, fitting):
    boostImplantListByReq(fitting.implants, "rangeSkillBonus", "implantSetMordus",
                          lambda implant: "rangeSkillBonus" in implant.attributes and \
                          "implantSetMordus" in implant.attributes,
                          self.item, helper = multiply)