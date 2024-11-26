from manim import *

from slide_folder.contraction_definition import contraction_definition

def contraction_proof(self):

    # Contraction sequence visualization
    sequence_def = MathTex(r"x_{n+1} = \phi(x_n)").to_edge(UP)
    self.play(FadeIn(sequence_def))
    self.next_slide()

    # Define initial point
    initial_dot = Dot(LEFT * 5 + UP, color=BLUE)
    initial_label = MathTex("x_0").next_to(initial_dot, UP)
    self.play(FadeIn(initial_dot), FadeIn(initial_label))
    self.wait(1)

    # Generate and animate subsequent points to the right
    dot_list = []
    brace_list = []
    label_list = []
    lines_list = []
    dot_list.append(initial_dot)
    label_list.append(initial_label)

    num_iterations = 4  # You can increase this for more points
    curve_radius = 3  # Adjust to change the curvature of the sequence
    distance_labels = []

    for i in range(1, num_iterations + 1):
        # Define new point for each iteration
        angle = i * PI / 30  # Adjust the denominator to control spacing
        new_dot_position = dot_list[-1].get_center() + curve_radius * RIGHT * np.cos(angle) - curve_radius * UP * np.sin(angle)
        new_dot = Dot(new_dot_position, color=BLUE)
        var_label = MathTex(rf"\phi(x_{i-1})").next_to(new_dot, UP)

        # Animate the movement from previous point to the new point
        old_dot = dot_list[-1].copy()
        line = Line(start=old_dot.get_center(), end=new_dot.get_center())
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

        # Visualize the distance between the dots with a brace
        brace = Brace(line)
        distance_label = brace.get_text(f"$d(x_{i-1}, x_{i})$")
        self.play(FadeIn(brace), FadeIn(distance_label), FadeIn(line))
        lines_list.append(line)
        brace_list.append(brace)
        distance_labels.append(distance_label)

        # Update previous point
        dot_list.append(new_dot)
        dot_list.append(old_dot)
        label_list.append(new_label)

        self.wait(1)

    # Fade out all elements when finished...
    self.next_slide()
    self.play(FadeOut(VGroup(*dot_list, *label_list, *lines_list, *brace_list)))

    # Setup LaTeX preambles.
    definition_template = TexTemplate()
    definition_template.add_to_preamble(r"\usepackage{amsthm}")
    definition_template.add_to_preamble(r"\newtheorem*{definition}{Definition}")
    definition_template.add_to_preamble(r"\newtheorem*{theorem}{Theorem}")
    # Contraction definition
    contraction_def = Tex(r"""
        Let $X$ be a metric space, with metric $d$. If $\phi$ maps $X$ into $X$ and if there is a number $c<1$ such that
        \begin{equation*}
            d(\phi(x), \phi(y)) \leq c \cdot d(x, y)
        \end{equation*}
        for all $x,y\in X$, then $\phi$ is said to be a contraction of $X$ into $X$.
    """, tex_template=definition_template,tex_environment="definition").scale(0.75).to_edge(UP)
    # Contraction theorem
    contraction_theorem = Tex(r"""
        If $X$ is a complete metric space, and if $\phi$ is a contraction of $X$ into X, then there exists one and only one $x\in X$ such that $\phi (x) = x$.
    """, tex_template=definition_template, tex_environment="theorem").scale(0.75).to_edge(UP)

    # Convert distance_label into inequalities
    ineq = MathTex(
        "d(x_0, x_4)", r"&\leq ", "d(", "x_0,", "x_1", r")\\", 
                        "&+ ", "d(", "x_1,", "x_2", r")\\", 
                        "&+ ", "d(", "x_2,", "x_3", r")\\", 
                        "&+ ", "d(", "x_3,", "x_4", ")", tex_environment='align*'
    ).to_edge(DOWN)
    self.play(ReplacementTransform(VGroup(*distance_labels), ineq))
    self.play(ReplacementTransform(sequence_def, contraction_def))
    self.next_slide()
    ineq_1 = MathTex(
        "d(x_0, x_4)", r"&\leq ", "d(", "x_0,", "x_1", r")\\", 
                        "&+ ", "d(", r"\phi(x_0),", r"\phi(x_1)", r")\\", 
                        "&+ ", "d(", r"\phi^2(x_0),", r"\phi^2(x_1)", r")\\", 
                        "&+ ", "d(", r"\phi^3(x_0),", r"\phi^3(x_1)", ")", tex_environment='align*'
    ).to_edge(DOWN)
    self.play(TransformMatchingTex(ineq, ineq_1))
    self.next_slide()
    ineq_2 = MathTex(
        "d(x_0, x_4)", r"&\leq ", "d(", "x_0,", "x_1", r")\\", 
                        "&+ ", "c", r"\cdot ", "d(", "x_0,", "x_1", r")\\", 
                        "&+ ", "c^2", r"\cdot ", "d(", "x_0,", "x_1", r")\\", 
                        "&+ ", "c^3", r"\cdot ", "d(", "x_0,", "x_1", ")", tex_environment='align*'
    ).to_edge(DOWN)
    self.play(TransformMatchingTex(ineq_1, ineq_2))
    self.next_slide()
    ineq_3 = MathTex(
        "d(x_0, x_4)", r"&\leq ", 
        "d(", "x_0,", "x_1", ")", r"\cdot ", 
        "(", "1", "+", "c", "+", "c^2", "+", "c^3", ")"
    )
    self.play(TransformMatchingTex(ineq_2, ineq_3))
    self.next_slide()
    self.play(ReplacementTransform(contraction_def, contraction_theorem))
    self.next_slide()
    proof = Tex(r"""
    \raggedright
    If $n < m$, it follows that
    \begin{equation*}
        \begin{split}
        d(x_n, x_m) &\leq   \sum_{i=n+1}^m d(x_{i-1}, x_i)    \\
                    &\leq   (c^n + c^{n+1} + \cdots + c^{m-1}) d(x_0, x_1)  \\
                    &\leq   [ (1 - c)^{-1} d(x_0, x_1) ] c^n  \to 0.
        \end{split}
    \end{equation*}
    \par
    Since $x_n$ is a Cauchy sequence, $x_n$ converges to some $x \in X$. Furthermore, since $\phi$ is a contraction, it's also a continuous function, which implies
    \begin{equation*}
        \phi(x) = \phi(\lim_{n\to \infty} x_n) = \lim_{n\to \infty} \phi(x_n) = \lim_{n\to \infty} x_{n+1} = x.
    \end{equation*}
    """, tex_template=definition_template, tex_environment="proof").scale(0.75).shift(DOWN)
    self.play(ReplacementTransform(ineq_3, proof))
    self.next_slide()

