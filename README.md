# Proyecto2-HBase

## 📡 Tecnologias Utilizadas

- Python 🐍: Modern syntax, Interpreted Languaje
  > Python 10.0 or higher needed

## ✅ Rúbrica

### Funciones
- Funciones DDL:
  - [x] Create
  - [x] List 
  - [x] Disable
  - [x] Enable
  - [x] Is_enabled
  - [x] Alter
  - [x] Drop
  - [x] Drop All
  - [x] Describe

- Funciones DML:
  - [x] Put (como función para insertar y actualizar. Si actualiza el timestamp deberá ser actualizado).
  - [x] Get
  - [x] Scan
  - [x] Delete
  - [x] Deleteall
  - [x] Count
  - [ ] Truncate (deberá replicar el disable, drop y recreate de la tabla) 

## 🗃️ Estructura de Archivos

- **`src`**: Código fuente del proyecto

- **`data`**: Archivos json (json Arrays) que contienen la data de cada una de las tablas.
  
  - `example.json`: Maqueta ejemplo de data
  - `table_status.json`: Información de status de tablas (*enabled* | *disabled*).

- `main.py`: Programa principal (Driver Program).

## 🕹️ Getting Started

1. Ejecute el archivo `main.py`
2. Se crearan varias carpetas `__pycache__` con compilados del codigo.
3. Se abrira una CLI donde podrá interactuar con el *HDFS*.

## 🤓 Autores

- Diego Cordova - 20212
- Roberto Vallecillos - 20441
