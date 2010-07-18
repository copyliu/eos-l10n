#Items from group: Heavy Assault Ship (2 of 8) [Ship]
from customEffects import boostModListByReq
def eliteBonusHeavyGunshipAssaultMissileLaunhcerRof2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListByReq(fitting.modules, "speed", "eliteBonusHeavyGunship2",
                      lambda mod: mod.group.name == "Missile Launcher Assault",
                      self.item, extraMult = level)