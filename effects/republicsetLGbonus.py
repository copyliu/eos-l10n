#Item: Low-grade Jackal Alpha [Implant]
#Item: Low-grade Jackal Beta [Implant]
#Item: Low-grade Jackal Delta [Implant]
#Item: Low-grade Jackal Epsilon [Implant]
#Item: Low-grade Jackal Gamma [Implant]
#Item: Low-grade Jackal Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def republicsetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanLadarStrengthModifier", "implantSetLGRepublicFleet",
                          lambda implant: "implantSetLGRepublicFleet" in implant.attributes \
                          and "scanLadarStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)