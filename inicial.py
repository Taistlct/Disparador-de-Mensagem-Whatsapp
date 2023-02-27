import tkinter as tk
import webbrowser
import os


root = tk.Tk()
root.title("WhatsApp Bot")
root.geometry("788x600")
root.resizable(False, False)
fonte = ("Helvetica", 20)
fonte_butom = ("Arial", 20)
fonte_butom1 = ("Arial", 15)

# Cria label "Digite sua mensagem aqui:"
label = tk.Label(root, text="Mensagem:", font=fonte)
label.grid(row=0, column=0, padx=10, pady=10)

# Cria campo de texto
input_text = tk.Text(root, height=20, width=95)
input_text.grid(row=1, column=0, padx=10, pady=10)

# Função para imprimir o texto no terminal
def enviar_mensagem():
    global mensagem
    mensagem = input_text.get("1.0", "end-1c")
    

# Cria botão "Enviar"
enviar_button = tk.Button(root, text="Inserir Mensagem", command=enviar_mensagem, font=fonte_butom1)
enviar_button.grid(pady=10)

# Cria frame para os botões
button_frame = tk.Frame(root)
button_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Cria botão "Editar Planilha"
def open_excel():
    os.system('start Enviar.xlsx')

edit_button = tk.Button(button_frame, text="Editar Planilha", command=open_excel,  bg='#f03a7f', fg='#ffffff', font=fonte_butom )
edit_button.grid(row=0, column=0, padx=10, pady=20)



# Cria botão "Iniciar WhatsApp"
def start_whatsapp():
    global mensagem
    print(mensagem)
    import bootwpp
    if __name__ == '__main__':
        bootwpp.roadr(mensagem)
        

whatsapp_button = tk.Button(button_frame, text="Iniciar WhatsApp", command=start_whatsapp,  bg='#46f084', fg='#ffffff', font=fonte_butom )
whatsapp_button.grid(row=0, column=1, padx=10, pady=20)


root.mainloop()
