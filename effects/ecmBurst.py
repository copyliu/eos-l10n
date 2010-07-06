#Used by: Item: ECM Burst
from model import attribute
type = ("projected", "active")
def ecmBurst(self, fitting, state):
    self.item.attributes["maxRange"] = self.item.attributes["ecmBurstRange"]
