import turtle

# Configuração da tela
screen = turtle.Screen()
screen.bgcolor("white")

# Configuração da caneta
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")

# Função para desenhar um triângulo equilátero
def draw_triangle(side_length):
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)

# Desenha um triângulo com lados de 100 pixels
draw_triangle(100)

# Finaliza o desenho
turtle.done()