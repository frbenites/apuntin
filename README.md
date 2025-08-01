# Apuntin 🗣️🤖📝
Apuntín desgraba clases.  
Agarra grabaciones de clases en formatos .mp3, .wav o .m4a provistos por el usuario y devuelve una desgrabación de lo escuchado en formato apuntes de clase bien estructurados en markdown.  

Apuntín tiene varios módulos:

**El Chunker**  
He visto que a las LLMs de transcripción por ahí empiezan a fallar a partir de cierto tamaño de audio. La mayoría tienen un límite cerca de los 10 minutos.  
El Chunker agarra un audio, lo separa en partes de aproximadamente ~7 mins y las guarda en una carpeta. Lista para ser usada por el transcriptor.

**El Transcriptor**  
Usa Whisper de OpenAI para transcribir cada chunk de audio y los une en una transcripción completa.

**El Formateador**  
Usa ChatGPT para transformar la transcripción cruda en un documento markdown bien estructurado con:
- Títulos y subtítulos organizados
- Puntos clave resaltados
- Términos importantes en **negrita**
- Eliminación de muletillas y repeticiones
- Formato optimizado para estudiar
Como punto a resaltar, el formateador está obligado a no cambiar la información de la transcripción, solo a estructurarla.

## Uso

```bash
python main.py audio_file.mp3 [opciones]
```

### Opciones:
- `--chunk-length N`: Duración de chunks en minutos (default: 7)
- `--keep-chunks`: Mantener archivos de audio temporales
- `--no-format`: Saltar formateo con ChatGPT y guardar transcripción cruda (tiene todas las oraciones juntas)

## Configuración

Para usarlo es necesario tener una API key de OpenAI configurada:
```bash
export OPENAI_API_KEY="tu-api-key-aqui"
```