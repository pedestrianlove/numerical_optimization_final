from manim import *

def conclusion(self):

    # Content
    con_0 = Text("So").scale(0.75)
    con = Text("Fixed Point Theorem is useful.").scale(0.75)
    con_1 = Text("It can be applied to any iterative scheme.").scale(0.75)
    con_2 = Text("Even if it's not necessarily numerical.").scale(0.75)

    self.play(Write(con_0))
    self.next_slide()
    self.play(ReplacementTransform(con_0, con))
    self.next_slide()
    self.play(ReplacementTransform(con, con_1))
    self.next_slide()
    self.play(ReplacementTransform(con_1, con_2))
    self.next_slide()
    self.play(FadeOut(con_2))

    # Fade out all elements when finished...
    thank_you = Text("Thank You.")
    self.play(Write(thank_you))
    self.next_slide()
    self.play(FadeOut(thank_you))
