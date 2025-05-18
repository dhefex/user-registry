import customtkinter as ctk 
import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
  host="localhost",
  user="dhefex",
  password="ZW@1proc",
  database="cadastro",
  charset='utf8mb4',
  collation='utf8mb4_general_ci'

)

cursor = conexao.cursor()
print("Conexão feita com sucesso!")



# Função para cadastrar 
def cadastrar():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    sexo = sexo_entry.get()
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    nacionalidade = nacionalidade_entry.get()


    sql = "INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade) VALUES (%s, %s, %s,%s,%s,%s)"
    valores = (nome,idade, sexo, peso, altura, nacionalidade)


    cursor.execute(sql, valores)
    conexao.commit()

    status_label.configure(text="Cadastro realizado com sucesso!")

# Interface com customtkinter
ctk.set_appearance_mode("blue")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cadastro de pessoas")
app.geometry("400x400")

# Campo de entrada 
nome_entry = ctk.CTkEntry(app, placeholder_text="Nome")
nome_entry.pack(pady=5)

idade_entry = ctk.CTkEntry(app, placeholder_text="Idade ")
idade_entry.pack(pady=5)

sexo_entry = ctk.CTkEntry(app, placeholder_text="Sexo(M/F)")
sexo_entry.pack(pady=5)

peso_entry = ctk.CTkEntry(app, placeholder_text="Peso(kg)")
peso_entry.pack(pady=5)

altura_entry = ctk.CTkEntry(app, placeholder_text="Altura(m) ")
altura_entry.pack(pady=5)

nacionalidade_entry = ctk.CTkEntry(app, placeholder_text="Nacionalidade")
nacionalidade_entry.pack(pady=5)

# Botão de cadastro
cadastrar_btn = ctk.CTkButton(app, text="Cadastrar", command=cadastrar)
cadastrar_btn.pack(pady=10)

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)


app.mainloop()

# Fecha a conexão 
cursor.close()
conexao.close()






    

