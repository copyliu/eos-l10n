#Items from group: Cyberimplant (13 of 138)
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusSansha(self, fitting):
    boostImplantListByReq(fitting.implants, "armorHpBonus", "implantSetSansha",
                          lambda implant: "armorHpBonus" in implant.attributes and \
                          "implantSetSansha" in implant.attributes,
                          self.item, helper = multiply)