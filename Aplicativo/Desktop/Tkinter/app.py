import tkinter as tk
from tkinter import messagebox,filedialog

from  build.lib.pacote.backEnd import loadModel, useModel


class App:
    def __init__(self, largura, altura, x,y):
        self.root = tk.Tk()
        self.root.title("Aplicativo")

        self.button_font = ("Arial", "20","bold")
        self.label_font = ("Arial", "30","bold")

        self.path_img = ''

        self.borda = 20
        self.stiloBorda = 'ridge'
        """
        "flat": Sem borda, plano.
        "raised": Borda elevada, dá a aparência de um botão pressionado.
        "sunken": Borda afundada, dá a aparência de um botão levantado.
        "ridge": Borda em relevo, cria um efeito tridimensional.
        "groove": Borda em sulco, também cria um efeito tridimensional.
        """
        
        
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

        self.current_frame = None
        
        self.open_screen1()
        
        self.root.mainloop()
    
    def open_screen1(self):

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        

        verify_button = tk.Button(self.current_frame, text="VERIFICAR FAMACHA", command=self.open_screen2, width=120,height=12, font=self.button_font, bg="black", fg="white", bd=self.borda, relief=self.stiloBorda)
        verify_button.pack()
        verify_button.bind("<Enter>", self.change_cursor)   # Quando o mouse entra no botão
        verify_button.bind("<Leave>", self.restore_cursor)  # Quando o mouse sai do botão

        quit_button = tk.Button(self.current_frame, text="SAIR", command=self.root.quit, width=120,height=12, font=self.button_font, bg="black", fg="white", bd=self.borda, relief=self.stiloBorda)
        quit_button.pack()
        quit_button.bind("<Enter>", self.change_cursor)
        quit_button.bind("<Leave>", self.restore_cursor)

    def open_screen2(self):

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)

        self.current_frame.pack()



        navegation_button = tk.Button(self.current_frame, text="BUSCAR IMAGEM", command=self.abrir_arquivo, width=120,height=12, font=self.button_font, bg="black", fg="white", bd=self.borda, relief=self.stiloBorda)
        navegation_button.pack()
        navegation_button.bind("<Enter>", self.change_cursor)
        navegation_button.bind("<Leave>", self.restore_cursor)



        back_button = tk.Button(self.current_frame, text="VOLTAR", command=self.open_screen1,width=120,height=12, font=self.button_font, bg="black", fg="white", bd=self.borda, relief=self.stiloBorda)
        back_button.pack()
        back_button.bind("<Enter>", self.change_cursor)
        back_button.bind("<Leave>", self.restore_cursor)


    def open_screen3(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        model = loadModel("Modelo.pkl")
        retorno = useModel(model,self.path_img)
        
        result = ''
        color = ''

        if retorno[0]:

            if retorno[1]:
                result = 'Precisa de Vermifugação'
                color = 'red'
            else:
               result = "Não precisa de Vermifugação"
               color = 'green'
        
        else:
            result = 'Informações invalidas foram fornecidas'

        result_label = tk.Label(self.current_frame, text=result.upper())
        
        result_label.config(width=120,height=12, font=self.label_font, bg="black", fg=color)
        result_label.pack()

        back_button = tk.Button(self.current_frame, text="VOLTAR AO INÍCIO", command=self.open_screen1,width=120,height=12, font=self.button_font, bg="black", fg="white", bd=self.borda, relief=self.stiloBorda)
        back_button.pack()
        back_button.bind("<Enter>", self.change_cursor)
        back_button.bind("<Leave>", self.restore_cursor)



    def abrir_arquivo(self):

        arquivo = filedialog.askopenfilename()
        
        self.path_img = arquivo
        
        if len(self.path_img) > 0:

            if ('.JPG' in self.path_img or '.jpg' in self.path_img):
                self.open_screen3()
            else:
                messagebox.showinfo("ATENÇÃO!", "ARQUIVO INVALIDO!\nSELECIONE UMA IMAGEM .JPG")

    def change_cursor(self,event):
        event.widget.config(cursor="hand2")  # Define o cursor para 'hand2' (mãozinha)

    def restore_cursor(self,event):
        event.widget.config(cursor="")  # Restaura o cursor padrão
        

#app = App(800,600,300,0)
app = App(1280,720,200,0)
#teste essa img -> imagens/0122_2.JPG

"""
Adicionar imagens

from tkinter import Tk, Button
from PIL import Image, ImageTk

root = Tk()

# Carrega uma imagem de botão com bordas arredondadas
image = Image.open("rounded_button.png")
photo = ImageTk.PhotoImage(image)

button = Button(root, image=photo)
button.pack()

root.mainloop()

"""