#Item: Loki Defensive - Adaptive Shielding [Subsystem]
from customEffects import boostModListByReq
def subsystemBonusMinmatarDefensive2RemoteShieldTransporterAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Defensive Systems")
    boostModListByReq(fitting.modules, "shieldBonus", "subsystemBonusMinmatarDefensive2",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)