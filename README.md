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

El 4 de septiembre de 2017 la profe comienza a utiliar Python 3.6.
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
---------------
En ambos casos luego de instalar Python se debe abrir una consola de comandos y tipear `python`.
Estaras dentro del Shell de Python y estara a la espera de ingresos de comandos.

Un ejemplo
```python
>>>print("¡Hola Mundo!")
¡Hola Mundo!
```
Para cerrar Python se debe ejecutar `exit()`.
