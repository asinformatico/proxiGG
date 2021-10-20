# proxiGG
Traductor de webs desde consola usando el servicio de Google Traductor.

Se adjunta el código fuente para Python3 y un binario compilado en C para quien quiera usarlo directamente como ejecutable.

El funcionamiento es sencillo, tan solo hay que ejecutar el archivo...

Para ejecutar el script en Python: <b>./proxiGG.py</b><br>
Para ejecutar el binario compilado en C: <b>./proxiGG.bin</b><br>

Recordar que al descargar el archivo es probable que deban añadírsele permisos de ejecución, esto puede hacerse con el siguiente comando:

<b>chmod +x nombre_archivo</b>

Una vez ejecutado, el programa pedirá al usuario la dirección que quiera traducir, el idioma de origen de la web y el idioma de destino. Una vez introducidos los datos solicitados por el programa, se abrirá el navegador web con la web traducida al idioma elegido.

Los idiomas se introducen son los códigos usados por Google en su servicio de traducción web:

<b>'af','sq','de','am','ar','hy','az','bn','be',
'my','bs','bg','km','kn','ca','ce','cs','ny',
'zh-CN','si','ko','co','ht','hr','da','sk','sl',
'es','eo','et','eu','fi','fr','fy','gd','gl',
'ka','el','gu','ha','haw','iw','hi','hmn','hu',
'ig','id','en','ga','is','it','ja','jw','kk',
'rw','ky','ku','lo','la','lv','lt','lb','mk','ml',
'ms','mg','mt','mi','mr','mn','nl','no','or','pa',
'ps','fa','pl','pt','ro','ru','sm','sr','st','sn',
'sd','so','sw','sv','su','tl','th','ta','tt','tg',
'te','tr','tk','uk','ug','ur','uz','vi','xh','yi',
'yo','zu'</b>

Cuando el programa solicita el código de idioma, puede introducir la palabra <b>'lista'</b> como ayuda para ver un listado con todos los idiomas disponibles y sus correspondientes códigos ordenados alfabéticamente.

También puede usarse sin interacción del usuario llamándolo desde la línea de comandos con los parámetros "dirección web", "idioma origen" e "idioma destino" directamente.

<b>./proxiGG.py direccion_web idioma_origen idioma_destino</b>

Ejemplo de uso con parámetros:

<b>./proxiGG.py https://www.dominio.com/loquesea/pagina es en<b>

En este ejemplo se ve claramente que el primer parámetro es la web a traducir (https://www.dominio.com/loquesea/pagina), el segunndo parámetro es el idioma de origen (es) y el tercer parámetro es el idioma de destino (en).
  
Una funcionalidad adicional es que puede usarse como proxy, ya que la navegación se realiza a través del servidor de traducción de Google.
