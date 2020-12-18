# add bouncy image
if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
    player_y_momentum = -player_y_momentum
else:
    player_y_momentum += 0.2
player_location[1] += player_y_momentum