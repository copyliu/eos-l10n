#Items from group: Cyberimplant (6 of 138) [Implant]
from customEffects import boostImplantListByReq, multiply
runTime = "early"
def federationsetbonus3(self, fitting):
    boostImplantListByReq(fitting.implants, "scanMagnetometricStrengthPercent",
                          "implantSetFederationNavy",
                          lambda implant: "implantSetFederationNavy" in implant.attributes and\
                          "scanMagnetometricStrengthPercent" in implant.attributes,
                          self.item, helper = multiply)