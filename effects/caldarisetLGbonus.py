#Items from group: Cyberimplant (6 of 138)
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def caldarisetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanGravimetricStrengthModifier", "implantSetLGCaldariNavy",
                          lambda implant: "implantSetLGCaldariNavy" in implant.attributes \
                          and "scanGravimetricStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)