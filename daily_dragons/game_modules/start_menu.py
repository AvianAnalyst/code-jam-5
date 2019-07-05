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

    def on_unfocus(self, text):
        self.name = text


class Boy(glooey.Button):
    class Background(glooey.Image):
        custom_image = pyglet.resource.texture('boy Idle (1).png')


class Girl(glooey.Button):
    class Background(glooey.Image):
        custom_image = pyglet.resource.texture('girl Idle (1).png')


class StartMenu(glooey.Gui):
    def __init__(self, window):
        self.gui = super().__init__(window)

        self.screen = glooey.VBox()
        self.bottom = glooey.HBox()

        self.boy = Boy()
        self.girl = Girl()

        self.bottom.add(self.boy)
        self.bottom.add(self.girl)

        self.name_field = NameForm()

        self.screen.add(NamePrompt(), size=0)
        self.screen.add(self.name_field, size=0)
        self.screen.add(self.bottom, size='expand')

        self.gui.add(self.screen)
