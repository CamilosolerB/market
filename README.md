# market

## Descripción General

`market` es una aplicación web de comercio electrónico o mercado, desarrollada principalmente con Python (Django) y que integra tecnologías frontend como HTML, CSS y JavaScript. El proyecto demuestra una solución completa para la gestión de productos, usuarios y transacciones.

## Características Principales

*   **Gestión de Productos:** Funcionalidades para añadir, editar y eliminar productos.
*   **Gestión de Usuarios:** Registro, autenticación y perfiles de usuario.
*   **Carrito de Compras:** Funcionalidad para añadir productos al carrito y gestionar pedidos.
*   **Base de Datos:** Persistencia de datos para productos, usuarios y pedidos.
*   **Automatización de Despliegue:** Script `build.sh` para la configuración y despliegue de la aplicación.

## Tecnologías Utilizadas

*   **Python** (Framework: Django)
*   **HTML, CSS, JavaScript:** Para el desarrollo frontend.
*   **SQLite:** Base de datos por defecto (`db.sqlite3`).
*   **Shell Scripting:** Para automatización de tareas de construcción y despliegue (`build.sh`).
*   **psycopg2-binary:** Indica posible uso de PostgreSQL en entornos de producción.

## Instalación y Configuración

Para configurar y ejecutar el proyecto localmente, sigue los siguientes pasos:

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/CamilosolerB/market.git
    cd market
    ```

2.  **Crear y activar un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate   # En Windows
    ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar el script de construcción/despliegue:**

    El proyecto incluye un script `build.sh` que se encarga de instalar dependencias, recolectar archivos estáticos y aplicar migraciones de base de datos.

    ```bash
    ./build.sh
    ```

5.  **Iniciar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

    La aplicación estará disponible en `http://127.0.0.1:8000`.

## Credenciales de Acceso (Iniciales)

Para acceder al software, se proporcionan las siguientes credenciales iniciales:

**Administrador:**
*   **Correo:** `caansobu2@gmail.com`
*   **Clave:** `1234`

**Cajero:**
*   **Correo:** `camilosolerbu@gmail.com`
*   **Clave:** `1234`

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un *issue* o *pull request* con tus sugerencias o mejoras.
