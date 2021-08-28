from controller import controller
from logger import logger
from utils import utils

#Nao esquecer de levar os arquivos de config e logo para a pasta depois  de compilar

def main():
    logger.write_log("Iniciando...")
    utils.read_config()
    controller.create_window()

if __name__ == '__main__':
    main()