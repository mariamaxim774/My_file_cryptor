import os
import os.path
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
        for root,directories,files in os.walk("C:\\Users\\User\\Desktop\\Python\\github\\Python2024\\myFileCryptor"):
            if self.filename in files:
                return os.path.join(root,self.filename)
        else:
            return None


class FileCryptor:

    def __init__(self,filename,password):
        self.filename=filename
        self.password=password

    def crypt(self):
        out_file=f"{self.filename}.crypted"
        file_hash=self.compute_hash()

        with open(self.filename,'rb') as input_file, open(out_file, 'wb') as output_file:
            output_file.write(file_hash)
            for index,byte in  enumerate(input_file.read()):
                password_offset=index%len(self.password)
                key=ord(self.password[password_offset])
                encrypted_byte=(byte+key)%256
                output_file.write(bytes([encrypted_byte]))

    def  decrypt(self):
        print('In decrypt')

    def compute_hash(self):
        hash=hashlib.sha256()#64 bytes
        with open(self.filename, "rb") as file:  #
            data=file.read()
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
            print('decrypt')
            #exit_file=cryptor.decrypt()
        else:
            print('Singurele comenzi ce pot fi apelate sunt <crypt> si <decrypt>')

if __name__ == '__main__':
    main()

