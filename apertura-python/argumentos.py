#Blibliotecas
import argparse

#Parser

parser = argparse.ArgumentParser()
parser.add_argument ("img_src", help="Imagen a buscar en la BD de caras")
parser.add_argument ("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

ruta = args.img_src + " " + args.db_path

print("las rutas recibidas son: " + ruta)