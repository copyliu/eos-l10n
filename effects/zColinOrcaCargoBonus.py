#Item: Orca
from customEffects import boost
def zColinOrcaCargoBonus(self, fitting):
    skill, level = fitting.getCharSkill("Industrial Command Ships")
    boost(fitting.ship, "capacity", "shipOrcaCargoBonusOrca1", self.item,
          extraMult = level)
