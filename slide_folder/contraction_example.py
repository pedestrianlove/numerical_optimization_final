from manim import *

def contraction_example(self):
    # Axes for the R^2 space (grid formation)
    axes = Axes(
        x_range=[-3, 3, 1],
        y_range=[-3, 3, 1],
        axis_config={"color": BLUE}
    ).to_edge(DOWN)
    labels = axes.get_axis_labels(x_label="x", y_label="y")

    self.play(Create(axes), Write(labels))
    self.wait(1)

    # Points before contraction mapping (9 points in grid formation)
    points = [np.array([x, y, 0]) for x in np.linspace(-2, 2, 3) for y in np.linspace(-2, 2, 3)]

    contraction_factor = 0.5
    contracted_points = [contraction_factor * point for point in points]

    # Create dots for original points
    dots = [Dot(axes.c2p(point[0], point[1]), color=YELLOW) for point in points]
    self.play(*[Create(dot) for dot in dots])
    self.wait(1)

    # Highlight the fixed point (0, 0)
    fixed_point = Dot(axes.c2p(0, 0), color=BLUE).scale(1.5)
    fixed_point_label = Text("Fixed Point", font_size=24).next_to(fixed_point, UP)
    self.play(Create(fixed_point), Write(fixed_point_label))
    self.wait(1)

    # Create lines connecting original points in grid fashion
    original_lines = []
    for i in range(3):
        # Horizontal lines
        original_lines.append(Line(axes.c2p(-2, -2 + i * 2, 0), axes.c2p(2, -2 + i * 2, 0), color=GREEN))
        # Vertical lines
        original_lines.append(Line(axes.c2p(-2 + i * 2, -2, 0), axes.c2p(-2 + i * 2, 2, 0), color=GREEN))
    
    self.play(*[Create(line) for line in original_lines])
    self.wait(1)

    # Create dots for contracted points
    contracted_dots = [Dot(axes.c2p(contracted_point[0], contracted_point[1]), color=RED) for contracted_point in contracted_points]

    # Create lines connecting contracted points in grid fashion
    contracted_lines = []
    for i in range(3):
        # Horizontal lines
        contracted_lines.append(Line(axes.c2p(-1, -1 + i, 0), axes.c2p(1, -1 + i, 0), color=PURPLE))
        # Vertical lines
        contracted_lines.append(Line(axes.c2p(-1 + i, -1, 0), axes.c2p(-1 + i, 1, 0), color=PURPLE))
    
    # Animate the transformation from original to contracted points
    arrows = [Arrow(axes.c2p(point[0], point[1]), axes.c2p(contracted_point[0], contracted_point[1]), buff=0.1, color=WHITE)
              for point, contracted_point in zip(points, contracted_points)]

    self.play(*[Create(contracted_dot) for contracted_dot in contracted_dots],
              *[Create(arrow) for arrow in arrows],
              *[Create(line) for line in contracted_lines])
    self.wait(2)

    # Add a label to indicate contraction mapping
    contraction_label = MathTex(r"f(x, y) = (\frac{1}{2}x, \frac{1}{2}y)")
    contraction_label.to_corner(UP + LEFT)
    self.play(Write(contraction_label))

    # Add a text description indicating that f is a contraction mapping
    contraction_text = Text("f is a contraction mapping (shrinks distances)", font_size=24).to_edge(UP)
    self.play(Write(contraction_text))

    self.next_slide()

    # Fade out all elements
    self.play(FadeOut(VGroup(axes, labels, *dots, *contracted_dots, *arrows, *original_lines, *contracted_lines, contraction_label, fixed_point, fixed_point_label, contraction_text)))
