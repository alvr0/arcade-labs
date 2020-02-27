
import arcade

arcade.open_window(800,700, "Draw")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.csscolor.GREEN)
arcade.draw_lrtb_rectangle_filled(0, 800, 300, 100, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(0, 400, 200, 700, 400, 400, arcade.csscolor.SADDLE_BROWN)
arcade.draw_triangle_filled(400, 400, 600, 700, 800, 400, arcade.csscolor.SADDLE_BROWN)
arcade.draw_triangle_filled(100, 550, 200, 700, 300, 550, arcade.csscolor.SNOW)
arcade.draw_triangle_filled(500, 550, 600, 700, 700, 550, arcade.csscolor.SNOW)
arcade.draw_line(20, 200, 100, 200,arcade.csscolor.WHITE, line_width=3)
arcade.draw_line(150, 200, 230, 200,arcade.csscolor.WHITE, line_width=3)
arcade.draw_line(280, 200, 360, 200,arcade.csscolor.WHITE, line_width=3)
arcade.draw_line(410, 200, 490, 200,arcade.csscolor.WHITE, line_width=3)
arcade.draw_line(540, 200, 620, 200,arcade.csscolor.WHITE, line_width=3)
arcade.draw_line(670, 200, 750, 200,arcade.csscolor.WHITE, line_width=3)


arcade.draw_circle_filled(320, 600, 35, arcade.csscolor.YELLOW)


arcade.draw_line(370, 590, 400, 580,arcade.csscolor.BLACK, line_width=3)
arcade.draw_line(400, 580, 430, 590,arcade.csscolor.BLACK, line_width=3)





arcade.finish_render()
arcade.run ()


