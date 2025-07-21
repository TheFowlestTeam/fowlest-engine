from fowlest import FSTEngine
from fowlest.node import FSTBaseNode, FSTSpriteNode
from fowlest.math import Vec2

nodes = []

fowlest = FSTEngine()
fowlest.start()

sprite1 = FSTSpriteNode("./assets/fowlest.png")
sprite1.set_position(Vec2(sprite1.get_horizontal_align_position(640, 1), sprite1.get_vertical_align_position(480, 1)))
fowlest.add(nodes, sprite1)

while fowlest.is_running():
    fowlest.events()
    fowlest.draw(nodes)
    fowlest.update(nodes)

fowlest.quit()