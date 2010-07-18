#Items from group: ECM Burst (7 of 7)
from model import attribute
type = ("projected", "active")
def ecmBurst(self, fitting, state):
    self.item.attributes["maxRange"] = self.item.attributes["ecmBurstRange"]
