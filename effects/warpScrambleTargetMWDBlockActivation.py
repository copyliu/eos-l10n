#Variations of item: Warp Scrambler I (19 of 19) [Module]
from customEffects import increase
import model.fitting
type = ("projected", "active")
runTime = "early"
def warpScrambleTargetMWDBlockActivation(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        increase(fitting.ship, "warpScrambleStatus", "warpScrambleStrength", self.item)
        for module in fitting.modules:
            for skill in module.getItem().requiredSkills:
                if skill.name == "High Speed Maneuvering":
                    fitting.blockedItems.add(module.getItem())
                    break

type = "projected", "active"
def handler(fit, module, context):
    if context != "projected" or fit.ship.getModifiedItemAttr("disallowOffensiveModifiers") == 1:
        return
    
    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))
    for module in fit.modules:
        if module.item.requiresSkill("High Speed Maneuvering"):
            module.block()
            