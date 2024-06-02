import tkinter
import customtkinter
from pytube import YouTube

def start_download():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink,on_progress_callback=on_progress)
        video = ytobject.streams.get_highest_resolution()

        title.configure(text = ytobject.title,text_color = "White")
        finish_label.configure(text = "")
        video.download()

        finish_label.configure(text = "Downloaded",text_color = "Green",font=("Helvetica",20)) 
    
    except:
        finish_label.configure(text = "Download Error!",text_color = "red",font=("Helvetica",20))
    

def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size-bytes_remaining
    percentage_of_completion = (bytes_downloaded/total_size)*100
    per = str(int(percentage_of_completion))

    percentage.configure(text = per+"%")
    percentage.update()

    #Update Progress Bar
    progress_bar.set(float(percentage_of_completion/1000))

#System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI elements
title = customtkinter.CTkLabel(app,text="Insert a Youtube link")
title.pack(padx = 10,pady = 10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350,height=40, textvariable=url_var)
link.pack()

#Finished downloading
finish_label = customtkinter.CTkLabel(app,text="",font=("Helvetica",20))
finish_label.pack(pady = 10)

#Progress percentage
percentage = customtkinter.CTkLabel(app,text="0%",font=("Helvetica",20))
percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app,width=400)
progress_bar.set(0.0)
progress_bar.pack(padx = 10, pady = 10)

#Download Button
download = customtkinter.CTkButton(app,text="Download",command=start_download)
download.pack(pady = 30)



#Run app
app.mainloop()
