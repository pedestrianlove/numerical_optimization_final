from manim import *  # or: from manimlib import *

def title_page(self):
    # Create title and name
    title = Text("Fixed Point Theorem \nand \nIts Applications").scale(1.2)
    name = Text("113062566 資工所 李智修").next_to(title, DOWN, buff=1.5)

    # Animate title and name appearing
    self.play(FadeIn(title), FadeIn(name))

    self.next_slide()
    self.play(FadeOut(VGroup(title, name)))
