from manim import *

class InsertionSort(Scene):

    def construct(self):

        np.random.seed(42)

        title = Title('Insertion Sort')
        self.play(Write(title))

        self.next_section("Algorithm execution")

        n = 6
        array = list(range(n))
        
        rects = VGroup(
            *[VGroup(
                Rectangle(width=0.5, height=a/2.0 + 0.5, color=BLUE, fill_opacity=0.2), 
                Tex(f'{a}')
            ) for a in array]
        )

        rects.scale(1.5)
        rects.shuffle()
        rects.arrange()

        self.play(FadeIn(rects))

        self.wait()

        self.insertion_sort(rects, n)

        self.wait(2)

        self.play(FadeOut(rects))

        self.next_section("Comparisons Counting")

        rects.shuffle()
        rects.arrange()
        rects.scale(0.8)
        rects.to_edge(LEFT)
        rects.shift(RIGHT * 1.2)
        for (rect, _) in rects:
            rect.set_fill(opacity=0.2)

        self.play(FadeIn(rects))

        self.wait()

        grid = VGroup(*[
            VGroup(*[
                Square(color=YELLOW, fill_opacity=0.1).scale(0.2) 
                for _ in range(n - 1)
            ]) for _ in range(n - 1)
        ])
        
        for row in grid:
            row.arrange(RIGHT)
        grid.arrange(DOWN)
        grid.to_edge(RIGHT)

        count = Tex(r'Comparison Counts', font_size=32)
        count.next_to(grid, UP)

        table = VGroup(grid, count)
        table.shift(LEFT * 1.5)

        self.play(FadeIn(table))

        self.wait()

        self.count_insertion_sort(grid, rects, n)

        self.wait(2)

        self.play(FadeOut(rects), FadeOut(count))

        self.play(grid.animate.move_to(ORIGIN).scale(1.3))

        left_brace = Brace(grid, direction=LEFT)
        left_label = left_brace.get_text(r"n-1")

        bottom_brace = Brace(grid, direction=DOWN)
        bottom_label = bottom_brace.get_text(r"n-1")

        self.play(GrowFromCenter(left_brace), GrowFromCenter(bottom_brace))
        self.play(Write(left_label), Write(bottom_label))

        self.wait()

        count_space = Polygon(UL * 2, DOWN * 2, DR * 2).set_stroke(YELLOW)

        self.play(Create(count_space))

        self.wait()

        comparisons = Tex(r'Comparisons: ', r'$\sim\frac{n^2}{4}$')

        self.play(
            count_space.animate.set_fill(YELLOW, opacity=1.0),
            FadeOut(grid),
            FadeOut(left_brace), FadeOut(bottom_brace),
            FadeOut(left_label), FadeOut(bottom_label),
        )

        self.play(ReplacementTransform(count_space, comparisons))
        
        self.wait(2)

        time_complaxity = Tex(r'Time Complaxity') 
        time_complaxity.shift(UP*2)

        complexities = Tex(r'Best ', r' Average ', r' Worst')
        complexities.shift(UP)

        self.play(Write(time_complaxity), Write(complexities))

        times = MathTex(r'O(n)\ ', r'\ O(n^2)\ ', r'\ O(n^2)')

        self.play(ReplacementTransform(comparisons, times))

        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(times), 
            FadeOut(time_complaxity), FadeOut(complexities)
        )

    def insertion_sort(self, rects: VGroup(VGroup(Rectangle())), n: int) -> None:
        self.play(rects[0][0].animate.set_fill(BLUE, opacity=0.5))
        for i in range(1, n):
            self.play(Indicate(rects[i]))
            j = i 
            while j > 0:
                if self.value(rects[j]) < self.value(rects[j - 1]):
                    self.play(Indicate(VGroup(rects[j], rects[j - 1]), color=RED))
                    rects[j], rects[j - 1] = rects[j - 1], rects[j]
                    self.play(Swap(rects[j], rects[j - 1]))
                    j -= 1
                else:
                    self.play(Indicate(VGroup(rects[j], rects[j - 1]), color=GREEN))
                    break
            self.play(rects[j][0].animate.set_fill(BLUE, opacity=0.5))

    def count_insertion_sort(self, count : list(list(Square())), rects: VGroup(VGroup(Rectangle())), n: int) -> None:
        self.play(rects[0][0].animate.set_fill(BLUE, opacity=0.5))
        for i in range(1, n):
            self.play(Indicate(rects[i]))
            j = i 
            while j > 0:
                if self.value(rects[j]) < self.value(rects[j - 1]):
                    self.play(
                        Indicate(VGroup(rects[j], rects[j - 1]), color=RED),
                        Indicate(count[i-1][j-1]),
                        count[i-1][j-1].animate.set_fill(opacity=1.0)
                    )
                    rects[j], rects[j - 1] = rects[j - 1], rects[j]
                    self.play(Swap(rects[j], rects[j - 1]))
                    j -= 1
                else:
                    self.play(
                        Indicate(VGroup(rects[j], rects[j - 1]), color=GREEN), 
                        Indicate(count[i-1][j-1]),
                        count[i-1][j-1].animate.set_fill(opacity=1.0)
                    )
                    break
            self.play(rects[j][0].animate.set_fill(BLUE, opacity=0.5))

    def value(self, rect: VGroup) -> int:
        return int(rect[1].get_tex_string())


