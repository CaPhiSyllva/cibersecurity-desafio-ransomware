import os
import pyaes

def decrypt_file(file_name, key):
    try:
        # Verificar se o arquivo criptografado existe
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"Arquivo {file_name} não encontrado.")

        # Ler os dados do arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Configurar a descriptografia AES
        aes = pyaes.AESModeOfOperationCTR(key)

        # Descriptografar os dados do arquivo
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar um novo arquivo com os dados descriptografados
        new_file_name = file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado criado: {new_file_name}")
    except Exception as e:
        print(f"Ocorreu um erro durante a descriptografia: {e}")

if __name__ == "__main__":
    # Definir a chave para a descriptografia
    key = b"testeransomwares"

    # Nome do arquivo a ser descriptografado
    file_name = "teste.txt.ransomwaretroll"

    # Chamar a função de descriptografia
    decrypt_file(file_name, key)
