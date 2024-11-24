from manim import *

def misc_page(self):
    circle = Circle(radius=4, color=BLUE)
    dot = Dot()
    self.play(GrowFromCenter(circle))
    self.next_slide()  # Waits user to press continue to go to the next slide
    self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
    self.next_slide()  # This will start a new non-looping slide

    self.play(dot.animate.move_to(ORIGIN))

    self.next_slide(loop=True)  # Start loop
