#Item: Tengu Electronics - Obfuscation Manifold
from customEffects import boostModListByReq
def subsystemBonusCaldariElectronicECMRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Electronic Systems")
    boostModListByReq(fitting.modules, "maxRange", "subsystemBonusCaldariElectronic",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)