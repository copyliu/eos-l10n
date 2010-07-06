#Used by: Item: Legion Electronics - Energy Parasitic Complex
from customEffects import boostModListByReq
def subsystemBonusAmarrElectronicEnergyDestabilizerAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boostModListByReq(fitting.modules, "energyDestabilizationAmount",
                      "subsystemBonusAmarrElectronic",
                      lambda mod: mod.group.name == "Energy Destabilizer",
                      self.item, extraMult = level)