class SelectionSort(Scene):

    def construct(self):

        np.random.seed(42)

        title = Title('Selection Sort')
        self.play(Write(title))

        self.next_section("Algorithm execution")

        n = 6
        array = list(range(n))

        rects = VGroup(
            *[VGroup(
                Rectangle(width=0.5, height=a/2.0 + 0.5, color=BLUE, fill_opacity=0.2), 
                Tex(f'{a + 1}')
            ) for a in array]
        )

        rects.scale(1.5)
        rects.shuffle()
        rects.arrange()

        self.play(FadeIn(rects))

        self.wait()

        self.selection_sort(rects, n)

        self.wait(2)

        self.play(FadeOut(rects))

        self.next_section("Comparisons Counting")

        rects.shuffle()
        rects.arrange()
        rects.scale(0.8)
        rects.to_edge(LEFT)
        rects.shift(RIGHT * 1.2)
        for (rect, _) in rects:
            rect.set_fill(opacity=0.2)

        self.play(FadeIn(rects))

        self.wait()

        grid = VGroup(*[
            VGroup(*[
                Square(color=YELLOW, fill_opacity=0.1).scale(0.2) 
                for _ in range(n - 1)
            ]) for _ in range(n - 1)
        ])
        
        for row in grid:
            row.arrange(RIGHT)
        grid.arrange(DOWN)
        grid.to_edge(RIGHT)

        count = Tex(r'Comparison Counts', font_size=32)
        count.next_to(grid, UP)

        table = VGroup(grid, count)
        table.shift(LEFT * 1.5)

        self.play(FadeIn(table))

        self.wait()

        self.count_selection_sort(grid, rects, n)

        self.wait(2)

        self.play(FadeOut(rects), FadeOut(count))

        self.play(grid.animate.move_to(ORIGIN).scale(1.3))

        left_brace = Brace(grid, direction=LEFT)
        left_label = left_brace.get_text(r"n-1")

        bottom_brace = Brace(grid, direction=DOWN)
        bottom_label = bottom_brace.get_text(r"n-1")

        self.play(GrowFromCenter(left_brace), GrowFromCenter(bottom_brace))
        self.play(Write(left_label), Write(bottom_label))

        self.wait()

        count_space = Polygon(UL * 2, UR * 2, DR * 2).set_stroke(YELLOW)

        self.play(Create(count_space))

        self.wait()

        comparisons = Tex(r'Comparisons: ', r'$\sim\frac{n^2}{2}$')

        self.play(
            count_space.animate.set_fill(YELLOW, opacity=1.0),
            FadeOut(grid),
            FadeOut(left_brace), FadeOut(bottom_brace),
            FadeOut(left_label), FadeOut(bottom_label),
        )

        self.play(ReplacementTransform(count_space, comparisons))
        
        self.wait(2)

        time_complaxity = Tex(r'Time Complaxity') 
        time_complaxity.shift(UP*2)

        complexities = Tex(r'Best ', r' Average ', r' Worst')
        complexities.shift(UP)

        self.play(Write(time_complaxity), Write(complexities))

        times = MathTex(r'O(n)\ ', r'\ O(n^2)\ ', r'\ O(n^2)')

        self.play(ReplacementTransform(comparisons, times))

        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(times), 
            FadeOut(time_complaxity), FadeOut(complexities)
        )

    def selection_sort(self, rects: VGroup(VGroup(Rectangle())), n: int) -> None:
        for i in range(0, n):
            m = i;
            self.play(rects[i][0].animate.set_fill(YELLOW, opacity=0.5))
            for j in range(i + 1, n):
                if self.value(rects[j]) < self.value(rects[m]):
                    self.play(Indicate(VGroup(rects[j], rects[m]), color=RED))
                    self.play(
                        rects[m][0].animate.set_fill(BLUE, opacity=0.2),
                        rects[j][0].animate.set_fill(YELLOW, opacity=0.5)
                    )
                    m = j
                else:
                    self.play(Indicate(VGroup(rects[j], rects[m]), color=GREEN))
                    
            rects[i], rects[m] = rects[m], rects[i]
            self.play(Swap(rects[i], rects[m]))
            self.play(rects[i][0].animate.set_fill(BLUE, opacity=0.5))

    def count_selection_sort(self, count : list(list(Square())), rects: VGroup(VGroup(Rectangle())), n: int) -> None:
        for i in range(0, n):
            m = i;
            self.play(rects[i][0].animate.set_fill(YELLOW, opacity=0.5))
            for j in range(i + 1, n):
                if self.value(rects[j]) < self.value(rects[m]):
                    self.play(
                        Indicate(VGroup(rects[j], rects[m]), color=RED),
                        Indicate(count[i][j - 1]),
                        count[i][j - 1].animate.set_fill(opacity=1.0)
                    )
                    self.play(
                        rects[m][0].animate.set_fill(BLUE, opacity=0.2),
                        rects[j][0].animate.set_fill(YELLOW, opacity=0.5)
                    )
                    m = j
                else:
                    self.play(
                        Indicate(VGroup(rects[j], rects[m]), color=GREEN),
                        Indicate(count[i][j - 1]),
                        count[i][j - 1].animate.set_fill(opacity=1.0)
                    )
                    
            rects[i], rects[m] = rects[m], rects[i]
            self.play(Swap(rects[i], rects[m]))
            self.play(rects[i][0].animate.set_fill(BLUE, opacity=0.5))

    def value(self, rect: VGroup) -> int:
        return int(rect[1].get_tex_string())

