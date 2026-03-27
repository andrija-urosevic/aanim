from manim import *

class EuclidAlgorithm(Scene):

    def construct(self):

        np.random.seed(42)

        title = Title('Euclid\'s Algorithm')
        self.play(Write(title))

        self.next_section('Algorithm execution')

        self.a, self.b = 48, 18

        rect = Rectangle(width=self.a, height=self.b, color=GRAY, fill_opacity=0.2).scale(0.2)

        a_text = Tex(f'{self.a}').next_to(rect, DOWN)
        b_text = Tex(f'{self.b}').next_to(rect, RIGHT)

        self.play(FadeIn(rect))

        self.play(Write(a_text), Write(b_text))

        cut_squares = self.euclid_algorithm(rect, a_text, b_text)

        self.play(
            FadeOut(cut_squares), FadeOut(rect), 
            FadeOut(a_text), FadeOut(b_text), 
            FadeOut(title)
        )

    def euclid_algorithm(self, rect : Rectangle, a_text : Tex, b_text : Tex) -> VGroup:
        cut_squares = VGroup()
        while self.a != self.b:
            if self.a > self.b:
                old_a = self.a
                self.a -= self.b


                square = Rectangle(
                    width=self.b,
                    height=self.b,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.25,
                    stroke_width=2,
                ).scale(0.2)

                square.move_to(rect.get_left() + RIGHT * (self.b * 0.1))
                cut_squares.add(square)

                self.play(FadeIn(square))

                new_a = Tex(f"{self.a}").next_to(
                    rect.copy().stretch_to_fit_width(self.a * 0.2).next_to(square, RIGHT, buff=0),
                    DOWN,
                )

                self.play(
                    rect.animate.stretch_to_fit_width(self.a * 0.2).next_to(square, RIGHT, buff=0),
                    Transform(a_text, new_a),
                )
            else:
                old_b = self.b
                self.b -= self.a

                square = Rectangle(
                    width=self.a,
                    height=self.a,
                    color=ORANGE,
                    fill_color=ORANGE,
                    fill_opacity=0.25,
                    stroke_width=2,
                ).scale(0.2)

                square.move_to(rect.get_top() + DOWN * (self.a * 0.1))
                cut_squares.add(square)

                self.play(FadeIn(square))

                new_b = Tex(f"{self.b}").next_to(
                    rect.copy().stretch_to_fit_height(self.b * 0.2).next_to(square, DOWN, buff=0),
                    RIGHT,
                )

                self.play(
                    rect.animate.stretch_to_fit_height(self.b * 0.2).next_to(square, DOWN, buff=0),
                    Transform(b_text, new_b),
                )

        self.play(Indicate(rect, color=YELLOW), rect.animate.set_fill(color=GREEN))

        return cut_squares