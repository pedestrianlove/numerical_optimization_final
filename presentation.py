from manim import *  # or: from manimlib import *

from manim_slides import Slide

# import slide pages
import slide_folder.title_page as title_page
import slide_folder.misc_page as misc_page

class OptimizationFinal(Slide):
    def construct(self):

        title_page.title_page(self)

        misc_page.misc_page(self)

