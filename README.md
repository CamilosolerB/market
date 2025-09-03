# Invensoft

**Proceso de instalacion del Software**

Para este proceso se requiere tener las siguientes aplicaciones.

-   Git

-   Python (preferiblemente entre las versiones 3.7 a 3.11)

Lo primero es hacer un pull del proyecto desde la terminal
~~~
  git pull https://github.com/CamilosolerB/market.git
~~~
Si esta trabajando desde linux (cualquier distro) puede correr el
siguiente comando desde la terminal.
~~~
  source ./local/bin/activate
~~~
Posterior a eso corra el comando
~~~
  pip install -r requirements.txt
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
Tambien poseemos una version desplegada en el PaaS Render accediendo
desde la web

https://market-mwtx.onrender.com/

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
