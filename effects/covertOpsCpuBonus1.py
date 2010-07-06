#Used by: Ship: Covert Ops
#               Stealth Bombers
#               Force Recon Ships
#               Blockade Runners
#         Item: Covert Reconfiguration Subsystems
from customEffects import boostModListByReq, multiply
def covertOpsCpuBonus1(self, fitting, state = None):
    #take cpu consumption static multiplier
    if "cloakingCpuNeedBonus" in self.item.attributes: staticBonus = self.item.getModifiedAttribute("cloakingCpuNeedBonus")
    else: staticBonus = 1
    #get all data for bonus per skill lvl
    itemGroup = self.item.group.name
    #item group name : (skill used for bonus multiplication, bonus per lvl)
    cloakyShips = { "Transport Ship" : ("Transport Ships", 0.0015),
                        "Covert Ops" : ("Covert Ops", 0.005),
                  "Force Recon Ship" : ("Recon Ships", 0.01),
                    "Stealth Bomber" : None,
                 "Offensive Systems" : None }    
    if itemGroup in cloakyShips:
        if cloakyShips[itemGroup]:
            skill, level = fitting.getCharSkill(cloakyShips[itemGroup][0])
            lvlBonus = cloakyShips[itemGroup][1]
        else:
            level = 0
            lvlBonus = 0
    else:
        level = 0
        lvlBonus = 0
        print "Warning: unsupported cloaking device cpu bonus carrier:", self.item.name, "(" + self.item.group.name + ")"
 
    boostModListByReq(fitting.modules, "cpu", staticBonus - (lvlBonus * level),
                      lambda mod: mod.group.name == "Cloaking Device",
                      self.item, helper = multiply)