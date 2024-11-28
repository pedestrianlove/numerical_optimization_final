from manim import *

def interlude(self):

    # Content
    intro = Text("So, we can start to see the pattern...").scale(0.75)
    self.play(Write(intro))
    self.next_slide()

    outro = Text("Let's look at some other examples.").scale(0.75)
    self.play(ReplacementTransform(intro, outro))
    self.next_slide()
    
    # Fade out all elements when finished...
    self.play(FadeOut(outro))
