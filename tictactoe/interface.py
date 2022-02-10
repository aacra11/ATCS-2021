import arcade

screen_width = 600
screen_height = 600
screen_title = "Tic Tac Toe"

arcade.open_window(screen_width, screen_height, screen_title)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_line(screen_width/3,0,screen_width/3,screen_height, arcade.color.BLACK)
arcade.draw_line(2*screen_width/3,0,2*screen_width/3,screen_height, arcade.color.BLACK)
arcade.draw_line(0,screen_width/3,screen_width,screen_width/3, arcade.color.BLACK)
arcade.draw_line(0,2*screen_width/3,screen_width,2*screen_width/3, arcade.color.BLACK)

arcade.finish_render()

arcade.run()