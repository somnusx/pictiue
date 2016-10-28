import os
import time
import random
import pyglet
import webbrowser
from urllib import request, parse


ur = "http://n.njcit.cn/index.php/index/login"
data={"username":"7PPPPPP","domain":"studentphone","password":"MTU0ODcyNzYzMw==","enablemacauth":"0"}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(ur, data=data)
page = request.urlopen(req).read()


urls = []

for i in range(0,11):
     urls.append('http://pics.sc.chinaz.com/Files/pic/faces/4083/0{}.gif'.format(i))


for i in range(10,47):
     urls.append('http://pics.sc.chinaz.com/Files/pic/faces/4083/{}.gif'.format(i))


for i in range(0,9):
     urls.append('http://pics.sc.chinaz.com/Files/pic/faces/3866/0{}.gif'.format(i))

for i in range(0,8):
     urls.append('http://pics.sc.chinaz.com/Files/pic/faces/3953/0{}.gif'.format(i))


url = random.choice(urls)

da = request.urlopen(url).read()

with open('in.gif','wb') as code:
    code.write(da)

ag_file = 'in.gif'

animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

win = pyglet.window.Window(width=sprite.width, height=sprite.height)

green = 0, 1, 0, 1
pyglet.gl.glClearColor(*green)

@win.event
def on_draw():
    win.clear()
    sprite.draw()

pyglet.app.run()
os.remove('in.gif')
webbrowser.open('http://n.njcit.cn/')
