import pyglet
import glooey

pyglet.resource.path.append('resources/imgs/menu')
pyglet.resource.path.append('resources/imgs/player')
pyglet.resource.reindex()


left = 'form_left.png'
right = 'form_right.png'
center = 'form_center.png'


class NamePrompt(glooey.Label):
    custom_text = "What is your name?"
    custom_alignment = 'center'


class NameForm(glooey.Form):
    custom_alignment = 'top'


    class Label(glooey.EditableLabel):
        custom_font_name = 'Times New Roman'
        custom_font_size = 10
        custom_color = '#ff00ff'
        custom_alignment = 'top left'
        custom_horz_padding = 5
        custom_top_padding = 5
        custom_width_hint = 200

    class Base(glooey.Background):
        custom_center = pyglet.resource.texture(center)
        custom_left = pyglet.resource.texture(left)
        custom_right = pyglet.resource.texture(right)


    def __init__(self):
        super().__init__()
        self.name = None

    def on_unfocus(self):
        self.name = self.get_text()


class Boy(glooey.Button):
    class Background(glooey.Image):
        custom_image = pyglet.resource.texture('boy Idle (1).png')


class Girl(glooey.Button):
    class Background(glooey.Image):
        custom_image = pyglet.resource.texture('girl Idle (1).png')


def make_gui(window: pyglet.window.Window) -> glooey.Gui:
    gui = glooey.Gui(window)
    screen = glooey.VBox()
    bottom = glooey.HBox()

    boy = Boy()
    girl = Girl()

    bottom.add(boy)
    bottom.add(girl)

    screen.add(NamePrompt(), size=0)
    screen.add(NameForm(), size=0)
    screen.add(bottom, size='expand')
    gui.add(screen)

    return gui
