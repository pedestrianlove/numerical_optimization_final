from manim import *

def mdp_intro(self):

    # Brief intro
    title = Text("Markov Decision Process").to_edge(UP)
    image = ImageMobject("assets/mdp.png").scale(2).next_to(title, DOWN)
    self.play(FadeIn(title))
    self.next_slide()
    self.play(FadeIn(image))
    self.next_slide()
    self.play(FadeOut(title), FadeOut(image))

    # Target
    target = Tex(r"""
        Target: Given a reward function $R$, the discounting factor $0< \gamma < 1$ and the transition model $P(s'|s,a)$. Find a function (Bellman equation) $U$ that can evaluate the usefulness(utility) of a given state $s$ s.t.
        \begin{equation*}
            U(s) = R(s) + \gamma \max_{a\in A(s)}\sum_{s'} P(s'|s,a) U(s'),
        \end{equation*}
        \par
        where $A(s)$ denotes the set of all possible actions at state $s$.
    """).scale(0.75)
    self.play(FadeIn(target))
    self.next_slide()
    self.play(target.animate.to_edge(UP/2))

    # Show the iteration scheme
    algorithm_env = TexTemplate()
    algorithm_env.add_to_preamble(r"\usepackage{algcompatible}")
    algorithm_env.add_to_preamble(r"\usepackage{amsthm}")
    algorithm = Tex(r"""
        \STATE Input: Reward function $R: S \to \mathbb{R}$.
        \STATE Input: Set of all states $S$.
        \STATE Input: Transition model $P(s'|s,a)$
        \STATE Input: Set of all action $A(s)$ (depends on s).
        \STATE Input: Initial guess $U_0$
        \WHILE{$k \gets 0 \ldots n$ and $\max_{s\in S}|U_{k+1}(s) - U_k(s)| > \epsilon $}
            \State $U_{k+1}(s) \gets R(s) + \gamma \max_{a\in A(s)}\sum_{s'} P(s'|s,a) U(s'), \forall s\in S$
            \State $k \gets k + 1$
        \ENDWHILE
    """, tex_template=algorithm_env, tex_environment="algorithmic").scale(0.75).next_to(target, DOWN)
    self.play(Write(algorithm))
    self.next_slide()

    # Fade out all elements when finished...
    self.play(FadeOut(target), FadeOut(algorithm))
