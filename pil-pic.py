import io
# allows for image formats other than gif
from PIL import Image, ImageTk
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
 
root = tk.Tk()

root.overrideredirect(True)

url = "http://pics.sc.chinaz.com/Files/pic/faces/4083/17.gif"
 
image_bytes = urlopen(url).read()

data_stream = io.BytesIO(image_bytes)

pil_image = Image.open(data_stream)

im = pil_image.size 

w, h = pil_image.size

root.geometry(str(w)+"x"+str(h)+"+300+100")

fname = url.split('/')[-1]
sf = "{} ({}x{})".format(fname, w, h)
root.title(sf)
 

tk_image = ImageTk.PhotoImage(pil_image)
 

label = tk.Label(root, borderwidth=0, image=tk_image, bg='brown')
label.pack()
 
root.mainloop()
