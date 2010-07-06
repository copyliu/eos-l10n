#Used by: Item: Proteus Propulsion - Localized Injectors
from customEffects import boostModListByReq
def subsystemBonusGallentePropulsionABMWDCapNeed(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Propulsion Systems")
    boostModListByReq(fitting.modules, "capacitorNeed", "subsystemBonusGallentePropulsion",
                      lambda mod: mod.group.name == "Afterburner"
                      ,self.item, extraMult = level)