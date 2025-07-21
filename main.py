from fowlest import FSTEngine, FSTUtils
from fowlest.node import FSTSpriteNode, FSTBaseNode
from fowlest.math import Vec2

import time

nodes = []

fowlest = FSTEngine()
fowlest.start()

sprite1 = FSTSpriteNode("./assets/fowlest.png")
sprite1.set_position(Vec2(640 / 2, 480 / 2))
sprite1.pivot.x = 0.5
sprite1.pivot.y = 0.5
fowlest.add(nodes, sprite1)

class TestNode(FSTBaseNode):
    def __init__(self):
        super().__init__()
        
        self.type_name = "Test"
        self.last_time = time.time()
        self.current_time = 0
        
    def _update(self):
        self.current_time = time.time()
        if self.current_time - self.last_time >= 1:
            FSTUtils.print_info("Updated test node!")
            self.last_time = self.current_time
        return super()._update()

fowlest.add(nodes, TestNode())

while fowlest.is_running():
    fowlest.events()
    
    sprite1.rotation += 1 * (fowlest.dt * 60)
    
    fowlest.draw(nodes)
    fowlest.update(nodes)

fowlest.quit()