# Apuntin 🗣️🤖📝
Apuntín desgraba clases.  
Agarra grabaciones de clases en formatos .mp3, .wav o .m4a provistos por el usuario y devuelve una desgrabación de lo escuchado en formato apuntes de clase.  

Apuntín tiene varios módulos.

**El Chunker.**  
No puedo pasarle archivos larguísimos de audio a las LLMs de transcripción.  
La mayoría tienen un límite cerca de los 10 minutos.  
El Chunker agarra un audio, lo separa en partes de aproximadamente ~7 mins y las guarda en una carpeta. Lista para ser usada por el transcriptor.