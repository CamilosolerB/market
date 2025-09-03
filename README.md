# Invensoft

**Proceso de instalacion del Software**

Para este proceso se requiere tener las siguientes aplicaciones.

-   Git

-   Python (preferiblemente entre las versiones 3.7 a 3.11)

Lo primero es hacer un clone del proyecto desde la terminal
~~~
  git clone https://github.com/CamilosolerB/market.git
~~~
Tienes que tener instalado python y la libreria virtualenv, entras con vs code, abres una terminal en vscode y ejecutas
~~~
  ./myenv/Script/activate
~~~
Si sale algun problema con politicas ejecuta desde powershell como administrador
~~~
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
~~~

Esto hara que se instale todas las dependencias (antes de ejecutar esta
accion se debe tener instalado python)

finalmente, corremos el siguiente comando en la terminal donde se viene
trabajando
~~~
  python3 manage.py runserver
~~~
De esta manera se ejecuta el proyecto en su entorno local por lo cual
desde cualquier navegador web ingresamos a la siguiente url:
~~~
  localhost:8000/
~~~

los usuarios de acceso para el software inicialmente son:

Administrador:
~~~
  correo: caansobu2@gmail.com

  clave: 1234
~~~
Cajero:
~~~
  correo: camilosolerbu@gmail.com

  clave: 1234
~~~
