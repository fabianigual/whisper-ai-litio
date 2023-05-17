# Whisper AI para transcripción a documentos en formato markdown

El objetivo inicial del repositorio es utilizar `Whisper AI` para transcribir una entrevista del vicepresidente de CORFO acerca de la `Estrategia nacional del Litio`, a un documento
en formato markdown, el cual cuente con una estructura de minuta y que resuma los principales  
puntos abordados en la entrevista.  

Este repositorio contiene 3 archivos Python:

`download_audio.py`: Descarga el audio de un video de YouTube en formato MP3.
`transcript.py`: Transcribe el audio de un archivo MP3 utilizando `Whisper Ai` a través de la API de OpenAI.  
`to_markdown.py`: Convierte el transcript a un documento Markdown formateado utilizando la API de OpenAI a través de `GPT-3.5` o `GPT-4`, y entregando un Prompt con las instrucciones para la estructura y contexto (información sobre la temática).  

> En desarrollo.  
