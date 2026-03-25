from manim import *
import math

class BinarySearch(Scene):

    def construct(self):

        np.random.seed(42)

        title = Title('Binary Search')
        self.play(Write(title))

        self.next_section('Algorithm execution')

        array = [1, 1, 1, 3, 3, 4, 5, 7, 8, 8]

        rects = VGroup(
            *[VGroup(
                Rectangle(width=0.5, height=0.5, color=GRAY, fill_opacity=0.2), 
                Tex(f'{a}')
            ) for a in array]
        )

        rects.arrange()

        target_rect = VGroup(
            Rectangle(width=0.5, height=0.5, color=GREEN, fill_opacity=0.2), 
            Tex('5')
        )

        rects.move_to(UP * 0.2)

        target_rect.next_to(rects, DOWN, buff=1.5)

        self.play(FadeIn(rects))

        self.play(FadeIn(target_rect))

        self.binary_search_algorithm(rects, len(array), target_rect)

        self.wait(2)

        self.play(FadeOut(rects), FadeOut(title))

    def binary_search_algorithm(self, rects : VGroup(VGroup(Rectangle())), n : int, target : VGroup(Rectangle())) -> None:
        l, r = 0, n - 1

        l_ptr = Tex('l', color=BLUE).scale(0.8).next_to(rects[l], UP, buff=0.2)
        r_ptr = Tex('r', color=ORANGE).scale(0.8).next_to(rects[r], UP, buff=0.2)

        self.play(FadeIn(l_ptr), FadeIn(r_ptr))

        while l <= r:
            m = (l + r) // 2
            m_ptr = Tex('m', color=YELLOW).scale(0.8).next_to(rects[m], DOWN, buff=0.2)
            self.play(FadeIn(m_ptr))
            if rects[m][1].get_tex_string() == target[1].get_tex_string():
                self.play(Indicate(VGroup(rects[m], target), color=GREEN))
                self.play(rects[m][0].animate.set_color(GREEN))
                break
            elif rects[m][1].get_tex_string() < target[1].get_tex_string():
                self.play(Indicate(VGroup(rects[m], target), color=BLUE))
                moves = []
                for i in range(l, m + 1):
                    moves.append(rects[i][0].animate.set_color(BLUE))
                self.play(*moves)
                l = m + 1
                if l == r:
                    self.play(l_ptr.animate.next_to(r_ptr, LEFT, buff=0.1))
                elif l < n:
                    self.play(l_ptr.animate.next_to(rects[l], UP, buff=0.2))
                else:
                    self.play(l_ptr.animate.next_to(r_ptr, RIGHT, buff=0.2))
            else:
                self.play(Indicate(VGroup(rects[m], target), color=ORANGE))
                moves = []
                for i in range(m, r + 1):
                    moves.append(rects[i][0].animate.set_color(ORANGE))
                self.play(*moves)
                r = m - 1
                if r == l:
                    self.play(r_ptr.animate.next_to(l_ptr, RIGHT, buff=0.1))
                elif r >= 0:
                    self.play(r_ptr.animate.next_to(rects[r], UP, buff=0.2))
                else:
                    self.play(r_ptr.animate.next_to(l_ptr, LEFT, buff=0.2))
            self.play(FadeOut(m_ptr))

        self.play(FadeOut(l_ptr), FadeOut(r_ptr))


class DutchFlag(Scene):

    def construct(self):

        np.random.seed(42)

        title = Title('Dutch National Flag')
        self.play(Write(title))

        self.next_section('Algorithm execution')

        self.red = 0
        self.white = 1
        self.blue = 2

        num_red = 4
        num_white = 3
        num_blue = 3
        
        n = num_red + num_white + num_blue

        array = num_red * [self.red] + num_white * [self.white] + num_blue * [self.blue]

        rects = VGroup(
            *[VGroup(
                self.make_shape(a), 
                Tex(f'{a}')
            ) for a in array]
        )

        rects.scale(1.5)
        rects.shuffle()
        rects.arrange()

        self.play(FadeIn(rects))

        self.wait()

        self.dutch_flag_algorithm(rects, n)

        self.wait(2)

        self.play(FadeOut(rects), FadeOut(title))

    def dutch_flag_algorithm(self, rects : VGroup(VGroup(Rectangle())), n : int) -> None:
        l, m, r = 0, 0, n - 1

        l_ptr = Tex('l', color=RED).scale(0.8).next_to(rects[l], UP, buff=0.2)
        m_ptr = Tex('m', color=YELLOW).scale(0.8).next_to(rects[m], DOWN, buff=0.2)
        r_ptr = Tex('r', color=BLUE).scale(0.8).next_to(rects[r], UP, buff=0.2)

        self.play(FadeIn(l_ptr), FadeIn(m_ptr), FadeIn(r_ptr))

        l_edge_rect = Rectangle(width=0.5, height=0.5, color=RED).set_opacity(0.0).next_to(rects[l], LEFT, buff=0.2)
        r_edge_rect = Rectangle(width=0.5, height=0.5, color=RED).set_opacity(0.0).next_to(rects[l], RIGHT, buff=0.2)

        while m <= r:
            self.play(Indicate(rects[m][0], color=YELLOW))
            if rects[m][1].get_tex_string() == '0':
                rects[l], rects[m] = rects[m], rects[l]
                if l != m:
                    self.play(Swap(rects[l], rects[m]))
                self.play(rects[l][0].animate.set_color(RED))
                l += 1
                m += 1
                moves = []
                if m < n:
                    moves.append(l_ptr.animate.next_to(rects[l], UP, buff=0.2))
                    moves.append(m_ptr.animate.next_to(rects[m], DOWN, buff=0.2))
                elif l < n:
                    moves.append(l_ptr.animate.next_to(rects[l], UP, buff=0.2))
                    moves.append(m_ptr.animate.next_to(r_edge_rect, RIGHT, buff=0.2))
                else:
                    moves.append(l_ptr.animate.next_to(r_edge_rect, RIGHT, buff=0.2))
                    moves.append(m_ptr.animate.next_to(r_edge_rect, RIGHT, buff=0.2))
                self.play(*moves)
            elif rects[m][1].get_tex_string() == '1':
                self.play(rects[m][0].animate.set_color(WHITE))
                m += 1
                if m < n:
                    self.play(m_ptr.animate.next_to(rects[m], DOWN, buff=0.2))
                else:
                    self.play(m_ptr.animate.next_to(r_edge_rect, RIGHT, buff=0.2))
            else:
                rects[m], rects[r] = rects[r], rects[m]
                self.play(Swap(rects[m], rects[r]))
                self.play(rects[r][0].animate.set_color(BLUE))
                r -= 1
                if r >= 0:
                    self.play(r_ptr.animate.next_to(rects[r], UP, buff=0.2))
                else:
                    self.play(r_ptr.animate.next_to(l_edge_rect, LEFT, buff=0.2))

        self.play(FadeOut(l_ptr), FadeOut(m_ptr), FadeOut(r_ptr))

    def make_shape(self, a):
        if a == self.red:
            return Square(side_length=0.45, color=GRAY, fill_opacity=0.2)
        elif a == self.white:
            return Circle(radius=0.25, color=GRAY, fill_opacity=0.2)
        elif a == self.blue:
            return RegularPolygon(n=5, radius=0.25, color=GRAY, fill_opacity=0.2)
        return Rectangle(width=0.5, height=0.5, color=GRAY, fill_opacity=0.0).set_opacity(0.0)
