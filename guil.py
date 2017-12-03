import tkinter as tk
import time
import os          # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from clarifai import rest
from clarifai.rest import ClarifaiApp
import json
fp = open("Hello.txt","w")
from clarifai.rest import Image as ClImage
def mlh1():
    flag=0
    app = ClarifaiApp(api_key='cbd91ed9a3524abbb448f515d453517f')

    model = app.models.get("general-v1.3")
    hello = ClImage(file_obj=open('/home/santosh/Chegg/Human_Activity_Monitoring/PAMAP2_Dataset/Protocol/hello1.jpg', 'rb'))
    hello=model.predict([hello])
    hello = json.dumps(hello)
    hello1 = json.loads(hello)
    fp.write('hello1')
    fp.close()
    string = ['happy','joy','worried','fun','serious']
    #print(hello1['status'])
    for i in hello1['outputs'][0]['data']['concepts']:
        for j in string :
            if(i['name']==j) :

                fp.write(i['name'])
                fp.write(i['value'])
                flag=1;
                break
        if(flag==1) :
            break
def mlh2():
    flag=0
    app = ClarifaiApp(api_key='cbd91ed9a3524abbb448f515d453517f')

    model = app.models.get("general-v1.3")
    hello = ClImage(file_obj=open('/home/santosh/Chegg/Human_Activity_Monitoring/PAMAP2_Dataset/Protocol/hello2.jpg', 'rb'))
    hello=model.predict([hello])
    hello = json.dumps(hello)
    hello1 = json.loads(hello)
    #print(hello1)
    string = ['happy','joy','worried','fun','serious']
    #print(hello1['status'])
    for i in hello1['outputs'][0]['data']['concepts']:
        for j in string :
            if(i['name']==j) :

                print(i['name'])
                print(i['value'])
                flag=1;
                break
        if(flag==1) :
            break


def webcam() :
   os.system("fswebcam -r 640x480 --jpeg 85 -D 1 hello1.jpg --save /home/santosh/Chegg/Human_Activity_Monitoring/PAMAP2_Dataset/Protocol/hello1.jpg ")
def webcam2() :
     os.system("fswebcam -r 640x480 --jpeg 85 -D 1 hello2.jpg --save /home/santosh/Chegg/Human_Activity_Monitoring/PAMAP2_Dataset/Protocol/hello2.jpg ")
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="This is the start page", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)

            button1 = tk.Button(self, text="Go to Page One",
                                command=lambda:controller.show_frame("PageOne")&webcam()&mlh1())
            button2 = tk.Button(self, text="Go to Page Two",
                                command=lambda: controller.show_frame("PageTwo")&webcam())
            button3 = tk.Button(self, text="Go to Page three",
                                command=lambda: controller.show_frame("PageThree")&webcam())
            button4 = tk.Button(self, text="Go to Page 4",
                                command=lambda: controller.show_frame("PageFour")&webcam())
            button5 = tk.Button(self, text="Go to Page 5",
                                command=lambda: controller.show_frame("PageFive")&webcam())
            button1.pack()
            button2.pack()
            button3.pack()
            button4.pack()
            button5.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage")&webcam2()&mlh2())
        button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage")&webcam2())
        button.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage")&webcam2())
        button.pack()


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage")&webcam2())
        button.pack()


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question 5", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage")&webcam())
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
