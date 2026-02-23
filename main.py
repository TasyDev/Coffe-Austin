import sys
import os

# Añadimos la carpeta 'src' al path para poder importar 'domain'
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from datetime import datetime
from domain.models import Cliente, Colaborador

def probar_modelos():
    print("--- Probando Modelos de Coffe-Austin ---")

    # 1. Probar Cliente
    try:
        # Ahora el cliente requiere: historialDeCompras (list) y puntos (int)
        cliente1 = Cliente("Juan", "Perez", "555-1234", "juan@correo.com", ["Café", "Pan"], 10)
        print(f"Cliente: {cliente1.nombre_completo}")
        print(f"Puntos: {cliente1.puntos}")
    except Exception as e:
        print(f"Error al crear cliente: {e}")

    print("-" * 30)

    # 2. Probar Colaborador
    try:
        # Ahora el colaborador requiere: fechaDeIngreso (datetime), salario (int) y cargo (str)
        fecha = datetime(2023, 5, 15)
        profe = Colaborador("Ana", "Gomez", "555-5678", "ana@coffe.com", fecha, 2500, "Barista")
        print(f"Colaborador: {profe.nombre_completo}")
        print(f"Cargo: {profe.cargo}")
        print(f"Salario: ${profe.salario}")
    except Exception as e:
        print(f"Error al crear colaborador: {e}")

if __name__ == "__main__":
    probar_modelos()