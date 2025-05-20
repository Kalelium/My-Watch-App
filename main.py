def on_start_pressed():
    if menu_open:
        pass
controller.start.on_event(ControllerButtonEvent.PRESSED, on_start_pressed)

def on_c_pressed():
    if menu_open:
        blockMenu.set_selected_index(blockMenu.selected_menu_index() + 1)
controller.C.on_event(ControllerButtonEvent.PRESSED, on_c_pressed)

def on_menu_pressed():
    global menu_open, previously_selected_app, selected_app, app_sprites_list, initialize_app
    menu_open = not (menu_open)
    if menu_open:
        blockMenu.show_menu(menu_options, MenuStyle.LIST, MenuLocation.FULL_SCREEN)
    else:
        previously_selected_app = selected_app
        selected_app = blockMenu.selected_menu_option()
        if selected_app != previously_selected_app:
            if app_sprites_list:
                index = 0
                while index <= len(app_sprites_list):
                    app_sprites_list[index].destroy()
                    index += 1
                app_sprites_list = []
            initialize_app = True
        blockMenu.close_menu()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

time: TextSprite = None
app_sprites_list: List[TextSprite] = []
initialize_app = False
selected_app = ""
previously_selected_app = ""
menu_options: List[str] = []
menu_open = False
menu_open = False
menu_options = ["Home", "Watch", "c", "None"]
app_list = ["a", "b", "c"]
previously_selected_app = "None"
selected_app = "Home"
initialize_app = True
app_sprites_list = []
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(14, 97)
mySprite.say(":)")
# 0 = Watch

