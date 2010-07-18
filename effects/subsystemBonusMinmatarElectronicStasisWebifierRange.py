#Item: Loki Electronics - Immobility Drivers [Subsystem]
from customEffects import boostModListByReq
def subsystemBonusMinmatarElectronicStasisWebifierRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boostModListByReq(fitting.modules, "maxRange", "subsystemBonusMinmatarElectronic",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)