from manim import *  # or: from manimlib import *

from manim_slides import Slide

# import slide pages
import slide_folder as slides

class OptimizationFinal(Slide):
    def construct(self):

        # Title
        slides.title_page(self)
        # Contraction
        slides.contraction_example(self)
        slides.contraction_definition(self)
        slides.contraction_proof(self)
        # Simelp Example
        slides.newton_method(self)
        slides.high_dimension_newton_method(self)
        # Interlude
        slides.interlude(self)
        # Advanced Applications
        slides.mdp_intro(self)
        slides.mdp_proof(self)
        # Conclusion
        slides.conclusion(self)
