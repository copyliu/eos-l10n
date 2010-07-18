#Item: Spur Alpha [Implant]
#Item: Spur Beta [Implant]
#Item: Spur Delta [Implant]
#Item: Spur Epsilon [Implant]
#Item: Spur Gamma [Implant]
#Item: Spur Omega [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def federationsetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanMagnetometricStrengthPercent",
                          "implantSetFederationNavy",
                          lambda implant: "implantSetFederationNavy" in implant.attributes and\
                          "scanMagnetometricStrengthPercent" in implant.attributes,
                          self.item, helper = multiply)