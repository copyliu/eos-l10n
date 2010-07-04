#Used by: Ship: Leviathan
from customEffects import boostAmmoListByReq
def titanCaldariMissileKineticDmg2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Titan")
    boostAmmoListByReq(fitting.modules, "kineticDamage", "shipBonusCT1",
                       lambda ammo: ammo.group.name in ("Citadel Torpedo", "Citadel Cruise"),
                       self.item, extraMult = level)
