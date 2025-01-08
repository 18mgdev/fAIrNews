# 📰 fAIrNews
**Sistema de Agrupación y Resumen Automatizado de Noticias**

## 📝 Descripción
Este proyecto es un sistema automatizado que recoge, agrupa y sintetiza noticias del panorama mediático español utilizando técnicas avanzadas de inteligencia artificial. El objetivo es proporcionar resúmenes concisos y bien fundamentados de temas de actualidad, integrando diversos puntos de vista para crear una visión equilibrada y menos sesgada. Las noticias sintetizadas están disponibles a través de una aplicación web fácil de usar.

## 🌟 Funcionalidades
- **Recolección de noticias**: Automatización de la extracción de noticias usando fuentes RSS.
- **Agrupación por temáticas**: Utilización de algoritmos de NLP para agrupar noticias por temas relevantes.
- **Generación de resúmenes**: Implementación de modelos de inteligencia artificial de Hugging Face para sintetizar el contenido noticioso.
- **Interfaz de usuario**: Una aplicación web que muestra los resúmenes y permite a los usuarios interactuar con el contenido.

## 💻 Tecnologías Utilizadas
- Python
- Django para la aplicación web
- TensorFlow, spaCy y Hugging Face para el procesamiento de lenguaje natural
- MongoDB para la gestión de la base de datos

## ⚙️ Instalación
Instrucciones para configurar el entorno local:
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
pip install -r requirements.txt
python manage.py runserver
```

## 🚀 Uso

Para utilizar el sistema completo, necesitas abrir dos terminales simultáneamente:

1. 📟 **Ejecución de la Aplicación de Generación de Resúmenes:**
   Abre una terminal y navega hasta el directorio del proyecto. Ejecuta el siguiente comando para iniciar el proceso de recolección y generación de resúmenes:
   ```bash
   python __main__.py
   ```
   Este comando activará el proceso que recopila las noticias, las agrupa y genera resúmenes automáticos.

2. 📟 **Ejecución del Servidor Web:**
   Abre otra terminal y ejecuta el servidor web Django para acceder a la interfaz de usuario. Navega hasta el directorio donde se encuentra `manage.py` y ejecuta:
   ```bash
   python manage.py runserver
   ```
   Luego, abre un navegador web y visita `http://127.0.0.1:8000/` para interactuar con la aplicación web.

Asegúrate de tener ambas partes del sistema ejecutándose para poder utilizar todas las funcionalidades del proyecto, como la visualización de resúmenes y la interacción con ellos a través de la interfaz web.

## 🎬 Demostración

Para ver el sistema en acción, echa un vistazo al siguiente video de demostración. El video proporciona una visión clara de cómo funciona el sistema y muestra tanto la aplicación de generación de resúmenes como la interfaz de usuario de la aplicación web en funcionamiento.

<iframe width="500" height="250" src="https://www.youtube.com/watch?v=CEnqBGE3mJY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="1"></iframe>

## 📄 Licencia
[MIT](./LICENSE)

## 👤 Autor
- Miguel González - fAIrNews (Trabajo de Fin de Grado de Ingeniería del Software UPM) - [18mgdev](https://github.com/18mgdev)
