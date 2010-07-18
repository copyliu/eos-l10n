#Item: Cerberus [Ship]
#Item: Sacrilege [Ship]
from customEffects import boostModListByReq
def eliteBonusHeavyGunshipHeavyAssaultMissileLaunhcerRof2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListByReq(fitting.modules, "speed", "eliteBonusHeavyGunship2",
                      lambda mod: mod.group.name == "Missile Launcher Heavy Assault",
                      self.item, extraMult = level)