#Variations of item: Warp Scrambler I (19 of 19)
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
