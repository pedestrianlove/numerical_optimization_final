from manim import *  # or: from manimlib import *

from manim_slides import Slide

# import slide pages
import slide_folder as slides

class OptimizationFinal(Slide):
    def construct(self):
        slides.title_page(self)
        slides.misc_page(self)
        #test
