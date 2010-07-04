#Used by: Ship: Redeemer
#               Sin
#               Widow
#               Panther
from customEffects import multiply
from model.attribute import basicAttribute
def eliteBonusBlackOpsCloakVelocity2(self, fitting):
        skill, level = fitting.getCharSkill("Black Ops")
        cloakedVelocityMultiplier = fitting.ship.getModifiedAttribute("_cloakedVelocityMultiplier") or 1
        bonus = self.item.getModifiedAttribute("eliteBonusBlackOps2")
        for i in range(level):
            cloakedVelocityMultiplier *= bonus
            
        fitting.ship.attributes["_cloakedVelocityMultiplier"] = \
            basicAttribute(fitting.ship, "_cloakedVelocityMultiplier", None, cloakedVelocityMultiplier, 1)