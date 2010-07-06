#Used by: Item: Gallente Electronics - CPU Efficiency Gate
from customEffects import boost
def subsystemBonusGallenteElectronicCPU(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Electronic Systems")
    boost(fitting.ship, "cpuOutput", "subsystemBonusGallenteElectronic",
          self.item, extraMult = level)