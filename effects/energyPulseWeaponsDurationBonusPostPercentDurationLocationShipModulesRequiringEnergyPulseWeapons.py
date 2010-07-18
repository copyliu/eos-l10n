#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Engineering Implants (3 of 9)
#Item: Energy Pulse Weapons [Skill]
from customEffects import boostModListByReq
def energyPulseWeaponsDurationBonusPostPercentDurationLocationShipModulesRequiringEnergyPulseWeapons(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)