def on_on_update():
    global time, initialize_app, app_sprites_list
    if selected_app == "Home":
        if initialize_app:
            scene.set_background_image(img("""
                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333cccccccccccccbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb3333333ceeeeeeeeeeeeecbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbcccb333333cecccccccccce4ecbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbceeec33333cecccccccccce4ecbbbbbbbbbbbbbbbbbbb33333333333333333333bbbbbbbbbbbbbbbbbbbb33333333333333333333
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccceecccccecccccccccc888cbbbbbbbbbbbbbbbbbbbb88833333333333333333bbbbbbbbbbccbbbbbbbb33333333333333333333
                                bbbbbbb11111111111111111111111111bdd111111111111bbbbbbcfffffffffcbd1dbbcffc8444888bbbbbbbbbbbbbbb88844483333333333333333bbbbbbbbbbcbccbbbbbb33333333333333333333
                                bbbbbb1dddddddddddddddddddddb1111bd11111111111111bbbbbcccccceececccccccccce844444488888888888888844444483333333333333333bbbbbbbbbbcbbbccbbbb33333333333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd11111111111111bbbbceeeeeeeeeeeeeeeeeeeee844444444444444444444444444483333333333333333bbbbbbbbbbcbbbbbccbb33333333333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd11111111111111bbbbceeeeeeeeeeeee44444444e84444444444444444444444444833333333333333333bccbbbbbbbcbbbbbbbcb33333333333333333333
                                bbbbbb1dddd33ddddddddddddddddb111bd11111111111111bbbbceeeeeeeeeeeeeeeeeeeeee88844444444444444444444488833333333333333333bcbcbbbbbbcbccbbbbbc33333333333333333333
                                bbbbbb1dddb3333ddddddddddddddb111bd11ccccccccccccccccccccccccccccccccccccccc8e88884444444444444448888e833333333333333333bbcbcbbbccccbbcbbbbbc3333333333333333333
                                bbbbbb1ddd33333ddddddddddddddb111bd1ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee84eff88888844444888888ffe4833333333333333333bbbcbcccbbbbbbcbbbbb3c333333333333333333
                                bbbbbb1ddb3333dddddddddddddddb111bd1ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444845ccfff88884448888fffcc54833333333333333333bbbbcbbbbbbbbfbccbbb3c333333333333333333
                                bbbbbb1ddbbb33dddddddddddddddb111bd1ceeccccccccccccffffffffffffffeee44444444845cccccfffe848efffccccc54833333333333333333bbbbbcbbbdddbbbbfcbb33c33333333333333333
                                bbbbbb1ddddbbddddddddddddddddb111bd1ceecccccccccccbbbfffeeeeeeeeeeee44444444845cccccccc58485cccccccc548aaaaaaaa333333333bbbbbbcbdbddddcccbbb333c3333333333333333
                                bbbbbb1ddddddd7777dddddddddddb111bd1ceecccccc66aaabbbaaaeeeeee888eee44444444845cccccccc58485cccccccc54833333333a33333333bbbbbbcbcbcbcbcbbbbb3333c333333333333333
                                bbbbbb1ddddddb7777dddddddddddb111bd1ceecccccc66aaabbbaaaeeeccc888eee44444444845cccc11cc58485cc11cccc548333dddd3a33333333bbbbbbbccbcbccbbbbbb3333c333333333333333
                                bbbbbb1ddddddb7777dddddddddddb111bd1ceeccccc666aaabbbaaaeeeccc888eee444444448455ccc11c558e855c11ccc5548333dddd3a3333333eeebbbbbbbcbcbbbbbbbb33333c33333333333333
                                bbbbbb1ddddddb7777dddddddddddb111bd1ceeccccc996333dddbbb444888666eee4444444484455cccc558e5e855cccc55448333dddd3a33333ee444eebbbbbbbbbbbbbbbb33333c33333333333333
                                bbbbbb1ddddddbbbbddddddddddddb111bd1ceecccc9996333dddbbb444888666eee4444444844445555554e555e4555555444433dddd8869196e444444debbbbbbbbbbbbbbb333333c3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecccc9966333dddbbb444888666eee44444484444448884444e5e44411144444483ddd8d3a33ec8e4444dddebbbbbbbbbbbbbb333333c3333333333333
                                bbbbbb1dddddddddddddddddddddbddddbd1ceeccc99966333dddbbb444888666eee444444848844811188b44e441111188844448ddd8d3a33ec8ce44ddd4ebbbbbbbbbbbbbb333333c3333333333333
                                bbbbbbb111111111111111111111ddddbbd1ceeccc99666333dddbbb444888666eee4444448444888666118811111168884444448ddd8d88698e8cceddd4ebbbbbbbbbbbbbbb333333c3333333333333
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd1ceecc999666333dddbbb444888666eee4444448444448866661181116684444448848888888888888ccced44ebbbbbbbbbbbbbbb3333333c333333333333
                                bbbbbbb11111111111111111111111111bd1ceec9996666333dddbbb444888666eee44aaaa84444444866666111666aaaaaaaaaaaa88688886668cecce4ebbbbbbbbbbbbbbbb3333333c333333333333
                                bbbbbb1dddddddddddddddddddddb1111bd1ceecc996666333dddbbb444888666eee4ab3333844444486666661666ab33333333333111886699168eece4ebbbbbbbbbbbbbbbb3333333c333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeab3333384488886666666666ab333333d66691119686699168eeecebbbbbbbbbbbbbbbbb3333333c333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeab33333d8444866666666666ab33333dd6d669196886699688eebeebbbbbbbbbbbbbbbbb3333333c333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeccccccccccccffffffffffffffeeeab33333d8444866666666666ab33333dd66669196866666683eebbbbbbbbbbbbbbbbbbbb3333333c333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeccc6666666666fffffffffffffeeeab33333d8444866666666666ab33333ddddd669688888888eeeeeebbbbbbbbbbbbbbbbbb333333c3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecccc66666666ffffffffffffffeeeab33333dd844488866666666ab3333eeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbb333333c3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecccc66666666feeeeeeeeeeecceeeab33333ddd84444488666666ab333eddddddddddddddd1d1111d1dddddebbbbbbbbbbbbb333333c3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeccc666999966e44444444444eceeeab33333dddd8888888888888ab333ebbbbbbbbbbbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbb333333c3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeccc699999996e44444444444eceeeab33333baaaaaaaaaaaaaaaaab3333ccccccccccccccccccccccccccccbbbbbbbbbbbbbb33333cc3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecc6999999196e44444444444eceeeab3333baadddddddddddddbbab33333dddddddddddcccc333333bbbbbbbbbbbbbbbbbbbb33333cc3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecc6999999196eeeeeeeeeeeeeceeeab3333ba333333333333333bab33333dddddddddddcccc333333bbbbbbbbbbbbbbbbbbbb3333ccc3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecc6999999996e4444eee4444eceeeab3333ba333333333333333bab33333dddddddddddccce333333bbbbbbbbbbbbbbbbbbbb3333ccc3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecc6999999996e4444eee4444eceeeab3333ba333333333333333bab33333dddddddddddccbe333333bbbbbbbbbbbbbbbbbbbb333cccc3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeccc699999966e44444e44444eceeeab33333baaaaaaaaaaaaaaaaab33333dddddddddddcbbe333333bbbbbbbbbbbbbbbbbbbb33ccccc3333333333333
                                bbbbbb1ddddddddddddddddddddddb111bd1ceeccc699999966e44444444444eceeeab3333ba33333333333333bbab33333dddddddddddebde33ccccccccccccccccccccccccccccccccccccccccccc3
                                bbbbbb1ddddddddddddddddddddddb111bd1ceecccc69999666feeeeeeeeeeecceeeab3333ba333333333333333bab33333ddddddddddebd1dec544eececee4454e54e54e54e54e54e45511554e54e5c
                                bbbbbb1dddddddddddddddddddddbddddbddceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeab3333ba333333333333333bab33333ddddddddeebbd1dbc54eececee4454e54e54e54e54e54e45511554e54e54c
                                bbbbbbb111111111111111111111ddddbbddceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeabbbbbbabbbbbbbbbbbbbbbbabbbbbbbbbbbbbebbbdd1ddcc5ececce4c4ec4ec4ec4ec4ec4ec4ec4ec4ec4ec4ecc
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeccccccccccccccccccccccccccccccccccccccccccc3
                                6666666699666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666669966666666
                                6666666666996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666996666666666
                                c66666666666999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666999966666666666c
                                bc666666666666669999996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666699999966666666666666c3
                                bbcc66666666666666666699999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666999999666666666666666666cc33
                                bbbbccc66666666666666666666699999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999666666666666666666666ccc3333
                                bbbbbbbcccc666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666cccc3333333
                                bbbbbbbbbbbcccc6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666cccc33333333333
                                bbbbbbbbbbbbbbbccccc666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666ccccc333333333333333
                                bbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbb
            """))
            time = textsprite.create(rtcModules.read_time_in_format(TimeFormat.FORMATHMS))
            time.set_max_font_height(10)
            time.set_position(80, 60)
            initialize_app = False
            app_sprites_list = [time]
        time.set_text(rtcModules.read_time_in_format(TimeFormat.FORMATHMS))
    elif selected_app == "None":
        if initialize_app:
            scene.set_background_image(assets.image("""
                myImage
            """))
            initialize_app = False
            app_sprites_list = []
    else:
        pass
game.on_update(on_on_update)

def on_update_interval():
    mySprite.say(blockMenu.selected_menu_option())
game.on_update_interval(500, on_update_interval)
