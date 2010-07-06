#Used by: Ship: Cerberus
#               Sacrilege
from customEffects import boostModListByReq
def eliteBonusHeavyGunshipHeavyMissileLaunhcerRof2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListByReq(fitting.modules, "speed", "eliteBonusHeavyGunship2",
                      lambda mod: mod.group.name == "Missile Launcher Heavy",
                      self.item, extraMult = level)