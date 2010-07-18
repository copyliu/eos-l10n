#Item: Hyena [Ship]
from customEffects import boost
def eliteBonusElectronicAttackShipSignatureRadius2(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boost(fitting.ship, "signatureRadius", "eliteBonusElectronicAttackShip2",
                      self.item, extraMult = level)