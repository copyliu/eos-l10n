#Item: Tengu Electronics - CPU Efficiency Gate [Subsystem]
from customEffects import boost
def subsystemBonusCaldariElectronicCPU(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Electronic Systems")
    boost(fitting.ship, "cpuOutput", "subsystemBonusCaldariElectronic",
          self.item, extraMult = level)