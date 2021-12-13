from tkinter import *
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
from tqdm import tqdm
import os
import easygui

class app():
    def __init__(self, master=None):

        self.clips = []
        self.caminho_arq = ""
        self.nome_musica = ""
        self.nome_saida = ""
        
        self.container1 = Frame(master)
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5.pack()

        self.musica_entry = Button(self.container3, text="Selecionar Arquivo", command=self.selecionaArq)
        self.musica_entry['width'] = 50
        self.musica_entry.pack(side=RIGHT)

        self.saida = Label(self.container2, text="Nome final da música")
        self.saida['width'] = 20
        self.saida['height'] = 3
        self.saida.pack(side=LEFT)

        self.nome_saida_entry = Entry(self.container2)
        self.nome_saida_entry['width'] = 40
        self.nome_saida_entry.pack(side=RIGHT)

        self.msg = Label(self.container5, text="")
        self.msg['width'] = 30
        self.msg['height'] = 3

        self.lets = Button(self.container4, text="Juntar")
        self.lets['command'] = self.concatenaMusica
        self.lets['width'] = 20
        self.lets.pack()


    def selecionaArq(self):
        self.nome_arq = easygui.fileopenbox()# Isto te permite selecionar um arquivo
        self.nome_musica = self.caminho_arq.split("/")[-1]
        self.nome_saida = self.nome_saida_entry.get()
  
    def concatenaMusica(self):
        for i in range(2):
            self.clip = AudioSegment.from_file(self.nome_musica, extension="mp3")
            self.clips.append(self.clip)

        self.final_clip = self.clips[0]

        for i in range(1, len(self.clips)):
            self.final_clip = self.final_clip + self.clips[i] 

        #self.final_clip.export(self.nome_saida, format="mp3")

        self.msg['text'] = "Música juntada com sucesso!"
        self.msg['fg'] = "green"
        self.msg.pack()

   
root = Tk()

root.title("Juntar Músicas")
app(root)
root.mainloop()
