from manim import *



class FourierSeriesDeepSeek(Scene):
    def construct(self):
        # Configurações iniciais
        axes = Axes(
            x_range=[-PI, PI],
            y_range=[-2, 2],
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        # Função original (onda quadrada)
        def square_wave(x):
            return np.sign(np.sin(x))

        graph = axes.plot(square_wave, color=YELLOW)
        self.play(Create(graph))

        # Série de Fourier (primeiros N termos)
        N = 5  # Número de termos
        terms = []  # Lista para armazenar os termos
        for n in range(1, N + 1):
            term = axes.plot(
                lambda x: (4 / (np.pi * n)) * np.sin(n * x),  # Termo da série
                color=interpolate_color(BLUE, RED, n / N),
            )
            terms.append(term)

        # Animação com LaggedStart
        self.play(LaggedStart(*[Create(term) for term in terms], lag_ratio=0.5))

        # Soma dos termos
        sum_graph = axes.plot(lambda x: 0, color=GREEN)  # Começa com zero
        self.play(Create(sum_graph))

        # Atualização da soma com Updater
        def update_sum(graph):
            new_graph = axes.plot(
                lambda x: sum(term.underlying_function(x) for term in terms),
                color=GREEN,
            )
            graph.become(new_graph)

        sum_graph.add_updater(update_sum)
        self.wait()

        # Textos explicativos
        title = Tex("Série de Fourier: Aproximação de uma Onda Quadrada").to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Fim da animação
        self.play(FadeOut(*self.mobjects))




class PitagorasDeepSeek(Scene):
    def construct(self):
        # Cores para os quadrados
        colors = [BLUE, RED, GREEN]

        # Criar o triângulo retângulo
        triangle = Polygon(
            [-2, -1, 0],  # Vértice A
            [1, -1, 0],   # Vértice B
            [-2, 2, 0],   # Vértice C
            color=WHITE
        )
        self.play(Create(triangle))

        # Rótulos para os lados
        labels = [
            Tex("a").next_to(triangle.get_vertices()[0], DOWN),
            Tex("b").next_to(triangle.get_vertices()[1], RIGHT),
            Tex("c").next_to(triangle.get_vertices()[2], UP + LEFT)
        ]
        self.play(*[Write(label) for label in labels])

        # Criar os quadrados sobre os lados
        squares = []
        for i, side in enumerate(triangle.get_vertices()):
            # Calcular o tamanho do quadrado com base no comprimento do lado
            if i == 0:
                square = Square(side_length=2).next_to(triangle, DOWN, buff=0)
            elif i == 1:
                square = Square(side_length=3).next_to(triangle, RIGHT, buff=0)
            else:
                square = Square(side_length=np.sqrt(13)).rotate(np.arctan(3/2)).next_to(triangle, UP + LEFT, buff=0)
            square.set_fill(colors[i], opacity=0.5)
            squares.append(square)

        # Animar a criação dos quadrados com LaggedStart
        self.play(LaggedStart(*[Create(square) for square in squares], lag_ratio=0.5))

        # Mostrar as áreas dos quadrados
        area_labels = [
            MathTex("a^2").move_to(squares[0]),
            MathTex("b^2").move_to(squares[1]),
            MathTex("c^2").move_to(squares[2])
        ]
        self.play(*[Write(label) for label in area_labels])

        # Explicação do Teorema de Pitágoras
        theorem = MathTex("a^2 + b^2 = c^2").to_edge(UP)
        self.play(Write(theorem))

        # Fim da animação
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
