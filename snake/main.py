from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randrange
from kivy.core.window import Window
from kivy.graphics import *

speed = 2

class Snake(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Snake, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
            
        if keycode[1] == 'left' :
            self.velocity_x = -1
            self.velocity_y = 0
        if keycode[1] == 'right':
            self.velocity_x = 1
            self.velocity_y = 0
        if keycode[1] == 'up':
            self.velocity_x = 0
            self.velocity_y = 1
        if keycode[1] == 'down':
            self.velocity_x = 0
            self.velocity_y = -1
    
    def move(self):
        self.x += self.width * self.velocity_x
        self.y += self.width * self.velocity_y

class Fruit(Widget):
    def throw_fruit(self):
        self.x = randrange(0,Window.width, 1/20 * Window.width)
        self.y = randrange(0,Window.height, 1/20 * Window.height)
    

class Game(Widget):
    snake = ObjectProperty(None)
    fruit = ObjectProperty(None)

    def on_board(self, dt):
        #snake out of board
        if self.snake.x >= Window.width:
            self.snake.x = 0
        elif self.snake.x < 0:
            self.snake.x = Window.width - self.snake.width
        elif self.snake.y >= Window.height:
            self.snake.y = 0
        elif self.snake.y < 0:
            self.snake.y = Window.height - self.snake.height

        #if snake eat fruit, fruit change position
        if self.fruit.pos == self.snake.pos:
            self.fruit.throw_fruit()
            global speed
            speed += 100

    def update(self, dt):
        self.snake.move()

        
    

class SnakeApp(App):

    def build(self):
        game = Game()
        game.fruit.throw_fruit()
        Clock.schedule_interval(game.on_board, 1.0/60.0)
        global speed
        Clock.schedule_interval(game.update, 1.0/speed)
        return game

if __name__ == '__main__':
    Window.size = (500, 500)
    SnakeApp().run()