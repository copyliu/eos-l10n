from customEffects import boostModListByReq
def shipBonusHeatDamageATF1(self, fitting):
    boostModListByReq(fitting.modules, "heatDamage", "shipBonusATF1",
                           lambda mod: "heatDamage" in mod.attributes,
                           self.item)