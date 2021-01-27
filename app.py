from manim import (
    Scene,
    Circle,
    Square,
    RIGHT,
    TAU,
    PINK,
    ShowCreation,
    Transform,
    FadeOut,
)


class S1(Scene):

    """Hello world from manim. Scene 1"""

    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
