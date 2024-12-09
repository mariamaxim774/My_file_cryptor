import os
import sys
import hashlib


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
        for root,directories,files in os.walk("C:\\Users\\User\\Desktop"):
            if self.filename in files:
                self.file_path=os.path.join(root,self.filename)
                return os.path.join(root,self.filename)
        else:
            return None

class FileCryptor:

    def __init__(self,file_path,password):
        self.file_path=file_path
        self.password=password

    def crypt(self):
        out_file = f"{self.file_path}.crypted"
        file_hash = self.compute_hash(self.file_path,is_file=True)

        with open(self.file_path, 'rb') as file_to_encrypt, open(out_file, 'wb') as encrypted_file:
            encrypted_file.write(file_hash)


            encrypted_data = bytearray()
            for index, byte in enumerate(file_to_encrypt.read()):
                password_offset = index % len(self.password)
                key = ord(self.password[password_offset])
                encrypted_byte = (byte + key) % 256
                encrypted_data.append(encrypted_byte)

            encrypted_file.write(encrypted_data)

            print(f"Fisierul criptat este : {out_file}")


    def decrypt(self):

        out_file = self.file_path.replace('.crypted', '')
        with open(self.file_path, 'rb') as encrypted_file, open(out_file, 'wb') as decrypted_file:
            file_hash = encrypted_file.read(32)
            encrypted_data = encrypted_file.read()
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
             print('Parola pe care ati introdus-o nu este corecta! Incercati din nou!')
        else:
            print('Parola este corecta, fisierul a fost decriptat.')
            decrypted_file.write(decrypted_data)



    def compute_hash(self,data_to_hash,is_file=False):
       hash = hashlib.sha256()
       if is_file:
           with open(data_to_hash, "rb") as file:  #
               data = file.read()
               hash.update(data)
       else:
           hash.update(data_to_hash)
       return hash.digest()

def main():
    if len(sys.argv)!=4:
        print('Trebuie sa apelezi scriptul astfel: python main.py crypt/decrypt nume_fisier parola')
        sys.exit(1)

    command = sys.argv[1]
    file=sys.argv[2]
    password=sys.argv[3]


    fileHandler=FileHandler(file)
    if not fileHandler.is_file():
        print('Fisierul nu exista, dati un fisier valid')
        sys.exit(1)
    else:
        file_path=fileHandler.search_file()
        cryptor = FileCryptor(file_path,password)
        if command=='crypt':
            cryptor.crypt()
        elif command=='decrypt':
            cryptor.decrypt()
        else:
            print('Singurele comenzi ce pot fi apelate sunt crypt si decrypt!')

if __name__ == '__main__':
    main()

