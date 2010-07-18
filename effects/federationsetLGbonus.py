#Item: Low-grade Spur Alpha [Implant]
#Item: Low-grade Spur Beta [Implant]
#Item: Low-grade Spur Delta [Implant]
#Item: Low-grade Spur Epsilon [Implant]
#Item: Low-grade Spur Gamma [Implant]
#Item: Low-grade Spur Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def federationsetLGbonus(self, fitting):
    boostImplantListByReq(fitting.implants, "scanMagnetometricStrengthModifier", "implantSetLGFederationNavy",
                          lambda implant: "implantSetLGFederationNavy" in implant.attributes \
                          and "scanMagnetometricStrengthModifier" in implant.attributes,
                          self.item, helper = multiply)