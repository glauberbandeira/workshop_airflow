# pip install streamlit pandas

import io
import streamlit as st
import pandas as pd
import subprocess

#Funcao para carregar os dados do arquivo CSV
def carregar_dados():
    with open("execution_logs.log", "rb") as arquivo:
        linhas = arquivo.readlines()

    linhas_decodificadas = []
    for linha in linhas:
        try:
            linhas_decodificadas.append(linha.decode("utf-8-sig"))
        except UnicodeDecodeError:
            linhas_decodificadas.append(linha.decode("cp1252"))

    df = pd.read_csv(
        io.StringIO("".join(linhas_decodificadas)),
        sep=" - ",
        header=None,
        names=["Time", "Message"],
    )
    return df

# Funcao para executar o script python
def executar_script():
    subprocess.Popen(["python", "frontend/pipeline/minha_etl.py"])

# Layout do Streamlit
def main():
    st.title("Monitoramento de Logs do Pipeline")
    st.image("pics/airflowlogo.png", width=200)

    # carregar os dados do arquivo CSV
    df = carregar_dados()

    #exibir os dados na interface do Streamlit
    st.write("### Logs de Execução", df)

    # Botão para executar o script
    if st.button("Atualizar Pipeline"):
        df = carregar_dados()  # Recarregar os dados antes de executar o script
        st.write("Dados atualizados:", df)

if __name__ == "__main__":
    main()