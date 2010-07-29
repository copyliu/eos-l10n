#Items from group: Cap Drain Drone (3 of 3) [Drone]
#Items from group: Energy Destabilizer (41 of 41) [Module]
from model.types import State
type = "active", "projected"
def handler(fit, container, context):
    if "projected" in context and ((hasattr(container, "state") \
    and container.state > State.ACTIVE) or hasattr(container, "amountActive")):
        multiplier = container.amountActive if hasattr(container, "amountActive") else 1
        amount = container.getModifiedItemAttr("energyDestabilizationAmount")
        time = container.getModifiedItemAttr("duration") / 1000.0
        drain = amount / time * multiplier
        fit.extraAttributes["capDrain"].increase(drain)
