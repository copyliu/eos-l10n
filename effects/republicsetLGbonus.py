#Used by: Item: Low-Grade Jackal Set
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def republicsetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanLadarStrengthModifier", "implantSetLGRepublicFleet",
                          lambda implant: "implantSetLGRepublicFleet" in implant.attributes \
                          and "scanLadarStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)