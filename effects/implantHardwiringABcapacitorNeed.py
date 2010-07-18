#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Navigation Implants (3 of 3)
from customEffects import boostModListBySkillReq
def implantHardwiringABcapacitorNeed(self, fitting):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Afterburner", self.item)