class BubbleSort(Scene):

    def construct(self):
        
        np.random.seed(42)

        title = Title('Bubble Sort')
        self.play(Write(title))

        self.next_section("Algorithm execution")

        n = 6
        array = list(range(n))
        
        rects = VGroup(
            *[VGroup(
                Rectangle(width=0.5, height=a/2.0 + 0.5, color=BLUE, fill_opacity=0.2), 
                Tex(f'{a + 1}')
            ) for a in array]
        )

        rects.scale(1.5)
        rects.shuffle()
        rects.arrange()

        self.play(FadeIn(rects))

        self.wait()

        self.bubble_sort(rects, n)

        self.wait(2)

        self.play(FadeOut(rects))

        self.next_section("Comparisons Counting")

        np.random.seed(42)

        rects.shuffle()
        rects.arrange()
        rects.scale(0.8)
        rects.to_edge(LEFT)
        rects.shift(RIGHT * 1.2)
        for (rect, _) in rects:
            rect.set_fill(opacity=0.2)

        self.play(FadeIn(rects))

        self.wait()

        grid = VGroup(*[
            VGroup(*[
                Square(color=YELLOW, fill_opacity=0.1).scale(0.2) 
                for _ in range(n - 1)
            ]) for _ in range(n - 1)
        ])
        
        for row in grid:
            row.arrange(RIGHT)
        grid.arrange(DOWN)
        grid.to_edge(RIGHT)

        count = Tex(r'Comparison Counts', font_size=32)
        count.next_to(grid, UP)

        table = VGroup(grid, count)
        table.shift(LEFT * 1.5)

        self.play(FadeIn(table))

        self.wait()

        self.count_bubble_sort(grid, rects, n)

        self.wait(2)

        self.play(FadeOut(rects), FadeOut(count))

        self.play(grid.animate.move_to(ORIGIN).scale(1.3))

        left_brace = Brace(grid, direction=LEFT)
        left_label = left_brace.get_text(r"n-1")

        bottom_brace = Brace(grid, direction=DOWN)
        bottom_label = bottom_brace.get_text(r"n-1")

        self.play(GrowFromCenter(left_brace), GrowFromCenter(bottom_brace))
        self.play(Write(left_label), Write(bottom_label))

        self.wait()

        count_space = Polygon(UL * 2, DL * 2 + UP, DL * 2 + UP + RIGHT,UR * 2).set_stroke(YELLOW)

        self.play(Create(count_space))

        self.wait()

        comparisons = Tex(r'Comparisons: ', r'$\sim\frac{n^2}{2}$')

        self.play(
            count_space.animate.set_fill(YELLOW, opacity=1.0),
            FadeOut(grid),
            FadeOut(left_brace), FadeOut(bottom_brace),
            FadeOut(left_label), FadeOut(bottom_label),
        )

        self.play(ReplacementTransform(count_space, comparisons))
        
        self.wait(2)

        time_complaxity = Tex(r'Time Complaxity') 
        time_complaxity.shift(UP*2)

        complexities = Tex(r'Best ', r' Average ', r' Worst')
        complexities.shift(UP)

        self.play(Write(time_complaxity), Write(complexities))

        times = MathTex(r'O(n)\ ', r'\ O(n^2)\ ', r'\ O(n^2)')

        self.play(ReplacementTransform(comparisons, times))

        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(times), 
            FadeOut(time_complaxity), FadeOut(complexities)
        )

    def bubble_sort(self, rects: VGroup(VGroup(Rectangle())), n: int) -> None:
        for i in range(n - 1):
            flag = False
            for j in range(n - i - 1):
                if self.value(rects[j]) > self.value(rects[j + 1]):
                    self.play(Indicate(VGroup(rects[j], rects[j + 1]), color=RED))
                    rects[j + 1], rects[j] = rects[j], rects[j + 1]
                    self.play(Swap(rects[j], rects[j + 1]))
                    flag = True
                else:
                    self.play(Indicate(VGroup(rects[j], rects[j + 1]), color=GREEN))
            if not flag:
                j = n - i - 1
                while j >= 0:
                    self.play(rects[j][0].animate.set_fill(BLUE, opacity=0.5))
                    j -= 1
                break
            self.play(rects[n - i - 1][0].animate.set_fill(BLUE, opacity=0.5))
        self.play(rects[0][0].animate.set_fill(opacity=0.5)) 
   
    def count_bubble_sort(self, count : list(list(Square())), rects: VGroup(VGroup(Rectangle())), n: int) -> None:
        for i in range(n - 1):
            flag = False
            for j in range(n - i - 1):
                if self.value(rects[j]) > self.value(rects[j + 1]):
                    self.play(
                        Indicate(VGroup(rects[j], rects[j + 1]), color=RED),
                        Indicate(count[i][j]),
                        count[i][j].animate.set_fill(opacity=1.0)
                    )
                    rects[j + 1], rects[j] = rects[j], rects[j + 1]
                    self.play(Swap(rects[j], rects[j + 1]))
                    flag = True
                else:
                    self.play(
                        Indicate(VGroup(rects[j], rects[j + 1]), color=GREEN),
                        Indicate(count[i][j]),
                        count[i][j].animate.set_fill(opacity=1.0)
                    )
            if not flag:
                j = n - i - 1
                while j >= 0:
                    self.play(rects[j][0].animate.set_fill(BLUE, opacity=0.5))
                    j -= 1
                break
            self.play(rects[n - i - 1][0].animate.set_fill(BLUE, opacity=0.5))
        self.play(rects[0][0].animate.set_fill(opacity=0.5)) 
   
    def value(self, rect: VGroup) -> int:
        return int(rect[1].get_tex_string())

