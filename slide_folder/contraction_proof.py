from manim import *

def contraction_proof(self):

    # Contraction sequence visualization
    sequence_def = MathTex(r"x_{n+1} = g(x_n)").to_edge(UP)
    self.play(FadeIn(sequence_def))


    # Define initial point
    initial_dot = Dot(LEFT * 5, color=BLUE)
    initial_label = MathTex("x_0").next_to(initial_dot, UP)
    self.play(FadeIn(initial_dot), FadeIn(initial_label))
    self.wait(1)

    # Generate and animate subsequent points to the right
    dot_list = []
    label_list = []
    dot_list.append(initial_dot)
    label_list.append(initial_label)

    num_iterations = 4  # You can increase this for more points
    curve_radius = 3  # Adjust to change the curvature of the sequence
    for i in range(1, num_iterations + 1):
        # Define new point for each iteration
        angle = i * PI / 30  # Adjust the denominator to control spacing
        new_dot_position = dot_list[-1].get_center() + curve_radius * RIGHT * np.cos(angle) - curve_radius * UP * np.sin(angle)
        new_dot = Dot(new_dot_position, color=BLUE)
        var_label = MathTex(f"g(x_{i-1})").next_to(new_dot,UP)

        # Animate the movement from previous point to the new point
        old_dot = dot_list[-1].copy()
        self.play(
            Transform(old_dot, new_dot),  # Line to show movement (optional)
            FadeIn(new_dot),
            FadeIn(var_label),
            run_time=1
        )
        label_list.append(var_label)
        new_label = MathTex(f"x_{i}").next_to(new_dot, UP)
        self.play(
            Transform(var_label, new_label),
            run_time=2
        )


        # Update previous point
        dot_list.append(new_dot)
        dot_list.append(old_dot)
        label_list.append(new_label)

        self.wait(1)

    etc = MathTex("...").next_to(dot_list[-1], RIGHT)
    self.play(FadeIn(etc))

    # Fade out all elements when finished...
    self.next_slide()
    self.play(FadeOut(VGroup(sequence_def, *dot_list, *label_list, etc)))
