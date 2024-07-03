from config import *;
from utilities import *;
from lexer import *;
import zipfile;

folder_name = input ("Project route: ")
print("\n")
compressed_filename = input ("Compressed file name: ")
print ("\n\n")
folder_path = PROJECTS+folder_name
cfn_path = os.path.join(folder_path,compressed_filename)


with zipfile.ZipFile(compressed_filename, 'w') as zipf:
    for carpeta in [folder_path]:
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            # Agregar archivo al .ocf respetando la estructura
            zipf.write(ruta_completa, os.path.relpath(ruta_completa, carpeta))