from manim import *

def newton_method(self):

    # Question
    text = Text("But why is fixed point theorem useful?").scale(0.75)
    self.play(FadeIn(text))
    self.next_slide()
    self.play(FadeOut(text))

    # Use Newton's Method as an example
    newton_title = Text("Recall the Newton's method used to find root.").scale(0.75).to_edge(UP)
    self.play(Write(newton_title))
    self.next_slide()

    # List out algorithm
    algorithm_env = TexTemplate()
    algorithm_env.add_to_preamble(r"\usepackage{algcompatible}")
    algorithm_env.add_to_preamble(r"\usepackage{amsthm}")
    newton_algorithm = Tex(r"""
        \STATE Input: Objective function $f: \mathbb{R} \to \mathbb{R}$
        \STATE Input: Initial guess $x_0$
        \WHILE{$k \gets 0 \ldots n$ and $|f(x_k)| > \epsilon $}
            \State $x_{k+1} \gets x_k - \frac{f(x_k)}{f'(x_k)}$
            \State $k \gets k + 1$
        \ENDWHILE
    """, tex_template=algorithm_env, tex_environment="algorithmic").scale(0.75).to_edge(UP)
    print(newton_algorithm.tex_strings)
    self.play(ReplacementTransform(newton_title, newton_algorithm))
    self.next_slide()

    newton_it = MathTex(r"\phi(x)", "=", "x", "-", r"\frac{f(x)}{f'(x)}")
    self.play(ReplacementTransform(newton_algorithm, newton_it))
    self.next_slide()
    self.play(newton_it.animate.to_edge(UP))

    # Question: But is \phi a contraction?
    # Answer: Yes! Since
    question = Tex(r"Question: But is $\phi$ a contraction?").scale(0.75).next_to(newton_it, DOWN)
    answer = Tex(r"""
        Answer: Yes! $\phi$ is a contraction, because MVT guarantees the existence of $c$ between given $x, y$ such that 
        \begin{equation*}
            \phi(y) - \phi(x) = \phi'(c)(y - x).
        \end{equation*}
        \par
        Since $f', f''$ are both continuous function, Extreme Value Theorem shows that $|\frac{f''(c)}{f'(c)}| < M$ for some $M > 0$ on an open interval $U\subset \mathbb{R}$ containing $c$. Also, since $c$ is close to $x^*$, we can also have $|f(c)| < \frac{1}{M}$ such that
        \begin{equation*}
            |\phi'(c)| = |f(c)|\cdot |\frac{f''(c)}{f'(c)}| < \frac{1}{M} \cdot M = 1.
        \end{equation*}
        \par
        Threefore, $\phi$ is a contraction.
    """).scale(0.75).next_to(newton_it, DOWN)
    self.play(Write(question))
    self.next_slide()
    self.play(ReplacementTransform(question, answer))

    # Fade out all elements when finished...
    self.next_slide()
    self.play(FadeOut(VGroup(answer, newton_it)))
