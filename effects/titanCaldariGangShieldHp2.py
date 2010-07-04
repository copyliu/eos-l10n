#Used by: Ship: Leviathan
type = ("gang", "normal")
from customEffects import boost, multiply
def titanCaldariGangShieldHp2(self, fitting, activeLayer):
    if activeLayer == "ship":
        skill, level = fitting.getCharSkill("Caldari Titan")
        multiply(self.item, "shipBonusCT2", level)
        self.item.attributes["commandBonus"] = self.item.attributes["shipBonusCT2"]
    else:
        boost(fitting.ship, "shieldCapacity", "shipBonusCT2", self.item)
