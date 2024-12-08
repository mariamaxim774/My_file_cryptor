import fileinput
import os
import os.path
import sys
import hashlib
import urllib.parse


class FileHandler:
    def __init__(self,filename):
        self.filename=filename

    def is_file(self):
        path_to_file = self.search_file()
        if path_to_file and os.path.isfile(path_to_file):
            return True
        else:
            return False
    def search_file(self):
        for root,directories,files in os.walk("C:\\Users\\User\\Desktop\\Python\\github\\Python2024\\myFileCryptor"):
            if self.filename in files:
                self.file_path=os.path.join(root,self.filename)
                return os.path.join(root,self.filename)
        else:
            return None

class FileCryptor:

    def __init__(self,filename,password):
        self.filename=filename
        self.password=password

    def crypt(self):
        out_file = f"{self.filename}.crypted"
        file_hash = self.compute_hash(self.filename)

        with open(self.filename, 'rb') as input_file, open(out_file, 'wb') as output_file:
            output_file.write(file_hash)  
        
            encrypted_data = bytearray()
            for index, byte in enumerate(input_file.read()):
                password_offset = index % len(self.password)
                key = ord(self.password[password_offset])
                encrypted_byte = (byte + key) % 256
                encrypted_data.append(encrypted_byte)

            output_file.write(encrypted_data)
            print(f"Fisier criptat: {out_file}")

    def decrypt(self):
        real_file = self.filename.replace('.crypted', '')

        with open(self.filename, 'rb') as crypted_file, open(real_file, 'wb') as output_file:
            file_hash = crypted_file.read(32)
            print(f"Hash citit din fisier: {file_hash.hex()}")

            encrypted_data = crypted_file.read()

            decrypted_data = bytearray()
            for index, byte in enumerate(encrypted_data):
                password_offset = index % len(self.password)
                key = ord(self.password[password_offset])
                decrypted_byte = (byte - key) % 256
                decrypted_data.append(decrypted_byte)

            output_file.write(decrypted_data)
            print(f"Fisier decriptat: {real_file}")


        calculated_hash = self.compute_hash(real_file)
        print(f"Hash calculat: {calculated_hash.hex()}")  

        if file_hash != calculated_hash:
            print('Parola pe care ati introdus-o nu este corecta')
            os.remove(real_file)
        else:
            print('Parola este corecta, fisierul a fost decriptat.')

    def compute_hash(self,filename):
       hash = hashlib.sha256()
       with open(filename, "rb") as file:  #
           data = file.read()
           hash.update(data)
       return hash.digest()

def main():
    if len(sys.argv)!=4:
        print('Trebuie sa apelezi scriptul astfel: python main.py <crypt>/<decrypt> filename password')
        sys.exit(1)

    command = sys.argv[1]
    file=sys.argv[2]
    password=sys.argv[3]


    fileHandler=FileHandler(file)
    if not fileHandler.is_file():
        print('Fisierul nu exista, dati un fisier valid')
        sys.exit(1)
    else:
        cryptor = FileCryptor(file,password)
        if command=='crypt':
            cryptor.crypt()
        elif command=='decrypt':
            cryptor.decrypt()
        else:
            print('Singurele comenzi ce pot fi apelate sunt <crypt> si <decrypt>')

if __name__ == '__main__':
    main()

