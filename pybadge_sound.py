#!/usr/bin/env python3

# Created by:Euel Yirga
# Created on:October 2019
# This makes sound on the pybadge


import ugame
import stage

import constants


def game_scene():
    # This function is a scene

    # buttons to keep state information on
    a_button_pressed = constants.BUTTON_UP
    b_button_pressed = constants.BUTTON_UP
    start_button_pressed = constants.BUTTON_UP
    select_button_pressed = constants.BUTTON_UP
    
    # get sound ready
    pew_sound = open("pew2.wav", 'rb') # to change the volume: https//audioalter.com/volume/
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

     # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_X, constants.SCREEN_Y)

    # a list of sprites that will be updated every frame
    sprites = []

    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE + constants.SPRITE_SIZE / 2))
    sprites.append(ship)  # insert at the top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)

        # A button to fire
        if keys & ugame.K_X != 0: # A button
            if a_button_pressed == constants.BUTTON_UP:
                a_button_pressed = constants.BUTTON_JUST_PRESSED
            elif a_button_pressed == constants.BUTTON_JUST_PRESSED:
                a_button_pressed = constants.BUTTON_STILL_PRESSED
        else:
            a_button_pressed = constants.BUTTON_UP
        
        # update game logic
        # move ship right
        if keys & ugame.K_RIGHT!= 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        # move ship left
        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)

        
       #play sound if A is pressed
        if a_button_pressed == constants.BUTTON_JUST_PRESSED:
            sound.play(pew_sound) 
        
        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes
