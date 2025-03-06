from manim import *


class Basics(Scene):
    def construct(self):

        quadrado = Square().set_opacity(.6).set_color(GREEN)
        circulo = Circle().set_opacity(.6).set_color(RED)
        triangulo = Triangle().set_opacity(.6).set_color(BLUE)

        circulo.move_to(RIGHT*2).rotate(PI/2)
        triangulo.move_to(LEFT*2).rotate(-PI/2)


        self.play(GrowFromCenter(quadrado))
        self.wait(.5)
        self.play(Transform(quadrado, circulo))
        self.wait(.5)
        self.play(Transform(quadrado, triangulo))
        self.wait()
        self.play(Rotate(quadrado, 3), run_time = .5)
        self.play(FadeOut(quadrado))
        self.wait()

