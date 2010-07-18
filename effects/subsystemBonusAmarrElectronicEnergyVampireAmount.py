#Item: Legion Electronics - Energy Parasitic Complex [Subsystem]
from customEffects import boostModListByReq
def subsystemBonusAmarrElectronicEnergyVampireAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boostModListByReq(fitting.modules, "powerTransferAmount", "subsystemBonusAmarrElectronic",
                      lambda mod: mod.group.name == "Energy Vampire",
                      self.item, extraMult = level)