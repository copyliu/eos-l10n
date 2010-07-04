#Used by: Skill: Gas Cloud Harvesting
from customEffects import boostModListByReq, increase
def gasCloudHarvestingMaxGroupSkillLevel(self, fitting, level):
    boostModListByReq(fitting.modules, "maxGroupActive", level,
                      lambda mod: mod.group.name == "Gas Cloud Harvester",
                      helper = increase)