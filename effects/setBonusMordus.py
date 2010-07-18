#Item: Low-grade Centurion Alpha [Implant]
#Item: Low-grade Centurion Beta [Implant]
#Item: Low-grade Centurion Delta [Implant]
#Item: Low-grade Centurion Epsilon [Implant]
#Item: Low-grade Centurion Gamma [Implant]
#Item: Low-grade Centurion Omega [Implant]
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusMordus(self, fitting):
    boostImplantListByReq(fitting.implants, "rangeSkillBonus", "implantSetMordus",
                          lambda implant: "rangeSkillBonus" in implant.attributes and \
                          "implantSetMordus" in implant.attributes,
                          self.item, helper = multiply)