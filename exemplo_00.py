from time import sleep

def primeira_atividade():
    print("Esta é a primeira atividade.")
    sleep(2)  # Simula um atraso

def segunda_atividade():
    print("Esta é a segunda atividade.")
    sleep(2)  # Simula um atraso

def terceira_atividade():
    print("Esta é a terceira atividade.")
    sleep(2)  # Simula um atraso

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print("Pipeline concluído com sucesso!")    

if __name__ == "__main__":
    pipeline()