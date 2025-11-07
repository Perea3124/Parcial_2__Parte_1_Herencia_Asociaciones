# Proyecto de Programación Orientada a Objetos
Parcial 2 – Herencia y Asociaciones

## Contexto académico
- Universidad Tecnológica de Pereira
- Docente: Alejandro Rodas Vásquez
- Asignatura: Programación 4

## Descripción general
El objetivo es modelar un flujo básico de facturación para una tienda agrícola aplicando principios de herencia, composición y validaciones orientadas a objetos. El dominio incluye productos de control agrícola (fertilizantes y controles de plagas), antibióticos veterinarios y clientes con historial de facturación. El comportamiento se garantiza con pruebas unitarias que cubren validaciones, cálculos y asociaciones entre objetos.

## Estructura del repositorio
```text
.
├── .copilotignore
├── .git/
├── .gitignore
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── crud/
│   ├── __init__.py
│   ├── operaciones.py
│   └── __pycache__/...
├── evidencias/
│   ├── diagrama_componentes.mmd
│   ├── diagrama_componentes.png
│   ├── diagrama_UML_clases.mmd
│   ├── diagrama_UML_clases.png
│   ├── screenshot_debug_busqueda.png
│   ├── screenshot_debugger.png
│   ├── screenshot_demo_terminal.png
│   ├── screenshot_project_structure.png
│   └── screenshot_tests_terminal.png
├── modelo/
│   ├── __init__.py
│   ├── antibiotico.py
│   ├── cliente.py
│   ├── control_plagas.py
│   ├── factura.py
│   ├── fertilizante.py
│   ├── linea_factura.py
│   ├── producto.py
│   ├── producto_control.py
│   └── __pycache__/...
├── tests/
│   ├── test_antibiotico.py
│   ├── test_crud.py
│   ├── test_factura_cliente.py
│   ├── test_producto_control.py
│   └── __pycache__/...
├── ui/
│   ├── __init__.py
│   ├── cli.py
│   └── __pycache__/...
├── README.md
└── tests_output.txt
```

### Núcleo del modelo (`modelo/`)
- `Producto`: dataclass base con validaciones para nombre y precio.
- `ProductoControl` → (`ControlPlagas`, `Fertilizante`): extienden atributos con información ICA, frecuencia y datos específicos.
- `Antibiotico` y `TipoAnimal`: modelan medicamentos veterinarios con validación de dosis y tipo.
- `LineaFactura`: garantiza que cualquier ítem facturable posea un `precio` y cantidad válida.
- `Factura`: acepta `LineaFactura` o productos directos, calcula `valor_total()` y permite `agregar_producto()`.
- `Cliente`: agrupa facturas, permite agregarlas, calcular `total_facturado()` y filtrarlas por fecha.

### Capa CRUD (`crud/operaciones.py`)
- Maneja almacenamiento en memoria de `CLIENTES` y `FACTURAS`.
- Expone funciones `crear_cliente`, `agregar_factura` y `buscar_por_cedula` usadas en las pruebas y la demo CLI.

### Interfaz de demostración (`ui/cli.py`)
- Ejecuta un flujo mínimo de creación de cliente, factura y búsqueda para depuración.
- Se puede lanzar con:

```powershell
python ui/cli.py
```

## Pruebas automatizadas
Desde la raíz del repositorio:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

La suite actual incluye 16 pruebas que cubren validaciones de antibióticos, productos de control, facturación y operaciones CRUD. El archivo `tests_output.txt` conserva la salida más reciente (codificada en UTF-16 por PowerShell); eliminarlo es opcional si se requiere una ejecución limpia.

Para un módulo en particular:

```powershell
python -m unittest -v tests.test_factura_cliente
```

## Evidencias
- Diagramas Mermaid y exportaciones: `evidencias/diagrama_UML_clases.mmd|.png`, `evidencias/diagrama_componentes.mmd|.png`.
- Capturas actualizadas: `screenshot_project_structure.png`, `screenshot_tests_terminal.png`, `screenshot_debugger.png`, `screenshot_debug_busqueda.png`, `screenshot_demo_terminal.png`.

## Autoría
- Autor: David Quintero Perea
- Correo: d.quintero4@utp.edu.co
- Docente: Alejandro Rodas Vásquez
- Universidad Tecnológica de Pereira
- Última actualización: 2025-11-07