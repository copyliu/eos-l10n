#Used by: Item: Armor Plates
runTime = "early"
from customEffects import increase
import model.fitting

def armorHPBonusAdd(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "armorHP", "armorHPBonusAdd", self.item, position = "pre")
