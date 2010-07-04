#Used by: Item: Armored Warfare Mindlink
from customEffects import boost
type = "gang"
runTime = "early"
def armorTankingGang2(self, fitting):
    skill, level = fitting.getCharSkill("Armored Warfare")
    if skill != None: fitting.gangSkills[skill]["level"] = 0
    boost(fitting.ship, "armorHP", "armorHpBonus2", self.item)
