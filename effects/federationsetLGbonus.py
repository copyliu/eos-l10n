#Used by: Item: Low-Grade Spur Set
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def federationsetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanMagnetometricStrengthModifier", "implantSetLGFederationNavy",
                          lambda implant: "implantSetLGFederationNavy" in implant.attributes \
                          and "scanMagnetometricStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)