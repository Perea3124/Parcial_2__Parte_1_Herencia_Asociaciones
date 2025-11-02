# Proyecto de Programación Orientada a Objetos
Parcial 2 – Herencia y Relaciones

## Contexto académico
- Universidad Tecnológica de Pereira
- Docente: Alejandro Rodas Vásquez
- Asignatura: Programación 4

## Descripción general
Este proyecto implementa un sistema de facturación para una tienda agrícola, aplicando principios de Programación Orientada a Objetos tales como herencia, composición y modularidad. El sistema gestiona productos de control agrícola (fertilizantes y control de plagas), antibióticos para animales y clientes con su historial de facturas. La calidad del diseño se valida mediante una batería de pruebas unitarias.

## Estructura del repositorio
```text
.
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── modelo/
│   ├── antibiotico.py
│   ├── cliente.py
│   ├── control_plagas.py
│   ├── factura.py
│   ├── fertilizante.py
│   ├── linea_factura.py
│   ├── producto.py
│   ├── producto_control.py
│   └── __init__.py
├── tests/
│   ├── test_antibiotico.py
│   ├── test_factura_cliente.py
│   └── test_producto_control.py
├── evidencias/
│   ├── diagrama_UML_clases.mmd
│   ├── diagrama_UML_clases.png
│   ├── diagrama_componentes.mmd
│   ├── diagrama_componentes.png
│   ├── screenshot_project_structure.png
│   ├── screenshot_tests_terminal.png
│   └── screenshot_debugger.png
├── tests_output.txt
├── estructura.txt
└── README.md
```

## Modelo de clases
- `Producto`: clase base con nombre y precio.
- `ProductoControl` (hereda de `Producto`): incorpora `codigo_ica` y `frecuencia_aplicacion_dias`.
- `ControlPlagas` (hereda de `ProductoControl`): añade `periodo_carencia_dias`.
- `Fertilizante` (hereda de `ProductoControl`): registra `fecha_ultima_aplicacion`.
- `Antibiotico`: gestiona `dosis_mg_por_kg` y `tipo_animal`.
- `Factura`: mantiene fecha, colecciones de `LineaFactura` y calcula `valor_total()`.
- `Cliente`: almacena datos personales, historial de facturas y expone `total_facturado()`.

**Relaciones clave**: herencia `Producto → ProductoControl → (ControlPlagas | Fertilizante)` y composición `Cliente → Factura → LineaFactura → Producto`.

## Ejecución de pruebas
Desde la raíz del proyecto:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Ejemplo del resultado esperado:

```text
Ran 14 tests in 0.002s
OK
```

Para ejecutar un caso en particular:

```powershell
python -m unittest -v tests.test_factura_cliente
```

## Depuración en VS Code
1. Verificar la configuración de `.vscode/launch.json`.
2. Abrir el archivo de prueba (`tests/test_factura_cliente.py`), colocar un breakpoint y ejecutar la depuración (`F5` o *Debug Test*).
3. Inspeccionar los paneles *Variables* y *Call Stack* para analizar la herencia y la composición (ver `evidencias/screenshot_debugger.png`).

## Evidencias disponibles
- Diagramas UML: `evidencias/diagrama_UML_clases.png`, `evidencias/diagrama_componentes.png`.
- Capturas de apoyo: `evidencias/screenshot_project_structure.png`, `evidencias/screenshot_tests_terminal.png`, `evidencias/screenshot_debugger.png`.
- Registro opcional de pruebas: `tests_output.txt`.

## Autoría
Autor: David Quintero Perea  
Correo: d.quintero4@utp.edu.co  
Docente: Alejandro Rodas Vásquez  
Universidad Tecnológica de Pereira  
Fecha de entrega: 2025-11-02