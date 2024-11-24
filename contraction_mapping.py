from manim import *
import numpy as np

class ContractionMapping(Scene):
    def construct(self):
        # Axes for the R^2 space (two separate coordinate systems)
        axes_1 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        ).to_corner(DOWN + LEFT)
        labels_1 = axes_1.get_axis_labels(x_label="x_1", y_label="y_1")

        axes_2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GREEN}
        ).to_corner(UP + RIGHT)
        labels_2 = axes_2.get_axis_labels(x_label="x_2", y_label="y_2")

        self.play(Create(axes_1), Write(labels_1), Create(axes_2), Write(labels_2))
        self.wait(1)

        # Points before contraction mapping (in the first coordinate system)
        point_a = np.array([2, 1, 0])
        point_b = np.array([-2, -1, 0])

        contraction_factor = 0.5
        contracted_point_a = contraction_factor * point_a
        contracted_point_b = contraction_factor * point_b

        # Create dots for original points in the first coordinate system
        dot_a = Dot(axes_1.c2p(*point_a[:2]), color=YELLOW)
        dot_b = Dot(axes_1.c2p(*point_b[:2]), color=YELLOW)
        self.play(Create(dot_a), Create(dot_b))
        self.wait(1)

        # Create dots for contracted points in the second coordinate system
        contracted_dot_a = Dot(axes_2.c2p(*contracted_point_a[:2]), color=RED)
        contracted_dot_b = Dot(axes_2.c2p(*contracted_point_b[:2]), color=RED)

        # Animate the transformation from original to contracted points
        arrow_a = Arrow(axes_1.c2p(*point_a[:2]), axes_2.c2p(*contracted_point_a[:2]), buff=0.1, color=WHITE)
        arrow_b = Arrow(axes_1.c2p(*point_b[:2]), axes_2.c2p(*contracted_point_b[:2]), buff=0.1, color=WHITE)

        self.play(Create(contracted_dot_a), Create(contracted_dot_b), Create(arrow_a), Create(arrow_b))
        self.wait(2)

        # Add a label to indicate contraction mapping
        contraction_label = MathTex(r"f(x, y) = 0.5 \cdot (x, y)")
        contraction_label.to_corner(UP + LEFT)
        self.play(Write(contraction_label))
        self.wait(2)

        # Fade out all elements
        self.play(FadeOut(VGroup(axes_1, labels_1, axes_2, labels_2, dot_a, dot_b, contracted_dot_a, contracted_dot_b, arrow_a, arrow_b, contraction_label)))
        self.wait(1)

# To render this scene, save this script as contraction_mapping.py and run:
# manim -pql contraction_mapping.py ContractionMapping

