from time import sleep

from loguru import logger

logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")  # Configura o log para ser salvo em um arquivo

def primeira_atividade():
    logger.info("Iniciando primeira atividade.")
    sleep(2)  # Simula um atraso

def segunda_atividade():
    logger.info("Iniciando segunda atividade.")
    sleep(2)  # Simula um atraso

def terceira_atividade():
    logger.info("Iniciando terceira atividade.")
    sleep(2)  # Simula um atraso

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(10)  # Aguarda 5 segundos antes de iniciar a próxima execução do pipeline