import tkinter as tk
from tkinter import messagebox,filedialog

from  build.lib.pacote.backEnd import loadModel, useModel


class App:
    def __init__(self, largura, altura, x,y):
        self.root = tk.Tk()
        self.root.title("Aplicativo")

        self.button_font = ("Arial", "20","bold")

        self.path_img = ''
        
        
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

        self.current_frame = None
        
        self.open_screen1()
        
        self.root.mainloop()
    
    def open_screen1(self):

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        

        verify_button = tk.Button(self.current_frame, text="VERIFICAR FAMACHA", command=self.open_screen2, width=120,height=10, font=self.button_font, bg="black", fg="white")
        verify_button.pack()

        quit_button = tk.Button(self.current_frame, text="SAIR", command=self.root.quit, width=120,height=10, font=self.button_font, bg="black", fg="white")
        quit_button.pack()

    def open_screen2(self):
        """
        Tela responsavel pela coleta do diretorio e nome da imagem
        permite buscar a imagem ou voltar a tela inicial
        """
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)

        self.current_frame.pack()

        
        """
        #barra de busca
        self.navigation_bar = tk.Entry(self.current_frame, font=self.button_font,borderwidth=5)
        #ajustando ela no canto esquerdo superior (n funcionou)
        #self.navigation_bar.pack(side='top', padx=100)
        #self.navigation_bar.config(justify='left')
        self.navigation_bar.pack()
        """

        #botão para navegar no sistema
        navegation_button = tk.Button(self.current_frame, text="BUSCAR IMAGEM", command=self.abrir_arquivo, width=120,height=10, font=self.button_font, bg="black", fg="white")
        navegation_button.pack()

        """
        confirm_button = tk.Button(self.current_frame, text="AVANÇAR", command=self.readLabel, width=120,height=6, font=self.button_font, bg="black", fg="white")
        confirm_button.pack()
        """


        back_button = tk.Button(self.current_frame, text="VOLTAR", command=self.open_screen1,width=120,height=10, font=self.button_font, bg="black", fg="white")
        back_button.pack()
    """
    def open_screen3(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()
        
        #se a imagem existe
        color = 'black'
        result = ''
        if os.path.exists(self.path_img):
            result = 'Imagem Encontrada!'
            color = 'green'
        else:
            result = 'Imagem Não Encontrada!'
            color = 'red'

        label = tk.Label(self.current_frame, text=result)
        label.config(width=120,height=5, font=self.button_font, bg=color, fg="white")
        label.pack()

        continue_button = tk.Button(self.current_frame, text="CONTINUAR TESTE", command=self.open_screen4, width=120,height=5, font=self.button_font, bg="black", fg="white")
        continue_button.pack()

        search_another_button = tk.Button(self.current_frame, text="Procurar outra imagem", command=self.open_screen2,width=120,height=5, font=self.button_font, bg="black", fg="white")
        search_another_button.pack()

        back_button = tk.Button(self.current_frame, text="Voltar ao início", command=self.open_screen1, width=120,height=10, font=self.button_font, bg="black", fg="white")
        back_button.pack()
    """
    def open_screen3(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        model = loadModel("Modelo.pkl")
        retorno = useModel(model,self.path_img)
        
        result = ''
        if retorno[0]:
            if retorno[1]:
                result = 'Precisa de Vermifugação'
            else:
                result = "Não precisa de Vermifugação"
        else:
            result = 'Informações invalidas foram fornecidas'

        result_label = tk.Label(self.current_frame, text=result.upper())
        result_label.config(width=120,height=10, font=self.button_font, bg="black", fg="white")
        result_label.pack()

        back_button = tk.Button(self.current_frame, text="VOLTAR AO INÍCIO", command=self.open_screen1,width=120,height=10, font=self.button_font, bg="black", fg="white")
        back_button.pack()



############################################### FUNÇÕES PARA A INTERFACE GRÁFICA ###################### 
    
    #fuções da tela 2
    """
    def readLabel(self):
        
        self.path_img = self.navigation_bar.get()
        if self.path_img != '':
            print(self.path_img)
            self.open_screen3()
        else:
            messagebox.showinfo("ATENÇÃO!", "PREENCHA A CAIXA DE TEXTO!")
    """
    def abrir_arquivo(self):
        arquivo = filedialog.askopenfilename()
        
        self.path_img = arquivo
        
        if len(self.path_img) > 0:
            if ('.JPG' in self.path_img or '.jpg' in self.path_img):
                self.open_screen3()
            else:
                messagebox.showinfo("ATENÇÃO!", "ARQUIVO INVALIDO!\nSELECIONE UMA IMAGEM .JPG")
        

app = App(800,600,300,0)
#teste essa img -> imagens/0122_2.JPG
