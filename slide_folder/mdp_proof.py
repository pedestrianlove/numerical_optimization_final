from manim import *

def mdp_proof(self):

    # Content
    mdp_it = Tex(r"""
        Let $X$ be the set of all function that maps from $S$ to $\mathbb{R}$, and $d = \|\cdot \|_{\infty}$ the max norm to be the metric for $X$. Define the iterative function $\phi : X\to X$ such that
        \begin{equation*}
            \phi(U)(s) = R(s) + \gamma \max_{a\in A(s)}\sum_{s'} P(s'|s,a) U(s'), \forall s\in S.
        \end{equation*}

        Given arbitrary $s\in S$ and $U_x, U_y$, we can define $a^*(s)$ to be the optimal action for given state $s$, then we have
        \begin{equation*}
            \begin{split}
            \| (\phi (U_x) - \phi(U_y))(s) \|    &=      \gamma | \max_{a\in A(s)}\sum_{s'}P(s'|s,a)U_x(s') - \max_{a\in A(s)}\sum_{s'}P(s'|s,a)U_y(s') |  \\
                                                &\leq   \gamma | \sum_{s'}P(s'|s,a^*(s))(U_x(s') - U_y(s')) |    \\
                                                &=      \gamma | (\sum_{s'}P(s'|s,a^*(s)))(\max_s(U_x(s) - U_y(s)) |    \\
                                                &=      \gamma | 1 \cdot (\max_s (U_x(s) - U_y(s))) |
            \end{split}
        \end{equation*}
    """).scale(0.7).to_edge(UP)
    self.play(Write(mdp_it))
    self.next_slide()
    self.play(FadeOut(mdp_it))

    mdp_it_2 = Tex(r"""
        Since
        \begin{equation*}
            \begin{split}
            d(\phi(U_x), \phi(U_y)) &= \max_s |(\phi (U_x) - \phi(U_y))(s)| \\
                                    &\leq \gamma \cdot \max_s |U_x(s) - U_y(s)| \\
                                    &= \gamma \cdot d(U_x, U_y),
            \end{split}
        \end{equation*}
        where $0<\gamma <1$, $\phi$ is a contraction.    \\
        Since $X$ is a complete metric space, Fixed Point Theorem shows that the value iteration algorithm converges.
    """).scale(0.75).to_edge(UP)
    self.play(Write(mdp_it_2))
    self.next_slide()

    conclusion = Tex(r"After finding the utility function $U$, we can use it to compute the optimal policy model $\pi: S \to S$ to determine the best state switching strategy.").scale(0.75).next_to(mdp_it_2, DOWN)
    self.play(FadeIn(conclusion))
    self.next_slide()

    # Fade out all elements when finished...
    self.play(FadeOut(VGroup(mdp_it_2, conclusion)))
