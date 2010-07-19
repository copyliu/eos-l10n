#Variations of item: Large Energy Discharge Elutriation I (2 of 2) [Module]
#Variations of item: Medium Energy Discharge Elutriation I (2 of 2) [Module]
#Variations of item: Small Energy Discharge Elutriation I (2 of 2) [Module]
from customEffects import boostModListByReq
def capNeedBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Energy Weapon", self.item)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoostr(lambda mod: mod.group.name == "Energy Weapon",
                                   "capacitorNeed", module.getModifiedItemAttr("capNeedBonus"))