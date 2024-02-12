from ursina import *
import cefpanda

app=Ursina(borderless=False,development_mode=False,title="SineWave")
app.ui = cefpanda.CEFPanda(
            transparent=False,
            size=[-0.75, 0.75, -0.75, 0.75],
        )
app.ui.node().set_scale(0.9)
app.ui.node().set_pos(0.05, 0.0, -0.1)
app.ui.load_url('www.google.com')
def title_window(title_,color_=color.black):
    Text(title_, y=.5, x=-.886, color=color_)
Text("SineWave", y=.497, x=-.883, color=color._80)#Shader of Title
title_window("SineWave",color.hex("90ee90"))#Title
url=InputField(y=.45,default_value="SineWave - Enter URL")
Button(text="Open",scale=.1,y=.45,x=.3,on_click=lambda:app.ui.load_url(url.text))
Text(y=-.45,x=-.1,text="Works with Chromium")
sine_wave_logo=Entity(model="quad",texture="SineWave",position=(4.48,3.3),scale=(1.76,1.00))
bookmarks=[]
def add_to_bookmarks(url):
    bookmarks.append(url)
    bookmarks_text.text="".join(bookmarks)

Text(text="Bookmarks",y=.4,x=-.886,color=color.light_gray)
Button(text="Show Code",scale=(.25,.1),x=.77,y=.15,on_click=lambda:app.ui.load_url("view-source://"+app.ui.browser.GetUrl().replace("https://","").replace("http://","")))
Button(text="Reload",scale=(.25,.1),x=.77,y=0,on_click=lambda:app.ui.load_url(app.ui.browser.GetUrl()))
Button(text="Add to Bookmarks",scale=(.25,.1),x=.77,y=-.15,on_click=lambda:add_to_bookmarks(app.ui.browser.GetUrl()+str("\n")))
bookmarks_text=Text(text=bookmarks,x=-.886,y=.375,color=color.white)
def update():
    sine_wave_logo.rotation_x+=1
    sine_wave_logo.rotation_y+=1
    sine_wave_logo.rotation_z+=1
app.run()
