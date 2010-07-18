#Item: Defender I [Charge]
def defenderMissileLaunching(self, fitting, containerModule):
    #Ignore defender missile damage
    self.item.attributes["explosiveDamage"].overrideValue = 0