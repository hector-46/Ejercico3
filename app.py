import datetime
import os

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
LOG_FILE = "backup.log"

def procesar_archivo(version="v1"):
    if not os.path.exists(INPUT_FILE):
        print("El archivo no existe")
        return

    with open(INPUT_FILE, "r") as f:
        lineas = f.readlines()

    # Filtro: solo líneas con ERROR
    filtradas = [l for l in lineas if "ERROR" in l]

    # Guardar resultado
    with open(OUTPUT_FILE, "w") as f:
        f.writelines(filtradas)

    # Crear log
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"{fecha} | Archivo: {INPUT_FILE} | Filtrados: {len(filtradas)} | Version: {version}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log)

    print(f"Se filtraron {len(filtradas)} datos")

if __name__ == "__main__":
    procesar_archivo("v1")