from manim import *

def high_dimension_newton_method(self):

    # Intro bits...
    text = Text("Newton's Method in higher dimension is similar...(by MVT)").scale(0.75)
    self.play(FadeIn(text))
    self.next_slide()
    self.play(FadeOut(text))

    # Newton's Method (Higher dimensional)
    newton_method = MathTex(r"\vec{x_{k+1}}", "=",  r"\vec{x_k}", "- H(", r"\vec{x_k}", r")^{-1}\nabla f(", r"\vec{x_k}", ")")
    newton_it = MathTex(r"\phi(", r"\vec{x}", ") =",  r"\vec{x}", "- H(", r"\vec{x}", r")^{-1}\nabla f(", r"\vec{x}", ")")
    self.play(Write(newton_method))
    self.next_slide()
    self.play(TransformMatchingTex(newton_method, newton_it))
    self.play(newton_it.animate.to_edge(UP))
    self.next_slide()

    # Show why Newton's iteration is a contraction (MVT inequality)
    contraction_eq = Tex(r"""
        Given any $\vec{x}, \vec{y}$, there exists $\vec{z} \in \{ t\vec{x} + (1-t)\vec{y}\ :\ 0 \leq t \leq 1 \}$ such that
        \begin{equation*}
            \begin{split}
                \| \phi (\vec{x}) - \phi(\vec{y}) \|    &\leq \| \phi'(\vec{z}) (\vec{x} - \vec{y}) \|  \\
                                                        &\leq \| \phi'(\vec{z})\| \|(\vec{x} - \vec{y}) \|
            \end{split}
        \end{equation*}
    """).scale(0.75).next_to(newton_it, DOWN)
    self.play(Write(contraction_eq))
    self.next_slide()

    # Show why Newton's iteration is a contraction (factor)
    conclusion = Tex(r"""
        Since $\phi'$ is continuous near $\vec{x^*}$, by applying Extreme Value Theorem to each component of $\phi'$, we can find an open set $U\subset \mathbb{R}^n$ containing $\vec{x^*}$ such that
        \begin{equation*}
            \| \phi'(\vec{x^*}) \| \leq 1
        \end{equation*}

        \par
        Hence, $\phi$ is a contraction. Therefore, the Newton's Method converges.
    """).scale(0.75).next_to(contraction_eq, DOWN)
    self.play(Write(conclusion))
    self.next_slide()

    # Fade out all elements when finished...
    self.play(FadeOut(VGroup(newton_it, contraction_eq, conclusion)))
