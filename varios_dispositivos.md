## Cómo tener la cuenta de FGO en varios dispositivos a la vez.
Los archivos donde se guarda la información de la cuenta son los siguientes:
* authsave.dat
* authsave2.dat
* signupsave.dat
* friendcodesave.dat

Se encuentran en la carpeta `/data/com.aniplex.fategrandorder.en/files/data/`, a la que no se puede acceder sin root.  
**Si tienes acceso root tanto en el dispositivo donde tienes la cuenta como en los demás, simplemente copia los archivos.**
##
En caso de que no, asegúrate de que cumples los siguientes requisitos y contáctame por DM/Discord:
* [Python 3.7.X](https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe) instalado y **añadido al PATH**.
* Siguientes [archivos](https://github.com/ShiroSR/FateGO/releases/download/0.1/python.zip) descargados y extraídos en una carpeta (preferiblemente vacía).
* La cuenta tiene que estar iniciada en el dispositivo sin root (generalmente móvil).

El archivo python se encarga de realizar un backup de la aplicación y sus archivos (backup.ab), lo desempaqueta (backup.tar) y extrae los cuatro archivos mencionados arriba.