class MergeSort(Scene):

    def construct(self):

        np.random.seed(42)

        title = Title('Merge Sort')
        self.play(Write(title))

        self.next_section('Algorithm description')

        n = 8
        arr = list(range(n))

        array = VGroup(*[
            VGroup(
                Rectangle(width=0.5, height=a/2.0 + 0.5, color=BLUE, fill_opacity=0.2), 
                Tex(f'{a + 1}')
            ) for a in arr]
        )

        array.shuffle()
        array.arrange()

        self.play(FadeIn(array))

        split_line = Line(UP, DOWN)
        split_text = Tex(r'Split')
        split_text.next_to(split_line, DOWN)

        self.play(Create(split_line), Write(split_text))

        left_array = array[0:n//2]
        right_array = array[n//2:n]

        self.play(
            FadeOut(split_text),
            left_array.animate.shift(LEFT),
            right_array.animate.shift(RIGHT)
        )

        self.play(FadeOut(split_line))

        left_brace = Brace(left_array)
        left_label = left_brace.get_text(r'Sort')

        self.play(GrowFromCenter(left_brace), Write(left_label))

        self.minimal_swap_sort(left_array)

        right_brace = Brace(right_array)
        right_label = right_brace.get_text(r'Sort')

        self.play(FadeOut(left_brace), FadeOut(left_label))
        self.play(GrowFromCenter(right_brace), Write(right_label))

        self.minimal_swap_sort(right_array)

        self.play(FadeOut(right_brace), FadeOut(right_label))

        merge = Tex(r'Merge')
        merge.shift(UP * 1.7)

        self.play(
            Write(merge),
            VGroup(left_array, right_array).animate.shift(DOWN * 2)
        )

        self.merge(array, left_array, right_array)
        
        self.play(FadeOut(merge))

        self.wait()

        self.play(FadeOut(array))

        self.next_section('Time Complexity')

        np.random.seed(42)

        array.scale(0.8)
        array.shuffle()
        array.arrange()
        for element in array:
            element[0].set_fill(opacity=0.2)

        time_complexity = Tex(r'Time Complexity $T(n)$')
        time_complexity.next_to(title, DOWN)

        self.play(FadeIn(array), Write(time_complexity))

        split_line = Line(UP, DOWN)
        split_text = Tex(r'Split')
        split_text.next_to(split_line, DOWN)

        split_time = MathTex(r'O(1)')
        split_time.next_to(split_line, UP)

        self.play(Create(split_line), Write(split_text))

        left_array = array[0:n//2]
        right_array = array[n//2:n]

        self.play(
            FadeOut(split_text), Write(split_time),
            left_array.animate.shift(LEFT),
            right_array.animate.shift(RIGHT)
        )

        self.play(FadeOut(split_line))

        left_brace = Brace(left_array)
        left_label = left_brace.get_text(r'Sort')

        left_time = MathTex(r'T(n/2)')
        left_time.next_to(split_time, LEFT * 2)

        self.play(GrowFromCenter(left_brace), Write(left_label))

        self.minimal_swap_sort(left_array)

        self.play(Write(left_time))

        right_brace = Brace(right_array)
        right_label = right_brace.get_text(r'Sort')

        right_time = MathTex(r'T(n/2)')
        right_time.next_to(split_time, RIGHT * 2)

        self.play(FadeOut(left_brace), FadeOut(left_label))
        self.play(GrowFromCenter(right_brace), Write(right_label))

        self.minimal_swap_sort(right_array)

        self.play(Write(right_time))

        self.play(FadeOut(right_brace), FadeOut(right_label))

        merge = Tex(r'Merge')

        self.play(
            Write(merge),
            VGroup(left_array, right_array).animate.shift(DOWN * 2)
        )

        self.play(FadeOut(merge))

        self.merge(array, left_array, right_array)

        merge_time = MathTex(r'O(n)')
        merge_time.shift(DOWN * 1.7)

        self.play(Write(merge_time))        

        self.play(FadeOut(array))
        
        total_time = MathTex(r'T(1) &= O(1) \\ T(n) &= 2 T(n / 2) + O(n)')
        
        self.play(ReplacementTransform(VGroup(split_time, left_time, right_time, merge_time), total_time))

        self.wait(3)

        final_time = MathTex(r'T(n) = O(n \log n)')

        self.play(ReplacementTransform(total_time, final_time))

        self.wait(2)

        self.play(FadeOut(time_complexity), FadeOut(final_time))            

    def merge(
        self, 
        array: VGroup(VGroup(Rectangle(), Tex())),
        array_left: VGroup(VGroup(Rectangle(), Tex())), 
        array_right: VGroup(VGroup(Rectangle(), Tex()))
    ) -> None:
        n, m = len(array_left), len(array_right)
        array = VGroup()
        i, j = 0, 0
        while i < n and j < m:
            self.play(Indicate(array_left[i]), Indicate(array_right[j]))
            if self.value(array_left[i]) <= self.value(array_right[j]):
                array.add(array_left[i])
                self.play(array_left[i][0].animate.set_fill(opacity=0.5))
                self.play(
                    array_left[i].animate.move_to(ORIGIN), 
                    array.animate.arrange()
                )
                i += 1
            else:
                array.add(array_right[j])
                self.play(array_right[j][0].animate.set_fill(opacity=0.5))
                self.play(
                    array_right[j].animate.move_to(ORIGIN), 
                    array.animate.arrange()
                )
                j += 1
        
        while i < n:
            array.add(array_left[i])
            self.play(array_left[i][0].animate.set_fill(opacity=0.5))
            self.play(
                array_left[i].animate.move_to(ORIGIN), 
                array.animate.arrange()
            )
            i += 1
        
        while j < m:
            array.add(array_right[j])
            self.play(array_right[j][0].animate.set_fill(opacity=0.5))
            self.play(
                array_right[j].animate.move_to(ORIGIN), 
                array.animate.arrange()
            )
            j += 1


    def minimal_swap_sort(self, array: VGroup(VGroup(Rectangle(), Tex()))) -> None:
        sorted_array = sorted(array, key=lambda x: self.value(x))

        position = {}
        for i, element in enumerate(array):
            position[element] = i 
        
        for i, element in enumerate(array):
            if element != sorted_array[i]:
                j = position[sorted_array[i]]
                array[i], array[j] = array[j], array[i]
                self.play(Swap(array[i], array[j]), run_time=0.5)
                position[array[i]] = i 
                position[array[j]] = j

    def value(self, element: VGroup(Rectangle(), Tex())) -> int:
        return int(element[1].get_tex_string())