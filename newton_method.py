from manim import *
import numpy as np

class NewtonMethodConvergence(Scene):
    def construct(self):
        # Define the function and its derivative
        def func(x):
            return x**2 - 4*x + 4

        def func_prime(x):
            return 2*x - 4

        def func_double_prime(x):
            return 2

        # Create axes
        axes = Axes(
            x_range=[-1, 6],
            y_range=[-1, 10],
            axis_config={"color": BLUE},
        )

        # Labels for the axes
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Graph of the function
        graph = axes.plot(func, color=WHITE)
        graph_label = axes.get_graph_label(graph, label="f(x) = x^2 - 4x + 4")

        # Initial guess
        x_n = 5
        x_tracker = ValueTracker(x_n)

        # Dot for the current point
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(x_tracker.get_value(), func(x_tracker.get_value())), color=RED
            )
        )

        # Tangent line at the current point
        tangent_line = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x_tracker.get_value(),
                graph=graph,
                dx=0.1,
                secant_line_length=4,
                secant_line_color=YELLOW,
            ).secant_line
        )

        # Add all elements to the scene
        self.play(Create(axes), Create(labels))
        self.play(Create(graph), Write(graph_label))
        self.play(FadeIn(dot), Create(tangent_line))

        # Iteratively apply Newton's method with larger initial steps for the first few iterations
        for i in range(5):
            x_n = x_tracker.get_value()
            x_next = x_n - (func_prime(x_n) / func_double_prime(x_n))  # Larger step size initially

            # Highlight the next point before moving
            next_dot = Dot(axes.c2p(x_next, func(x_next)), color=GREEN)
            self.play(FadeIn(next_dot))
            self.wait(1)

            # Show evaluation of function at next point
            eval_text = MathTex(f"f({x_next:.10f}) = {func(x_next):.10f}")
            eval_text.next_to(next_dot, UP)
            self.play(Write(eval_text))

            # Animate the movement to the next point step by step
            self.play(x_tracker.animate.set_value(x_next), run_time=2)
            self.wait(1)

            # Remove the highlighted dot and evaluation text
            self.play(FadeOut(next_dot), FadeOut(eval_text))

        # Accelerate the convergence for the remaining steps with smaller step size
        for _ in range(5):
            x_n = x_tracker.get_value()
            x_next = x_n - func_prime(x_n) / func_double_prime(x_n)

            # Highlight the next point before moving
            next_dot = Dot(axes.c2p(x_next, func(x_next)), color=GREEN)
            self.play(FadeIn(next_dot))
            self.wait(0.5)

            # Show evaluation of function at next point
            eval_text = MathTex(f"f({x_next:.2f}) = {func(x_next):.2f}")
            eval_text.next_to(next_dot, UP)
            self.play(Write(eval_text))

            # Animate the movement to the next point with faster animation
            self.play(x_tracker.animate.set_value(x_next), run_time=1)
            self.wait(0.5)

            # Remove the highlighted dot and evaluation text
            self.play(FadeOut(next_dot), FadeOut(eval_text))

        # Hold the final frame
        self.wait(2)

# To render this, run the following command in the terminal:
# manim -pql newton_method_manim.py NewtonMethodConvergence

