#Items from group: Cyberimplant (12 of 138)
runTime = "early"
from customEffects import boostImplantListByReq, multiply
def setBonusGuristas(self, fitting):
    boostImplantListByReq(fitting.implants, "shieldBoostMultiplier", "implantSetGuristas",
                          lambda implant: "shieldBoostMultiplier" in implant.attributes and \
                          "implantSetGuristas" in implant.attributes,
                          self.item, helper = multiply)