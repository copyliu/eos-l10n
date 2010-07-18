#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Missile Implants (3 of 6)
from customEffects import boostAmmoListBySkillReq
def missileVelocityBonusDefender(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "missileVelocityBonus",
                       lambda skill: skill.name == "Defender Missiles")