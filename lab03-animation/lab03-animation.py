
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



def draw_suelo():
    """SUELO"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snowman():
    """MUÑECO"""

    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

def on_draw(delta_time):
    """ Draw everything """

    arcade.start_render()

    draw_suelo()
    draw_snowman(150,140)
    draw_snowman(450,180)

def main():
    """MAIN BARDO"""

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "dibujo animado")
    arcade.set_background_color(arcade.color.DARK_BLUE)


    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()







