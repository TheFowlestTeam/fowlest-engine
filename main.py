from fowlest import FSTEngine, FSTConfig
from fowlest.display import FSTLayer

nodes = []

config = FSTConfig([640, 480, "Fowlest Game"])

fowlest = FSTEngine(config)
fowlest.start()

fowlest.add_layer(FSTLayer())\

while fowlest.is_running():
    fowlest.events()
    
    fowlest.draw(nodes)
    fowlest.update(nodes)

fowlest.quit()