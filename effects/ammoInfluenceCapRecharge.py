#Used by: T2 Ammo
from customEffects import multiply
def ammoInfluenceCapRecharge(self, fitting, containerModule):
    multiply(fitting.ship, "rechargeRate", "capacitorRechargeRateMultiplier", self.item)