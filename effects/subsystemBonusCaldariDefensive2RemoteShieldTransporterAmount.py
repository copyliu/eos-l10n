#Item: Tengu Defensive - Adaptive Shielding
from customEffects import boostModListByReq
def subsystemBonusCaldariDefensive2RemoteShieldTransporterAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Defensive Systems")
    boostModListByReq(fitting.modules, "shieldBonus", "subsystemBonusCaldariDefensive2",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)