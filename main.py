import sys
import os
from datetime import datetime

# ==============================================================================
# CONFIGURACIÓN DE ENTORNO
# ==============================================================================
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from domain.aplicación.tienda import Tienda
    from domain.aplicación.venta import Venta
    from domain.models import Cafe, Comida, Cliente, Colaborador
except ImportError as e:
    print(f"Error de Arquitectura: No se pudieron cargar las capas del dominio: {e}")
    sys.exit(1)

def mostrar_titulo(texto):
    print(f"\n{'='*60}")
    print(f" {texto}")
    print(f"{'='*60}")

def ejecutar_test_arquitectura():
    # --------------------------------------------------------------------------
    # CAPA 1: MODELOS DE DOMINIO - ENTIDADES BASE (Persona / Producto)
    # --------------------------------------------------------------------------
    mostrar_titulo("1. CAPA DE MODELOS - ENTIDADES Y ENCAPSULAMIENTO")
    
    # Probando Herencia y Polimorfismo en Productos
    cafe_espuma = Cafe("Macchiato", 5000, "Con espuma de leche", True, "Mezcla", "Caliente", "Pequeño")
    galleta = Comida("Galleta de Avena", 1500, "Con chispas de chocolate", True, "Snack", 120)

    print("[Atributos de Producto]")
    print(f" - ID: {cafe_espuma.id} | Nombre: {cafe_espuma.nombre} | Precio: ${cafe_espuma.precio}")
    print(f" - ID: {galleta.id} | Nombre: {galleta.nombre} | Categoría: {galleta.categoria}")

    # Probando Herencia en Personas
    barista = Colaborador("Juan", "Vargas", "555-0101", "juan@cafe.com", datetime.now(), 2000, "Barista")
    cliente_fiel = Cliente("Sofía", "Castro", "555-0202", "sofia@email.com", [], 100)

    print("\n[Atributos de Persona]")
    print(f" - Nombre Completo: {barista.nombre_completo}")
    print(f" - Contacto: {cliente_fiel.informacion_contacto}")
    print(f" - Puntos Cliente: {cliente_fiel.puntos}")

    # --------------------------------------------------------------------------
    # CAPA 2: COMPORTAMIENTO DEL DOMINIO (Métodos Específicos)
    # --------------------------------------------------------------------------
    mostrar_titulo("2. CAPA DE MODELOS - COMPORTAMIENTOS ESPECÍFICOS")
    
    cafe_espuma.prepararCafe()
    print("-" * 20)
    galleta.haciendoComida()

    # --------------------------------------------------------------------------
    # CAPA 3: SERVICIOS DE APLICACIÓN - LÓGICA DE NEGOCIO (Venta)
    # --------------------------------------------------------------------------
    mostrar_titulo("3. CAPA DE APLICACIÓN - LÓGICA DE NEGOCIO (VENTA)")
    
    lista_items = [cafe_espuma, galleta, cafe_espuma] # Venta de 2 cafés y 1 galleta
    venta_actual = Venta(
        fecha=datetime.now(),
        cliente=cliente_fiel.nombre_completo,
        colaborador=barista.nombre_completo,
        productos=lista_items,
        metodo_de_pago="Efectivo"
    )

    print(f"Resumen de Venta #{venta_actual.id}:")
    print(f" - Cliente: {venta_actual.cliente}")
    print(f" - Atendido por: {venta_actual.colaborador}")
    print(f" - Items: {len(venta_actual.productos)}")
    print(f" - TOTAL CALCULADO: ${venta_actual.total}")

    # --------------------------------------------------------------------------
    # CAPA 4: ORQUESTACIÓN - ENTIDAD RAÍZ (Tienda)
    # --------------------------------------------------------------------------
    mostrar_titulo("4. CAPA DE ORQUESTACIÓN - AGGREGATE ROOT (TIENDA)")
    
    # Inicializando el núcleo del sistema
    coffe_austin = Tienda(
        clientes=[cliente_fiel],
        colaboradores=[barista],
        menu=[cafe_espuma, galleta],
        ventas=[]
    )

    # Probando gestión de listas
    coffe_austin.agregar_cliente("Manuel Rivera")
    coffe_austin.agregar_producto(Cafe("Tinto", 1500, "Clásico", True, "Oscuro", "Caliente", "Estándar"))
    coffe_austin.agregar_venta(venta_actual)

    print(f"Estado de la Tienda:")
    print(f" - Menú disponible: {[p.nombre for p in coffe_austin.menu]}")
    print(f" - Total Clientes: {len(coffe_austin.clientes)}")
    print(f" - Ventas en Histórico: {len(coffe_austin.obtener_ventas())}")

    # --------------------------------------------------------------------------
    # VALIDACIONES FINALES (Setters y Estados)
    # --------------------------------------------------------------------------
    mostrar_titulo("5. VALIDACIÓN DE ESTADOS Y SETTERS")
    
    print(f"Antes de actualizar: {galleta.nombre} - ${galleta.precio} (Disponible: {galleta.disponible})")
    
    # Usando setters para modificar estado
    galleta.disponible = False
    cliente_fiel.puntos += 50
    
    print(f"Después de actualizar:")
    print(f" - {galleta.nombre} Disponible: {galleta.disponible}")
    print(f" - {cliente_fiel.nombre_completo} Puntos: {cliente_fiel.puntos}")

if __name__ == "__main__":
    ejecutar_test_arquitectura()
    print(f"\n{'='*60}")
    print(" TEST FINALIZADO EXITOSAMENTE")
    print(f"{'='*60}")
