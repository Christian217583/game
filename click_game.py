character = Actor('cat1')
character.topright = 0, 10

WITDTH = 500
HEIGHT = character.height + 96

def draw():
    screen.clear()
    character.draw()

def update():
    character.left = character.left + 2
    if character.left > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

def on_mouse_down(pos, button):
    if button == mouse.LEFT and character.collidepoint(pos):
        print("Eek!")

