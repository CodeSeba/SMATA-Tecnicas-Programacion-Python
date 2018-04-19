# SMATA-Tecnicas-Programacion-Python
~~Se aclara que el lenguaje Python se enseña en las ultimas clases de este curso.~~

Las primeras son de pseudocodigo TIMBA.

En principio se utilizara PSeInt como interprete de pseudocodigo en español.

Como la profe nos sugiere que no lo usemos para no confundirnos más adelante, se esta buscando actualmente un alternativo.

Hasta entonces los pseudocodigos seguiran siendo para PSeInt hasta nuevo aviso.

Para usar los indices de arreglos en base 0 (cero) se debe ir a 

`Configurar > Perfiles > Personalizar`

Activar **Utilizar indices en arreglos y cadenas en base 0**

`Aceptar > Aceptar`

---

# PYTHON

El 4 de septiembre de 2017 la profe comienza a utilizar Python 3.6.
Se debe aclarar que hay dos versiones actualmente utilizadas.
La version 2.x y la version 3.x.  Vamos a utilizar la version 3.6.2 para este curso.

* Windows

Se debe bajar el instalador de Python 3.6 en este [LINK](https://www.python.org/downloads/windows/).

* Linux

Se debe bajar el codigo fuente en este [LINK](https://www.python.org/downloads/).

Para instalar se deben seguir estos pasos.

### Para Debian / Ubuntu / Mint

* Descomprimir el archivo .tar.xz .
* Abrir una Terminal en la carpeta Python-3.6.2 .
* Ejecutar los siguientes comandos.

```
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev python3-dev
```
```
./configure
make
make test
sudo make install
```

Ejecutar Python
---
En ambos casos luego de instalar Python se debe abrir una consola de comandos y tipear `python`.
Estaras dentro del Shell de Python y estara a la espera de ingresos de comandos.

Un ejemplo
```python
>>>print("¡Hola Mundo!")
¡Hola Mundo!
```
Para cerrar Python se debe ejecutar `exit()`.

Aclaraciones para Linux
---
Para ejecutar el shell de Python se debe tipear `python` si la distribucion que utiliza ya vino instalado por default, estara instalado la version 2.x. Se debe instalara la version 3.x para no tener problemas con el curso. Despues instalar la version 3.x, este no sobreescribe la anterior, sino que se instala con el nombre python3 entonces para ejecutar el shell de Python 3 se debe ejecutar en una terminal con `python3`.

Si se quiere ejecutar archivos `*.py` para tener un mejor control de errores, se debe ejecutar de la siguiente manera
```
python3 archivo.py
```

Sublime Text 3 y Python 3
---
Para utilizar el editor de texto Sublime Text 3 y probar el codigo desde adentro se tiene que configurar primero con los siguientes pasos.
* Ir a `Tools` > `Build System` > `New Build System...`
* Se creara un nuevo archivo con algunos datos por default.
* Borrar todos los datos y escribir lo siguiente
```
{
   "cmd": ["gnome-terminal -e 'bash -c \"/usr/local/bin/python3 -u $file;echo;echo Press ENTER to exit...;read line\"'"],
   "shell": true
}
```
* Guardar el archivo en el mismo lugar donde aparece por default `~/.config/sublime-text-3/Packages/User/`
* El nombre del archivo se sugiere que sea `Python3.sublime-build` para que no sobreescriba el default `Python` que es para la version 2.x
* Listo. Se puede probar con un codigo python pero se debe guardar antes de ejecutar para que no tiere error.
* Para ejecutar el codigo se debe oprimir `Ctrl+B` y aparecera una ventana de terminal ejecutando el codigo escrito.
* Cuando termina de ejecutar todo el codigo, aparecera una mensaje `Press ENTER to exit...` que indica que se debe oprimir enter para salir y cerrar la terminal. El mensaje se puede cambiar en el archivo `Python3.sublime-build`.
