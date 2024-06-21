# fAIrNews
Trabajo de Fin de Grado
### Abstract

In an increasingly saturated and polarized media environment, the ability to access impartial and verified information becomes increasingly crucial. This project develops a software system to address this need through the automation of the news collection, analysis, and synthesis process, as well as a web application to visualize the generated narratives.

Utilizing RSS feeds from major Spanish newspapers, the system collects front-page news and extracts keywords using the 'TF-IDF' algorithm, employing the entire collection of gathered news as the corpus. Subsequently, the news items are clustered into related themes using the 'sBERT' embedding to vectorize phrases within the news and serve as input for the 'K-means' algorithm, which groups the news by theme and context.

Content analysis and summary generation in this project are performed using advanced Natural Language Processing techniques. For the actual creation of the summaries, automatic summarization models available through the HuggingFace Transformers library are used. These models, trained on large data corpora and optimized to understand and synthesize information, generate summaries that maintain the meaning and idea of the input texts. 'spaCy' is also used for sentence prioritization, which helps identify and select the most relevant parts of the text based on their meaning and relevance within the general context of the article.

The implementation of this system is carried out in Python, using the Django web framework, which ensures a robust and scalable platform. Additionally, the 'MongoDB Atlas' service is used for the persistence of the generated news, a cloud database solution that offers high availability and flexibility, facilitating efficient management of large volumes of data and its scalability.

### Resumen

En un contexto mediático cada vez más saturado y polarizado, la capacidad de acceder a una información imparcial y verificada se vuelve más crucial por momentos. Este proyecto desarrolla un sistema software para abordar esta necesidad mediante la automatización del proceso de recopilación, análisis y síntesis de noticias, además de una aplicación web para visualizar las narrativas generadas.

Utilizando fuentes RSS de los principales periódicos de España, el sistema, en su ejecución, recoge las noticias de portada y extrae las palabras clave mediante el algoritmo ‘TF-IDF’, utilizando como corpus la colección completa de noticias recolectadas. Posteriormente, las noticias se agrupan por temáticas afines en clústeres haciendo uso del embedding ‘sBERT’ para vectorizar frases dentro de las noticias y actuar como entrada para el algoritmo ‘K-means’, que agrupa las noticias por temática y contexto.

El análisis de contenido y la generación de resúmenes en este proyecto se realizan mediante el uso de técnicas avanzadas de procesamiento de lenguaje natural. Para la creación de los resúmenes propiamente dichos, se emplean modelos de resumen automático disponibles a través de la librería ‘Transformers’ de ‘HuggingFace’. Estos modelos, entrenados en grandes corpus de datos y optimizados para entender y sintetizar información, generan resúmenes manteniendo el significado y la idea de los textos de entrada. También se utiliza ‘spaCy’ para la priorización de sentencias, lo que permite identificar y seleccionar las partes más relevantes del texto basándose en su significado y relevancia dentro del contexto general del artículo.

La implementación de este sistema se realiza en Python, utilizando el framework web Django, lo que asegura una plataforma robusta y escalable. Además, para la persistencia de las noticias generadas, se utiliza el servicio ‘MongoDB Atlas’, una solución de base de datos en la nube que ofrece alta disponibilidad y flexibilidad, facilitando la gestión eficiente de grandes volúmenes de datos y su escalabilidad.

 
