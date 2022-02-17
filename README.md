# ¿Qué es qrgenerator?

Generador automático de QR para acreditar particiapantes en un evento, dado su nombre y un identificador.

# ¿Cómo instalar?

Instalar las dependencias (qrcode) directamente con el comando **pip install** qrcode o instalar desde el fichero requirements (**pip install -r requirements.txt**).

# ¿Cómo usar?

Ejecutar el comando **python qrgenerator.py**. Se creará una carpeta llamada "qr" con todos los png de QR generados.

Para modificar los datos (nombre e identificador) a incluir en cada QR, se debe modificar el fichero **whitelist.txt**. Este fichero contiene, por cada QR a generar una línea para el nombre y otra para el identificador. Los datos entre cada QR a generar tienen que estar separador por una línea en blanco.

También se pueden especificar estos datos en otro fichero de texto. Para ejecutar el script tomando esos datos, debe especificar la ruta del fichero (**python qrgenerator.py <nombre_fichero>**).