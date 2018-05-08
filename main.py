# Imports the Google Cloud client library and streaming libraries
import io
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

from google.cloud import vision
from google.cloud.vision import types


# Consumes google.api.vision
def func():
    # The name of the image file to annotate
    file_path = filedialog.askopenfilename()
    # set enviromental variable to the API credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cred.json"
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    bandera = False
    print('Labels:')
    for label in labels:
        if label.description == "toddler" or label.description == "child" or label.description == "kid" or\
                        label.description == "infant":
            bandera = True
    if bandera == False:
        messagebox.showinfo("Safe Area", "No Children in the danger zone")
    else:
        messagebox.showinfo("Danger", "Beware! There are children in the danger zone")


# deploy GUI
root = tk.Tk()
root.title('Safe Child App')
root.geometry("250x300")
# Create 2 frames for interface
leftFrame = Frame(root)
leftFrame.pack(side=LEFT, padx=5, pady=20)
#Create widgets for 1st frame
label1 = Label(leftFrame,text="Keeping your children safe since 2018")
label1.pack(side=TOP)
label2 = Label(leftFrame,text="Select the image you want to verify")
label2.pack(side=TOP)
buttonSeek = Button(leftFrame, text="Check picture", fg="Blue", command=lambda : func())
buttonSeek.pack(side=LEFT)


root.mainloop()



