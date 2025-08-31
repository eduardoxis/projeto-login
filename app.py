import customtkinter as ctk

#config aparencia
ctk.set_appearance_mode("dark")

# cricao das funcoes de funcionalidade
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # verificar se o user e dudu e a password e 1234
    if usuario == "dudu" and senha =="1234":
        resultado_login.configure(text="Login bem sucedido!", text_color="green")
    else:
        resultado_login.configure(text="Login Invalido!", text_color="red")  
    

#criacao da janela principal
app = ctk.CTk()

app.title("Sistema de Login")
app.geometry("400x300")

# criacao dos campos 

#label usuario
label_usuario = ctk.CTkLabel(app, text="Usuario:")
label_usuario.pack(pady=10)
    
#entrada usuario
campo_usuario =ctk.CTkEntry(app, placeholder_text="Digite seu usuario")
campo_usuario.pack(pady=10)

#label senha
label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)

#entrada senha
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=10)

#botao login
botao_login = ctk.CTkButton(app, text="Login",command=validar_login)
botao_login.pack(pady=10)

#campo feedback de login
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

 




# iniciacao da aplicacao
app.mainloop()
