try:
    userfrom mysql import connector
except ModuleNotFoundError:
    print("MySql connector não está instalado")
else:
    print("MySql está instalado!")
