# Guía Basica de Comandos

### Inicializacion de un proyecto
Esto se suele hacer cuando no se ha clonado un repositorio, va seguido de otro comando para apuntar al repositorio que deseemos

```bash
git init

git remote add <name> <url>
```

#

### Revisando el estado de los archivos
#### Esto se hace para que verificar en que estado estan tus archivos
```bash
git status
```
### Añadiendo y quitando archivos
#### Con el siguiente comando añadimos un archivo al commit que quieras hacer luego 
#### Nota: Puedes reemplazar el punto para especificar un archivo
```bash
git add .
```

#### También puedes usar el siguiente comando para quitar archivos antes de hacer un commit
```bash
git restore --staged <fileName>
```

### Haciendo un commit
#### Usamos el siguiente comando
```bash
git commit -m "Mensaje del commit"
```

#

### Revision de Ramas
#### Con los siguientes comandos revisaremos cuales son las ramas locales y remotas (solo añade un ' -r ')
```bash
git branch
```
#### Nota: El repositorio que tenga un ' * ' a la izquierda cuando uses el comando sin el parametro es en el que te encuentras

### Cambiando de Rama
#### Los siguientes comandos se usan para cambiar la rama local en la que estas, para crear una nueva solo añade un ' -b ' antes del nombre de la rama
```bash
git checkout <branchName>
```

#

### Haciendo Push
#### El push es el siguiente paso, sirve para enviar los commit al repositorio remoto, hasta el momento tenemos todo en nuestro respositorio local

```bash
git push origin <branchName>
```
#### Nota: Debes verificar que el nombre de la rama local en la que estes coincida con el de tu repositorio remoto en caso de que no desees crear una nueva
