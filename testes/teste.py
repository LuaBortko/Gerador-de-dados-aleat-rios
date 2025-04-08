import csv



dictionary ={'id': "12346", 'name': "Brandon", 'dept_name': 'Accounting', 'salary': "100000"} #usar exatamente o nome da coluna no banco de dados



import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    ) #dados para conseguir conectar com o banco de dados (usar arquivo .env)
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)
    tabela = "instructor" #tabela na qual as informações serão inseridas
    query = "INSERT INTO " + tabela + "("  #começo da query
    query1 = "" #query com todas as colunas
    query2 = "" #query com todos os valores que serão inseridos
    for chave, valor in dictionary.items(): #navegar pelo dicionario para adicionar os nomes e valores à query
        query1+=   chave + "," #string das colunas exemplo: nome,id,departamento,RA,
        query2+= "'" + valor + "'" + "," #string dos valores | exemplo: jeremias,1234,robotica,24.123.035-8
    query1 = query1.rstrip(",") # tira a última vírgula da string | exemplo: ANTES: nome,id,departamento,RA,  DEPOIS: nome,id,departamento,RA
    query2 = query2.rstrip(",") #mesma coisa do comentário acima(linha 48)

    print(query1) #imprimir cada parte da query para ver como está 
    print(query2)
    query+= query1 + ") VALUES ("  #final da parte INSERT INTO tabela(coluna1,coluna2,coluna3) e começo da inserção dos valores
    query+= query2 + ")" #inserção dos valores na query e fechamento de parenteses do VALUES()
    print(query) #imprimir query completa para checar

    

    cursor.execute(query) #execução da query para inserir no banco de dados 
    cursor.execute("commit") # confirmação da alteração no banco de dados 
    # Close the cursor and connection
    cursor.close()
    connection.close() #fim da conexão com o banco de dados 
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")



