from pymongo import MongoClient
def get_database():
 
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://miguelgonzalez72:0rX7jez6iYG027cS@cluster0.31g1g5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Cree una conexión con MongoClient. Puede importar MongoClient o usar pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cree la base de datos para nuestro ejemplo (usaremos la misma base de datos en todo el tutorial
    return client['tfg']

def get_frontpage():
    # Establecer la conexión con la base de datos
    db = get_database()
    # Seleccionar la colección de noticias
    collection = db['noticias']
    # Obtener las noticias de la portada
    frontpage = collection.find({"portada": True})
    # Devolver las noticias
    return frontpage
# Esto se agrega para que muchos archivos pueden reutilizar la función get_database()
if __name__ == "__main__":   
    all_items=[
    {
        "title": "Ayuso y el Gobierno se dan una tregua por el 2 de Mayo tras una semana convulsa por el amago de dimisión de Sánchez",
        "pubDate": "2024-05-02 13:13:24",
        "link": "https://www.20minutos.es/noticia/5241557/0/la-politica-madrilena-se-da-una-aparente-tregua-por-el-dos-de-mayo-cordialidad-entre-ayuso-y-los-miembros-del-gobierno/",
        "guid": "https://www.20minutos.es/noticia/5241557/0/la-politica-madrilena-se-da-una-aparente-tregua-por-el-dos-de-mayo-cordialidad-entre-ayuso-y-los-miembros-del-gobierno/",
        "author": "Luis Miguel Gutiérrez Machio",
        "thumbnail": "",
        "description": "Lobato se compromete a \"no entrar al trapo de insultos\" y \"ser respetuoso\", aunque confiesa que \"no será fácil\".",
        "content": "Los actos institucionales del Dos de Mayo han reunido este jueves en la Puerta de Sol a representantes políticos de varios niveles administrativos y de distinto signo político. La situación se ha prestado para observar si las palabras de este lunes del presidente del Gobierno, Pedro Sánchez, sobre moderar y relajar el tono político han calado entre los asistentes. Uno de los focos estaba puesto en la presidenta de la Comunidad de Madrid, Isabel Díaz Ayuso, y el ministro de Política Territorial y Memoria Democrática, Ángel Víctor Torres. Sin embargo, ambos han mantenido un tono correcto en su relación. Durante su discurso, Díaz Ayuso ha evitado hacer alusiones directas o críticas expresas al Gobierno de España, como en otras ocasiones. Con un marcado semblante institucional, la dirigente ha manifestado que en la región \"no triunfan las identidades de terruño, ni el saberse más que nadie, ni los abusos e injusticias\". Por su parte, Torres ha tendido la mano al Gobierno regional para \"caminar juntos en la cogobernanza\" y tratar los temas que preocupan a los madrileños, como la vivienda o el empleo. Ambos han mantenido una relación protocolaria. Al igual que con el delegado del Gobierno en Madrid, Francisco Martínez. Mucho dista esta celebración de lo vivido el año pasado, cuando el ministro de Presidencia, Relaciones con las Cortes y Memoria Democrática, Félix Bolaños, decidió asistir al evento, pero al no estar invitado se le negó ocupar uno de los espacios reservados en la tribuna de autoridades del exterior y el personal de Protocolo le impidió el acceso. Punto y seguido en la confrontación en otros escenarios Sin embargo, a pesar de esta templanza entre el ejecutivo autonómico y nacional durante el Dos de Mayo, la confrontación se ha producido en otros frentes. El alcalde de Madrid, José Luis Martínez-Almeida, ha aprovechado para remarcar su posición sobre el \"señor bulo\", apelativo con el que se ha dirigido al presidente del Gobierno central: \"Es un día para decirle a Sánchez que él no va a marcar la historia de España\". Para Almeida, el punto y aparte al que se refirió consiste en la \"persecución\" de todo aquel que no piensa y acata los deseos \"del amado líder\". En una línea similar se ha pronunciado el portavoz del PP en la Cámara de Vallecas, Carlos Díaz-Pache, al afirmar que las palabras de Sánchez son \"un engaño como todo lo que hace\". Por ello, ha expresado que la región debe \"permanecer con ese espíritu que no se doblega antes las imposiciones\", al igual que hizo en 1808 contra la ocupación francesa. Desde Más Madrid, la portavoz del grupo en la Asamblea de Madrid, Manuela Bergerot, ha lamentado que en este Dos de Mayo \"el PP sigue amordazando a la oposición en la Asamblea de Madrid\". En su intervención, ha vuelto a denunciar la falta de explicaciones que la presidenta regional ha dado sobre las víctimas de la residencia o sobre sus dos áticos en el centro que \"disfruta por un aparente fraude fiscal\". Begerot ha afirmado que mientras Ayuso \"siga negando verdad, justicia y reparación, seguiremos luchando\". Quien sí ha mostrado ganas de poner punto y aparte ha sido el portavoz del PSOE-M en la Asamblea regional, Juan Lobato. \"¿Vamos a ser capaces de dejar de insultarnos y a hablar sobre propuestas?, se preguntaba. Lobato se ha comprometido a no \"entrar al trapo\" y ser respetuoso, aunque ha confesado que no es una tarea fácil. El dirigente socialista ha considerado que sería necesario que todos, incluido él, hicieran autocrítica y reflexionasen sobre la forma en la que se hace política y pedía \"subir un poco el nivel de la política en Madrid\". Lobato ha querido centrar sus palabras en los desafíos que hay en la comunidad con la justicia social: \"Que las oportunidades estén bien repartidas\". En sintonía con Lobato, la portavoz municipal en el Ayuntamiento de Madrid, Reyes Maroto, ha recalcado la necesidad de hacer una política al servicio de la ciudadanía. Sin embargo, reprocha a Almeida que en el último pleno usara su turno para \"insultar y difundir bulos\". Maroto espera que la carta del presidente sirva para \"hacer reflexionar al PP\" y para que el alcalde de Madrid \"cambie esta forma de hacer política del fango\". La dirigente de Vox en Madrid, Rocío Monasterio, se ha mostrado escandalizada por escuchar a Sánchez hablar de limpieza, ya que, \"eso ya lo hemos escuchado en otros países, la limpieza de los periodistas que discrepen, la limpieza los políticos que disientas\". Por ello, la dirigente estima que es necesario seguir denunciando las actuaciones que van en contra de la libertad y troquelan la democracia en España.",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/la-presidenta-de-la-comunidad-de-madrid-isabel-diaz-ayuso-saluda-al-ministro-de-politica-territorial-y-memoria-democratica-angel-victor-torres-durante-los-actos-del-dos-de-mayo-1.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Madrid"
        ],
        "medio": "20minutos"
    },
    {
        "title": "La presidenta de la Comunidad de Madrid reivindica un Madrid \"de todos\" y \"en común\": \"La libertad sigue siendo nuestro motor como en aquel mayo de 1808\"",
        "pubDate": "2024-05-02 10:49:32",
        "link": "https://www.20minutos.es/noticia/5241513/0/discurso-ayuso-dos-mayo-2024-madrid/",
        "guid": "https://www.20minutos.es/noticia/5241513/0/discurso-ayuso-dos-mayo-2024-madrid/",
        "author": "Mónica Tragacete",
        "thumbnail": "",
        "description": "La presidenta califica a la región como un \"cruce de caminos\" en el que \"no caben identidades de terruño\".",
        "content": "La Real Casa de Correos se ha vestido este jueves de gala para celebrar el 2 de mayo, día de la Comunidad de Madrid. Isabel Díaz Ayuso ha presidido el acto central de la jornada festiva, marcado por la entrega de las Grandes Cruces de la Orden del Dos de Mayo a diferentes organizaciones y personalidades, de la Policía Nacional a Telefónica pasando por Camela, y ha pronunciado un discurso con más carga emotiva que política. Esto es algo que no ha pasado inadvertido entre los más de 600 invitados que han asistido al acto en la Puerta del Sol, porque no es algo habitual en la presidenta madrileña y porque se produce en la misma semana en la que el presidente Pedro Sánchez ha decidido seguir al frente del Gobierno con un ánimo renovado y con reformas en el Poder Judicial y los medios en la agenda tras cinco días de parón. Díaz Ayuso ha reivindicado un Madrid con una forma de vida \"muy propia\" -\"brava, callejera, popular\", ha descrito- ya desde 1808, cuando los habitantes de la región, que no madrileños porque ya entonces había gran presencia de naturales de otras provincias, se levantaron ante el invasor francés. La presidenta ha hablado de un pueblo que no se somete ni es sumiso porque no cede ante \"los abusos\" ni ante \"las injusticias\". Una comunidad abierta, \"de todos\", y crisol de diferentes culturas. \"El Madrid de entonces, ya ven, tan parecido al de ahora\", ha incidido la presidenta, \"porque ha sido y será siempre será cruce de caminos\". En esa encrucijada \"no caben identidades de terruño ni saberse más que nadie\", ha proclamado la presidenta, una frase que ya había utilizado en otras veces para resaltar el carácter de Madrid. Este Dos de Mayo, de nuevo Díaz Ayuso ha reivindicado a la Comunidad y a su forma de ser estar. \"Siempre hemos sabido que esto no va de nosotros solos, que esto va de España\", ha asegurado. \"La libertad, como en aquel mayo de 1808, sigue siendo nuestro motor, por lo que más merece la pena vivir\", ha remarcado en otro momento de su intervención, en la que ha pedido a los presentes que sigan construyendo un Madrid \"atrayente y hospitalario\" en un momento en el que está \"más de moda que nunca\". \"Somos la región al servicio de España (...) la plaza mayor de todos\", ha insistido. Más allá de la clave regional, Díaz Ayuso también ha querido tener un recuerdo para la recientemente fallecida Victoria Prego. \"Añoramos aquellos trabajos periodísticos en una España que quería levantarse unida, libre, sin ira, sin perderse en las diferencias\", ha destacado en referencia a esta periodista de referencia en la Transición y también al Grupo Crónica -uno de los reconocidos este jueves- en lo que se ha entendido como una crítica al planteamiento respecto a los medios de comunicación que está haciendo Sánchez y el resto de su Ejecutivo en los últimos días. El Gobierno madrileño y el de la Nación están acostumbrados a chocar cada día, pero este jueves han rubricado una suerte de tregua porque no ha habido ningún choque que haya empañado la fiesta. El gabinete que lidera Pedro Sánchez ha estado representado en el acto de Sol por el ministro de Política Territorial, Ángel Víctor Torres, al que se ha visto sonriente junto a Díaz Ayuso y al presidente del Senado, Pedro Rollán, y por el delegado del Gobierno en Madrid, Francisco Martín, también en primera fila pero algo más serio. La oposición madrileña también se ha contagiado de ese toma y daca diario generalizado, aunque en las declaraciones previas al inicio del acto se han escuchado algunas críticas cruzadas que han desentonado ligeramente. Ha sido el caso de la portavoz de Más Madrid, Manuela Bergerot, que ha reprochado al PP que \"amordace\" a la oposición en la Asamblea de Madrid, y del alcalde de la capital, José Luis Martínez-Almeida, que se ha referido al presidente del Gobierno como \"señor Bulo\". La comparecencia de Sánchez del lunes y las cábalas sobre cómo se materializará esa agenda reformista, han sido los principales temas de conversación de los numerosos corrillos que se han formado en el patio de la Real Casa de Correos tras el acto. La ausencia de Alberto Núñez Feijóo, líder del PP y de la oposición a Sánchez, también ha sido muy comentada. Altos cargos 'populares' no le han dado mayor importancia a este hecho y han reivindicado que entre los asistentes había una óptima representación del partido con 'primeros espadas' como Pedro Rollán. Este año, la música, con permiso de la política, ha sido una de las grandes protagonistas de la jornada. El grupo OBK ha puesto a bailar -aunque en sus sillas, eso sí- a muchos de los presentes al ritmo de sus míticos temas 'Historias de amor' y 'El cielo no entiende' y la entrega de la Gran Cruz a Mari Ángeles Muñoz y Dioni Martín de Camela ha sido una de las más aplaudidas. Una emoción muy distinta ha embargado a todos los presentes cuando Díaz Ayuso ha impuesto la condecoración al guardia civil José María Ortiz Díaz. Este sargento primero destinado en el puesto de Torrelaguna ha recogido la Gran Cruz a título póstumo concedida a su compañero José Antonio Rosa Alcocer, fallecido la semana pasada en un acto de servicio en San Agustín del Guadalix. La ovación cerrada de varios minutos ha hecho que Ortiz no haya podido contener las lágrimas y, señalando al cielo, ha enviado un cariñoso recuerdo al agente fallecido. La Policía Nacional por su 200 aniversario; los profesionales sanitarios en formación; los rumanos residentes en la Comunidad de Madrid; los conserjes y porteros de fincas; el cabo primero del Ejército de Tierra Fernando Martín Pozueco o el Ilustre Colegio de Procuradores de Madrid también han sido premiados por el Gobierno regional. En la nómina de condecorados con la Gran Cruz de la Orden del Dos de Mayo también han estado este año el servicio de Cardiología del hospital Clínico San Carlos, Telefónica, la modelo Nieves Álvarez, el Rayo Vallecano y el jugador de baloncesto Rudy Fernández. Por el escenario de la sede del Gobierno regional igualmente han pasado el matrimonio formado por Elena Huertas y Octavio Torres, por su labor como familia de acogida a menores en situación de desamparado durante años, y Constantino Mediavilla, periodista y cronista de la Villa de Madrid. \"Cuarenta años contando cosas de Madrid, aprendiendo de muchos\", ha aseverado el comunicador, que ha tenido otro recuerdo para Victoria Prego y ha hecho un alegato a favor del periodismo, de los sanitarios y de los cuidadores. A Prego también la han reivindicado los miembros del Grupo Crónica Pilar García-Cernuda y Antonio Casado, que han sido los últimos en subir al escenario e igualmente han defendido el ejercicio del periodismo en libertad. \"Es incomprensible que en este momento los periodistas y los jueces seamos demonizados\", ha proclamado Cernuda, una línea en la que ha ahondado su compañero, que ha defendido el acceso a la información de la profesión \"por cauces no reglamentados pero no menos eficaces y virtuosos\". Como es habitual, tras la entrega de las condecoraciones el acto por el Dos de Mayo ha continuado en el exterior del edificio. Pasado el mediodía, las principales autoridades presentes en la Real Casa de Correos han salido a la Puerta del Sol donde ha tenido lugar una parada militar en la que han participado el Ejército, la Policía Nacional, la Guardia Civil, policías locales como la de la capital y los bomberos, entre otros cuerpos de seguridad y emergencias. Cientos de ciudadanos se han congregado en la plaza y han podido ver como platos fuertes del acto cívico-militar a la Patrulla Águila, que ha dibujado en el cielo de la capital una bandera de España, y a tres paracaidistas de la Escuela Militar de Paracaidismo Méndez Parada con sede en Alcantarilla (Murcia) que han aterrizado en el 'kilómetro cero' con una bandera de la Comunidad de Madrid y otra de España. También ha habido otro momento de emoción contenida cuando se ha recordado a Miguel Ángel Hernández, bombero del cuerpo regional que perdió la vida este martes a los 35 años cuando hacía barranquismo en la provincia de Huesca y al que se ha querido recordar en el día del Dos de Mayo, que ha quedado ajeno a cualquier polémica política por primera vez en mucho tiempo.",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/ayuso-reivindica-un-madrid-de-todos-y-en-comun-la-libertad-sigue-siendo-nuestro-motor-como-en-aquel-mayo-de-1808.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Madrid"
        ],
        "medio": "20minutos"
    },
    {
        "title": "Pilar Cernuda, periodista premiada: \"Es vergonzoso que los periodistas y los jueces seamos demonizados\"",
        "pubDate": "2024-05-02 03:27:38",
        "link": "https://www.20minutos.es/noticia/5241431/0/dos-mayo-madrid-directo-amago-dimision-sanchez-choque-institucional-marcan-un-acto-que-no-habra-nuevo-roce-con-bolanos/",
        "guid": "https://www.20minutos.es/noticia/5241431/0/dos-mayo-madrid-directo-amago-dimision-sanchez-choque-institucional-marcan-un-acto-que-no-habra-nuevo-roce-con-bolanos/",
        "author": "20minutos",
        "thumbnail": "",
        "description": "La presidenta madrileña, Isabel Díaz Ayuso, preside la celebración del día de la región ante 650 invitados.",
        "content": "La presidenta de la Comunidad de Madrid, Isabel Díaz Ayuso, ha presidido este jueves el tradicional acto del Dos de Mayo y en esta ocasión lo hace en medio de una gran agitación política por el amago de dimisión de Pedro Sánchez y su declaración de \"punto y aparte\" hacia una regeneración democrática. Los reporteros de Grupo Crónica se hicieron con el último galardón de la mañana, entregado a Pilar García- Cernuda y a Antonio Casado. En su discurso de aceptación, Pilar García-Cernuda ha recordado a Victoria Prego, recientemente fallecida, y ha dicho: \"Hemos hecho nuestro trabajo con rigor y libertad. Por eso es doloroso que los periodistas y los jueces seamos demonizados. Poco menos que responsables de que desaparezca la democracia en España\". Entre los asistentes estaba el alcalde de la capital, José Luis Martínez Almeida, quien ha pedido al presidente del Gobierno que no cuente con los madrileños para \"el fango\" y para \"levantar muros\". De parte del Gobierno, el ministro Ángel Víctor Torres, que ha dicho venir a \"tender la mano\" hacia una cogobernanza. En su discurso de cierre del acto de la Casa de Correos, Ayuso ha reivindicado a Madrid como \"la plaza mayor de todos\" y \"eternamente al servicio de España\".",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/pilar-cernuda-periodista-premiada-es-vergonzoso-que-los-periodistas-y-los-jueces-seamos-demonizados.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Madrid"
        ],
        "medio": "20minutos"
    },
    {
        "title": "Fernando De Yarza: \"La amenaza sobre la libertad de prensa y las tentaciones totalitarias se extienden por todo el mundo\"",
        "pubDate": "2024-05-02 15:28:06",
        "link": "https://www.20minutos.es/noticia/5241631/0/fernando-yarza-amenaza-sobre-libertad-prensa-las-tentaciones-totalitarias-se-extienden-por-todo-mundo/",
        "guid": "https://www.20minutos.es/noticia/5241631/0/fernando-yarza-amenaza-sobre-libertad-prensa-las-tentaciones-totalitarias-se-extienden-por-todo-mundo/",
        "author": "20minutos",
        "thumbnail": "",
        "description": "El presidente de WAN-IFRA hace un llamamiento a la sociedad civil para apoyar a los medios que practican “el periodismo de verdad y comprometido frente al pozo de odio y desinformación” de las redes sociales.",
        "content": "El presidente de la Asociación Mundial de Editores (WAN-IFRA), Fernando de Yarza, ha advertido de que \"la amenaza sobre la libertad de prensa y las tentaciones totalitarias se extienden por todo el mundo\" y ha hecho referencia a los últimos ataques a los medios de comunicación y periodistas en España por parte del Gobierno. De Yarza ha aprovechado su intervención en el Encuentro Internacional de Medios en Santiago de Chile, con motivo del Día Mundial de la Libertad de Prensa y de la firma de la Declaración de Santiago +30, para mostrar su apoyo y respaldo a todos ellos. El también presidente de Henneo ha criticado que se culpe a la prensa y a los jueces cuando se destapan irregularidades que tienen que ver con el poder. \"Detrás está el viejo acoso del poder a los medios que hoy se disfraza de bulos y de nuevos paradigmas\", ha denunciado De Yarza, que ha hablado de \"tentaciones totalitarias\" por parte de los gobiernos. En esta línea, De Yarza ha hecho un llamamiento a la sociedad civil para que \"apoyen a los medios que practican el periodismo de verdad y comprometido frente al pozo de odio y desinformación que suponen las redes sociales\" y ha recordado que los medios, que se han convertido en \"resilientes\", son \"la piedra angular de la libertad de expresión y la llave de todas las libertades\". Por eso, ha respaldado firmemente la Declaración de Santiago+30 que ha firmado como presidente de WAN-IFRA. \"Es muy importante que sea la luz que nos guie en un futuro que tenemos que ganar\". Además de Fernando de Yarza, también han participado en el encuentro el rector de la Universidad Católica de Santiago de Chile, Ignacio Sánchez; el presidente de la Sociedad Interamericana de Prensa, Roberto Rock; y el presidente de la Asociación Nacional de Prensa de Chile, Eduardo Sepúlveda. Todos han coincidido en el \"papel clave\" de la prensa y la necesidad de combatir los ataques a la libertad de prensa y de \"la nueva mirada\" que supone esta nueva Declaración de Santiago. La Declaración de Santiago + 30 surge en el entorno de la reunión convocada nuevamente por Unesco en esta ciudad para celebrar el Día Mundial de la Libertad de Prensa. En 1994 se hizo bajo el lema El Desarrollo de los Medios de Comunicación y la Democracia en América Latina y el Caribe y en esta oportunidad el tema de la reunión será El periodismo ante la crisis ambiental. El contenido de la Declaración de Santiago + 30 será presentado este viernes en la Conferencia del Día Mundial de la Libertad de Prensa 2024, organizada por la Unesco. En concreto, durante el panel titulado Perspectivas sobre cómo actualizar la Declaración de Santiago a los nuevos tiempos, en el que participarán los presidentes de la WAN-IFRA, Fernando De Yarza López-Madrazo, y de la SIP, Roberto Rock, además de Martha Ramos, presidenta World Editors Forum; Carlos Jornet, presidente de la Comisión de Libertad de Prensa e Información, SIP; Cristina Zahar, representante del Comité para la Protección de los Periodistas, y Eduardo Sepúlveda, presidente de la Asociación Nacional de la Prensa de Chile.",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/imagen-de-whatsapp-2024-05-02-a-las-16-34-38-b7ff88e8.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Comunicación"
        ],
        "medio": "20minutos"
    },
    {
        "title": "OBK une a políticos de izquierdas y derechas, que lo dan todo en su actuación por el Dos de Mayo: \"El rebajar el tono era esto\"",
        "pubDate": "2024-05-02 11:35:04",
        "link": "https://www.20minutos.es/gonzoo/noticia/5241561/0/obk-une-politicos-izquierdas-derechas-que-dan-todo-su-concierto-por-dos-mayo-rebajar-tono-era-esto/",
        "guid": "https://www.20minutos.es/gonzoo/noticia/5241561/0/obk-une-politicos-izquierdas-derechas-que-dan-todo-su-concierto-por-dos-mayo-rebajar-tono-era-esto/",
        "author": "20minutos",
        "thumbnail": "",
        "description": "Ayuso, Ángel Víctor Torres o Almeida han disfrutado de las canciones de Jordi Sánchez, vocalista de la banda.",
        "content": "La Casa de Correos ha acogido este jueves el tradicional acto del Dos de Mayo, en el que han condecorado a distintas personalidades y han celebrado el Día de la Comunidad de Madrid. Pero, en esta celebración, el toque musical lo puso Jordi Sánchez, de OBK, que levantó a los asistentes. Entre los presentes estaban Reyes Maroto, portavoz del PSOE en el Ayuntamiento de Madrid, Ángel Víctor Torres, ministro socialista de Política Territorial, José Luis-Martínez Almeida, alcalde de Madrid, y, por supuesto, Isabel Díaz Ayuso. La presidenta de la comunidad ha dirigido el acto, en el que se ha galardonado con la Cruz de Mayo a Telefónica, al cabo José Antonio Rosa Alcocer (a título póstumo), al jugador de baloncesto Rudy Fernández, al periodista Constantino Mediavilla, a Camela, al Rayo Vallecano y a los reporteros de Grupo Crónica. Tras la entrega, Ayuso ha pronunciado su discurso, en el que ha proclamado que \"Madrid está eternamente al servicio de España, porque habla en nombre de todos\". Y, tras esto, OBK ha cerrado el acto. El vocalista, Jordi Sánchez, que también actuará este jueves a las 21 en la Puerta del Sol para celebrar el Dos de Mayo, ha cantado en directo sus temas Historias de amor y El cielo no entiende, y ha levantado a la Casa de Correos, donde todos los asistentes han aplaudido y bailado al ritmo de la música. De hecho, sus canciones han llamado mucho la atención entre los espectadores que estaban siguiendo el evento, pues han servido de unión para la izquierda y la derecha, que han disfrutado a partes iguales de la música. \"La política es una fiesta\", ha celebrado una tuitera. \"OBK está haciendo bailar a la Comunidad de Madrid y al Gobierno. El rebajar el tono era esto\", ha comentado otro usuario.",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/entrega-de-condecoraciones-grandes-cruces-de-la-orden-del-dos-de-mayo.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Gonzoo"
        ],
        "medio": "20minutos"
    },
    {
        "title": "Carta de Sánchez a la militancia: califica al PSOE como \"partido sistémico\" y vuelve a cargar contra las webs \"que fabrican bulos\"",
        "pubDate": "2024-05-02 09:29:41",
        "link": "https://www.20minutos.es/noticia/5241527/0/sanchez-reivindica-psoe-como-partido-sistemico-pero-sigue-sin-anunciar-medidas-ante-avance-agenda-regresiva/",
        "guid": "https://www.20minutos.es/noticia/5241527/0/sanchez-reivindica-psoe-como-partido-sistemico-pero-sigue-sin-anunciar-medidas-ante-avance-agenda-regresiva/",
        "author": "Daniel Ríos",
        "thumbnail": "",
        "description": "El presidente del Gobierno, Pedro Sánchez, envió este jueves una carta a la militancia del PSOE para agradecer a los afiliados las movilizaciones de la semana...",
        "content": "El presidente del Gobierno, Pedro Sánchez, envió este jueves una carta a la militancia del PSOE para agradecer a los afiliados las movilizaciones de la semana pasada para que se mantuviera al frente del Ejecutivo. En su misiva, dedicada a celebrar el 145 aniversario de la formación socialista, Sánchez asegura que el PSOE es \"el partido sistémico de la democracia y la Constitución española\" y alerta de nuevo ante el peligro que sufre una democracia que, dijo, está \"en juego\". El presidente, no obstante, volvió a no anunciar ninguna medida concreta para atajar \"el avance de una internacional ultraderechista que trata de imponer su agenda regresiva\". En su carta, Sánchez agradece haber \"sentido el apoyo de miles de socialistas, de progresistas, de demócratas\" en los últimos días, y afirma tener \"una inmensa deuda de gratitud con todas esas personas, con todos vosotros y vosotras\". \"He sentido el cariño personal, la preocupación por mi familia y por mí. Es precisamente esa preocupación por las personas el motor último de nuestra causa política. Porque el socialismo es humanismo. Pero sé bien que no es el apoyo a mi persona lo que nos une. Por encima de todo, nos une el apoyo a una causa\", sostiene el presidente. Esa causa, plantea Sánchez, pasa por defender \"lo que está en juego, y no solo en España\", que a su juicio \"es la democracia como una forma de convivencia en libertad\". \"Nuestra democracia, como las del resto del mundo, se enfrenta al avance de una internacional ultraderechista que trata de imponer su agenda regresiva, no mediante el debate de ideas y el contraste de propuestas, sino por la destrucción del adversario\", alerta la carta, que dibuja el funcionamiento de lo que llama \"la máquina del fango, alentada por la derecha y la ultraderecha, junto a páginas web y asociaciones ultraderechistas\". Esos actores, sostiene Sánchez, \"fabrican bulos y mentiras\", \"bulos que a continuación se propagan en tertulias y en las tribunas para después judicializar falsas denuncias, deteriorando gravemente nuestra democracia y nuestra convivencia\". \"Estos días hemos comprendido que defender la democracia no consiste únicamente en acudir a votar cada cuatro años. Debemos defender nuestra democracia todos los días, rechazando a aquellos que convierten la política en un barrizal de insultos y falsedades\", argumenta el presidente del Gobierno. Para Sánchez, el mensaje que enviaron las movilizaciones del pasado fin de semana para pedirle que siguiera en la Moncloa \"han enviado un poderoso mensaje de coraje y lucidez a nuestra sociedad: que no estamos dispuestos a asistir impasibles al deterioro y la degradación de nuestra democracia\". \"También han enviado otro mensaje: el PSOE es el partido sistémico de la democracia y la Constitución española. Cuanto más fuerte es la democracia, más fuerte es el PSOE y mayor su capacidad transformadora\", afirma el presidente. Y, \"por esa razón, la principal tarea de nuestro partido es contribuir al fortalecimiento de nuestra democracia\". \"Le quedan muchos años de liderazgo\" Poco después de conocerse la misiva a la militancia, el ministro de la Presidencia, Justicia y Relaciones con las Cortes, Félix Bolaños, ha dicho que a Sánchez le quedan \"muchos años de liderazgo\" al frente del Gobierno y que el \"proyecto de transformación de la sociedad\" de los socialistas \"merece mucho la pena\". \"Le quedan tantos años como quieran los españoles\", ha asegurado antes de su visita al Instituto Nacional de Toxicología y Ciencias Forenses en la Universidad Pablo de Olavide de Sevilla. Una afirmación en la misma línea de lo que dijo el propio Sánchez, hace dos días, en una entrevista en la Cadena Ser en la que asegura que a su Gobierno le quedaban tres años más legislatura \"y lo que quieran los españoles con su voto\".",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/carta-de-sanchez-a-los-militantes-del-psoe.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Nacional"
        ],
        "medio": "20minutos"
    },
    {
        "title": "La crítica de Alfonso Guerra a Sánchez en 'The Times': \"Es cada vez más autócrata y está cavando su propia tumba\"",
        "pubDate": "2024-05-02 16:21:24",
        "link": "https://www.20minutos.es/noticia/5241635/0/sanchez-es-cada-vez-mas-autocrata-esta-cavando-su-propia-tumba-las-palabras-alfonso-guerra-the-times/",
        "guid": "https://www.20minutos.es/noticia/5241635/0/sanchez-es-cada-vez-mas-autocrata-esta-cavando-su-propia-tumba-las-palabras-alfonso-guerra-the-times/",
        "author": "20minutos",
        "thumbnail": "",
        "description": "El exvicepresidente dice que el parón ha sido \"un cálculo político\" y que el socialista está \"dividiendo\" España.",
        "content": "Alfonso Guerra, el que fuera vicepresidente del Gobierno de Felipe González de 1982 a 1991, ha cargado contra el presidente del Ejecutivo, Pedro Sánchez, en una entrevista en The Times. El histórico socialista no ha dudado en tachar a Sánchez de \"autócrata\" al ser preguntado por el citado medio por el descanso de cinco días del presidente. \"Es cada vez más autócrata y está cavando su propia tumba\", ha señalado Guerra, que también ha puesto de manifiesto que las acciones de los últimos días \"no son compatibles con una democracia parlamentaria\". En esta línea, Guerra cree que Sánchez está \"dividiendo las dos Españas\", y cuenta al rotativo británico que la decisión de reflexionar durante cinco días tras conocer la investigación penal contra su esposa, Begoña Gómez, por tráfico de influencias, ha sido \"un cálculo político\" porque no solo anunció este lunes que permanecería en el Gobierno, sino que afirmó tener la intención de ganar otro mandato. \"Este estilo presidencial recuerda las tensiones de la década de 1930, cuando un líder decía 'yo decido y el pueblo escucha y aplaude\", señala Guerra a The Times. \"Es una señal de su enfoque autocrático cada vez más peligroso\", agrega. Tezanos y su \"reputación empañada\" Pero Guerra no solo habla de Sánchez en la entrevista, también opina sobre la encuesta flash del Centro de Investigaciones Sociológicas (CIS) que se publicó inmediatamente después de su decisión y que ha sido denunciada por ERC y PP ante la Junta Electoral Central. \"Fue obra de un encuestador estatal con una reputación empañada por adaptar los resultados a las necesidades políticas de Sánchez\", asevera en referencia a José Félix Tezanos, presidente del organismo. En opinión de Guerra, todo lo ocurrido en el seno del Gobierno en los últimos días \"ha provocado un grave deterioro de la imagen internacional de España\". \"Requirió mucho esfuerzo construir el prestigio de España en la transición que puso a España en el mapa después de la larga dictadura de Franco. Recuperarlo costará mucho\", afirma. \"España se encuentra en un grave estado de confrontación\", agrega. \"El socialismo están en decadencia\" En este sentido, Guerra también pone en el foco de la entrevista la decisión de Sánchez de reforzar el control de los medios después de que se usaran artículos de medios para reforzar la denuncia contra su esposa. \"La prensa es un elemento central de la democracia. Existe un Código Penal para abordar la difamación. No hay necesidad de más\", sentencia. El histórico socialista también habla de la renovación del Consejo General del Poder Judicial (CGPJ) y hace hincapié en que el presidente del Gobierno está haciendo una \"persecución del sistema judicial en un momento en el que los pilares de la democracia española se tambalean por los acontecimientos\". Guerra, que siempre ha sido muy crítico con la ley de amnistía, también pone de manifiesto en la entrevista que \"el socialismo están en decadencia\" por culpa de \"las concesiones de Sánchez a los separatistas catalanes a cambio de mantenerlo en el poder\".",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/el-exvicepresidente-del-gobierno-alfonso-guerra.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Nacional"
        ],
        "medio": "20minutos"
    },
    {
        "title": "Biden rompe su silencio y condena por primera vez las protestas propalestinas: \"Debe prevalecer el orden\"",
        "pubDate": "2024-05-02 15:24:30",
        "link": "https://www.20minutos.es/noticia/5241634/0/biden-condena-violencia-las-protestas-universitarias-contra-guerra-gaza/",
        "guid": "https://www.20minutos.es/noticia/5241634/0/biden-condena-violencia-las-protestas-universitarias-contra-guerra-gaza/",
        "author": "EFE",
        "thumbnail": "",
        "description": "El presidente de Estados Unidos, Joe Biden, condenó este jueves la violencia en las protestas universitarias contra la guerra en Gaza durante un discurso en...",
        "content": "El presidente de Estados Unidos, Joe Biden, ha condenado este jueves la violencia en las protestas universitarias contra la guerra en Gaza durante un discurso convocado \"de urgencia\" en la Casa Blanca. \"La protesta violenta no está protegida, la protesta pacífica sí lo está\", afirmó. Esta es la primera vez que el mandatario emite una declaración propia sobre las protestas estudiantiles propalestinas, algo que hasta ahora ha dejado a sus portavoces. De este modo, en apenas tres minutos Biden defendió el derecho de los estudiantes a manifestarse, pero insistió en que \"debe prevalecer el orden\" ante los disturbios que se han registrado en los últimos días. Y es que son ya alrededor de 1.600 los manifestantes detenidos en protestas convocadas en campus universitarios de todo el país, donde los estudiantes piden el fin de la cooperación de sus instituciones con el gobierno israelí. \"Nada de esto es una protesta pacífica\" En este sentido, Biden ha insistido en que las protestas pacíficas \"sí están protegidas\". \"Es ilegal cuando se produce violencia. Destruir propiedades no es una protesta pacífica, es ilegal. El vandalismo, los allanamientos, romper ventanas, paralizar los campus, forzar la cancelación de clases y graduaciones. Nada de esto es una protesta pacífica\", enfatizó el presidente estadounidense. Asimismo, el mandatario añadió que \"la disidencia es esencial para la democracia\", pero que esta \"nunca debe derivar en el desorden y nunca debe resultar en que se niegan los derechos que tienen otros estudiantes para terminar el semestre y su educación universitaria\". El presidente, que se había mantenido en silencio en los últimos días sobre la extensión de las protestas por todo el país, afirmó que en los campus universitarios \"no hay lugar para el discurso de odio o la violencia de ningún tipo\", ya sea \"antisemitismo, islamofobia\" o discriminación contra los estudiantes de origen árabe o palestino. No se replantea sus políticas hacia Israel Al término de su discurso, Biden respondió con un seco \"no\" cuando un periodista le preguntó si las protestas universitarias le habían hecho reconsiderar sus políticas hacia Israel. También contestó negativamente cuando le preguntaron si los reservistas de la Guardia Nacional deberían intervenir en estas protestas, algo a lo que recurrió el gobernador de Texas, el republicano Greg Abbott, para reprimir a los manifestantes de la Universidad de Texas en Austin. La última vez que Biden se pronunció sobre las manifestaciones fue el 22 de abril, cuando, en respuesta a preguntas de los periodistas, dijo que condenaba las \"protestas antisemitas\" y a \"aquellos que no entienden lo que está ocurriendo con los palestinos\".",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/04/24/520190f300d628c8b46aca5f7c2435977302856d.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Internacional"
        ],
        "medio": "20minutos"
    },
    {
        "title": "Decenas de manifestantes propalestinos detenidos tras irrumpir la policía en el campamento de la UCLA",
        "pubDate": "2024-05-02 13:26:24",
        "link": "https://www.20minutos.es/noticia/5241596/0/decenas-manifestantes-propalestinos-detenidos-tras-irrumpir-policia-campamento-ucla/",
        "guid": "https://www.20minutos.es/noticia/5241596/0/decenas-manifestantes-propalestinos-detenidos-tras-irrumpir-policia-campamento-ucla/",
        "author": "EFE",
        "thumbnail": "",
        "description": "La Policía de Los Ángeles comenzó a desmantelar las barricadas del campus en la madrugada de este jueves.",
        "content": "Numerosos agentes de Policía han irrumpido este jueves en el campamento propalestino instalado en el campus de la Universidad de California (UCLA) en Los Ángeles, llevando a cabo decenas de detenciones de manifestantes universitarios. La operación comenzó en la madrugada, cuando la Policía de Los Ángeles lanzó bengalas que provocaron fuertes explosiones sobre el campamento, según Los Angeles Times. A continuación, los agentes comenzaron a desmontar las barricadas metálicas y de madera levantadas para proteger las tiendas. La UCLA había lanzado un aviso con antelación para anunciar el inicio de esta intervención policial, avisando de que a quienes siguieran en el campamento podían estar cometiendo un delito. Asimismo, ha advertido a los estudiantes que se estuvieran manifestando de que se arriesgaban a sufrir \"medidas disciplinarias\", entre ellas la expulsión de la universidad. Las autoridades iban con equipos antidisturbios, cascos, máscaras antigás, bridas y preparando sus porras al acceder al campamento de los manifestantes que protestan por la guerra de Israel en Gaza. Algunos de los manifestantes se arrodillaron en el suelo con los brazos atados a la espalda mientras los agentes los detenían y continuaban sacando a más personas fuera del campamento, asegura la CNN. Una vez detenidos, eran trasladados en autobuses ubicados en las inmediaciones del campus universitario californiano. Enfrentamientos con proisraelíes la noche anterior La intervención se produjo después de que grupos de manifestantes proisraelíes vestidos de negro y con máscaras blancas se enfrentaran la noche anterior a los estudiantes propalestinos instalados en el recinto universitario. Tras estos altercados, la UCLA canceló sus clases hasta el viernes para frenar los enfretamientos violentos entre ambos grupos. Según informó el Departamento de Policía de Los Ángeles (LAPD) en sus redes sociales, tuvieron que desplegar a los agentes a primera hora del miércoles debido a \"múltiples actos de violencia\" que se habían desarrollado en la instalación del campus. La actuación policial en Los Ángeles se suma a los incidentes similares que durante los últimos días han tenido lugar en decenas de universidades de todo Estados Unidos y que se han saldado con varios cientos de detenciones. En este sentido, los incidentes más graves han ocurrido en Columbia y en Wisconsin.",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/04/26/manifestantes-propalestinos.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Internacional"
        ],
        "medio": "20minutos"
    },
    {
        "title": "Más de 1.500 detenidos, choque con la Policía... EEUU vive una oleada de protestas propalestinas en los campus de todo el país",
        "pubDate": "2024-05-02 15:30:09",
        "link": "https://www.20minutos.es/noticia/5241604/0/mas-1-500-detenidos-barricadas-universidades-enfrentamientos-con-policia-que-esta-pasando-ee-uu/",
        "guid": "https://www.20minutos.es/noticia/5241604/0/mas-1-500-detenidos-barricadas-universidades-enfrentamientos-con-policia-que-esta-pasando-ee-uu/",
        "author": "Sara Méndez",
        "thumbnail": "",
        "description": "Hace meses que la guerra entre Hamás e Israel traspasó las fronteras físicas y provocó reacciones diferentes en diversas partes del mundo.",
        "content": "Las voces de los estudiantes estadounidenses resuenan con fuerza en los campus universitarios de todo el país para exigir el fin de la guerra en Gaza. Desde hace dos semanas, una oleada de protestas contra el apoyo del Gobierno de EEUU a Israel en su ofensiva contra la Franja de Gaza ha inundado más de 25 universidades y establecido un movimiento de protestas propalestino sin precedentes. El presidente estadounidense, Joe Biden, ha condenado la violencia en las manifestaciones este jueves en su primera declaración sobre lo que está ocurriendo en las universidades de todo el país. De esta forma, ha reafirmado que \"las protestas no son pacíficas\", además de subrayar la necesidad de que \"prevalezca el orden\". Son ya alrededor de 1.600 los manifestantes detenidos por las autoridades policiales desde el 18 de abril, según ha señalado The Washington Post. El último operativo ha sido en el campus de la Universidad de California (UCLA) en Los Ángeles, donde los agentes desmantelaron este jueves un campamento propalestino instalado desde el martes, y ha arrestado a decenas de protestantes. Según ha señalado la cadena CNN, la Policía había considerado esta instalación como \"asamblea ilegal\", y la dirección de la UCLA alertó a los manifestantes de la inmediatez de la intervención policial. Asimismo, alertó de que quienes siguieran entonces en el campamento podrían \"estar cometiendo un delito\" y los estudiantes que se estuvieran manifestando se arriesgaban a \"ser expulsados\" de la universidad. Además, durante la madrugada del miércoles se produjeron diversos enfrentamientos contra manifestantes pro-israelíes que aparecieron encapuchados y enmascarados en el campamento arrojando objetos contra los propalestinos. Tras este altercado, en la madrugada de este jueves los agentes comenzaron a derribar las barricadas para desmantelar el campamento e ir trasladando a los detenidos en autobuses. La Universidad de Columbia: epicentro de las protestas La 'zona cero' de las protestas ha sido la Universidad de Columbia, en Nueva York, donde los estudiantes llevaban manifestándose desde el 17 de abril. Allí, los universitarios tomaron el emblemático Hamilton Hall, ocupado también por estudiantes en las protestas contra la guerra de Vietnam en 1968, y finalmente las protestas han culminado en la noche de este martes con cerca de 300 detenciones por parte de la Policía neoyorquina. De acuerdo con la BBC, los agentes desalojaron a cientos de alumnos que permanecían atrincherados en las instalaciones educativas exigiendo el boicot a empresas e individuos con vínculos con Israel. Los protestantes habían bloqueado los accesos con mesas y sillas apiladas en los pasillos a modo de barricadas, pero las autoridades consiguieron finalmente desmantelarlas. En este sentido, ya han comparecido al menos 20 detenidos ante un tribunal de Nueva York durante la noche de este jueves, en base a información compartida por NBC News. Noventa detenidos en Dartmouth y 34 en Wisconsin Las protestas también se han desplazado a la ciudad de Hanover, en New Hampshire, donde noventa estudiantes del Dartmouth College fueron arrestados este miércoles por las autoridades estadounidenses, acusados de haber cometido \"delitos de allanamiento de morada y resistencia al arresto\", según fuentes policiales citadas por la CNN. Las detenciones se produjeron después de la instalación de otro campamento propalestino en el campus de Dartmouth Green, una acción que el departamento de seguridad universitario no había permitido. Ante la negativa de algunos manifestantes a retirarse, los agentes policiales fueron sacándolos \"uno por uno\" de la multitud, deteniéndolos con bridas. Por su parte, en la Universidad de Wisconsin-Madison la policía ha desmantelado durante la mañana de este miércoles otro campamento propalestino en el que han detenido al menos a 34 estudiantes. Aproximadamente 30 de ellos han sido citados a declarar tras resistirse \"a la acción policial de retirar las tiendas de campaña o interferir de cualquier otro modo en la operación\", según ha explicado la rectora Jennifer L. Mnookin, en una carta citada por la CNN. Fordham, Texas y Buffalo De nuevo en Nueva York, la Policía también ha detenido al menos a 15 personas en la noche de este miércoles tras dispersar un campamento en el campus Lincoln Center de la Universidad de Fordham. Según recoge la CNN, los manifestantes se habían instalado en el edificio Lowenstein de la universidad para protestar contra el apoyo a Israel en la guerra con Gaza, y desde el departamento policial neoyorquino esperan que aumente el número de arrestos. Por su parte, en la Universidad de Buffalo de la misma ciudad, fueron arrestadas alrededor de una quincena de manifestantes tras una protesta propalestina llevada a cabo durante la noche de este miércoles en el campus norte de la universidad, y paralelamente otras 17 fueron detenidas en el campus de Dallas de la Universidad de Texas por los mismos motivos.",
        "enclosure": {
            "link": "https://imagenes.20minutos.es/files/image_1920_1080/uploads/imagenes/2024/05/02/agentes-de-la-policia-de-los-angeles-frente-a-manifestantes-propalestinos-del-campus-de-la-ucla.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Internacional"
        ],
        "medio": "20minutos"
    },
    {
        "title": "El Barcelona busca en Atenas el billete para la Final Four",
        "pubDate": "2024-05-02 16:58:36",
        "link": "https://www.abc.es/deportes/baloncesto/olympiacos-barcelona-directo-hoy-20240502174209-di.html",
        "guid": "https://www.abc.es/deportes/baloncesto/olympiacos-barcelona-directo-hoy-20240502174209-di.html",
        "author": "",
        "thumbnail": "",
        "description": "",
        "content": "",
        "enclosure": {
            "link": "https://s3.abcstatics.com/abc/www/multimedia/deportes/2024/05/02/Kalinic-RYfNS3MS3SnXL7WkJ3zxt3K-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "Un joven de 17 años mata a su madre adoptiva a cuchilladas tras una discusión en Badajoz",
        "pubDate": "2024-05-02 16:46:22",
        "link": "https://www.abc.es/sociedad/joven-anos-mata-madre-tras-discusion-badajoz-20240502180515-nt.html",
        "guid": "https://www.abc.es/sociedad/joven-anos-mata-madre-tras-discusion-badajoz-20240502180515-nt.html",
        "author": "",
        "thumbnail": "",
        "description": "La Policía Nacional ha detenido a un menor de 17 años de edad este jueves en Badajoz como presunto autor de la muerte de su madre tras una discusión, según recoge Europa Press.En concreto, sobre las 14.35 horas, la Policía ha recibido una llamada en la que un joven manifestaba que había discutido con su madre, de 60 años de edad, y la había agredido con un arma blanca , según han informado fuentes policiales.El periódico ' Hoy ' informa de que el menor ha confesado los hechos a las autoridades, a quienes les ha explicado que ha matado a su madre adoptiva acuchillándola , tras una discusión, y a su perro. En ese momento, en la casa también se encontraba su hermana.Los hechos han tenido lugar en una vivienda de la calle América, hasta donde se han desplazado varias dotaciones policiales y los servicios sanitarios, que han certificado su muerte.Asimismo, se ha procedido a la detención del supuesto autor, un menor de 17 años de edad, mientras que la investigación para aclarar lo ocurrido continúa abierta .",
        "content": "La Policía Nacional ha detenido a un menor de 17 años de edad este jueves en Badajoz como presunto autor de la muerte de su madre tras una discusión, según recoge Europa Press.En concreto, sobre las 14.35 horas, la Policía ha recibido una llamada en la que un joven manifestaba que había discutido con su madre, de 60 años de edad, y la había agredido con un arma blanca , según han informado fuentes policiales.El periódico ' Hoy ' informa de que el menor ha confesado los hechos a las autoridades, a quienes les ha explicado que ha matado a su madre adoptiva acuchillándola , tras una discusión, y a su perro. En ese momento, en la casa también se encontraba su hermana.Los hechos han tenido lugar en una vivienda de la calle América, hasta donde se han desplazado varias dotaciones policiales y los servicios sanitarios, que han certificado su muerte.Asimismo, se ha procedido a la detención del supuesto autor, un menor de 17 años de edad, mientras que la investigación para aclarar lo ocurrido continúa abierta .",
        "enclosure": {
            "link": "https://s1.abcstatics.com/abc/www/multimedia/sociedad/2024/05/02/suceso-badajoz--758x531.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "El complicado futuro del CD Badajoz: dos descensos en un año y una millonaria deuda en Segunda RFEF",
        "pubDate": "2024-05-02 16:40:00",
        "link": "https://www.abc.es/deportes/futbol/complicado-futuro-badajoz-dos-descensos-ano-millonaria-20240502181146-nt.html",
        "guid": "https://www.abc.es/deportes/futbol/complicado-futuro-badajoz-dos-descensos-ano-millonaria-20240502181146-nt.html",
        "author": "",
        "thumbnail": "",
        "description": "El CD Badajoz , que el pasado fin de semana firmaba su segundo descenso de categoría en menos de un año, atraviesa no solo una complicada situación deportiva, también económica, según ha explicado este jueves en rueda de prensa Javier Peña, director general del club. El conjunto blanquinegro consumaba en la última jornada su descenso a Tercera Federación y este jueves Javier Peña ha explicado la difícil situación económica del club, que el marzo volvía a manos del grupo Lanuspe (Luis Olivier). El director general ha acusado al grupo mexicano que gestionó anteriormente la entidad de haber dejado «tiritando» la caja.Según los datos aportados por Peña, los ingresos por patrocinios, subvenciones, abonos y taquilla han ascendido a 959.000 euros, mientras que los gastos de plantilla y trabajadores superan a 3.269.000 euros, por lo que el CD Badajoz acumula esta temporada una deuda de 2,3 millones de euros.Noticia Relacionada Fútbol estandar No El filial de la UD Almería firma una goleada propia de otra época Jorge Abizanda El conjunto rojiblanco vence por 14-1 al Atlético Melilla en su partido de Tercera FederaciónA pesar de esa cuantiosa deuda y del desfase en el presupuesto de esta temporada, el grupo Lanuspe ha explicado su hoja de ruta: «Ni el club desaparece, ni se vende». La idea es hacer un proyecto acorde a la Tercera Federación, pero ambicioso para intentar ascender y regresar a Segunda RFEF.",
        "content": "El CD Badajoz , que el pasado fin de semana firmaba su segundo descenso de categoría en menos de un año, atraviesa no solo una complicada situación deportiva, también económica, según ha explicado este jueves en rueda de prensa Javier Peña, director general del club. El conjunto blanquinegro consumaba en la última jornada su descenso a Tercera Federación y este jueves Javier Peña ha explicado la difícil situación económica del club, que el marzo volvía a manos del grupo Lanuspe (Luis Olivier). El director general ha acusado al grupo mexicano que gestionó anteriormente la entidad de haber dejado \"tiritando\" la caja.Según los datos aportados por Peña, los ingresos por patrocinios, subvenciones, abonos y taquilla han ascendido a 959.000 euros, mientras que los gastos de plantilla y trabajadores superan a 3.269.000 euros, por lo que el CD Badajoz acumula esta temporada una deuda de 2,3 millones de euros.Noticia Relacionada Fútbol estandar No El filial de la UD Almería firma una goleada propia de otra época Jorge Abizanda El conjunto rojiblanco vence por 14-1 al Atlético Melilla en su partido de Tercera FederaciónA pesar de esa cuantiosa deuda y del desfase en el presupuesto de esta temporada, el grupo Lanuspe ha explicado su hoja de ruta: \"Ni el club desaparece, ni se vende\". La idea es hacer un proyecto acorde a la Tercera Federación, pero ambicioso para intentar ascender y regresar a Segunda RFEF.",
        "enclosure": {
            "link": "https://s1.abcstatics.com/abc/www/multimedia/deportes/2024/05/02/badajoz8-R9SFK82qCWs1kfDE58JFS5K-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "Debate elecciones Cataluña: horario y dónde ver en directo en televisión y online hoy",
        "pubDate": "2024-05-02 16:27:31",
        "link": "https://www.abc.es/espana/cataluna/debate-elecciones-cataluna-horario-ver-directo-television-20240502182731-nt.html",
        "guid": "https://www.abc.es/espana/cataluna/debate-elecciones-cataluna-horario-ver-directo-television-20240502182731-nt.html",
        "author": "",
        "thumbnail": "",
        "description": "Los catalanes tienen una cita con las urnas este domingo 12 de mayo tras el adelanto electoral convocado por Pere Aragonès después de que no prosperara la aprobación de los Presupuestos. Con la camapaña electoral ya en marcha, los candidatos buscan acercar sus propuestas a la población para hacerse con aquellos votos que les puedan dar la victoria en los comicios.Habrá dos debates para que quienes todavía no tienen decidido su voto puedan conocer más en profundidad las propuestas de cada uno de los líderes y decantarse por un programa. El primero de ambos será este jueves organizado por RTVE .Los rostros para estos debates de las elecciones catalanas son bien conocidos por los ciudadanos, catalanes o no, ya que llevan años al frente de la política de esta comunidad autónoma. En estos comicios los electores deberán decidir nuevamente entre opciones independentistas o no para conformar el Parlamento.Pere Aragonès , de ERC, aspira a mantener la presidencia de la Generalitat. Por su parte, al debate no acudirá Carles Puigdemont , candidato por Junts, que continúa huido de la justicia española. Según las encuestas, el otro gran candidato en liza es Salvador Illa , del PSC, que aspira a repetir o mejorar los resultados de las elecciones de 2021, donde empató a 33 escaños con ERC.¿Quienes participan en el debate electoral de Cataluña?Como ha informado RTVE, en el debate de este jueves participarán ocho grupos políticos que se presentan en estas elecciones.El debate transcurrirá dividido en cuatro bloques y el minuto de oro final . En el primer bloque los candidatos debatirán sobre sanidad, educación, seguridad y vivienda; en el segundo bloque lo harán sobre sistema de financiación y las infraestructuras; el tercero lo protagonizarán la Ley de amnistía y del futuro político de Cataluña. El cuarto y último bloque estará dedicado a posibles pactos y estabilidad.Participantes en el debate de RTVE Salvador Illa, del Partit dels Socialistes de Catalunya (PSC) Pere Aragonès, de Esquerra Republicana de Catalunya (ERC) Josep Rull, de Junts + Puigdemont por Catalunya Ignacio Garriga, de VOX Laia Estrada, de la Candidatura d'Unitat Popular – Defensem la Terra (CUP-DT) Jéssica Albiach, de Comuns Sumar Carlos Carrizosa, de Ciutadans-Partido de la Ciudadanía (Cs) Alejandro Fernández, del Partido Popular (PPC)Los moderadores del debate serán Gemma Nierga y Xabier Fortes y se emitirá desde los estudios de RTVE Cataluña en Sant Cugat del Vallès.Horario y dónde ver el debate de RTVE de las elecciones catalanasEl debate de RTVE se retransmitirá en directo en La 1 y Ràdio 4, en Cataluña, y en el Canal 24 horas y Radio 5 para el resto de España.Noticias Relacionadas estandar Si Elecciones catalanas 2024 Los escenarios posibles en Cataluña tras el 12M: cuatro mayorías y un bloqueo Daniel Tercero estandar No Un manifiesto constitucionalista firmado por históricos socialistas pide no votar al PSC Daniel TerceroAsimismo, en abc.es podrás estar informado de todas las novedades en torno a la camapaña catalana y de lo que suceda en este debate.",
        "content": "Los catalanes tienen una cita con las urnas este domingo 12 de mayo tras el adelanto electoral convocado por Pere Aragonès después de que no prosperara la aprobación de los Presupuestos. Con la camapaña electoral ya en marcha, los candidatos buscan acercar sus propuestas a la población para hacerse con aquellos votos que les puedan dar la victoria en los comicios.Habrá dos debates para que quienes todavía no tienen decidido su voto puedan conocer más en profundidad las propuestas de cada uno de los líderes y decantarse por un programa. El primero de ambos será este jueves organizado por RTVE .Los rostros para estos debates de las elecciones catalanas son bien conocidos por los ciudadanos, catalanes o no, ya que llevan años al frente de la política de esta comunidad autónoma. En estos comicios los electores deberán decidir nuevamente entre opciones independentistas o no para conformar el Parlamento.Pere Aragonès , de ERC, aspira a mantener la presidencia de la Generalitat. Por su parte, al debate no acudirá Carles Puigdemont , candidato por Junts, que continúa huido de la justicia española. Según las encuestas, el otro gran candidato en liza es Salvador Illa , del PSC, que aspira a repetir o mejorar los resultados de las elecciones de 2021, donde empató a 33 escaños con ERC.¿Quienes participan en el debate electoral de Cataluña?Como ha informado RTVE, en el debate de este jueves participarán ocho grupos políticos que se presentan en estas elecciones.El debate transcurrirá dividido en cuatro bloques y el minuto de oro final . En el primer bloque los candidatos debatirán sobre sanidad, educación, seguridad y vivienda; en el segundo bloque lo harán sobre sistema de financiación y las infraestructuras; el tercero lo protagonizarán la Ley de amnistía y del futuro político de Cataluña. El cuarto y último bloque estará dedicado a posibles pactos y estabilidad.Participantes en el debate de RTVE Salvador Illa, del Partit dels Socialistes de Catalunya (PSC) Pere Aragonès, de Esquerra Republicana de Catalunya (ERC) Josep Rull, de Junts + Puigdemont por Catalunya Ignacio Garriga, de VOX Laia Estrada, de la Candidatura d'Unitat Popular – Defensem la Terra (CUP-DT) Jéssica Albiach, de Comuns Sumar Carlos Carrizosa, de Ciutadans-Partido de la Ciudadanía (Cs) Alejandro Fernández, del Partido Popular (PPC)Los moderadores del debate serán Gemma Nierga y Xabier Fortes y se emitirá desde los estudios de RTVE Cataluña en Sant Cugat del Vallès.Horario y dónde ver el debate de RTVE de las elecciones catalanasEl debate de RTVE se retransmitirá en directo en La 1 y Ràdio 4, en Cataluña, y en el Canal 24 horas y Radio 5 para el resto de España.Noticias Relacionadas estandar Si Elecciones catalanas 2024 Los escenarios posibles en Cataluña tras el 12M: cuatro mayorías y un bloqueo Daniel Tercero estandar No Un manifiesto constitucionalista firmado por históricos socialistas pide no votar al PSC Daniel TerceroAsimismo, en abc.es podrás estar informado de todas las novedades en torno a la camapaña catalana y de lo que suceda en este debate.",
        "enclosure": {
            "link": "https://s1.abcstatics.com/abc/www/multimedia/espana/2024/05/02/montaje-candidatos--758x531.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "Excluyen a más de 7.000 candidatos de las oposiciones docentes en Andalucía",
        "pubDate": "2024-05-02 16:26:09",
        "link": "https://www.abc.es/espana/andalucia/excluyen-7000-candidatos-oposiciones-docentes-andalucia-20240502115929-nts.html",
        "guid": "https://www.abc.es/espana/andalucia/excluyen-7000-candidatos-oposiciones-docentes-andalucia-20240502115929-nts.html",
        "author": "",
        "thumbnail": "",
        "description": "La Consejería de Desarrollo Educativo y Formación Profesional de la Junta ha excluido a 7.028 aspirantes de las próximas oposiciones docentes en Andalucía , programadas para junio. Los candidatos han quedado fuera del proceso selectivo al no haber cumplido uno de los requisitos clave de la convocatoria: la presentación de una unidad didáctica dentro del plazo establecido. Aquellos que no han completado este paso han sido automáticamente eliminados del proceso de selección, reduciendo así el número total de candidatos a poco más de 52.000.Pero, ¿qué es la unidad didáctica? Según la Lomloe, es un conjunto estructurado de actividades de enseñanza diseñadas para alcanzar objetivos educativos específicos, adaptados a los nuevos enfoques pedagógicos propuestos por la ley.El plazo para presentarla se extendió del 20 de marzo al 4 de abril , siendo este un requisito fundamental de la convocatoria. Si bien, desde 2018, los profesores interinos no están obligados a realizar exámenes de oposición para permanecer en las bolsas de trabajo.El 12 de diciembre de 2022 se publicó la convocatoria de procedimiento selectivo para el ingreso en los Cuerpos de Profesores de Enseñanza Secundaria, Profesores de Música y Artes Escénicas, Profesores de Artes Plásticas y Diseño, Maestros de Taller de Artes Plásticas y Diseño, Maestros y Profesores Especialistas en Sectores Singulares de Formación Profesional. «El apartado 7.3 de la citada orden de 12 de diciembre de 2022, establece que las personas aspirantes que no entreguen en el plazo establecido la citada unidad no podrán realizar la parte B.1 de la prueba ni podrán, en consecuencia, continuar participando en el procedimiento», señala la Consejería en la resolución publicada el pasado 25 de abril donde se incluye la relación de personas excluidas.¿Cómo afecta a las ratios?El proceso selectivo incluye 2.826 plazas de estabilización , con la mayoría de ellas (2.030) destinadas al cuerpo de Maestros. Además, se han convocado plazas para el cuerpo de Profesores de Enseñanza Secundaria (660), Música y Artes Escénicas (95), Artes Plásticas y Diseño (4), Maestros de Taller de Artes Plásticas y Diseño (4), y profesores especialistas en sectores singulares de Formación Profesional (33). Se reserva un 10% de las plazas para personas con discapacidad igual o superior al 33 por ciento.La salida de más de 7.000 opositores afectará a las ratios de aspirantes por plaza, ya que, aunque el número de plazas en cada especialidad se mantiene, la cantidad de aspirantes por cada plaza disminuye considerablemente. Así, especialidades como la de Primaria del Cuerpo de Maestros pierde 887 aspirantes.El procesoEl concurso-oposición se rige por el Real Decreto 270/2022, que establece que la fase de oposición no será eliminatoria y que el examen práctico solo será obligatorio para algunas especialidades. Los candidatos deben desarrollar un tema y presentar una unidad didáctica, con una calificación mínima de 5 sobre 10 en la suma de ambos. La fase de concurso representa el 40% de la puntuación final, mientras que la fase de oposición aporta el 60% restante.El proceso continuará con la presentación de los candidatos ante el tribunal el 15 de junio, seguido de la parte A de la prueba el día 22, que consistirá en el desarrollo escrito de un tema específico. La parte B de la prueba incluirá la exposición oral de una unidad didáctica y, en el caso de las especialidades de Formación Profesional, un ejercicio práctico.",
        "content": "La Consejería de Desarrollo Educativo y Formación Profesional de la Junta ha excluido a 7.028 aspirantes de las próximas oposiciones docentes en Andalucía , programadas para junio. Los candidatos han quedado fuera del proceso selectivo al no haber cumplido uno de los requisitos clave de la convocatoria: la presentación de una unidad didáctica dentro del plazo establecido. Aquellos que no han completado este paso han sido automáticamente eliminados del proceso de selección, reduciendo así el número total de candidatos a poco más de 52.000.Pero, ¿qué es la unidad didáctica? Según la Lomloe, es un conjunto estructurado de actividades de enseñanza diseñadas para alcanzar objetivos educativos específicos, adaptados a los nuevos enfoques pedagógicos propuestos por la ley.El plazo para presentarla se extendió del 20 de marzo al 4 de abril , siendo este un requisito fundamental de la convocatoria. Si bien, desde 2018, los profesores interinos no están obligados a realizar exámenes de oposición para permanecer en las bolsas de trabajo.El 12 de diciembre de 2022 se publicó la convocatoria de procedimiento selectivo para el ingreso en los Cuerpos de Profesores de Enseñanza Secundaria, Profesores de Música y Artes Escénicas, Profesores de Artes Plásticas y Diseño, Maestros de Taller de Artes Plásticas y Diseño, Maestros y Profesores Especialistas en Sectores Singulares de Formación Profesional. \"El apartado 7.3 de la citada orden de 12 de diciembre de 2022, establece que las personas aspirantes que no entreguen en el plazo establecido la citada unidad no podrán realizar la parte B.1 de la prueba ni podrán, en consecuencia, continuar participando en el procedimiento\", señala la Consejería en la resolución publicada el pasado 25 de abril donde se incluye la relación de personas excluidas.¿Cómo afecta a las ratios?El proceso selectivo incluye 2.826 plazas de estabilización , con la mayoría de ellas (2.030) destinadas al cuerpo de Maestros. Además, se han convocado plazas para el cuerpo de Profesores de Enseñanza Secundaria (660), Música y Artes Escénicas (95), Artes Plásticas y Diseño (4), Maestros de Taller de Artes Plásticas y Diseño (4), y profesores especialistas en sectores singulares de Formación Profesional (33). Se reserva un 10% de las plazas para personas con discapacidad igual o superior al 33 por ciento.La salida de más de 7.000 opositores afectará a las ratios de aspirantes por plaza, ya que, aunque el número de plazas en cada especialidad se mantiene, la cantidad de aspirantes por cada plaza disminuye considerablemente. Así, especialidades como la de Primaria del Cuerpo de Maestros pierde 887 aspirantes.El procesoEl concurso-oposición se rige por el Real Decreto 270/2022, que establece que la fase de oposición no será eliminatoria y que el examen práctico solo será obligatorio para algunas especialidades. Los candidatos deben desarrollar un tema y presentar una unidad didáctica, con una calificación mínima de 5 sobre 10 en la suma de ambos. La fase de concurso representa el 40% de la puntuación final, mientras que la fase de oposición aporta el 60% restante.El proceso continuará con la presentación de los candidatos ante el tribunal el 15 de junio, seguido de la parte A de la prueba el día 22, que consistirá en el desarrollo escrito de un tema específico. La parte B de la prueba incluirá la exposición oral de una unidad didáctica y, en el caso de las especialidades de Formación Profesional, un ejercicio práctico.",
        "enclosure": {
            "link": "https://s1.abcstatics.com/abc/www/multimedia/espana/2024/05/02/oposiciones-docentes-andalucia-Rx3vHKEeMPycYlJgwRMjC6K-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "Demi Vollering se desquita y lidera la Vuelta a España",
        "pubDate": "2024-05-02 16:04:53",
        "link": "https://www.abc.es/deportes/ciclismo/demi-vollering-desquita-lidera-vuelta-espana-20240502180352-nt.html",
        "guid": "https://www.abc.es/deportes/ciclismo/demi-vollering-desquita-lidera-vuelta-espana-20240502180352-nt.html",
        "author": "",
        "thumbnail": "",
        "description": "Holandesa por holandesa en virtud de la incomparable tradición en los Países Bajos por la bicicleta. Demi Vollering se postula como la sucesora de Anemiek van Vleuten, la carismática ciclista del Movistar que se retiró el año pasado y que fue la primera ganadora de la Vuelta a España femenina.Vollering, que fue segunda en 2023, se apresta ahora a capturar la pieza que se la escapó ante su compatriota. En el Alto del Fuerte Rapitán, a las afueras de Jaca, dio un potente zarpazo para ser considerada la gran favorita a la victoria final.«Me he sentido fuerte y me ha hecho mucha ilusión ganar con el maillot de campeona de los Países Bajos. El maillot rojo de líder es muy bonito y espera defenderlo hasta el final», declaró la ciclista del equipo SD Wors , el mejor equipo femenino del mundo.Noticias Relacionadas estandar Si Exdeportistas hablan con abc El cuerpo tras la retirada: «Engordas siempre» José Carlos Carabias estandar Si entrevista Joane Somarriba y Dori Ruano: «Hemos dormido en reformatorios y casas de acogida» José Carlos CarabiasLlega el pelotón hasta la hermosa Jaca y su visión del Pirineo entre un enjambre de incertidumbres, que empiezan con el rendimiento de la líder Mariane Vos en la montaña. Pronto queda despejada esa incógnita. La holandesa no sube.Hay expectación por saber si la española Mavi García podrá alcanzar el tranco de las mejores. También se desaloja pronto la idea. La veterana mallorquina se queda en los primeras rampas del alto más duro, aunque corto de esta edición.Así lo dispone Demi Vollering, en teoría la mejor ciclista del mundo, famosa por una supuesta oferta de un millón de euros por parte del UAE y que no había ganado nada esta temporada. En el Fuerte Rapitán (3,2 kms. al 8,2 por ciento) Vollering impone un ritmo a la antigua, estilo Induráin, sin levantarse del sillín, efecto aspiradora que va devorando adversarias con una presunta facilidad tan difícil de conseguir.Solo dos ciclistas se pegan a la neerlandesa, su compatriota Kastelijn y la italiana Longo Borghini. Nadie le da un relevo a Vollering ante la sospecha luego evidente de que posee más ritmo que las otras. A un kilómetro y medio kilómetros de meta, se confirma. Vollering es más fuerte y viaja sola hacia la victoria de etapa (la primera del año) y el maillot rojo de líder.",
        "content": "Holandesa por holandesa en virtud de la incomparable tradición en los Países Bajos por la bicicleta. Demi Vollering se postula como la sucesora de Anemiek van Vleuten, la carismática ciclista del Movistar que se retiró el año pasado y que fue la primera ganadora de la Vuelta a España femenina.Vollering, que fue segunda en 2023, se apresta ahora a capturar la pieza que se la escapó ante su compatriota. En el Alto del Fuerte Rapitán, a las afueras de Jaca, dio un potente zarpazo para ser considerada la gran favorita a la victoria final.\"Me he sentido fuerte y me ha hecho mucha ilusión ganar con el maillot de campeona de los Países Bajos. El maillot rojo de líder es muy bonito y espera defenderlo hasta el final\", declaró la ciclista del equipo SD Wors , el mejor equipo femenino del mundo.Noticias Relacionadas estandar Si Exdeportistas hablan con abc El cuerpo tras la retirada: \"Engordas siempre\" José Carlos Carabias estandar Si entrevista Joane Somarriba y Dori Ruano: \"Hemos dormido en reformatorios y casas de acogida\" José Carlos CarabiasLlega el pelotón hasta la hermosa Jaca y su visión del Pirineo entre un enjambre de incertidumbres, que empiezan con el rendimiento de la líder Mariane Vos en la montaña. Pronto queda despejada esa incógnita. La holandesa no sube.Hay expectación por saber si la española Mavi García podrá alcanzar el tranco de las mejores. También se desaloja pronto la idea. La veterana mallorquina se queda en los primeras rampas del alto más duro, aunque corto de esta edición.Así lo dispone Demi Vollering, en teoría la mejor ciclista del mundo, famosa por una supuesta oferta de un millón de euros por parte del UAE y que no había ganado nada esta temporada. En el Fuerte Rapitán (3,2 kms. al 8,2 por ciento) Vollering impone un ritmo a la antigua, estilo Induráin, sin levantarse del sillín, efecto aspiradora que va devorando adversarias con una presunta facilidad tan difícil de conseguir.Solo dos ciclistas se pegan a la neerlandesa, su compatriota Kastelijn y la italiana Longo Borghini. Nadie le da un relevo a Vollering ante la sospecha luego evidente de que posee más ritmo que las otras. A un kilómetro y medio kilómetros de meta, se confirma. Vollering es más fuerte y viaja sola hacia la victoria de etapa (la primera del año) y el maillot rojo de líder.",
        "enclosure": {
            "link": "https://s3.abcstatics.com/abc/www/multimedia/deportes/2024/05/02/demi-RnHX2sEqRwgtpquOyFFmwjK-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "El emotivo gesto de Andy y Lucas con Marta del Castillo en su concierto de Sevilla",
        "pubDate": "2024-05-02 16:02:01",
        "link": "https://www.abc.es/sevilla/ciudad/emotivo-gesto-andy-lucas-marta-castillo-concierto-20240502144326-nts.html",
        "guid": "https://www.abc.es/sevilla/ciudad/emotivo-gesto-andy-lucas-marta-castillo-concierto-20240502144326-nts.html",
        "author": "",
        "thumbnail": "",
        "description": "Andy y Lucas están haciendo una gira muy especial antes de despedirse de los escenarios de manera temporal. Desde que a Lucas le diagnosticaron una cardiopatía, el dúo anunció que habían decidido parar por recomendación médica, pero antes han querido despedirse con 'Nuestros últimos acordes' .Los artistas han repetido d os noches seguidas cantando en el Cartuja Center de Sevilla con un lleno absoluto, con un público de todas las edades. Y entre todas esas personas se encontraba el padre de Marta del Castillo.Con la canción 'Pido la palabra' , en 2010, ambos cantantes quisieron mostrar su apoyo a la familia de Marta . Desde entonces siempre la cantan en los conciertos para que nadie se olvide de ella ni de su familia.En esta ocasión los artistas han aprovechado que los padres de Marta del Castillo estaban presentes en el concierto para dedicarles la canción a ellos directamente, con una foto de su hija en la pantalla del escenario mientras cantaban.Antonio del Castillo ha compartido este momento en redes sociales para agradecer a Andy y a Lucas la canción . Además cuenta que eran unos de los grupos favoritos de su hija y que sus canciones siempre sonaban en el coche cuando iban en el coche de camino a la playa.",
        "content": "Andy y Lucas están haciendo una gira muy especial antes de despedirse de los escenarios de manera temporal. Desde que a Lucas le diagnosticaron una cardiopatía, el dúo anunció que habían decidido parar por recomendación médica, pero antes han querido despedirse con 'Nuestros últimos acordes' .Los artistas han repetido d os noches seguidas cantando en el Cartuja Center de Sevilla con un lleno absoluto, con un público de todas las edades. Y entre todas esas personas se encontraba el padre de Marta del Castillo.Con la canción 'Pido la palabra' , en 2010, ambos cantantes quisieron mostrar su apoyo a la familia de Marta . Desde entonces siempre la cantan en los conciertos para que nadie se olvide de ella ni de su familia.En esta ocasión los artistas han aprovechado que los padres de Marta del Castillo estaban presentes en el concierto para dedicarles la canción a ellos directamente, con una foto de su hija en la pantalla del escenario mientras cantaban.Antonio del Castillo ha compartido este momento en redes sociales para agradecer a Andy y a Lucas la canción . Además cuenta que eran unos de los grupos favoritos de su hija y que sus canciones siempre sonaban en el coche cuando iban en el coche de camino a la playa.",
        "enclosure": {
            "link": "https://s2.abcstatics.com/abc/www/multimedia/sevilla/2024/05/02/andy-lucas-martadelcastillo-RLKtBxL1Li6Oo8V0FUh77kJ-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "La OCDE advierte sobre el gasto en pensiones y urge a un ajuste fiscal \"más fuerte y sostenido\"",
        "pubDate": "2024-05-02 15:59:26",
        "link": "https://www.abc.es/economia/ocde-advierte-sobre-gasto-pensiones-espana-urge-20240502103541-nt.html",
        "guid": "https://www.abc.es/economia/ocde-advierte-sobre-gasto-pensiones-espana-urge-20240502103541-nt.html",
        "author": "",
        "thumbnail": "",
        "description": "La Organización para la Cooperación y el Desarrollo Económicos (OCDE) lanza dos advertencias muy claras para España en su último informe de previsiones económicas. Primero, sobre el crecimiento del gasto en pensiones ; segundo, sobre el desequilibrio de las cuentas públicas. «El gasto se inclina fuertemente hacia las pensiones en detrimento del crecimiento, y el gasto relacionado con el envejecimiento aumentará». Así se pronuncia el 'think tank' de las economías avanzadas en el documento, que entre líneas señala que el gasto habría de dedicarse a mejorar el crecimiento, así como la productividad. Noticia Relacionada estandar Si El Banco de España alerta de los riesgos de la inestabilidad política: «sus efectos económicos tienden a ser duraderos» Bruno PérezLa situación de las cuentas públicas también se coloca como un asunto central del informe. La OCDE afirma que nuestro país «necesitará una consolidación fiscal más fuerte y sostenida en el medio plazo», todo para intentar mantener la senda descendente de la deuda pública tras el Covid y cumplir con las reglas fiscales que llegan ya de nuevo. No son pocos los organismos que han advertido recientemente que el endeudamiento público, sin medidas de ajuste, crecerá a medio plazo y dejará a España sin margen para afrontar futuras crisis; el Banco de España es una de las instituciones que ha puesto el foco en este asunto, en su último informe de estabilidad financiera. La OCDE calcula un déficit del 3,3% para este año y del 2,6% para el siguiente, mientras que en términos de deuda pública esta se situará, dice, este año en el 107,1% y en el 106,7% el que viene. Números que complican el cumplimiento de España de las reglas fiscales.Dentro de esa consolidación fiscal que reclama la OCDE, menciona algunas medidas para movilizar ingresos adicionales para las cuentas públicas. Esto incluye una ampliación gradual de la base del IVA, el aumento de impuestos 'verdes', y también mejorar la eficiencia del gasto. Asimismo, la organización reclama también hacer crecer la productividad en España, potenciando la innovación, mejorando las habilidades y reforzando los resultados educativos. La productividad es uno de los deberes que arrastra España desde hace años y en el que han puesto el foco numerosas organizaciones nacionales e internacionales. «Es necesaria una renovación de las políticas activas del mercado laboral para mejorar la eficiencia de la contratación laboral y abordar los desajustes de habilidades», añade el informe.Mejora de la estimación de crecimientoEn términos de crecimiento, la OCDE ha mejorado su estimación para nuestro país en tres décimas hasta dejarla en el 1,8% en 2024 , por debajo todavía de la previsión del Gobierno de Pedro Sánchez. De cara a 2025 calcula un alza del PIB del 2%. Así las cosas, el Gobierno celebra las cifras mostradas por el 'think tank' de las economías avanzadas. «Seguiremos liderando el crecimiento entre las principales economías de la zona euro en 2024 y 2025, con un incremento este año que será más del doble que la media de la eurozona», señala el Ejecutivo. En el caso de la zona euro, la OCDE ha revisado también al alza su estimación de crecimiento hasta el 0,7% y el 1,5% respectivamente para 2024 y 2025. «El consumo privado sustentará el crecimiento respaldado por un mercado laboral resistente y aumentos de los ingresos reales», apunta la OCDE, como recoge Ep, añadiendo que espera que la tasa de inflación armonizada de España caiga al 3% en 2024 y al 2,3% en 2025, mientras que el dato subyacente bajaría al 2,9% este año y al 2,2% el siguiente.Asimismo, como recoge la citada agencia, la organización con sede en París anticipa que la inversión seguirá siendo débil en 2024, aunque confía en que aumentará en 2025 debido a la implementación del Plan de Recuperación, Transformación y Resiliencia (RTRP) , por lo que apunta entre los riesgos a la baja para sus previsiones, además de una mayor escalada de las tensiones geopolíticas que empeorasen la demanda de los principales socios comerciales de España, una implementación más lenta del plan.",
        "content": "La Organización para la Cooperación y el Desarrollo Económicos (OCDE) lanza dos advertencias muy claras para España en su último informe de previsiones económicas. Primero, sobre el crecimiento del gasto en pensiones ; segundo, sobre el desequilibrio de las cuentas públicas. \"El gasto se inclina fuertemente hacia las pensiones en detrimento del crecimiento, y el gasto relacionado con el envejecimiento aumentará\". Así se pronuncia el 'think tank' de las economías avanzadas en el documento, que entre líneas señala que el gasto habría de dedicarse a mejorar el crecimiento, así como la productividad. Noticia Relacionada estandar Si El Banco de España alerta de los riesgos de la inestabilidad política: \"sus efectos económicos tienden a ser duraderos\" Bruno PérezLa situación de las cuentas públicas también se coloca como un asunto central del informe. La OCDE afirma que nuestro país \"necesitará una consolidación fiscal más fuerte y sostenida en el medio plazo\", todo para intentar mantener la senda descendente de la deuda pública tras el Covid y cumplir con las reglas fiscales que llegan ya de nuevo. No son pocos los organismos que han advertido recientemente que el endeudamiento público, sin medidas de ajuste, crecerá a medio plazo y dejará a España sin margen para afrontar futuras crisis; el Banco de España es una de las instituciones que ha puesto el foco en este asunto, en su último informe de estabilidad financiera. La OCDE calcula un déficit del 3,3% para este año y del 2,6% para el siguiente, mientras que en términos de deuda pública esta se situará, dice, este año en el 107,1% y en el 106,7% el que viene. Números que complican el cumplimiento de España de las reglas fiscales.Dentro de esa consolidación fiscal que reclama la OCDE, menciona algunas medidas para movilizar ingresos adicionales para las cuentas públicas. Esto incluye una ampliación gradual de la base del IVA, el aumento de impuestos 'verdes', y también mejorar la eficiencia del gasto. Asimismo, la organización reclama también hacer crecer la productividad en España, potenciando la innovación, mejorando las habilidades y reforzando los resultados educativos. La productividad es uno de los deberes que arrastra España desde hace años y en el que han puesto el foco numerosas organizaciones nacionales e internacionales. \"Es necesaria una renovación de las políticas activas del mercado laboral para mejorar la eficiencia de la contratación laboral y abordar los desajustes de habilidades\", añade el informe.Mejora de la estimación de crecimientoEn términos de crecimiento, la OCDE ha mejorado su estimación para nuestro país en tres décimas hasta dejarla en el 1,8% en 2024 , por debajo todavía de la previsión del Gobierno de Pedro Sánchez. De cara a 2025 calcula un alza del PIB del 2%. Así las cosas, el Gobierno celebra las cifras mostradas por el 'think tank' de las economías avanzadas. \"Seguiremos liderando el crecimiento entre las principales economías de la zona euro en 2024 y 2025, con un incremento este año que será más del doble que la media de la eurozona\", señala el Ejecutivo. En el caso de la zona euro, la OCDE ha revisado también al alza su estimación de crecimiento hasta el 0,7% y el 1,5% respectivamente para 2024 y 2025. \"El consumo privado sustentará el crecimiento respaldado por un mercado laboral resistente y aumentos de los ingresos reales\", apunta la OCDE, como recoge Ep, añadiendo que espera que la tasa de inflación armonizada de España caiga al 3% en 2024 y al 2,3% en 2025, mientras que el dato subyacente bajaría al 2,9% este año y al 2,2% el siguiente.Asimismo, como recoge la citada agencia, la organización con sede en París anticipa que la inversión seguirá siendo débil en 2024, aunque confía en que aumentará en 2025 debido a la implementación del Plan de Recuperación, Transformación y Resiliencia (RTRP) , por lo que apunta entre los riesgos a la baja para sus previsiones, además de una mayor escalada de las tensiones geopolíticas que empeorasen la demanda de los principales socios comerciales de España, una implementación más lenta del plan.",
        "enclosure": {
            "link": "https://s3.abcstatics.com/abc/www/multimedia/economia/2024/05/02/sanchez-montero-congreso-R5RDAMp7tPlbUelDovNmEkP-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "Biden rompe su silencio sobre las protestas pro-palestinas: \"No somos un país sin ley, el orden debe prevalecer\"",
        "pubDate": "2024-05-02 15:58:19",
        "link": "https://www.abc.es/internacional/biden-rompe-silencio-sobre-protestas-propalestinas-pais-20240502174545-nt.html",
        "guid": "https://www.abc.es/internacional/biden-rompe-silencio-sobre-protestas-propalestinas-pais-20240502174545-nt.html",
        "author": "",
        "thumbnail": "",
        "description": "El presidente de EE.UU., Joe Biden , se posicionó este jueves sobre las protestas pro-palestinas que han tomado las universidades y que en los últimos días han derivado en desórdenes y episodios de violencia. «Todos hemos visto las imágenes», dijo sobre las intervenciones policiales para imponer el orden en campus como los de Columbia, en Nueva York, o UCLA, en Los Ángeles. «Ponen a prueba dos principios fundamentales estadounidenses: el derecho a la libertad de expresión, de asamblea pacífica y de que las voces sean escuchadas; y el imperio de la ley. Ambos deben ser respetados», dijo Biden, ante la tesitura a la que se enfrentan las autoridades universitarias, que tienen que conjugar el derecho a la protesta de los estudiantes, pero también a mantener el orden en la vida académica, entre episodios de campamentos ilegales y ocupación de edificios.«La protesta pacífica es una gran tradición estadounidense para responder a asuntos importantes. Pero no somos un país sin ley. Somos una sociedad civilizada y el orden debe prevalecer», dijo el presidente, que hasta ahora había optado por mantenerse al margen de unas protestas que le ponen, en términos políticos, entre la espada y la pared. Por un lado, las movilizaciones a favor de Gaza, contra la operación militar israelí y contra el apoyo de EE.UU. a su gran socio en Oriente Próximo amenazan con recortar todavía más el apoyo del electorado joven, donde Biden sufre mucho. Por el otro, los desórdenes alimentan la narrativa de Donald Trump , su rival en las presidenciales de noviembre, y de sus aliados republicanos de que Biden es débil con la criminalidad y que su Gobierno permite el caos.El presidente solo se había referido a las protestas hace dos semanas, el 22 de abril, cuando condenó los episodios de antisemitismo vinculados a estas movilizaciones, pero añadió, de forma críptica, que también condenaba a «aquellos que no entienden lo que está pasando con los palestinos».Noticia Relacionada estandar No La policía entra en Columbia y desocupa el edificio tomado por activistas pro-palestinos Javier Ansorena | corresponsal en nueva york«Seré claro», dijo en su discurso del martes, que no estaba en su agenda y que incluyó a última hora para tratar de controlar el mensaje ante la avalancha de protestas. «Las protestas violentas no están protegidas en EE.UU. Las protestas pacíficas, sí. El vandalismo, la ocupación de espacios, romper ventanas, cerrar los campus, forzar la cancelación de las clases y de las graduaciones está contra la ley. Nada de esto son protestas pacíficas, lo mismo que amenazar, intimidar o meter miedo a personas. Disentir es esencial para la democracia, pero la disensión nunca debe llevar al desorden.«Hay derecho a protestar, pero no derecho a crear caos», resumió Biden, que también repitió sus palabras contra el acoso y ataques a estudiantes judíos. «No hay lugar en el campus, ni en ningún sitio de E.UU., para el antisemitismo o amenazas de violencia contra estudiantes judíos. No hay lugar para el discurso de odio o la violencia de ningún tipo, sea antisemitismo, islamofobia o discriminación contra árabes estadounidenses».Biden no respondió a las preguntas de los periodistas. Solo cortó con un seco «no» cuando le gritaron si las protestas le van a hacer cambiar sus políticas hacia la guerra de Gaza. Y la misma respuesta cuando le dijeron si apoyaba el envío de la Guardia Nacional a los campus, como han exigido algunos líderes republicanos.",
        "content": "El presidente de EE.UU., Joe Biden , se posicionó este jueves sobre las protestas pro-palestinas que han tomado las universidades y que en los últimos días han derivado en desórdenes y episodios de violencia. \"Todos hemos visto las imágenes\", dijo sobre las intervenciones policiales para imponer el orden en campus como los de Columbia, en Nueva York, o UCLA, en Los Ángeles. \"Ponen a prueba dos principios fundamentales estadounidenses: el derecho a la libertad de expresión, de asamblea pacífica y de que las voces sean escuchadas; y el imperio de la ley. Ambos deben ser respetados\", dijo Biden, ante la tesitura a la que se enfrentan las autoridades universitarias, que tienen que conjugar el derecho a la protesta de los estudiantes, pero también a mantener el orden en la vida académica, entre episodios de campamentos ilegales y ocupación de edificios.\"La protesta pacífica es una gran tradición estadounidense para responder a asuntos importantes. Pero no somos un país sin ley. Somos una sociedad civilizada y el orden debe prevalecer\", dijo el presidente, que hasta ahora había optado por mantenerse al margen de unas protestas que le ponen, en términos políticos, entre la espada y la pared. Por un lado, las movilizaciones a favor de Gaza, contra la operación militar israelí y contra el apoyo de EE.UU. a su gran socio en Oriente Próximo amenazan con recortar todavía más el apoyo del electorado joven, donde Biden sufre mucho. Por el otro, los desórdenes alimentan la narrativa de Donald Trump , su rival en las presidenciales de noviembre, y de sus aliados republicanos de que Biden es débil con la criminalidad y que su Gobierno permite el caos.El presidente solo se había referido a las protestas hace dos semanas, el 22 de abril, cuando condenó los episodios de antisemitismo vinculados a estas movilizaciones, pero añadió, de forma críptica, que también condenaba a \"aquellos que no entienden lo que está pasando con los palestinos\".Noticia Relacionada estandar No La policía entra en Columbia y desocupa el edificio tomado por activistas pro-palestinos Javier Ansorena | corresponsal en nueva york\"Seré claro\", dijo en su discurso del martes, que no estaba en su agenda y que incluyó a última hora para tratar de controlar el mensaje ante la avalancha de protestas. \"Las protestas violentas no están protegidas en EE.UU. Las protestas pacíficas, sí. El vandalismo, la ocupación de espacios, romper ventanas, cerrar los campus, forzar la cancelación de las clases y de las graduaciones está contra la ley. Nada de esto son protestas pacíficas, lo mismo que amenazar, intimidar o meter miedo a personas. Disentir es esencial para la democracia, pero la disensión nunca debe llevar al desorden.\"Hay derecho a protestar, pero no derecho a crear caos\", resumió Biden, que también repitió sus palabras contra el acoso y ataques a estudiantes judíos. \"No hay lugar en el campus, ni en ningún sitio de E.UU., para el antisemitismo o amenazas de violencia contra estudiantes judíos. No hay lugar para el discurso de odio o la violencia de ningún tipo, sea antisemitismo, islamofobia o discriminación contra árabes estadounidenses\".Biden no respondió a las preguntas de los periodistas. Solo cortó con un seco \"no\" cuando le gritaron si las protestas le van a hacer cambiar sus políticas hacia la guerra de Gaza. Y la misma respuesta cuando le dijeron si apoyaba el envío de la Guardia Nacional a los campus, como han exigido algunos líderes republicanos.",
        "enclosure": {
            "link": "https://s2.abcstatics.com/abc/www/multimedia/internacional/2024/05/02/biden-RUC2Vnut4dOhmuEV4njwLXO-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "Mazón se muestra \"preocupado\" por la concentración de mercado si se consuma la fusión de BBVA y Sabadell",
        "pubDate": "2024-05-02 15:57:50",
        "link": "https://www.abc.es/espana/comunidad-valenciana/mazon-muestra-preocupado-concentracion-mercado-consuma-fusion-20240502114542-nt.html",
        "guid": "https://www.abc.es/espana/comunidad-valenciana/mazon-muestra-preocupado-concentracion-mercado-consuma-fusion-20240502114542-nt.html",
        "author": "",
        "thumbnail": "",
        "description": "El presidente de la Generalitat, Carlos Mazón , y los presidentes de la Confederación Empresarial Valenciana (CEV), Salvador Navarro, y las cámaras de comercio valencianas, José Vicente Morata, han mostrado su «preocupación» por la posible fusión entre el BBVA y Sabadell , ya que dos grupos llegarían a concentrar el 60% del mercado bancario en la Comunidad Valenciana y la sede social de la segunda entidad dejaría de estar en Alicante si prospera la oferta planteada.«La noticia no me ha gustado nada», ha manifestado Mazón después de que el BBVA comunicara el martes a la Comisión Nacional del Mercado de Valores (CNMV) su traslado al presidente del consejo de administración del Sabadell del interés por explorar una fusión en la que se generaría el mayor banco de España. Esta operación formaría una entidad con unas 400 oficinas y 2.500 trabajadores en la Comunitat.El jefe del Consell ha explicado que ha contactado «directamente con el Banco Sabadell» a primera hora de este jueves y le han traslado que «están estudiando la operación con detalle, con exhaustividad y en estos momentos están analizando la respuesta que van a dar».«Me preocupa. En primer lugar porque estoy a favor de la competencia , de que los ciudadanos tengan las mayores alternativas posibles. De fraguarse esta operación estaríamos hablando de que en la Comunitat Valenciana dos grandes entidades financieras concentran casi el 60% del mercado, y a mí esto no me parece una buena noticia. Yo quiero más entidades financieras en las que los ciudadanos puedan elegir», ha expuesto a los periodistas junto al presidente de la CEV antes de un acto organizado por 'La Vanguardia' en Valencia.MÁS INFORMACIÓN noticia No Mazón apela a la «cautela» ante una posible fusión BBVA-Sabadell aunque ofrece Alicante como sedeParalelamente, Mazón ha advertido que estarán «vigilantes» ante la posibilidad de que la sede social deje de estar en Alicante , ciudad a la que el Sabadell la trasladó en 2017 ante la situación política en Catalunya. «Tenemos que defender nuestro territorio», ha subrayado, aunque ha remarcado que «al final (las sedes sociales) acaban todas en Madrid, más allá de un guiño institucional o simbólico».En cualquier caso, ha defendido que «hay que ser cautos» y «terminar de analizar los detalles». «Vamos a estar encima, siempre lo hemos estado durante estos días, vamos a tener un flujo de diálogo muy constante para estar pendiente de cuáles son las decisiones y cuál es la evolución que pueda tener», ha declarado, para insistir en que está «preocupado» y que no lo dice «con una sonrisa».«Presión» de los empresariosEn la misma línea, el presidente de la CEV ha mostrado «cierta preocupación» desde el empresariado valenciano por la posible fusión, ya que la falta de competencia «hace que el crédito deje de fluir» .«Vamos a intentar trasladar la presión, y lo digo así, a la entidad que resulte para que se mantenga en lo posible el compromiso con el territorio», ha aseverado, y ha advertido que si sale adelante la fusión «perjudicará a la Comunitat Valenciana» porque «de nuevo las sociedades se irán al domicilio social de Madrid, que es lo que está ocurriendo con algunas entidades».«Poco más sabemos», ha añadido Navarro, tras señalar que es una decisión empresarial y resaltar la implicación del Sabadell en la región con «un porcentaje muy alto de participación tanto a nivel de crédito o de participaciones de empresas o ciudadanos».Como presidente del Consejo de Cámaras de Comercio de la Comunitat, José Vicente Morata ha lamentado la posible fusión porque «no es bueno que el número de operadores de bancos se reduzca de forma tan drástica» . «No sé si será una buena noticia para los accionistas, pero para las empresas no», ha declarado.Además, Morata ha señalado que la pérdida de la sede social «no es una buena noticia ni para Alicante ni para la Comunitat Valenciana». «Justamente aquí trabajamos para que realmente los bancos estén muy apoyados, y no nos parece lo que hemos visto hasta ahora una buena noticia para los intereses de la Comunitat Valenciana», ha insistido.",
        "content": "El presidente de la Generalitat, Carlos Mazón , y los presidentes de la Confederación Empresarial Valenciana (CEV), Salvador Navarro, y las cámaras de comercio valencianas, José Vicente Morata, han mostrado su \"preocupación\" por la posible fusión entre el BBVA y Sabadell , ya que dos grupos llegarían a concentrar el 60% del mercado bancario en la Comunidad Valenciana y la sede social de la segunda entidad dejaría de estar en Alicante si prospera la oferta planteada.\"La noticia no me ha gustado nada\", ha manifestado Mazón después de que el BBVA comunicara el martes a la Comisión Nacional del Mercado de Valores (CNMV) su traslado al presidente del consejo de administración del Sabadell del interés por explorar una fusión en la que se generaría el mayor banco de España. Esta operación formaría una entidad con unas 400 oficinas y 2.500 trabajadores en la Comunitat.El jefe del Consell ha explicado que ha contactado \"directamente con el Banco Sabadell\" a primera hora de este jueves y le han traslado que \"están estudiando la operación con detalle, con exhaustividad y en estos momentos están analizando la respuesta que van a dar\".\"Me preocupa. En primer lugar porque estoy a favor de la competencia , de que los ciudadanos tengan las mayores alternativas posibles. De fraguarse esta operación estaríamos hablando de que en la Comunitat Valenciana dos grandes entidades financieras concentran casi el 60% del mercado, y a mí esto no me parece una buena noticia. Yo quiero más entidades financieras en las que los ciudadanos puedan elegir\", ha expuesto a los periodistas junto al presidente de la CEV antes de un acto organizado por 'La Vanguardia' en Valencia.MÁS INFORMACIÓN noticia No Mazón apela a la \"cautela\" ante una posible fusión BBVA-Sabadell aunque ofrece Alicante como sedeParalelamente, Mazón ha advertido que estarán \"vigilantes\" ante la posibilidad de que la sede social deje de estar en Alicante , ciudad a la que el Sabadell la trasladó en 2017 ante la situación política en Catalunya. \"Tenemos que defender nuestro territorio\", ha subrayado, aunque ha remarcado que \"al final (las sedes sociales) acaban todas en Madrid, más allá de un guiño institucional o simbólico\".En cualquier caso, ha defendido que \"hay que ser cautos\" y \"terminar de analizar los detalles\". \"Vamos a estar encima, siempre lo hemos estado durante estos días, vamos a tener un flujo de diálogo muy constante para estar pendiente de cuáles son las decisiones y cuál es la evolución que pueda tener\", ha declarado, para insistir en que está \"preocupado\" y que no lo dice \"con una sonrisa\".\"Presión\" de los empresariosEn la misma línea, el presidente de la CEV ha mostrado \"cierta preocupación\" desde el empresariado valenciano por la posible fusión, ya que la falta de competencia \"hace que el crédito deje de fluir\" .\"Vamos a intentar trasladar la presión, y lo digo así, a la entidad que resulte para que se mantenga en lo posible el compromiso con el territorio\", ha aseverado, y ha advertido que si sale adelante la fusión \"perjudicará a la Comunitat Valenciana\" porque \"de nuevo las sociedades se irán al domicilio social de Madrid, que es lo que está ocurriendo con algunas entidades\".\"Poco más sabemos\", ha añadido Navarro, tras señalar que es una decisión empresarial y resaltar la implicación del Sabadell en la región con \"un porcentaje muy alto de participación tanto a nivel de crédito o de participaciones de empresas o ciudadanos\".Como presidente del Consejo de Cámaras de Comercio de la Comunitat, José Vicente Morata ha lamentado la posible fusión porque \"no es bueno que el número de operadores de bancos se reduzca de forma tan drástica\" . \"No sé si será una buena noticia para los accionistas, pero para las empresas no\", ha declarado.Además, Morata ha señalado que la pérdida de la sede social \"no es una buena noticia ni para Alicante ni para la Comunitat Valenciana\". \"Justamente aquí trabajamos para que realmente los bancos estén muy apoyados, y no nos parece lo que hemos visto hasta ahora una buena noticia para los intereses de la Comunitat Valenciana\", ha insistido.",
        "enclosure": {
            "link": "https://s3.abcstatics.com/abc/www/multimedia/espana/2024/05/02/mazon-archivo-RanLja8gt9pXuDdflBeeFfP-758x531@diario_abc.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ABC"
    },
    {
        "title": "Mazón y Morant estrenan su primera reunión sin llegar a acuerdos y con Vox como escollo",
        "pubDate": "2024-05-02 17:23:00",
        "link": "https://www.elconfidencial.com/espana/comunidad-valenciana/2024-05-02/diana-morant-mazon-reunion-vox_3877118/",
        "guid": "https://www.elconfidencial.com/espana/comunidad-valenciana/2024-05-02/diana-morant-mazon-reunion-vox_3877118/",
        "author": "Víctor Romero. Valencia",
        "thumbnail": "",
        "description": "La ministra de Ciencias y líder del PSPV pide al 'president' que rompa con su socio en una cita en el Palau en la que apenas se habló de financiación y el barón popular propuso una mesa del agua",
        "content": "No hubo acuerdos de calado en la primera reunión entre el presidente de la Generalitat valenciana, Carlos Mazón, y la nueva secretaria general de los socialistas valencianos, la también ministra de Ciencia y Universidades, Diana Morant. La cita en el Palau de la Generalitat se prolongó este jueves durante dos horas, pero de ella apenas salió un compromiso de mantener abierto el diálogo Consell-oposición socialista e iniciar una negociación para desbloquear la renovación de órganos estatutarios como la Sindicatura de Cuentas o el Consejo Jurídico Consultivo, con mandatos caducados y sin consenso hasta ahora. El encuentro sirvió para constatar que la presencia de Vox en el gobierno que preside el barón popular es el principal escollo para fraguar consensos y que Morant trata de evitar, en la medida de lo posible, confrontar con el Ejecutivo del que forma parte, el de Pedro Sánchez, ante las apelaciones del dirigente del PP a \"constituir un frente constructivo\" en materia de agua, inversiones del Estado, reforma de la financiación autonómica o, en su defecto, fondo transitorio de nivelación. Sobre este asunto, la ministra despejó la pelota al líder del PP, Alberto Núñez Feijóo, al que acusó de bloquear la posible reforma. Del fondo de nivelación, que tendría que incorporar el Ministerio de Hacienda en unos nuevos Presupuestos Generales del Estado (PGE), esquivó las preguntas de los medios de comunicación. Sí se comprometió a estudiar su incorporación a una mesa del agua. La cita se producía poco más de un mes después de que el PSPV-PSOE ungiese a Morant como relevo de Ximo Puig en un congreso extraordinario celebrado en Benicàssim. Tras el cónclave, Mazón invitó por carta a la ministra a celebrar un encuentro institucional con el fin de abrir una ventana de diálogo. Este jueves, tras una reunión en la que el presidente autonómico no compareció ante los medios, cosa que sí hizo Morant, Mazón resaltó en un comunicado la voluntad de conversar, \"dejando de lado la confrontación y los muros y velando por los intereses reales de la ciudadanía\". Sánchez y Feijóo no arreglan la financiación porque no quieren (y este informe lo demuestra)Víctor RomeroUn grupo de expertos propone una fórmula que resolvería el entuerto en un contexto en el que las agencias de rating auguran tres años de consolidación fiscal más fuerte de lo esperada La ministra, por su parte, que llegaba como aspirante, fue más combativa, reclamando al president como primera medida que rompa el acuerdo de gobierno con Vox, al que acusó de quebrar los consensos institucionales en materia de lucha contra la violencia de género o memoria histórica. \"Le pedimos que repiense la decisión de gobernar con Vox y que deje de convertir la Generalitat en un instrumento político de la ultraderecha para hacer políticas que rompen consensos\", insistió. Según fuentes cercanas a la ministra, esa apelación constante a alejamiento de Vox y las políticas que despliega a través de la Generalitat terminó por irritar a Mazón en el tramo final de la reunión a puerta cerrada, que cuestionó los pactos de los socialistas en el Congreso de los Diputados con formaciones como Bildu. Morant le recordó que el socio en el Gobierno es Sumar, al margen de las alianzas parlamentarias coyunturales. 👥💼 El president de la Generalitat, @carlos_mazon_, es reunix amb la secretària general del PSPV, @DianaMorantR pic.twitter.com/MqUbe6HVwp— Generalitat (@generalitat) May 2, 2024 La dirigente socialista pidió a Mazón que retire el paquete legislativo de cinco leyes que se tramitan en las Cortes Valencianas y derogan la ley de memoria histórica del Consell del Botànic, modifican la política lingüística en el sistema educativo, relajarán los requisitos de trasparencia de los cargos públicos y las mayorías cualificadas necesarias ahora para renovar los órganos de gobierno de la radiotelevisión pública À Punt o la dirección de la Agencia Valenciana Antifraude. Morant entregó al presidente valenciano un paquete de propuestas entre las que figuran la de no cerrar la puerta a la aplicación de la Ley de Vivienda para topar los precios del alquiler y \"restaurar la justicia social para garantizar la financiación de los servicios públicos esenciales\", aunque no aclaró si se refería a recuperar el impuesto de sucesiones y donaciones, suprimido por el Consell de PP y Vox. La batería de exigencias incluye también la de desbloquear planes de inversiones que quedaron sin completar la pasada legislatura como el Edificant (colegios), Convivint (infraestructuras de uso social como residencias) o Crèixer (infraestructuras sanitarias).",
        "enclosure": {
            "link": "https://images.ecestaticos.com/JkHR-Dqwv3cdf4sKRjRwcNSEQ2Y=/0x0:2272x1605/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/b4a/d51/964/b4ad51964625c01aaad2730b3ec50b7f.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "Un joven de 17 años mata a su madre con un arma blanca durante una discusión en Badajoz",
        "pubDate": "2024-05-02 15:47:00",
        "link": "https://www.elconfidencial.com/espana/2024-05-02/joven-mata-madre-arma-blanca-discusion-badajoz_3877116/",
        "guid": "https://www.elconfidencial.com/espana/2024-05-02/joven-mata-madre-arma-blanca-discusion-badajoz_3877116/",
        "author": "EFE",
        "thumbnail": "",
        "description": "La agresión mortal se ha producido alrededor de las 14:30 horas de este jueves en el interior de la casa tras una discusión entre la madre y el hijo, según ha manifestado este último durante su aviso de lo sucedido a la Policía Nacional",
        "content": "Un joven de 17 años ha matado a su madre, de 59, con un arma blanca durante una discusión en la vivienda familiar, ubicada en la barriada María Auxiliadora de Badajoz, han informado a EFE fuentes de la Policía Nacional. La agresión mortal se ha producido alrededor de las 14:30 horas de este jueves en el interior de la casa tras una discusión entre la madre y el hijo, según ha manifestado este último durante su aviso de lo sucedido a la Policía Nacional en una llamada telefónica. Efectivos policiales y sanitarios se han desplazado a la vivienda, situada en la calle América, donde han encontrado el cadáver de la mujer y se ha procedido al arresto de uno de sus hijos como supuesto autor de la muerte. Fuentes vecinales del inmueble donde se ha producido este suceso han apuntado a EFE que tanto el joven ahora detenido como otra menor habían sido adoptados por la mujer. Asimismo, han expuesto que el joven también habría matado al perro que tenía la familia en el transcurso de la discusión. \"Nadie se esperaba esto\" Vecinos del menor de 17 años han afirmado estar \"impactados\" y han asegurado que \"nadie se esperaba esto\", ya que formaban una \"buena familia\". En declaraciones a los medios, Pablo Chávez, uno de los vecinos de María Auxiliadora, ha asegurado que dicho barrio se encuentra \"tocado\" tras el suceso, porque \"nadie se lo esperaba\". Asimismo ha indicado también que la madre era profesora y que conocía al presunto matricida, a quien se le veía \"muy tranquilo\" y \"muy normal\". \"Nadie se esperaba esto verdad. No se le veía con mal carácter, un muchacho muy normalito\" \"Nadie se esperaba esto, la verdad. No se le veía con mal carácter, un muchacho muy normalito, y sí, de buena familia\", ha dicho. \"No sé qué se le podría haber pasado por la cabeza, la verdad\", ha añadido. Por su parte, otra vecina ha señalado que el presunto autor de la muerte de su madre, de 60 años, era adoptado, al igual que otra hermana e hija de la víctima. De la víctima ha apuntado que era una mujer \"muy trabajadora\", \"estupenda\" y \"educada\" y que estaba con sus hijos \"como loca\".",
        "enclosure": {
            "link": "https://images.ecestaticos.com/qz4Zb8_yTJ4ANhtVqBfBFyypqXk=/0x0:2272x1515/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/a3f/86a/bf6/a3f86abf65e76201c32c911f69128ac2.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "Moreno baraja reformar su Gobierno tras la salida de su consejera de Agricultura a Bruselas",
        "pubDate": "2024-05-02 15:47:00",
        "link": "https://www.elconfidencial.com/espana/andalucia/2024-05-02/moreno-cambio-gobierno-lista-europea-bruselas_3877042/",
        "guid": "https://www.elconfidencial.com/espana/andalucia/2024-05-02/moreno-cambio-gobierno-lista-europea-bruselas_3877042/",
        "author": "Carlos Rocha. Sevilla",
        "thumbnail": "",
        "description": "En San Telmo y el PP admiten que están satisfechos con el Ejecutivo y no ven \"desgaste\", pero las formas del presidente alimentan la posibilidad de una reforma de mayor calado. No nombrará un sustituto inmediato de Carmen Crespo",
        "content": "Juanma Moreno tendrá que cambiar su Gobierno en el ecuador de la legislatura. Lo hará obligado porque ha decidido enviar a su consejera de Agricultura, Carmen Crespo, a Bruselas para dar voz al campo andaluz en la capital comunitaria. Pero en San Telmo no descartan que la reforma vaya más allá de un cambio quirúrgico. Y hay varias pistas que alimentan la posibilidad de que el presidente andaluz, poco amigo de los cambios, opte por una remodelación más ambiciosa. La primera de todas es que en el Ejecutivo autonómico no descartan una crisis mayor. Y esto es novedoso si se tiene en cuenta que hace sólo un año, en una situación similar, Moreno descartó tajantemente una reforma mayor en su gabinete. A principios de 2023, cuando el segundo Gobierno de Juanma Moreno no tenía ni un año, el malagueño desveló que Marifrán Carazo dejaría la Consejería de Fomento para ser la candidata de PP en Granada. En el momento en el que se conoció su designación, el jefe del Ejecutivo dejó claro que sería un cambio de cromos. Saldría Carazo y entraría otra persona para cubrir su perfil. Al poco tiempo desveló que sería una mujer y de Granada, para no tocar los equilibrios territoriales y de género en el gabinete. Un año después, Moreno ha actuado de una forma totalmente distinta. Carmen Crespo dejará el Consejo de Gobierno de forma \"inminente\", pero no tendrá sustituto o sustituta, por el momento. La intención del presidente de la Junta, como ha explicado este jueves, es delegar las competencias de Agricultura, Ganadería, Pesca y Agua en otro miembro del gabinete. Todas las miradas recaen sobre el portavoz y consejero de Sostenibilidad, Ramón Fernández Pacheco, pero en San Telmo insisten que esto no supondrá una mayor carga de trabajo para el exalcalde de Almería. Moreno no quiere que el equipo de Crespo se desgaje, ya que se trata de un grupo \"sólido\" que seguirán ejerciendo sus competencias bajo la batuta de Fernández-Pacheco mientras que el jefe del Ejecutivo piensa a quién quiere para sustituir a la futura eurodiputada. La fórmula elegida por el barón popular es extraña, sobre todo si se tiene en cuenta que Crespo saldrá del gabinete el próximo lunes, antes de la reunión del Consejo de Gobierno. Hay que recordar que las competencias de Medio Ambiente y Agricultura compartieron departamento en la pasada legislatura, precisamente controladas por Carmen Crespo. Pero a mitad del mandato Moreno decidió desgajar las delegaciones provinciales para evitar una sobrecarga de trabajo para los responsables territoriales de esta cartera, que tiene una importante responsabilidad en materia de permisos ambientales o agrarios. Entonces ya hubo rumores sobre una posible crisis de Gobierno y Crespo estuvo en las quinielas, pero Juanma Moreno no es muy dado a los cambios de Gobierno en medio de la legislatura. El CIS andaluz ve a un Juanma Moreno intocable con la izquierda en caída libreCarlos Rocha. SevillaEl barómetro del Centra no detecta apenas desgaste para el presidente de la Junta, que calca su mejor dato, mantiene el mal momento del PSOE y prevé una caída de Por Andalucía y un crecimiento de Vox Ese escaso gusto por las crisis de gabinete es uno de los argumentos que utilizan quienes descartan que Moreno vaya a hacer una remodelación más allá de buscar un sustituto a Crespo. Pero la forma de actuar de Moreno y los mensajes que salen de su equipo apuntan en la dirección contraria. En el PP andaluz rechazan que haya desgaste en el Ejecutivo, según varias fuentes consultadas. Pero es imposible obviar la presión que hay sobre la consejera de Salud, Catalina García. La jiennense se ha enfrentado a varias crisis, quizás las más importantes del Gobierno andaluz en esta legislatura. La primera fue la polémica provocada por la orden que abría la puerta a la externalización de las consultas de atención primaria. Y casi al mismo tiempo estallaron los datos de las listas de espera quirúrgicas y de pruebas diagnósticas y el intento de su exnúmero dos por fichar por la aseguradora Asisa, una incorporación que se declaró después incompatible. Todas las intervenciones públicas de Moreno sobre García han sido un cierre de filas, a pesar de que el PSOE intentará reprobarla este jueves en el Parlamento autonómico. Y al mismo tiempo el malagueño admitió hace unas semanas que su Ejecutivo está en \"constante evaluación\" para hacer los retoques necesarios. El nombre de Catalina García y la posibilidad de buscarle un encaje a la jiennense en las listas del Parlamento Europeo han planeado sobre la política andaluza en los últimos meses. Finalmente ha sido otra consejera quien tendrá salida en Bruselas desde el Gobierno de Juanma Moreno. Crespo ha recibido este jueves palabras cariñosas de sus compañeros de partido en el antiguo Hospital de las Cinco Llagas, sede del legislativo andaluz. El propio Juanma Moreno ha puesto el foco en la importancia que tiene que sea Crespo quien represente al PP andaluz en la Eurocámara. El barón popular ha convertido a la polític agraria y la gestión del agua en una de las señas de identidad de su Gobierno. En su equipo insisten en la importancia que tiene que alguien con experiencia en este campo tenga voz en Bruselas. Sólo hay que recordar que Miguel Arias Cañete, de Jerez de la Frontera, fue comisario europeo de Agricultura y que la eurodiputada socialista Clara Aguilera lleva una década en el Parlamento Europeo dedicada a estos asuntos y es una figura muy respetada. Aguilera, que no va en las listas del PSOE, fue precisamente consejera de Agricultura bajo los mandatos de Manuel Chaves. La actual titular de Agricultura es de las más veteranas del Gabinete de Juanma Moreno. Sólo otras dos consejeras (Patricia del Pozo y Rocío Blanco) siguen desde el primer Gobierno del malagueño. Crespo fue antes alcaldesa de Adra (2003-2011) hasta que Mariano Rajoy la nombró delegada del Gobierno en Andalucía en la primera etapa de su estancia en Moncloa. Después se convirtió en la portavoz parlamentaria del PP y desde ahí pasó al equipo de Juanma Moreno. Muchos dieron por hecho que no seguiría después de las elecciones del 19 de junio de 2022, cuando los populares lograron una histórica mayoría absoluta.",
        "enclosure": {
            "link": "https://images.ecestaticos.com/i3Gk_uw-czvkfvMbbpgfkI0IOlg=/0x0:2272x1573/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/8ef/ff5/100/8efff5100645eae529c377bba1794fd4.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "Muere en Salamanca el hombre de avanzada edad hospitalizado con fiebre hemorrágica de Crimea-Congo",
        "pubDate": "2024-05-02 14:07:00",
        "link": "https://www.elconfidencial.com/espana/2024-05-02/muere-salamanca-hombre-avanzada-edad-fiebre-hemorragica-crimea-congo_3877075/",
        "guid": "https://www.elconfidencial.com/espana/2024-05-02/muere-salamanca-hombre-avanzada-edad-fiebre-hemorragica-crimea-congo_3877075/",
        "author": "EFE",
        "thumbnail": "",
        "description": "El paciente estaba en una situación estable, dentro de la gravedad, en el Hospital de Salamanca y con las pertinentes medidas de aislamiento y protección para este tipo de situaciones, aunque finalmente falleció ayer",
        "content": "El hombre de avanzada edad que estaba hospitalizado en Salamanca por un caso de fiebre hemorrágica de Crimea-Gongo (FHCC), producida por la picadura de una garrapata hace una semana, falleció ayer en el hospital salmantino, según han confirmado hoy a EFE fuentes de la Consejería de Sanidad. Tras el deceso, la Consejería activó el protocolo de gestión de residuos y limpieza, de acuerdo a las mismas fuentes. El pasado 27 de abril, la autoridad sanitaria de Castilla y León confirmó ese caso de fiebre hemorrágica de Crimea-Gongo (FHCC) producida por la picadura de una garrapata a un hombre de avanzada edad que estaba hospitalizado en Salamanca. El paciente estaba en una situación estable, dentro de la gravedad, en el Hospital de Salamanca y con las pertinentes medidas de aislamiento y protección para este tipo de situaciones, aunque finalmente falleció ayer, 1 de mayo. El caso de FHCC fue confirmado por la Consejería de Sanidad después de los análisis realizados por el Centro Nacional de Microbiología del Instituto de Salud Carlos III, situado en Majadahonda (Madrid). Un virus emergente llega a España: la fiebre hemorrágica que transmiten las garrapatasJosé PichelInvestigadores acaban de diagnosticar un primer caso que pasó desapercibido en 2013: desde entonces, se contabilizan nueve y tres de ellos han acabado en muerte La fiebre hemorrágica de Crimea-Congo es consecuencia de un virus que principalmente transmite la picadura de una garrapata del género 'Hyaloma', como ha ocurrido en este caso, aunque también puede comunicarse entre personas por contacto con sangre o fluidos del enfermo. Las autoridades sanitarias, como medidas de prevención, recuerdan la importancia de usar ropa y calzado adecuados durante las salidas al campo, así como transitar por caminos y utilizar repelentes tanto para las personas como para los animales de compañía. Las garrapatas que se puedan haber fijado deben retirarse lo antes posible y de forma adecuada, preferentemente por profesionales sanitarios, según las mismas fuentes.",
        "enclosure": {
            "link": "https://images.ecestaticos.com/v3TqJdUDbO-IgoJfOq-3KIMGnqw=/0x0:2272x1515/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/a77/9f4/bba/a779f4bba3128f3d8ecc3722483daad9.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "¿Quién torea hoy, jueves 2 de mayo, en Madrid? Cartel completo de Las Ventas en la tradicional corrida Goyesca",
        "pubDate": "2024-05-02 10:55:00",
        "link": "https://www.elconfidencial.com/espana/madrid/2024-05-02/cartel-corrida-goyesca-2024-2-de-mayo-madrid_3876999/",
        "guid": "https://www.elconfidencial.com/espana/madrid/2024-05-02/cartel-corrida-goyesca-2024-2-de-mayo-madrid_3876999/",
        "author": "El Confidencial",
        "thumbnail": "",
        "description": "Abriendo la temporada de toros de San Isidro, la Feria de la Comunidad de Madrid, el 1 y 2 de mayo, recoge una novillada, un concurso de recortes y la tradicional corrida Goyesca",
        "content": "Programa completo de toros por la Feria de abril en Sevilla: cartel de cada día, horario de las corridas y toreros¿Les gustan los toros a los chinos?Como es tradición, la Feria de la Comunidad de Madrid abre la temporada de corridas de toros de San Isidro. Este pasado miércoles 1 de mayo, Día del Trabajador, se celebró una novillada con picadores, con novillos de seis ganaderías de la Comunidad de Madrid. Actuaron Jesús Moreno, Juan Herrero y Alejandro Chicharro. Hoy jueves 2 de mayo, en el segundo y último día de la feria, se celebrará la tradicional Corrida de Toros Goyesca, con seis astados de la ganadería toledana El Montecillo. Actuarán los diestros Fernando Robleño, Javier Cortés y Francisco José Espada. Tras la Feria de la Comunidad de Madrid, habrá una novillada previa a San Isidro el próximo domingo 5 de mayo, y la temporada de toros de San Isidro 2024 se inaugurará oficialmente el próximo viernes 10 de mayo. Cartel de la Feria de la Comunidad y San Isidro (las-ventas.com) La Feria de San Isidro consistirá en 21 corridas de toros, tres novilladas y dos festejos de rejones. Como informan desde Las Ventas, el serial cuenta con cuatro jornadas de descanso dentro del ciclo (los lunes 13, 20 y 27 de mayo, y el 3 de junio). Además. En total se han anunciado 59 actuantes, de los cuales 44 son matadores, 6 rejoneadores y 9 novilleros con picadores. Serán en total 25 ganaderías, representando 9 encastes distintos. Corrida Goyesca: horario y desfile La Corrida de Toros Goyesca se celebrará en la Plaza de Toros de Las Ventas a las 18:30 horas, con motivo del Dos de Mayo, día de la Comunidad de Madrid. Es tradición que todos los participantes de la corrida de este jueves 2 de mayo, incluyendo los toreros, picadores y subalternos, irán ataviados con los trajes populares de corte goyesco. Este tipo de estética es la que inmortalizó Fuendetodos en sus cuadros a principios del siglo XIX. Justo antes de las corridas de toros, a las 17:30 horas, en Las Ventas tendrá lugar un desfile de castizos y goyescos. Este desfile estará compuesto por unas 60 personas pertenecientes a la federación de grupos tradicionales madrileños, todos ataviados con el traje regional. Ocho serán las calesas que participarán en el desfile, partiendo desde la plaza de Manuel Becerra hacia la plaza de toros. Todo el desfile estará amenizado con la banda de música de la Policía Municipal.",
        "enclosure": {
            "link": "https://images.ecestaticos.com/ZoT0YTTA9CoC5FEmiC_yt6NeNck=/0x0:2272x1676/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/264/df8/d11/264df8d11e6a0b3f1d615aa49523dced.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "Las asociaciones de prensa exigen que cesen los ataques políticos para acallar a los periodistas",
        "pubDate": "2024-05-02 10:04:00",
        "link": "https://www.elconfidencial.com/espana/2024-05-02/asociaciones-de-prensa-ataques-politicos_3876968/",
        "guid": "https://www.elconfidencial.com/espana/2024-05-02/asociaciones-de-prensa-ataques-politicos_3876968/",
        "author": "A. P.",
        "thumbnail": "",
        "description": "La FAPE reitera de nuevo su \"firme compromiso con la defensa del periodismo como pilar fundamental de la democracia\" porque \"sin periodismo, no hay democracia\"",
        "content": "Las asociaciones de prensa vuelven a levantar la voz contra las presiones de partidos políticos y Gobierno a los medios de comunicación en el ejercicio de su labor. Así, la Federación de Asociaciones de Periodistas de España (FAPE) reitera de nuevo su \"firme compromiso con la defensa del periodismo como pilar fundamental de la democracia\" tras su asamblea general celebrada en Talavera de la Reina. Además, hace un llamamiento a acabar con la crispación \"generada por la polarización política\" y pide a Sánchez \"terminar con los ataques a la prensa y los periodistas para acallar voces críticas\". En un nuevo manifiesto defiende la necesidad de cumplir los principios éticos y profesionales, y de defender el libre ejercicio del periodismo, de la libertad de expresión y del derecho a la información veraz de los ciudadanos. Por ello, las asociaciones de prensa instan a Sánchez y a los grupos políticos a \"acabar con la crispación que reflejan en sus actuaciones\" y \"terminar con los ataques a la prensa y los periodistas\" después de las palabras del presidente y sus amenazas a la prensa. Pero este manifiesto va más allá y reclama a los grupos políticos que protejan ese derecho constitucional y no fomenten la \"difusión de mentiras y bulos mediante el uso perverso de las redes sociales\" y, sobre todo, que acaben con las presiones a los medios y los periodistas. Avisa a los políticos y gobernantes sobre \"los discursos de odio\" a la vez que solicitan a las instituciones \"no difundir noticias falsas o manipuladas\". Por ello, recuerda a los políticos que tarea principal de los periodistas es \"preguntar, investigar y denunciar los comportamientos irregulares\". La ley ya contempla límites a la libertad de expresión con penas para quien lance bulos e insulteAlejandro RequeijoEl Código Civil y el Código Penal regulan desde hace décadas la actuación de los medios de comunicación y los jueces pueden incluso inhabilitar a periodistas para ejercer la profesión En la misma línea, denuncia \"los ataques al libre ejercicio del periodismo con determinadas prácticas antidemocráticas, como los señalamientos, el acoso on line, la exclusión de medios y periodistas de convocatorias, las comparecencias sin preguntas y los intentos de imponer preguntas\". Para la FAPE, \"sin periodismo no hay democracia\". No obstante, también reconoce que los periodistas están sometidos a la ley y que cualquier vulneración de derechos que se registre en una información pueden ser llevados a los tribunales, o cualquier comportamiento irregular de un profesional o uno medios de comunicación a la Comisión de Arbitraje, Quejas y Dentología del Periodismo. Críticas a los medios Todo ello llega después de las asociaciones prensa pidieran al presidente del Gobierno que convocara a la prensa para explicar su proyecto de regeneración y las amenazas veladas a los medios. Tras sus cinco días de reflexión, Sánchez no atendió a las preguntas de los periodistas y tampoco aclaró las propuestas de regeneración que van a plantear un \"punto y aparte\". Y es que, tras la publicación de varias informaciones sobre su mujer y su período de reflexión, la prensa ha estado en el punto de mira del presidente, que no ha aclarado en ningún momento la regeneración que afecta a los medios, Por ello, tanto la FAPE como la Asociación de Prensa de Madrid (APM) defendieron que \"la regeneración que plantea el presidente del Gobierno ha de contemplar, como pilar fundamental, el respeto al trabajo de los periodistas y a la libertad de información, teniendo en cuenta además que, en su propio discurso, Sánchez ha denunciado el peligro que supone la desinformación para la calidad democrática de un país\". Carta al presidente Sánchez: la desinformación revisitadaBeatriz BecerraCréame si le digo, presidente, que me gustaría contribuir humildemente a ayudarle en su empeño. Para ello, permítame tan solo recordarle tres elementos relevantes al respecto de la desinformación Por su parte, la APM alertó de su preocupación por el hecho de que \"una situación tan excepcional se resuelva trasmitiendo una duda sobre la libertad de expresión\". \"Si el presidente y el Gobierno consideran que hay que abrir un debate sobre los límites de la información -que ya están marcados en nuestras leyes-, nos comprometemos a participar, desde la reflexión, el debate, la serenidad y, por supuesto, la autocrítica\", señaló la APM. Alertas de los medios internacionales Además, algunos medios internacionales criticaron duramente el periodo de reflexión del presidente tras la publicación de varias noticias sobre su mujer Begoña Gómez. The Times censura las \"amenazas a los periódicos\" del presidente tras destapar un posible conflicto de intereses de su mujer, mientras que el Financial Times cree que la protesta ha sido \"desacertada y unipersonal\" en una \"España tóxica\". \"Un espectáculo bochornoso\": la prensa extranjera critica la \"amenaza\" de Sánchez de controlar los mediosEl ConfidencialLos cinco días de reflexión le pasan factura al presidente. Medios internacionales no comparten ni las maneras ni las formas y creen que la solución de Sánchez no es la vía adecuada Era en concreto The Times destacaba la ofensiva del presidente del Gobierno contra los medios de comunicación tras varios artículos sobre su mujer. Bajo el titular de \"Pedro Sánchez amenaza con frenar a los medios por acusaciones de corrupción contra su esposa\", el diario británico explica que el presidente ha amenazado con \"reforzar el control sobre los medios de comunicación\" después de que un juez \"abriera una investigación penal sobre su esposa\". Critica The Times que estas medidas de control forman parte de lo que llamó \"regeneración democrática\".",
        "enclosure": {
            "link": "https://images.ecestaticos.com/N3o7lttl2uSX34pWVFDSvEJ2RLM=/0x0:2272x1513/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/402/41a/de5/40241ade5693ac7e7a96551f299d7c34.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "Sánchez insta a la militancia a defender la democracia: \"No es el apoyo a mi persona lo que nos une\"",
        "pubDate": "2024-05-02 08:22:00",
        "link": "https://www.elconfidencial.com/espana/2024-05-02/pedro-sanchez-carta-militantes-democracia-persona_3876945/",
        "guid": "https://www.elconfidencial.com/espana/2024-05-02/pedro-sanchez-carta-militantes-democracia-persona_3876945/",
        "author": "EFE",
        "thumbnail": "",
        "description": "En una carta dirigida a los militantes con motivo de la celebración del 145 aniversario de la fundación del PSOE y una semana después de la misiva dirigida a la ciudadanía",
        "content": "El presidente del Gobierno, Pedro Sánchez, ha instado este jueves a los militantes socialistas a defender la democracia todos los días tras su decisión de continuar al frente del Ejecutivo. En una carta dirigida a los militantes con motivo de la celebración del 145 aniversario de la fundación del PSOE y una semana después de la misiva dirigida a la ciudadanía para reflexionar sobre su futuro, Pedro Sánchez reconoce la \"deuda\" con los miles de socialistas que le han brindado su apoyo estos días, pero deja claro que él no es lo que une al PSOE. \"No es el apoyo a mi persona lo que nos une. Por encima de todo, nos une el apoyo a una causa\", añade Sánchez para quien la \"solidaridad\" y la \"unión\" de los socialistas es el principal activo y lo más valioso de su partido \"cuando las cosas se ponen difíciles\". Pedro Sánchez irrumpe por sorpresa en la Feria de Abril de BarcelonaEFESu reaparición oficial en campaña está prevista para este próximo jueves por la tarde, en el mitin que protagonizará en Sant Boi de Llobregat (Barcelona) Por eso, el secretario general del PSOE anima a todos sus compañeros a defender la democracia \"ante el avance de una internacional ultraderechista que trata de imponer su agenda regresiva\" mediante la destrucción del adversario con la puesta en macha de una \"máquina del fango\" que fabrica bulos y mentiras. \"Debemos defender nuestra democracia todos los días rechazando a aquellos que convierten la política en un barrizal de insultos y falsedades\", insiste Sánchez, que vuelve a reivindicar la \"política limpia\" y subraya que \"la principal tarea\" de su generación es contribuir al fortalecimiento de la democracia. Concentraciones de apoyo Sánchez señala que las concentraciones ante la sede del PSOE en Madrid el pasado sábado y las muestras de apoyo de \"cientos de miles de personas en cartas, redes y casas del pueblo\" han puesto de manifiesto un \"poderoso\" mensaje de coraje: \"que no estamos dispuestos a asistir impasibles al deterioro y degradación de nuestra democracia\". Tintes de drama en Ferraz: el PSOE juega la baza emocional para evitar la dimisión de Pedro SánchezMarisol HernándezLa vicepresidenta abre el Comité Federal con un mensaje también a la mujer del presidente: \"Begoña, compañera, todas estamos contigo\". Apelación al sufrimiento de quienes sufrieron la Guerra Civil o el terrorismo para que se quede Y añade: \"El PSOE es el partido sistémico de la democracia y la Constitución española. Cuanto más fuerte es la democracia, más fuerte es el PSOE y mayor su capacidad transformadora\".",
        "enclosure": {
            "link": "https://images.ecestaticos.com/hOa8peVu9gymTINHohJ3taNLz-g=/0x0:2272x1515/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/d4c/786/001/d4c7860010348c0e5ae7ca009878a280.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "Detenidos cuatro jóvenes por apuñalar a dos hombres en Madrid para robar un móvil",
        "pubDate": "2024-05-02 05:12:00",
        "link": "https://www.elconfidencial.com/espana/madrid/2024-05-02/dos-heridos-arma-blanca-madrid-grave_3876931/",
        "guid": "https://www.elconfidencial.com/espana/madrid/2024-05-02/dos-heridos-arma-blanca-madrid-grave_3876931/",
        "author": "EFE",
        "thumbnail": "",
        "description": "Los varones, de 31 y 43 años, el primero en condición grave, han sido trasladados a dos hospitales distintos tras ser atendidos por un equipo de SAMUR Protección Civil",
        "content": "La Policía Nacional ha detenido a cuatro jóvenes, dos de ellos menores de edad, como supuestos responsables del apuñalamiento de dos hombres la madrugada de este jueves en el distrito madrileño de Ciudad Lineal para robarles un teléfono móvil. Fuentes policiales han informado a EFE que los arrestados, de entre 16 y 21 años, fueron localizados poco después de la agresión, que tuvo lugar sobre las 3:40 horas en la confluencia entre las calles de Ascao y Emilio Ferrari. Las víctimas, dos hombres de 31 y 43 años, señalaron a los agentes que un grupo de jóvenes les había atacado y robado un teléfono móvil. #Agresión en Ascao con Emilio Ferrari@SAMUR_PC estabiliza y traslada graves a distintos hospitales a dos varones de 31 y 43 años con heridas de arma blanca@policiademadrid y @policia han realizado las primeras asistencias hasta la llegada de @SAMUR_PC, controlando hemorragias pic.twitter.com/NdcSTmnh4z— Emergencias Madrid (@EmergenciasMad) May 2, 2024 Gracias a la información facilitada por los heridos, los investigadores localizaron a los supuestos autores en las inmediaciones del lugar de los hechos, a quienes se les imputan delitos de lesiones graves y robo con violencia. Ambos fueron atendidos y trasladados por los sanitarios de SAMUR-Protección Civil a diferentes centros hospitalarios, donde ingresaron con pronóstico grave, ha indicado Emergencias Madrid. Uno de los agredidos presentaba dos heridas por arma blanca, mientras que el segundo tenía dos heridas incisas en las zonas renales derecha e izquierda. EFE",
        "enclosure": {
            "link": "https://images.ecestaticos.com/lD1wDFqQqwHZnKCobryrBreuqx4=/0x0:2272x1515/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/9c6/9b8/fab/9c69b8fabc4169984aee58a5c32998cc.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "La Guardia Civil evita el matrimonio forzado de una menor: su madre iba a venderla por 50.000€",
        "pubDate": "2024-05-02 03:00:00",
        "link": "https://www.elconfidencial.com/espana/2024-05-02/guardia-civil-matrimonio-forzado-albacete-venderla_3876686/",
        "guid": "https://www.elconfidencial.com/espana/2024-05-02/guardia-civil-matrimonio-forzado-albacete-venderla_3876686/",
        "author": "Europa Press",
        "thumbnail": "",
        "description": "La operación finalizó con la localización, identificación y posterior investigación del hombre que pretendió comprar a la menor y de su progenitora, ambos como presuntos autores de un delito de trata de seres humanos",
        "content": "Efectivos del Área de Personas de la Unidad Orgánica de Policía Judicial de la Benemérita albacetense, dentro del marco de la operación denominada Vinde, y en estrecha colaboración con los Servicios de Protección de Menores de la Junta de Comunidades de Castilla La Mancha de Albacete, han evitado que se consumara la \"venta\" de una menor por parte de su madre, por la cantidad de 50.000 euros, a un hombre con la intención de contraer matrimonio. Según ha informado en nota de prensa, la Guardia Civil tuvo conocimiento, a través de la sección del servicio de protección de menores de la delegación de Bienestar Social de Albacete de la Junta de Comunidades de Castilla-La Mancha, de que una menor de 16 años, que tenía tutelada la Junta de Comunidades de Castilla-La Mancha, podría estar siendo víctima de un posible delito de trata de seres humanos con fines de matrimonio forzado. Los agentes pudieron constatar que la menor residía con su madre, en una localidad de la provincia de Albacete, en régimen de permiso de convivencia, con seguimiento de los servicios sociales. Detenido un terapeuta por agresión sexual a dos niñas con trastorno del desarrollo en ValenciaEFEAl parecer, el hombre habría aprovechado su condición de pedagogo terapeuta para quedarse a solas con las mismas y realizarles tocamientos Ante la gravedad de los hechos, el Servicio de Protección de Menores revocó el permiso de convivencia, procediendo a la recogida de la menor y a su ingreso en un hogar residencial de menores de Albacete. Continuando con las investigaciones, los agentes pudieron comprobar cómo la madre de la menor, en una fiesta celebrada días antes en el propio domicilio de ésta, pactó con un hombre la \"venta\" de la menor, habiendo recibido parte de la cantidad económica pactada, para su inminente traslado a Italia. Detenido un hombre armado que amenazaba con matar a su mujer y exhibía un hacha en ValenciaEuropa PressEl varón llamó a la Policía para asegurar que había \"fallado\" en un disparo y advertía con matarla si no acudían a arrestarle La operación policial finalizó con la localización, identificación y posterior investigación del hombre que pretendió comprar a la menor, así como a la investigación de la madre de la menor, ambos como presuntos autores de un delito de trata de seres humanos con fines de matrimonio forzado. Las diligencias instruidas por los hechos han sido puestas a disposición del Juzgado de Instrucción, en funciones de guardia, del partido judicial donde sucedieron los hechos.",
        "enclosure": {
            "link": "https://images.ecestaticos.com/OZgEYujzme5VmMBWmo-U4aWWpJM=/0x0:1920x1378/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/d29/edc/83c/d29edc83c0be49ed15a86b19867f6024.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "La gresca con el cura de la ermita más antigua de Madrid llega a los juzgados: \"No queríamos molestarle\"",
        "pubDate": "2024-05-02 03:00:00",
        "link": "https://www.elconfidencial.com/espana/madrid/2024-05-02/litrona-cerveza-ermita-carbanchel-antigua-ecologistas_3876847/",
        "guid": "https://www.elconfidencial.com/espana/madrid/2024-05-02/litrona-cerveza-ermita-carbanchel-antigua-ecologistas_3876847/",
        "author": "Andrea Farnós",
        "thumbnail": "",
        "description": "El párroco Alberto, harto de los ecologistas, interpuso una denuncia en el mes de enero. Les acusa de causar revuelo en misa y llenar el entorno de escombros. El caso está en manos del Juzgado número 6 de Plaza Castilla",
        "content": "En el límite de los distritos de Latina y Carabanchel, hay un descampado repleto de hierbajos, pequeñas sendas para pasear, una antigua vía pecuaria, excrementos de mascotas y litronas de cerveza. \"Ahí me fumé mi primer porro\", reseña un vecino del barrio de Oporto. El lugar es peculiar. A un lado, el último resquicio de ladrillo de la antigua cárcel franquista de Carabanchel y el CIE de Aluche; al otro, la ermita más antigua de la región, datada del siglo XIII. Este templo fue declarado Bien de Interés Cultural (BIC) en 1981 y dicha protección se amplió al entorno en 2021. No obstante, la parroquia solo abre al público los sábados por la mañana. \"Reservado el derecho de admisión\", versa un cartel en el entorno de la ermita. A las once, además, hay misa; por lo que el acceso debe ser en silencio para respetar la oración. El párroco, Alberto Jerónimo Couto, tiene ahora una guerra judicial abierta con un grupo de ecologistas septuagenarios. Les culpa de causar revuelo en el interior del templo y llenar el entorno de escombros y litronas de cerveza. Para el eclesiástico, la acumulación de basura es solo una estrategia de coacción que lleva ocurriendo desde 2023. \"En fechas posteriores al cuatro de noviembre han venido sucediéndose congregaciones cada sábado por parte de los activistas haciendo caso omiso a las indicaciones del personal, accediendo al interior del edificio [...] manifestando literalmente Vamos a entrar por nuestros cojones y nadie nos lo va a impedir\", versa la denuncia que interpuso ante la Policía Nacional a finales del mes de enero. Pero, ¿por qué querían entrar al templo? Según el testimonio de Juan García Vicente, uno de los denunciados, de 76 años, lo hacían para mostrar \"las valiosas pinturas policromadas del siglo XV a los interesados, sin cobrarles\". El caso está judicializado en el Juzgado número 6 de Plaza Castilla. Este periódico no ha podido hablar con el párroco, pero sí con alguien de su entorno cercano: \"Los ecologistas quieren entrar y dar sus mítines\". Antes de desentrañar todas las aristas de esta historia, será necesario situar al lector en el espacio. 'Se reserva el derecho de admisión'. (A.F. El origen de la basura: un descampado Entre la Ermita y la antigua cárcel, existe un refugio para los adolescentes. \"Desde que tenía 17 o 18 años, después de clase, íbamos ahí con unas litros. Había que pasar una verja y se estaba muy tranquilo, se escuchaban los pajaritos. Además, no venía la policía\", confiesa Lorena, una joven del barrio de toda la vida de 26 años. Cecilia, residente durante los últimos 58 años en la única vivienda individual del entorno, relata que todos los fines de semana se hace botellón y se tiran escombros. Por suerte, a ella no le da mucho la tabarra ni una cosa ni la otra. La zona sirve como ciudad sin ley para beber y tirar deshechos. El último muro de la cárcel de Carabanchel en mitad del descampado. (A.F.) No es la primera vez que en esta explanada aparecen neumáticos, plásticos o restos de basura. Para tratar de visibilizar la suciedad acumulada en el entorno, un grupo de Ecologistas en Acción comenzó a trasladar los desechos a las puertas de la Ermita. \"Desde que se derribó la cárcel, toda la zona ha estado descuidada\", señala Juan, ecologista denunciado por Alberto. Además, existen unos 800 metros de vía pecuaria que conecta dos distritos, pero no está incluida en la red de vías protegidas la Comunidad de Madrid. ¿Por qué? Por su pequeño tamaño y desuso. Fuentes de la consejería de Medio Ambiente explican que es una vía menor que solo se utiliza en determinados momentos como \"nexo de territorios\" y para \"conexión ganadera\". Escombros en la explanada. (A.F.) Los tres objetivos de los ecologistas Los ecologistas, por tanto, se marcaron tres objetivos: transformar el sendero en una vía verde, visibilizar que el descampado estaba lleno de escombros y ampliar el horario de visita de la ermita se ampliase. Ahí empezó la gresca con el cura. \"Nosotros no llevábamos ahí los vertidos, los depositábamos para que se viera, porque el ayuntamiento no los recoge. No queríamos molestar al párroco\", continúa García. La cuestión es que gran parte del terreno pertenece al Ministerio de Defensa, es decir, que los servicios de limpieza del ayuntamiento no pueden acceder a todos los rincones donde se acumula la basura. Fuentes del área de Medio Ambiente del Ayuntamiento de Madrid explican que sus profesionales tienen competencias para limpiar hasta la explanada de la iglesia. Todas las semanas recogen escombros, pero hasta ese límite. La torre de la ermita. (A.F.) \"Mira, los videos están ahí\", defiende una de las personas del entorno cercano del párroco que no ha querido dar su nombre. Se refiere a unas grabaciones que publicó Telemadrid donde puede verse a una persona depositando residuos frente a la Ermita. \"Tenemos cámaras y se ve todo\", continúa. Dichas imágenes también fueron entregadas a la policía. Para los eclesiásticos, la labor de estos activistas no es más que una pantomima con tono político: \"Para ellos, la culpa de todo siempre la tiene la iglesia y el PP\". El protagonista de dicho video es Juan García Vicente: \"Soy yo. Acumulamos ahí los escombros para que se vean porque ahí sí le compete al Ayuntamiento. El cura lo ha interpretado a su manera. Además, también plantamos 300 árboles en la vía pecuaria para transformarla en una vía verde. Nos amenazaron con cortarlos\", explica el hombre. Vista de la vía pecuaria en dirección a Aluche. (A.F.) Litronas acumuladas frente al templo. (Cedida) \"Ese es su relato\", defiende el amigo del párroco. Al preguntarle si el cura quería cortar los árboles de los ecologistas, su rostro de sorpresa y estupefacción lo dice todo. \"Todo eso forma parte de su relato\", repite. Desde su punto de vista, lo que quieren los ecologistas es en realidad utilizar el espacio para armar bronca y dar sus discursos. Lo de visibilizar los escombros o plantar árboles está, otra vez, \"dentro de su relato\". Al final, el hartazgo del cura culminó en una querella contra tres miembros de Ecologistas en Acción. En el escrito, al que ha tenido acceso El Confidencial, se denuncia que \"los activistas han ido organizando reuniones en los exteriores de las instalaciones parroquiales con el fin de congregar diferentes personas y acceder posteriormente al interior de la propia parroquia con la intención de hacer una visita guiada dentro de las instalaciones [...] el grupo de personas no respeta el silencio solicitado por respeto a las personas que están orando\". Y continúa. \"Tales hechos están causando en el personal del cementerio una situación de inseguridad y ansiedad de acudir a su puesto de trabajo\". Juan se defiende: \"Pero si somos tres septuagenarios. Yo solo me dedico a regar los 300 árboles que hemos plantado en estos siete años\". Ahora, está en manos de la justicia resolver el conflicto.",
        "enclosure": {
            "link": "https://images.ecestaticos.com/SXAt-vKtOdLqCYW-YqjX38SZ5Dg=/0x0:2048x1536/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com/original/c1e/fad/5cc/c1efad5cc7b6ec7f54e3c2f85050da08.jpg"
        },
        "categories": [],
        "medio": "ElConfidencial"
    },
    {
        "title": "Guerra Rusia-Ucrania, en directo | Zelenski anuncia que la cumbre sobre su plan de paz tendrá lugar el 15 y 16 de junio",
        "pubDate": "2024-05-02 15:09:44",
        "link": "https://www.lasexta.com/noticias/internacional/guerra-rusiaucrania-directo-ucrania-asegura-haber-hundido-buque-ruso-caesar-kunikov-crimea_2024021465cc8dc182085c00016a69fc.html",
        "guid": "https://www.lasexta.com/noticias/internacional/guerra-rusiaucrania-directo-ucrania-asegura-haber-hundido-buque-ruso-caesar-kunikov-crimea_2024021465cc8dc182085c00016a69fc.html",
        "author": "lasextacom",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/364CF2D9-C157-4D4C-91D5-703CA4619E74/imagen-archivo-zelenski_96.jpg?crop=1920,1080,x0,y29&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "El presidente ucraniano ha confirmado que la cumbre sobre la llamada fórmula de paz promovida por su administración para exigir la retirada de las tropas rusas de todo el territorio de Ucrania tendrá lugar en Burgenstock.",
        "content": "El presidente ucraniano ha confirmado que la cumbre sobre la llamada fórmula de paz promovida por su administración para exigir la retirada de las tropas rusas de todo el territorio de Ucrania tendrá lugar en Burgenstock.",
        "enclosure": {
            "link": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/364CF2D9-C157-4D4C-91D5-703CA4619E74/imagen-archivo-zelenski_96.jpg?crop=1920,1080,x0,y29&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
            "type": "image/jpeg",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/364CF2D9-C157-4D4C-91D5-703CA4619E74/imagen-archivo-zelenski_96.jpg?crop=1920,1080,x0,y29&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Internacional",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Persecución al límite en Avilés grabada en directo: \"¡La verdad es que el chacho controla!\"",
        "pubDate": "2024-05-02 14:03:06",
        "link": "https://www.lasexta.com/noticias/sociedad/persecucion-limite-aviles-grabada-directo-verdad-que-chacho-controla_2024050266339d1a8e66020001c6ff47.html",
        "guid": "https://www.lasexta.com/noticias/sociedad/persecucion-limite-aviles-grabada-directo-verdad-que-chacho-controla_2024050266339d1a8e66020001c6ff47.html",
        "author": "sergio-illescas",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages01/2024/05/02/C63B986C-6561-4CAC-AF19-12FE38FD0361/persecucion_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "Un hombre roba un viejo Ford Fiesta rojo y es perseguido por la policía varios kilómetros por una carretera asturiana hasta que se le estropeó el coche y fue detenido.",
        "content": "Dos jóvenes grabaron ayer desde su vehículo una persecución en la variante de Avilés. Un viejo Ford Fiesta rojo se daba a la fuga y una patrulla de la Policía Nacional le pisaba los talones. \"¡Movidón en la variante!\" \"¡No te creo, chaval!\", se escucha exclamar a los chicos que graban en el vídeo. El coche que conducían era robado, según fuentes de la investigación, y no se encontraba en muy buen estado. De hecho, en el vídeo se le ve hacer eses. \"¿Tiene el puente jodido o qué?\", le pregunta uno de los que capta la persecución a su compañero. Para alcanzarlos, los agentes tienen que conducir incluso en sentido contrario. Los que graban, bromean con echar una mano a los policía. \"Me apetece a mí parar el coche. Déjame a mí empotrar el BMW contra él...\", manifiesta entre risas uno de ellos. Los que inmortalizan el momento en vídeo señalan: \"Sacando la mano por la ventanilla va el pavo... La verdad es que el chacho controla\". El ladrón no atiende tampoco al alto de otra patrulla de la Guardia Civil, que lo espera en un cruce. Pero cuando entra a la localidad asturiana de Salinas, el coche falla y tiene que parar, momento en el que son detenidos. En la detención colaboraron un matrimonio, una policía nacional y un guardia civil que está fuera de servicio. El detenido era un viejo conocido de la Policía por robos menores y el coche lo sustrajo en la localidad de Mieres. Dos agentes de la Policía Nacional y uno de Guardia Civil resultaron heridos. Desde la Policía aseguran que los compañeros siguieron los protocolos y no intervinieron con más dureza para no poner en peligro la vida de nadie.",
        "enclosure": {
            "link": "https://dpvclip.lasexta.com/assets16/2024/05/02/35AE2265-427B-4D61-BFBC-4DDB6F1844FF/640x360.mp4",
            "type": "video/mp4",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages01/2024/05/02/C63B986C-6561-4CAC-AF19-12FE38FD0361/persecucion_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Sociedad",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Investigan si los restos exhumados de la fosa del cementerio de Viana do Bolo pertenecen a la 'pasionaria gallega'",
        "pubDate": "2024-05-02 13:57:38",
        "link": "https://www.lasexta.com/noticias/nacional/investigan-restos-exhumados-fosa-cementerio-viana-bolo-pertenecen-pasionaria-gallega_2024050266339bd2c18d400001b0eb14.html",
        "guid": "https://www.lasexta.com/noticias/nacional/investigan-restos-exhumados-fosa-cementerio-viana-bolo-pertenecen-pasionaria-gallega_2024050266339bd2c18d400001b0eb14.html",
        "author": "lasextacom",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages01/2024/05/02/D0FB88E9-F599-472F-B40F-30FF37833F5A/pasionaria-gallega_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "Anuncia Casado fue una sindicalista reconocida por la defensa del campesinado. En 1936 fue perseguida, apaleada, violada y asesinada por los falangistas. Su hijo, Wladimiro confía en que los restos exhumados que han encontrado sean los de su madre.",
        "content": "La Universidad de Santiago y el Instituto de medicina legal de Galicia creen haber encontrado la tumba de Anuncia Casado, también conocida como la pasionaria de gallega, en una fosa del cementerio de Viana do Bolo en Ourense tras encontrar un cadáver con huesos fracturados. Anuncia Casado fue una sindicalista reconocida por la defensa del campesinado. En 1936 fue perseguida, apaleada, violada y asesinada por los falangistas. Su hijo, Wladimiro confía en que los restos exhumados que han encontrado en esta fosa sean los de su madre. \"La mataron a palos. Le destrozaron el cráneo\", cuenta a laSexta el hijo de la pasionaria gallega. Fernando Serrulla, forense del Instituto de medicina legal de Galicia, relata que, por entonces, en 1936, \"dejan a sus hijos muy pequeños en unas condiciones increíbles de un abandono absoluto\". \"La maltratan, la violan, la golpean y pasean su cuerpo con un carro por el pueblo de Viana\", añade. Esto, según Wladimiro, \"es inhumano\". En su acta de defunción el médico dice que murió por comunista: \"muerta a consecuencia de los recientes sucesos revolucionarios y por sus actividades en tal sentido, y de ostentación franca y descaradamente comunista\". Los restos encontrados se encuentran ahora en laboratorio y solo falta confirmar con el ADN de su hijo si son realmente los de Anuncia.",
        "enclosure": {
            "link": "https://dpvclip.lasexta.com/assets15/2024/05/02/038E4B9B-3D1F-4351-8E33-59301A7C9299/640x360.mp4",
            "type": "video/mp4",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages01/2024/05/02/D0FB88E9-F599-472F-B40F-30FF37833F5A/pasionaria-gallega_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "España",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Casa por casa buscando al migrante: así es la nueva política antimigratoria en Reino Unido",
        "pubDate": "2024-05-02 13:51:03",
        "link": "https://www.lasexta.com/noticias/internacional/casa-casa-buscando-migrante-asi-nueva-politica-antiinmigratoria-reino-unido_2024050266339a47c18d400001b0e821.html",
        "guid": "https://www.lasexta.com/noticias/internacional/casa-casa-buscando-migrante-asi-nueva-politica-antiinmigratoria-reino-unido_2024050266339a47c18d400001b0e821.html",
        "author": "lasextacom",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages01/2024/05/02/978A8968-CCFE-41C1-B088-70EE55D99493/caza-migrante_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "Esta semana, el gobierno de Reino Unido, con Rishi Sunak a la cabeza, ha aprobado una nueva reforma que está teniendo ya sus efectos: la policía está acudiendo a casas para encontrar a migrantes.",
        "content": "Desde este miércoles, oficiales del Departamento de Interior se aproximan a casas en Reino Unido en busca de migrantes que deportar por irregularidades en su situación legal en el país, como ser solicitantes de asilo con prácticamente ninguna posibilidad de quedarse en las islas. Esta es la nueva política antiinmigratoria impulsada por Rishi Sunak aprobada hace unos días y en marcha desde ayer. Y precisamente ya se están viendo los resultados. En vídeos mostrados por el propio gobierno británico, muestran el proceso en el que oficiales se presentan en una casa y salen de ellas con un migrante esposado, al que trasladan en un furgón policial. Su aplicación, aseguran periodistas británicos, no es casualidad. Y es que estas imágenes, criticadas por el partido laborista, se pueden ver a solo un día de la celebración de unas reñidas elecciones locales. Y en las calles, la respuesta también se hace notar con numerosas protestas que también han dado lugar a algún pequeño altercado. Una 'solución' que ha trasladado el problema sus vecinos irlandeses, que han visto como estos migrantes se instalaban en las calles de Dublín y la policía irlandesa ha tenido que desalojar las calles llenas de tiendas de campaña que habían llenado algunas zonas de la capital de Irlanda.",
        "enclosure": {
            "link": "https://dpvclip.lasexta.com/assets15/2024/05/02/78D7B343-E570-4FAF-8D5A-D798F88C8B6D/640x360.mp4",
            "type": "video/mp4",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages01/2024/05/02/978A8968-CCFE-41C1-B088-70EE55D99493/caza-migrante_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Internacional",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "¿Se puede reducir la jornada laboral de forma generalizada como piden los sindicatos? José María Camarero responde",
        "pubDate": "2024-05-02 13:17:02",
        "link": "https://www.lasexta.com/programas/al-rojo-vivo/puede-reducir-jornada-laboral-forma-generalizada-como-piden-sindicatos-jose-maria-camarero-responde_202405026633922b8e66020001c6e394.html",
        "guid": "https://www.lasexta.com/programas/al-rojo-vivo/puede-reducir-jornada-laboral-forma-generalizada-como-piden-sindicatos-jose-maria-camarero-responde_202405026633922b8e66020001c6e394.html",
        "author": "al-rojo-vivo",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/F7D493FC-CB36-4E31-B181-965B1D947571/puede-reducir-jornada-laboral-forma-generalizada-como-piden-sindicatos-respuesta-jose-maria-camarero_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "El periodista ha explicado que es difícil que la reducción de la jornada laboral se aplique a todos los trabajadores debido a la estructura que tiene la economía española. \"Hay sectores en los que sería complicado aplicarla\".",
        "content": "José María Camarero ha admitido que es \"complicado\" que se aplique la jornada laboral que piden los sindicatos debido a la estructura de la economía española. El periodista ha señalado que se establezca en el BOE una jornada laboral de 37 horas y media para todos los trabajadores. \"Tenemos una estructura muy centrada en servicios y turismo\", ha indicado, explicando que es complicado que la medida se aplique en estos sectores \"de hoy para mañana\". Sin embargo, ha destacado que no es imposible que acabe sucediendo. Para ello, ha explicado que están negociando una especie de \"flexibilidad\". Camarero ha reconocido que hay una serie de sectores en los que sí que se podría aplicar ya como la industria o la tecnología. \"Se está viendo cómo flexibilizar esa medida para que no haya un impacto en el empleo\", ha explicado, destacando que se puede reducir pero hay que ver cuáles son los matices y los sectores en los que hay que hacerlo más despacio para que \"la medida no provoque el efecto contrario\".",
        "enclosure": {
            "link": "https://dpvclip.lasexta.com/assets15/2024/05/02/D2CE8ED5-BF4C-4D3D-A068-2AB3F210AC2C/640x360.mp4",
            "type": "video/mp4",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/F7D493FC-CB36-4E31-B181-965B1D947571/puede-reducir-jornada-laboral-forma-generalizada-como-piden-sindicatos-respuesta-jose-maria-camarero_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Al Rojo Vivo",
            "Programas",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Investigan a un hombre que tenía a una familia viviendo y trabajando en su nave por 50 euros a la semana",
        "pubDate": "2024-05-02 12:29:22",
        "link": "https://www.lasexta.com/noticias/sociedad/investigan-hombre-que-tenia-familia-viviendo-trabajando-nave-50-euros-semana_20240502663387228e66020001c6c182.html",
        "guid": "https://www.lasexta.com/noticias/sociedad/investigan-hombre-que-tenia-familia-viviendo-trabajando-nave-50-euros-semana_20240502663387228e66020001c6c182.html",
        "author": "europa-press",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/0E9B786F-4F9D-4FEC-86CF-BC08783F914A/agentes-guardia-civil-tareas-investigacion_96.jpg?crop=2000,1125,x0,y189&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "Las víctimas no estaban dadas de alta en la Seguridad Social y se encontraban en una situación lamentable. Además, hay otros cuatro investigados por intimidar a la familia de trabajadores con un arma simulada para que retiraran la denuncia.",
        "content": "La Guardia Civil investiga al dueño de una empresa por tener a una familia viviendo y trabajando en una nave industrial, situada en la localidad valenciana de Silla, pagándoles apenas 50 euros a la semana, según ha informado el Instituto Armado. Además, hay otros cuatro investigados por presuntamente intimidar a la familia de trabajadores con un arma simulada para que retiraran la denuncia e incluso llegaron a robar su móvil a un menor de edad. Los agentes iniciaron la investigación, en el marco de la operación 'Costeiro', tras tener conocimiento de los hechos y comprobar que en el interior de la nave había una familia no solo trabajando, sino viviendo. Los trabajadores se encontraban en una situación lamentable, trabajaban por tan solo 50 euros a la semana y no estaban dados de alta en la Seguridad Social. Después de que los agentes inspeccionaran la nave, irrumpieron en el lugar de trabajo de la familia tres hombres encapuchados que portaban un arma simulada con la intención de que retiraran la denuncia. Llegaron incluso a robar el móvil a una de las víctimas, a quien provocaron lesiones. Los agentes, tras identificar a uno de los investigados, realizaron un dispositivo para localizarle, lo que resultó complicado por las diferentes evasivas utilizadas y por el hecho de que residía en otra provincia. Finalmente, se procedió a la investigación de un hombre de 48 años de nacionalidad española por la comisión de un delito contra los derechos de los trabajadores. También se ha procedido a la investigación de cuatro hombres de entre 21 y 52 años, de nacionalidad colombiana, por un delito de robo con violencia y otro delito contra la administración de justicia.",
        "enclosure": {
            "link": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/0E9B786F-4F9D-4FEC-86CF-BC08783F914A/agentes-guardia-civil-tareas-investigacion_96.jpg?crop=2000,1125,x0,y189&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
            "type": "image/jpeg",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/0E9B786F-4F9D-4FEC-86CF-BC08783F914A/agentes-guardia-civil-tareas-investigacion_96.jpg?crop=2000,1125,x0,y189&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Sociedad",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Albert Pla lanza 'Bombas en Madrid', su nueva canción junto a Alfred García",
        "pubDate": "2024-05-02 11:39:35",
        "link": "https://www.lasexta.com/noticias/cultura/albert-pla-lanza-bombas-madrid-nueva-cancion-junto-alfred-garcia_2024050266337b77c18d400001b08d2f.html",
        "guid": "https://www.lasexta.com/noticias/cultura/albert-pla-lanza-bombas-madrid-nueva-cancion-junto-alfred-garcia_2024050266337b77c18d400001b08d2f.html",
        "author": "efe",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/23A9BF40-8B5D-4706-8F52-80E5FC46C898/cantautor-actor-albert-pla_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "Junto con la colaboración de Alfred García, el cantautor ha sacado su nuevo tema 'Bombas en Madrid', una nueva canción marcada por su característica ironía.",
        "content": "Tras una intensa temporada destacando en la pequeña pantalla, Albert Pla vuelve a concentrarse en su faceta musical con el lanzamiento de 'Bombas en Madrid', una canción que ya sonaba en sus directos, pero que ahora cobra una nueva vida con los arreglos y la colaboración de Alfred García. El que es uno de los artistas más polivalentes de la escena sigue sorprendiendo al público tras más de 25 años en la carretera y ahora lo hace con este nuevo tema marcado por la ironía que caracteriza sus creaciones en torno al concepto de 'bomba' literal y metafóricamente, que ya ha sonado en directo hasta delante de una obra de la talla del 'Guernica' de Picasso. A partir de este jueves, esta canción, que ya se ha convertido en uno de los himnos del directo de Albert Pla, está disponible en todas las plataformas digitales en su versión de estudio de la mano del sello Oso Polita. El también catalán Alfred García fue uno de los causantes de que se realizase la grabación, ya que fueron sus guitarras y arreglos los que acabaron de darle forma. Tras haber trabajado con figuras como Pedro Almodóvar, Álex de la Iglesia o Isabel Coixet, uno de los puntos álgidos de la carrera de Pla llegaba hace unos meses con su papel protagonista en una de las series del año, 'La Mesías', que lo llevó a recibir grandes reconocimientos como el Premio Feroz a 'Mejor actor de reparto de una serie'. El de Sabadell está ahora inmerso en la Gira Rumbagenarios, que lo llevará junto a la The Surprise Band a recorrer salas y festivales de todo el país con este show festivo y de lo más especial que cuenta con todos los ingredientes: coreografía, proyecciones y unos músicos fantásticos que dejan a Albert Pla con las manos libres y el cuerpo desatado para entregarse a un repertorio infalible. El artista ha sumado esta misma semana cinco nuevas fechas a esta intensa gira, que incluye las siguientes paradas: el 3 de mayo en Zaragoza, el 18 de mayo en Palma, el 31 de mayo en Sabadell, el 28 de junio en Girona, el 11 de julio en Barcelona, el 12 de julio en Bilbao, el 13 de julio en Tarragona, el 26 de septiembre en Santiago de Compostela, el 27 de septiembre en Sevilla, el 30 de noviembre en Murcia y el 10 de enero de 2025 en Valencia.",
        "enclosure": {
            "link": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/23A9BF40-8B5D-4706-8F52-80E5FC46C898/cantautor-actor-albert-pla_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
            "type": "image/jpeg",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/23A9BF40-8B5D-4706-8F52-80E5FC46C898/cantautor-actor-albert-pla_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Cultura",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "¿A la tercera va la vencida? Sumar resucita la reforma de la ley mordaza",
        "pubDate": "2024-05-02 10:42:11",
        "link": "https://www.lasexta.com/noticias/nacional/tercera-vencida-sumar-resucita-reforma-ley-mordaza_2024050266336d4fc0b95c0001d95f65.html",
        "guid": "https://www.lasexta.com/noticias/nacional/tercera-vencida-sumar-resucita-reforma-ley-mordaza_2024050266336d4fc0b95c0001d95f65.html",
        "author": "efe",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/69E03254-7343-49C5-89C1-913F1BEB612B/imagen-archivo-yolanda-diaz_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "La primera promesa para acabar con ella llegó hace ya siete años con el PP todavía en el Gobierno. Una norma que, cerca de cumplir nueve años, está destinada a someterse a su tercer intento de reforma. ",
        "content": "La primera promesa para acabar con ella llegó hace ya siete años con el PP todavía en el Gobierno pero con una mayoría de izquierdas conjurada para enterrar la ley mordaza o de seguridad ciudadana, una norma que, cerca de cumplir nueve años, está destinada a someterse a su tercer intento de reforma. Lo ha recordado esta misma semana la vicepresidenta segunda del Gobierno y líder de Sumar, Yolanda Díaz, tras escuchar a Pedro Sánchez decir que continuaba al frente del Ejecutivo tras cinco días de reflexión. Díaz deja claro que en este periodo de reinicio Sánchez debe ir más allá de lo que se pactó en el acuerdo de investidura y pone sobre la mesa una reforma del Poder Judicial, sin negociarlo con el PP, y modificar la ley mordaza. Del primer asunto el propio Sánchez ha apuntado que la responsabilidad del Gobierno es renovar el Consejo General del Poder Judicial para sacarlo de la situación \"lamentable\" en la que el PP lo ha metido; del segundo envite, la mordaza, no se ha pronunciado, si bien es cierto que se trata de una reforma comprometida e incómoda, de la que, por el momento, ningún grupo ha registrado alguna proposición de ley de reforma o derogación. Hace un año su modificación se descalabró en la Comisión de Interior, en su penúltimo paso antes de pasar al Congreso, ante la imposibilidad de llegar a un acuerdo entre los seis partidos favorables a su reforma -PSOE, Unidas Podemos, PNV, ERC, EH Bildu y Junts- en los cuatro puntos más calientes de la ley. Esta fue la ocasión que la vigente norma, aprobada con la mayoría absoluta del PP en 2015, ha estado más cerca de su final, aunque en un primer intento el consenso parlamentario era mayor y lo que hizo fracasar la reforma, también casi ultimada, fue la convocatoria de las elecciones generales del 28 abril de 2019. Estos son los hechos más relevantes desde que hace siete años se diera el primer paso para dinamitar una ley que \"presume\" de ser la normativa más empleada durante el estado de alarma, de lograr el respaldo del Tribunal Constitucional en la mayoría de su articulado y hasta ahora de sobrevivir a su destino. Cronología de la ley mordaza En 2017 se produjo el primer intento de reformarla con el PP en Moncloa. El 21 de marzo el Pleno del Congreso daba el primer paso para modificar la ley al dar luz verde a la toma en consideración de dos proposiciones de ley del PSOE, que apostaba por derogarla, y del PNV, que pedía revisarla en 44 apartados. Con el PP aún en la Moncloa pero con minoría parlamentaria, PSOE, ERC, Unidos Podemos y PNV expresaron sus quejas con los retrasos en la tramitación. En 2018, la moción de censura despierta la reforma. El entonces ministro del Interior Juan Ignacio Zoido, del PP, tendió diálogo al PSOE. La propuesta siguió durmiendo en un cajón y no sería hasta meses después de la moción de censura al presidente Mariano Rajoy y con Pedro Sánchez en el Gobierno cuando la iniciativa se desempolvó para analizarse en ponencia. En 2019, las elecciones de abril frustran una nueva ley. Tras escuchar a 14comparecientes, los diputados tuvieron en febrero una última reunión. Dieron carpetazo a sus propuestas porque las elecciones del 28 de abril obligaron a disolver las Cortes. Solo restaban dos o tres reuniones para presentar un dictamen y el acuerdo. Los portavoces de PSOE, PP, Unidos Podemos y Ciudadanos coincidieron en que los retoques estaban bastante consensuados. En 2020, se convierte en la norma más usada en pandemia. Frustrada su reforma, la ley se convirtió en protagonista inesperada de la pandemia del coronavirus. Fue la norma más empleada para sancionar por desobediencia a quienes se saltaban las restricciones impuestas por los estados de alarma. En el primero -del 14 de marzo al 20 de junio- las multas resueltas por infracciones graves supusieron 115 millones de euros. Con todo, fue también el año en que se inició el segundo intento de dinamitarla. En septiembre todos los partidos, excepto PP y Vox, daban su visto bueno a la misma iniciativa que el PNV presentó en 2017. En 2021, despega el segundo intento. En febrero, se retoma su tramitación pero a paso muy lento. Tras más de 40 prórrogas de presentación de enmiendas, en noviembre la iniciativa parece que por fin se desatasca con PSOE y Unidas Podemos decididos a liderar los cambios con un paquete conjunto de más de 40 modificaciones contra los que policías nacionales y guardias civiles protestaron en Madrid. En 2022, vuelve a quedarse en punto muerto. El año arrancó con la celebración de varias sesiones de ponencia. Tras salvar los partidos de izquierdas sin ninguna dificultad cambios planteados hace años, como los cacheos o el plazo máximo para identificaciones en comisaria, los acuerdos llegan a punto muerto. Los grupos pro reforma -PSOE, Unidas Podemos, PNV, ERC, Eh Bildu y Junts- trasladan sus negociaciones fuera de la ponencia. Se celebraron más de 30 reuniones y se alcanzaron acuerdos en otros 15 artículos, pero no lograron esquivar sus escollos en los cuatro puntos que desde el inicio se calificaron como los preceptos \"calientes\" y \"polémicos\" de la ley: material antidisturbios, faltas de respeto a la autoridad, la desobediencia y resistencia y devoluciones en caliente. En 2023, ERC y EH Bildu apuntillan el fracaso. Después de un año y medio de negociaciones y medio centenar de reuniones formales e informales en las que hay acuerdo para modificar 36 de los 54 artículos, la ponencia se da por concluida y el 14 de marzo el dictamen se eleva a la comisión de Interior. Sigue sin haber acuerdo en los cuatro puntos sensibles, especialmente en el que afecta al material antidisturbios, asunto en el que ERC y EH Bildu se muestran muy en contra. Los 18 votos de PSOE, Unidas Podemos y PNV no son suficientes para sacar adelante el dictamen, que rechazan ERC, EH Bildu y Junts junto con los votos de PP, Vox, Ciudadanos y UPN, que consiguieron sumar 19, por lo que la reforma vuelve a fracasar.",
        "enclosure": {
            "link": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/69E03254-7343-49C5-89C1-913F1BEB612B/imagen-archivo-yolanda-diaz_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
            "type": "image/jpeg",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/69E03254-7343-49C5-89C1-913F1BEB612B/imagen-archivo-yolanda-diaz_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "España",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Comprobar los resultados de lotería de hoy | Bonoloto, Cupón Diario, Triplex y Super Once del miércoles 1 de mayo de 2024",
        "pubDate": "2024-05-02 10:27:02",
        "link": "https://www.lasexta.com/loteria/comprobar-resultados-loteria-hoy-bonoloto-cupon-diario-triplex-super-once-miercoles-1-mayo-2024_2024050166327830c0b95c0001d7a8b8.html",
        "guid": "https://www.lasexta.com/loteria/comprobar-resultados-loteria-hoy-bonoloto-cupon-diario-triplex-super-once-miercoles-1-mayo-2024_2024050166327830c0b95c0001d7a8b8.html",
        "author": "lasextacom",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2023/10/11/6A356B55-D839-40B0-BD73-84C6757A7E4C/comprobar-resultados-loteria-bonoloto-cupon-diario-triplex-super-once-miercoles-11-octubre-2023_96.jpg?crop=1600,900,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "Te traemos los resultados del miércoles 1 de mayo de los juegos diarios de la ONCE y de la Bonoloto de Loterías y Apuestas del Estado. Comprueba a continuación los números premiados.",
        "content": "Este miércoles 1 de mayo de 2024, Loterías y Apuestas del Estado y la ONCE sortean sus juegos de azar diarios. A las 21:25h conoceremos el resultado del Cupón Diario de la ONCE , con su premio de 35.000 euros y el premio especial de 500.000 euros al número y serie. A las 21.30h será el turno de la Bonoloto, que cuenta con un bote para hoy de ______ euros. Por su parte, tanto el Triplex como el Super Once se juegan a las 10:00h, a las 12:00h y a las 21:15h. Resultado Bonoloto Los números 05 17 28 40 41 47 son los premiados en el sorteo de la Bonoloto de este miércoles. El 45 pasa a ser el número complementario ganador y el reintegro es el 09. Recordamos que la cantidad de dinero correspondiente a cada premio varía en función de la recaudación diaria de la venta de boleto y del bote acumulado. Resultado del Cupón Diario de la ONCE El número premiado en el Cupón Diario de la ONCE con 35.000 euros es el 19685 en el sorteo de este miércoles 1 de mayo de 2024. Además, el premio de 500.000 euros para el jugador que haya acertado la serie 036 del mismo número premiado. Este último recibirá 36.000 euros anuales durante 25 años. Todos los décimos cuyo último número sea el 5 obtienen el reintegro. Resultados Triplex Los tres sorteos del Triplex de la ONCE han dejado como ganadoras a las siguientes cifras: Primer sorteo: 572 Segundo sorteo: 878 Tercer sorteo: 630 Resultados Super Once Los sorteos del Super Once han emitido las siguientes combinaciones de números ganadoras: Primer sorteo: 02 06 15 25 33 35 37 45 48 49 52 62 63 64 66 69 76 77 80 84 Segundo sorteo: 10 13 18 23 27 34 35 36 40 45 46 47 49 54 63 64 67 74 78 80 Tercer sorteo: 01 05 06 16 18 20 21 23 33 34 42 45 47 49 51 56 61 65 69 83 Sorteos de la ONCE El Cupón Diario de la ONCE es el sorteo más longevo de esta organización nacional. Los jugadores adquieren un boleto por 2 euros que contiene un número de cinco cifras, y cada boleto tiene un número de serie especial. Si se acierta el primero, el premio es de 35.000 euros, que ascienden a 500.000 para aquellos jugadores que acierten la serie del mismo número. También hay premios menores por el sistema de 'Ganar por los dos lados': las cuatros primeras y últimas cifras se llevan premio, como las tres y dos primeras y últimas cifras del número ganador, además de los dos reintegros generados. El Triplex de la ONCE y el Super Once se sortean de manera diaria a las 10:00h, a las 12:00h y a las 21:15h. En el primero se realiza una apuesta de 0,50 euros por un número de tres cifras que, si se acierta, otorga 150 euros. En el segundo, se escogen de 5 a 11 números del 1 al 85. En cada sorteo se extraen 20 números. La cantidad conseguida depende de la apuesta realizada. El premio máximo a conseguir en este juego es de un millón de euros, si se apuesta por 11 números y se aciertan los 11. Bonoloto La Bonoloto se sortea todos los días a las 21:30h, y es una de las loterías más jugadas en España por lo asequible de su precio. Consiste en escoger seis números del 1 al 49, a los que se asigna de manera aleatoria un reintegro. Para jugar es necesario realizar, como mínimo, dos apuestas de 0,50 euros cada una. La modalidad simple permite realizar entre una y ocho apuestas por boleto, mientras que la modalidad múltiple permite escoger hasta 11 números por apuesta. El funcionamiento de este juego es muy similar al de La Primitiva, siendo su precio menor al de este último. Esto repercute en los premios, que también son menores, ya que el dinero destinado a ellos corresponde al 55% de la recaudación total, yendo el 45% restante a las arcas del Estado. ___ *ADVERTENCIA: LaSexta.com no se hace responsable en caso de errores u omisiones. Las únicas listas oficiales válidas de resultados de los diferentes sorteos son las que publican la Organización Nacional de Ciegos Españoles (ONCE) y Loterías y Apuestas del Estado (SELAE).",
        "enclosure": {
            "link": "https://fotografias.lasexta.com/clipping/cmsimages02/2023/10/11/6A356B55-D839-40B0-BD73-84C6757A7E4C/comprobar-resultados-loteria-bonoloto-cupon-diario-triplex-super-once-miercoles-11-octubre-2023_96.jpg?crop=1600,900,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
            "type": "image/jpeg",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2023/10/11/6A356B55-D839-40B0-BD73-84C6757A7E4C/comprobar-resultados-loteria-bonoloto-cupon-diario-triplex-super-once-miercoles-11-octubre-2023_96.jpg?crop=1600,900,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Lotería",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Los detalles de la declaración de Daniel Sancho: lágrimas, amenazas y chantajes",
        "pubDate": "2024-05-02 09:59:13",
        "link": "https://www.lasexta.com/noticias/sociedad/detalles-declaracion-daniel-sancho-lagrimas-amenazas-chantajes_20240502663363f1c18d400001b05771.html",
        "guid": "https://www.lasexta.com/noticias/sociedad/detalles-declaracion-daniel-sancho-lagrimas-amenazas-chantajes_20240502663363f1c18d400001b05771.html",
        "author": "lasextacom",
        "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/B06630BD-20F4-466A-9BE1-AFC721D9EB06/arv-sancho_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply",
        "description": "El intérprete impuesto por el juzgado en el juicio contra Daniel Sancho, Somwang Khruasuwan, ha hablado por primera vez ante los medios y ha explicado todo lo ocurrido en el último día de juicio.",
        "content": "El juicio contra Daniel Sancho por el asesinato de Edwin Arrieta ha llegado a su fin este jueves en Tailandia, un día antes de la fecha inicialmente prevista para el final de un proceso que se ha prolongado cerca de un mes y que ha dejado la última imagen vista del español, captada en exclusiva por laSexta. El juez, cuya identidad es confidencial, ha fijado la fecha de la lectura de la sentencia para el 29 de agosto a las 10:00 horas, según ha avanzado la agencia Efe. Después, ambas partes tendrán la oportunidad de recurrir en el plazo de un mes. Durante la última sesión del juicio, Sancho ha realizado un alegato final de cerca de 45 minutos, que él mismo había solicitado, según la misma agencia. Y a la salida del juzgado, ha hablado por primera vez Somwang Khruasuwan, el intérprete impuesto para traducir todo lo que ocurriese dentro para ambas partes, que ha desvelado todo lo ocurrido durante el proceso. Khruasuwan ha ratificado la versión de Sancho, de la que señala que ha pedido disculpas y se arrepiente de lo sucedido: \"Lo sintió mucho por la muerte y para la familia de Edwin. Se arrepiente mucho. Lo que más sintió es que no pudo ayudar a la familia de Edwin a enterrar el cuerpo. Ha pedido perdón y se arrepiente. Quiere ayudar a la familia de Edwin, pero no tiene dinero para hacerlo\". \"Ha llorado muchas veces durante el proceso. Y durante su último alegato. Ha llorado varias veces durante el proceso. Es un proceso que le hace mucho dolor a él. Sabe lo que es la pérdida de una vida, de una familia y creo que lo que ve el mismo de cómo le aman sus padres a él\", añade. Además, Somwang Khruasuwan ha explicado de qué ha tratado el alegato final de Sancho: \"De su declaración podemos decir que habría explicado sus sentimientos y lo que piensa realmente de cómo se sintió durante todo este tiempo. Sintió mucho lo que pasó pero ha habido defensa personal\". Por último, el intérprete ha señalado la \"buena relación\" que Daniel Sancho mantiene con sus padres: \"Daniel tiene buena relación con sus padres. Su madre estuvo muy activa al principio visitándole en la cárcel y su padre también se preocupa por él\". De hecho, Rodolfo Sancho ha llevado la iniciativa por parte de la defensa, mientras que los abogados tailandeses \"son más relajados\". La versión de Daniel Sancho sobre lo ocurrido El intérprete ha explicado a los medios de comunicación desplazados al juzgado en Tailandia la versión que ha defendido Daniel Sancho de lo ocurrido el pasado 2 de agosto en el bungalow. Según Daniel (y a través de las palabras del intérprete), Edwin Arrieta le habría obligado a tener relaciones sexuales bajo la amenaza de matar a su hermana pequeña y a su novia en caso omiso. \"Sintió mucho miedo, mucha presión y no pudo controlarse\", confiesa Khruasuwan. Es entonces cuando se inicia la pelea y Sancho le da dos puñetazos, con el matiz que entre uno y otro Edwin tiene todavía vida. Cuando Arrieta ya se encuentra en el suelo, Daniel Sancho asegura que se sentó en la cama a pensar qué hacer durante una hora, hasta que decide desmembrarlo con unos cuchillos que tiene en el bungalow porque quería grabar vídeos de cocina. Según explica Khruasuwan, Sancho añade que después tira los restos al mar y a la basura porque la marea es muy baja y se pone a remar y no consigue alejarse de la tierra. Luego, denuncia la desaparición en la comisaría sabiendo que él ha hecho desaparecer el cuerpo de Edwin Arrieta.",
        "enclosure": {
            "link": "https://dpvclip.lasexta.com/assets15/2024/05/02/9A52E321-14B5-49C8-9D64-046DEC41F9B3/640x360.mp4",
            "type": "video/mp4",
            "thumbnail": "https://fotografias.lasexta.com/clipping/cmsimages02/2024/05/02/B06630BD-20F4-466A-9BE1-AFC721D9EB06/arv-sancho_96.jpg?crop=1920,1080,x0,y0&amp;width=1200&amp;height=675&amp;optimize=low&amp;format=webply"
        },
        "categories": [
            "Sociedad",
            "Noticias",
            "laSexta"
        ],
        "medio": "LaSexta"
    },
    {
        "title": "Lo que escondía la convocatoria de la orgía del Viña Rock en Villarrobledo",
        "pubDate": "2024-05-02 16:56:03",
        "link": "https://www.elcorreo.com/sociedad/orgia-villarrobledo-lo-que-escondia-20240502132027-nt.html",
        "guid": "https://www.elcorreo.com/sociedad/orgia-villarrobledo-lo-que-escondia-20240502132027-nt.html",
        "author": "Helena Rodríguez",
        "thumbnail": "",
        "description": "Los organizadores lamentan la polemica que se ha generado por «unos talleres»",
        "content": "Los organizadores lamentan la polemica que se ha generado por \"unos talleres\"",
        "enclosure": {
            "link": "https://s1.ppllstatics.com/elcorreo/www/multimedia/2024/05/02/orgia-villarrobledo-vina-rock-kzmF--758x531@El Correo.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Shanidar Z, un rostro femenino con más de 75.000 años de historia",
        "pubDate": "2024-05-02 16:54:58",
        "link": "https://www.elcorreo.com/ciencia/rostro-neanderta-investigacion-20240502170117-ntrc.html",
        "guid": "https://www.elcorreo.com/ciencia/rostro-neanderta-investigacion-20240502170117-ntrc.html",
        "author": "Daniel Roldán",
        "thumbnail": "",
        "description": "nvestigadores reconstruyen la cara de una mujer neandertal de unos 40 años gracias a 200 fragmentos óseos y las últimas tecnologías",
        "content": "nvestigadores reconstruyen la cara de una mujer neandertal de unos 40 años gracias a 200 fragmentos óseos y las últimas tecnologías",
        "enclosure": {
            "link": "https://s3.ppllstatics.com/rc/www/multimedia/2024/05/02/shanidar-k3MH--758x531@RC.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Valverde pide al club que \"valore\" el fichaje de un central, porque ha habido \"mucho riesgo\"",
        "pubDate": "2024-05-02 16:53:26",
        "link": "https://athletic.elcorreo.com/valverde-dice-club-valorar-fichar-central-jugado-20240502173442-nt.html",
        "guid": "https://athletic.elcorreo.com/valverde-dice-club-valorar-fichar-central-jugado-20240502173442-nt.html",
        "author": "Carlos Nieto",
        "thumbnail": "",
        "description": "El entrenador del Athletic rehúye hablar de su futuro y por hecho que habrá que reforzarse en defensa: «Normalmente no suele salir bien»",
        "content": "El entrenador del Athletic rehúye hablar de su futuro y por hecho que habrá que reforzarse en defensa: \"Normalmente no suele salir bien\"",
        "enclosure": {
            "link": "https://s3.ppllstatics.com/elcorreo/athletic/multimedia/2024/05/02/paredes-vivian-kDOI--758x531@El Correo.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Bordalás deja las cosas claras sobre su encontronazo con Williams en septiembre",
        "pubDate": "2024-05-02 16:52:37",
        "link": "https://athletic.elcorreo.com/bordalas-sobre-encontrazo-williams-septiembre-sinceramente-acuerdo-20240502175539-nt.html",
        "guid": "https://athletic.elcorreo.com/bordalas-sobre-encontrazo-williams-septiembre-sinceramente-acuerdo-20240502175539-nt.html",
        "author": "Juanma Mallo",
        "thumbnail": "",
        "description": "El técnico del Getafe dice que La Catedral es «un gran estadio» en el día antes de recibir al Athletic",
        "content": "El técnico del Getafe dice que La Catedral es \"un gran estadio\" en el día antes de recibir al Athletic",
        "enclosure": {
            "link": "https://s3.ppllstatics.com/elcorreo/athletic/multimedia/2024/05/02/bordalas-williams-kSRF--758x531@El Correo.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Precio y reparto de poder: claves del éxito en la fusión de BBVA y Sabadell",
        "pubDate": "2024-05-02 16:35:05",
        "link": "https://www.elcorreo.com/economia/banca/bbva-sufre-bolsa-sabadell-dispara-ante-posible-20240502090820-ntrc.html",
        "guid": "https://www.elcorreo.com/economia/banca/bbva-sufre-bolsa-sabadell-dispara-ante-posible-20240502090820-ntrc.html",
        "author": "Clara Alba",
        "thumbnail": "",
        "description": "El banco comprador sufre en bolsa mientras que Sabadell repunta otro 3,5% tras conocerse la oferta para la posible unión",
        "content": "El banco comprador sufre en bolsa mientras que Sabadell repunta otro 3,5% tras conocerse la oferta para la posible unión",
        "enclosure": {
            "link": "https://s1.ppllstatics.com/rc/www/multimedia/2024/05/02/bbva-sabadell-afp-k1GI--758x531@RC.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "El torneo Bilbao Iron Cup de cesta apunta al lleno desde la primera jornada",
        "pubDate": "2024-05-02 16:19:34",
        "link": "https://www.elcorreo.com/deportes/pelota/torneo-bilbao-iron-cup-cesta-apunta-lleno-20240502141845-nt.html",
        "guid": "https://www.elcorreo.com/deportes/pelota/torneo-bilbao-iron-cup-cesta-apunta-lleno-20240502141845-nt.html",
        "author": "Juan Pablo Martín",
        "thumbnail": "",
        "description": "El festival de este viernes enfrentará a Goitia y Basque con Urrutia y Del Río, así como a Erkiaga e Ibarluzea contra Barandika y Lekerika",
        "content": "El festival de este viernes enfrentará a Goitia y Basque con Urrutia y Del Río, así como a Erkiaga e Ibarluzea contra Barandika y Lekerika",
        "enclosure": {
            "link": "https://s2.ppllstatics.com/elcorreo/www/multimedia/2024/05/02/cesta-kHVG--758x531@El Correo.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Aitor Elordi: \"Mi partido empieza el sábado\"",
        "pubDate": "2024-05-02 16:19:25",
        "link": "https://www.elcorreo.com/deportes/pelota/aitor-elordi-partido-empieza-sabado-20240502131417-nt.html",
        "guid": "https://www.elcorreo.com/deportes/pelota/aitor-elordi-partido-empieza-sabado-20240502131417-nt.html",
        "author": "Juan Pablo Martín",
        "thumbnail": "",
        "description": "El campeón del Manomanista necesita que Artola gane a Zabala en el Labrit y una victoria ante Ezkurdia el domingo en el Bizkaia",
        "content": "El campeón del Manomanista necesita que Artola gane a Zabala en el Labrit y una victoria ante Ezkurdia el domingo en el Bizkaia",
        "enclosure": {
            "link": "https://s1.ppllstatics.com/elcorreo/www/multimedia/2024/05/02/mallabi-kMlH--758x531@El Correo.JPG",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Camela se moja sobre la canción 'Zorra' para Eurovisión: \"España es España\"",
        "pubDate": "2024-05-02 16:19:13",
        "link": "https://www.elcorreo.com/culturas/musica/eurovision/camela-moja-sobre-cancion-zorra-eurovision-2024-espana-20240502181748-nt.html",
        "guid": "https://www.elcorreo.com/culturas/musica/eurovision/camela-moja-sobre-cancion-zorra-eurovision-2024-espana-20240502181748-nt.html",
        "author": "Gabriel Cuesta",
        "thumbnail": "",
        "description": "Los reyes de la 'tecnorumba' opinan sobre la propuesta de Nebulossa para el festival",
        "content": "Los reyes de la 'tecnorumba' opinan sobre la propuesta de Nebulossa para el festival",
        "enclosure": {
            "link": "https://s2.ppllstatics.com/elcorreo/www/multimedia/2024/05/02/camela-eurovision-comentario-kxgD--758x531@El Correo.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Etxeita: \"Sabemos lo que tenemos que hacer para hacerles daño\"",
        "pubDate": "2024-05-02 16:18:36",
        "link": "https://www.elcorreo.com/deportes/futbol/liga-segunda/etxeita-sabemos-hacerles-dano-20240502181836-nt.html",
        "guid": "https://www.elcorreo.com/deportes/futbol/liga-segunda/etxeita-sabemos-hacerles-dano-20240502181836-nt.html",
        "author": "Fernando Romero",
        "thumbnail": "",
        "description": "El central zornotzarra augura un derbi «de tensión» porque «los dos necesitamos los puntos»",
        "content": "El central zornotzarra augura un derbi \"de tensión\" porque \"los dos necesitamos los puntos\"",
        "enclosure": {
            "link": "https://s2.ppllstatics.com/elcorreo/www/multimedia/2024/05/02/etxeita-kBPI--758x531@El Correo.jpeg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Orduña se prepara para vivir nueve días de fiesta por sus 'Ochomayos'",
        "pubDate": "2024-05-02 16:16:44",
        "link": "https://www.elcorreo.com/bizkaia/nervion/orduna-prepara-exprimir-nueve-dias-fiesta-ochomayos-20240502181643-nt.html",
        "guid": "https://www.elcorreo.com/bizkaia/nervion/orduna-prepara-exprimir-nueve-dias-fiesta-ochomayos-20240502181643-nt.html",
        "author": "Alba Peláez",
        "thumbnail": "",
        "description": "El grupo Txarlazo Mendi Taldea lanzará este viernes el txupinazo que abrirá las primeras grandes celebraciones del año en la comarca",
        "content": "El grupo Txarlazo Mendi Taldea lanzará este viernes el txupinazo que abrirá las primeras grandes celebraciones del año en la comarca",
        "enclosure": {
            "link": "https://s1.ppllstatics.com/elcorreo/www/multimedia/2024/05/02/ochomayos-orduna-kycF--758x531@El Correo.jpg",
            "type": "image/jpeg"
        },
        "categories": [],
        "medio": "ElCorreo"
    },
    {
        "title": "Sánchez se rodea en Barcelona de fans del PSC y redobla su ataque a la prensa: \"Van a ir con todo a por nosotros\"",
        "pubDate": "2024-05-02 19:24:40",
        "link": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/6633e199fdddff30578b45ab.html",
        "guid": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/6633e199fdddff30578b45ab.html",
        "author": "Víctor Mondelo",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146758780082_150x0.jpg",
        "description": "3.000 personas jalean al presidente en su ingreso oficial en la campaña catalana <a href=\"https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/6633e199fdddff30578b45ab.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "3.000 personas jalean al presidente en su ingreso oficial en la campaña catalana.",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146758780082.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146758780082_150x0.jpg"
        },
        "categories": [
            "Artículos Víctor Mondelo"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "Salvador Illa ya no esconde posibles pactos con el nacionalismo y se abre a gobernar con Junts tras las elecciones catalanas del 12-M",
        "pubDate": "2024-05-02 13:02:37",
        "link": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/66337225fdddff44708b45b0.html",
        "guid": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/66337225fdddff44708b45b0.html",
        "author": "Gerard Melgar",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146474685882_150x0.jpg",
        "description": "\"No pactaremos con el PSC\", asegura por su parte el cabeza de lista de JxCat, Carles Puigdemont <a href=\"https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/66337225fdddff44708b45b0.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "\"No pactaremos con el PSC\", asegura por su parte el cabeza de lista de JxCat, Carles Puigdemont.",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146474685882.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146474685882_150x0.jpg"
        },
        "categories": [
            "Artículos Gerard Melgar",
            "Elecciones Catalanas",
            "PSC",
            "Junts per Catalunya",
            "Salvador Illa",
            "Carles Puigdemont",
            "Jordi Turull",
            "ERC",
            "Catalunya en Comú",
            "Sumar",
            "Elecciones Autonómicas",
            "Generalitat de Cataluña",
            "Política",
            "PSOE"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "Un manifiesto liderado por el ex socialista Nicolás Redondo Terreros pide \"un voto constitucionalista sin engaños\" en las elecciones del 12-M",
        "pubDate": "2024-05-02 17:28:48",
        "link": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/66334ca1e4d4d8b8038b45b2.html",
        "guid": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/66334ca1e4d4d8b8038b45b2.html",
        "author": "Gerard Melgar",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146378968893_150x0.jpg",
        "description": "Denuncia que el PSC \"se ha apartado de la senda constitucional aceptando la amnistía, jaleando la política lingüística discriminatoria o aceptando negociaciones espurias en el extranjero\" <a href=\"https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/02/66334ca1e4d4d8b8038b45b2.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "Denuncia que el PSC \"se ha apartado de la senda constitucional aceptando la amnistía, jaleando la política lingüística discriminatoria o aceptando negociaciones espurias en el extranjero\".",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146378968893.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146378968893_150x0.jpg"
        },
        "categories": [
            "Artículos Gerard Melgar",
            "Elecciones Catalanas",
            "Elecciones Autonómicas",
            "PSOE",
            "PSC",
            "Pedro Sánchez",
            "Gobierno de España",
            "Generalitat de Cataluña",
            "Independencia Cataluña",
            "Referéndum en Cataluña",
            "Declaración unilateral de independencia (DUI)",
            "Amnistía",
            "Salvador Illa",
            "Política",
            "Ciudadanos",
            "UPyD"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "La Policía desmantela el campamento propalestino en la universidad de Los Ángeles y Biden advierte de que \"la protesta violenta no está protegida\"",
        "pubDate": "2024-05-02 17:29:11",
        "link": "https://www.elmundo.es/internacional/2024/05/02/66332fd2e85ece207b8b459a.html",
        "guid": "https://www.elmundo.es/internacional/2024/05/02/66332fd2e85ece207b8b459a.html",
        "author": "Pablo Scarpellini",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146551589310_150x0.jpg",
        "description": "\"La disidencia es esencial para la democracia\", dijo el presidente estadounidense, \"pero nunca debe conducir al desorden\" <a href=\"https://www.elmundo.es/internacional/2024/05/02/66332fd2e85ece207b8b459a.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "\"La disidencia es esencial para la democracia\", dijo el presidente estadounidense, \"pero nunca debe conducir al desorden\".",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146551589310.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146551589310_150x0.jpg"
        },
        "categories": [
            "Universidades",
            "Nueva York",
            "Israel",
            "Estados Unidos",
            "Franja de Gaza",
            "Hamas",
            "Guerra en Israel",
            "internacional"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "Ayuso reivindica Madrid como \"la plaza mayor de todos\" donde \"no triunfan las identidades de terruño\" y cede al PP las críticas al Gobierno el Dos de Mayo",
        "pubDate": "2024-05-02 14:13:29",
        "link": "https://www.elmundo.es/madrid/2024/05/02/6633613521efa0a2468b45a3.html",
        "guid": "https://www.elmundo.es/madrid/2024/05/02/6633613521efa0a2468b45a3.html",
        "author": "PABLO R. ROCES",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146424154325_150x0.jpg",
        "description": "La presidenta regional asegura que  \"sin la prensa libre no es posible la democracia\" <a href=\"https://www.elmundo.es/madrid/2024/05/02/6633613521efa0a2468b45a3.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "La presidenta regional asegura que \"sin la prensa libre no es posible la democracia\".",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146424154325.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146424154325_150x0.jpg"
        },
        "categories": [
            "Isabel Díaz Ayuso",
            "Ángel Víctor Torres",
            "Comunidad de Madrid",
            "Artículos Pablo R. Roces"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "De las lágrimas de Ayuso al baile con OBK y una reivindicación en el Dos de Mayo: \"Duele que periodistas y jueces seamos demonizados\"",
        "pubDate": "2024-05-02 10:57:51",
        "link": "https://www.elmundo.es/madrid/2024/05/02/663370a0e85ece962c8b4580.html",
        "guid": "https://www.elmundo.es/madrid/2024/05/02/663370a0e85ece962c8b4580.html",
        "author": "Carlos Guisasola",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146464122288_150x0.jpg",
        "description": "La tensión de otras recientes ocasiones se quedó fuera de la Real Casa de Correos, aunque abundaron los mensajes políticos variados y en todas direcciones <a href=\"https://www.elmundo.es/madrid/2024/05/02/663370a0e85ece962c8b4580.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "La tensión de otras recientes ocasiones se quedó fuera de la Real Casa de Correos, aunque abundaron los mensajes políticos variados y en todas direcciones.",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146464122288.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146464122288_150x0.jpg"
        },
        "categories": [
            "Isabel Díaz Ayuso",
            "Artículos Carlos Guisasola",
            "Madrid",
            "José Luis Martínez-Almeida"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "Arán, la nación del millón de esquiadores con \"derecho a decidir\": \"Que no nos invadan los catalanes\"",
        "pubDate": "2024-05-01 20:52:49",
        "link": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/01/6632442fe9cf4a6b3c8b457a.html",
        "guid": "https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/01/6632442fe9cf4a6b3c8b457a.html",
        "author": "Ana María Ortiz, Fotografías: Antonio Heredia",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/01/17145710656538_150x0.jpg",
        "description": "El aranés, su lengua propia, es la tercera oficial en Cataluña, y gozan de autogobierno. Son sólo 10.000 habitantes en medio de los Pirineos, los más desapegados del independentismo <a href=\"https://www.elmundo.es/elecciones/elecciones-catalanas/2024/05/01/6632442fe9cf4a6b3c8b457a.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "El aranés, su lengua propia, es la tercera oficial en Cataluña, y gozan de autogobierno. Son sólo 10.000 habitantes en medio de los Pirineos, los más desapegados del independentismo.",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/01/17145710656538.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/01/17145710656538_150x0.jpg"
        },
        "categories": [
            "Cataluña",
            "ERC",
            "Junts per Catalunya",
            "Elecciones Autonómicas",
            "Generalitat de Cataluña",
            "Lleida",
            "Política",
            "Artículos Ana María Ortiz"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "AstraZeneca admite que su vacuna contra el Covid-19 puede provocar efectos secundarios como la trombosis",
        "pubDate": "2024-05-02 12:18:50",
        "link": "https://www.elmundo.es/ciencia-y-salud/salud/2024/05/02/66338434e9cf4ab74b8b457d.html",
        "guid": "https://www.elmundo.es/ciencia-y-salud/salud/2024/05/02/66338434e9cf4ab74b8b457d.html",
        "author": "EL MUNDO",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2021/05/21/16216176682105_150x0.jpg",
        "description": "Por primera vez y a través de un documento legal, como recoge 'The Telegraph', la compañía británica-sueca revela que \"puede, en casos muy raros, causar TTS [síndrome de trombosis con trombocitopenia]\" <a href=\"https://www.elmundo.es/ciencia-y-salud/salud/2024/05/02/66338434e9cf4ab74b8b457d.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "Por primera vez y a través de un documento legal, como recoge 'The Telegraph', la compañía británica-sueca revela que \"puede, en casos muy raros, causar TTS [síndrome de trombosis con trombocitopenia]\".",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2021/05/21/16216176682105.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2021/05/21/16216176682105_150x0.jpg"
        },
        "categories": [
            "Ciencia y Salud",
            "salud",
            "Covid 19",
            "Vacunas",
            "AstraZeneca"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "Un adolescente mata a cuchilladas a su madre adoptiva en Badajoz y confiesa el crimen",
        "pubDate": "2024-05-02 16:04:43",
        "link": "https://www.elmundo.es/espana/extremadura/2024/05/02/6633b993e85ece877d8b4587.html",
        "guid": "https://www.elmundo.es/espana/extremadura/2024/05/02/6633b993e85ece877d8b4587.html",
        "author": "David Vigario",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146658273670_150x0.jpg",
        "description": "El propio joven de 17 años alertó a la Policía de que había mantenido una \"pequeña discusión\" con la mujer, de 60 años <a href=\"https://www.elmundo.es/espana/extremadura/2024/05/02/6633b993e85ece877d8b4587.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "El propio joven de 17 años alertó a la Policía de que había mantenido una \"pequeña discusión\" con la mujer, de 60 años.",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146658273670.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/02/17146658273670_150x0.jpg"
        },
        "categories": [
            "Badajoz",
            "Policía Nacional"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "Feijóo adelanta al PSOE y pide renovar ya en el Congreso el voto a favor de Palestina",
        "pubDate": "2024-05-01 23:36:34",
        "link": "https://www.elmundo.es/espana/2024/05/02/66324ebfe85eceee378b458d.html",
        "guid": "https://www.elmundo.es/espana/2024/05/02/66324ebfe85eceee378b458d.html",
        "author": "Marisa Cruz",
        "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/01/17145735824590_150x0.jpg",
        "description": "Aboga por recuperar la unanimidad de 2014 para actuar con la UE y respetando la legitimidad de Israel <a href=\"https://www.elmundo.es/espana/2024/05/02/66324ebfe85eceee378b458d.html\">Leer</a><img src=\"http://secure-uk.imrworldwide.com/cgi-bin/m?cid=es-widgetueditorial&amp;cg=rss-elmundo&amp;ci=es-widgetueditorial&amp;si=http://www.elmundo.es/rss/index.xml\" alt=\"\">\n",
        "content": "Aboga por recuperar la unanimidad de 2014 para actuar con la UE y respetando la legitimidad de Israel.",
        "enclosure": {
            "link": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/01/17145735824590.jpg",
            "thumbnail": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/05/01/17145735824590_150x0.jpg"
        },
        "categories": [
            "PP",
            "Palestina",
            "Mariano Rajoy",
            "Unión Europea",
            "Sumar",
            "Senado",
            "Delcy Rodríguez",
            "Pedro Sánchez",
            "Guerra en Israel",
            "Artículos Marisa Cruz",
            "HBPR"
        ],
        "medio": "ElMundo"
    },
    {
        "title": "La policía reprime las principales protestas de los campus de Estados Unidos",
        "pubDate": "2024-05-02 17:52:02",
        "link": "https://elpais.com/internacional/2024-05-02/la-policia-arresta-a-decenas-de-estudiantes-propalestinos-acampados-en-la-universidad-de-los-angeles.html",
        "guid": "https://elpais.com/internacional/2024-05-02/la-policia-arresta-a-decenas-de-estudiantes-propalestinos-acampados-en-la-universidad-de-los-angeles.html",
        "author": "María Antonia Sánchez-Vallejo Cobo,Luis Pablo Beauregard,Macarena  Vidal Liy",
        "thumbnail": "",
        "description": "Biden: “Los estadounidenses tienen el derecho a protestar, pero no el derecho a sembrar el caos”",
        "content": "La policía ha arrestado a más de 200 personas en la madrugada de este jueves durante el desalojo del campamento propalestino en el campus de Los Ángeles de la Universidad de California (UCLA) después de que los manifestantes desobedecieran la orden de abandonarlo. El Departamento de Policía de la ciudad no ha especificado cuántos de los arrestados eran estudiantes. Mientras se producían forcejeos entre fuerzas del orden y manifestantes, algunos de ellos en pijama, en el otro extremo del país, en la costa Este, comparecían ante un tribunal algunos de los activistas arrestados el martes por la noche al evacuar la policía un edificio ocupado en Columbia (Nueva York). En la Casa Blanca, el presidente Joe Biden defendía la libertad de asamblea pacífica, pero condenaba los actos de violencia, en su comentario más extenso y directo desde que comenzaron las protestas por la guerra en Gaza. \"Los estadounidenses tienen derecho a protestar, pero no el derecho a sembrar el caos\", ha dicho el mandatario, después de días sin pronunciarse al respecto, escudado en sus portavoces.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/7vpyI6XT9zHwFJIlS0kBvPo4Sv8=/arc-anglerfish-eu-central-1-prod-prisa/public/GOHYROPFXG7SYBBKAKEPP3X4AI.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "Conflicto árabe-israelí",
            "Guerra",
            "Conflictos",
            "Conflictos armados",
            "Conflictos internacionales",
            "Franja Gaza",
            "Israel",
            "Hamás",
            "Palestina",
            "Oriente Próximo"
        ],
        "medio": "ElPais"
    },
    {
        "title": "Guerra entre Israel y Gaza, en directo | Biden condena la violencia en las manifestaciones universitarias de apoyo a Palestina",
        "pubDate": "2024-05-02 15:51:48",
        "link": "https://elpais.com/internacional/2024-05-02/guerra-entre-israel-y-gaza-en-directo.html",
        "guid": "https://elpais.com/internacional/2024-05-02/guerra-entre-israel-y-gaza-en-directo.html",
        "author": "EL PAÍS",
        "thumbnail": "",
        "description": "“Existe el derecho a protestar, pero no el derecho a sembrar el caos”, ha dicho el presidente de EE UU | La policía desmantela una protesta en un campus de Los Ángeles con más de 130 detenidos | Hamás acudirá “con un espíritu positivo” a Egipto para retomar las negociaciones del alto el fuego",
        "content": "EL PAÍS ofrece de forma gratuita la última hora del conflicto árabe-israelí. Si quieres apoyar nuestro periodismo, suscríbete.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/zON-bvt10Y_qhT7WtB9ADM5GoPQ=/arc-anglerfish-eu-central-1-prod-prisa/public/6BGPIU54KVBQPF2TOGAB3XG6GE.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "Guerra",
            "Israel",
            "Hamás",
            "Palestina",
            "Conflicto árabe-israelí",
            "Franja Gaza",
            "Benjamin Netanyahu",
            "Territorios palestinos",
            "Conflictos armados",
            "Oriente próximo",
            "Jerusalén",
            "Tel Aviv",
            "Cisjordania",
            "Bombardeos",
            "Tregua"
        ],
        "medio": "ElPais"
    },
    {
        "title": "La pobreza se duplica en Palestina desde el inicio de la guerra en Gaza",
        "pubDate": "2024-05-02 18:16:58",
        "link": "https://elpais.com/internacional/2024-05-02/la-pobreza-se-duplica-en-palestina-desde-el-inicio-de-la-guerra-en-gaza.html",
        "guid": "https://elpais.com/internacional/2024-05-02/la-pobreza-se-duplica-en-palestina-desde-el-inicio-de-la-guerra-en-gaza.html",
        "author": "Luis De Vega Hernández",
        "thumbnail": "",
        "description": "La ONU estima que los índices de desarrollo han retrocedido a niveles de 2004 desde el 7 de octubre",
        "content": "Los niveles de destrucción y muerte \"sin precedente\" tras algo más de medio año de guerra en Gaza indican que ese territorio, su economía y sus habitantes tardarán décadas en recuperarse, según un informe del Programa de Naciones Unidas para el Desarrollo (PNUD) presentado este jueves. Mientras varios mandatarios de diferentes países tratan de acordar un alto el fuego que permita atisbar un posible final del conflicto, las estadísticas no dejan de hundirse. El dato más alarmante es el aumento de la pobreza, que se ha duplicado en menos de siete meses, hasta alcanzar al 58,4% de la población. El aumento del desempleo, el hambre o la menor esperanza de vida continuarán empeorando en la Franja mientras dure el conflicto armado y la tendencia no se frenará con el fin de las hostilidades, según vaticina la ONU.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/ReKBjMg1-d5zrasiZ79_nu6Gdsk=/arc-anglerfish-eu-central-1-prod-prisa/public/5ADGC4CFLFLQWVBY65XJN5KQ3E.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "Conflicto árabe-israelí",
            "Guerra",
            "Conflictos",
            "Conflictos armados",
            "Conflictos internacionales",
            "Franja Gaza",
            "Israel",
            "Hamás",
            "Palestina",
            "Oriente Próximo",
            "Pobreza",
            "Desempleo",
            "PIB",
            "Desarrollo humano"
        ],
        "medio": "ElPais"
    },
    {
        "title": "Últimas noticias de la información política, en directo | Sánchez: \"Somos más los que queremos una política limpia frente a quienes quieren una política de insultos y bulos\"",
        "pubDate": "2024-05-02 18:22:58",
        "link": "https://elpais.com/espana/2024-05-02/ultimas-noticias-de-la-informacion-politica-en-directo.html",
        "guid": "https://elpais.com/espana/2024-05-02/ultimas-noticias-de-la-informacion-politica-en-directo.html",
        "author": "EL PAÍS",
        "thumbnail": "",
        "description": "El presidente del Gobierno reaparece en la campaña catalana con un mitin junto al candidato socialista | El PSOE denuncia a Canal Sur ante la junta electoral por manipular unas imágenes de la manifestación de apoyo a Sánchez | Ni Feijóo ni los pesos pesados de la cúpula popular acuden a los actos del dos de mayo en Madrid",
        "content": "EL PAÍS ofrece de forma gratuita la última hora de la actualidad política. Si quieres apoyar nuestro periodismo, suscríbete.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/VHa0iYlaJK4J0aKT0xs0sFT9Np4=/arc-anglerfish-eu-central-1-prod-prisa/public/T4GRNDBGUNDY3DMDG2DHCSMFOE.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "España",
            "Política",
            "Políticos",
            "Gobierno",
            "Gobierno de España",
            "Gobierno de coalición",
            "Pedro Sánchez",
            "PSOE",
            "Legislaturas políticas",
            "XV Legislatura España",
            "PP",
            "Alberto Núñez Feijóo",
            "Congreso Diputados",
            "Caso Koldo",
            "Senado",
            "Crisis políticas",
            "Sumar",
            "Presidencia Gobierno",
            "Yolanda Díaz",
            "JuntsxCat",
            "ERC",
            "Elecciones",
            "Elecciones Catalanas"
        ],
        "medio": "ElPais"
    },
    {
        "title": "Vídeo | La desinformación, a debate, en el programa ¿Y ahora qué?",
        "pubDate": "2024-05-02 16:30:57",
        "link": "https://elpais.com/videos/2024-05-02/video-la-desinformacion-a-debate-en-el-programa-y-ahora-que.html",
        "guid": "https://elpais.com/videos/2024-05-02/video-la-desinformacion-a-debate-en-el-programa-y-ahora-que.html",
        "author": "EL PAÍS",
        "thumbnail": "https://imagenes.elpais.com/resizer/Ycfy8nnVLzrlCwUfXlPvruMura4=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/PXBPBYQEO5AYFKMTIBKSV4QNIA.jpg",
        "description": "Periodistas y columnistas de EL PAÍS y Cadena SER analizan el efecto de la carta de Pedro Sánchez, una semana después",
        "content": "¿Qué efectos puede tener el anuncio de Pedro Sánchez en la campaña de las elecciones catalanas?¿Cómo se puede luchar contra la desinformación?¿Cómo se crea un bulo?¿Qué herramientas se usan para amplificar las mentiras en redes? El programa ‘Y ahora qué' intenta responder esta semana a las preguntas generadas por la carta de Pedro Sánchez del miércoles pasado. El análisis político de los efectos en Cataluña será comentado por Camilo Baquero, corresponsal político de EL PAIS y David Junquera, corresponsal político de Cadena SER. Las consecuencias a medio plazo y en análisis de la regeneración política correrá a cargo de Anabel Díaz y Victor Lapuente. Jordi Pérez Colomé explicará cómo se monta y se amplifica un bulo. El programa incluirá también una entrevista con Xavier Vidal-Folch y con sus secciones habituales, como las ‘Notas desde la terraza’ de Aida Bao.",
        "enclosure": {
            "type": "application/octet-stream",
            "duration": "1",
            "thumbnail": "https://imagenes.elpais.com/resizer/Ycfy8nnVLzrlCwUfXlPvruMura4=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/PXBPBYQEO5AYFKMTIBKSV4QNIA.jpg"
        },
        "categories": [
            "Pedro Sánchez",
            "Elecciones Catalanas",
            "Cataluña",
            "Elecciones",
            "Política",
            "Comunicación",
            "Bulos internet",
            "Televisión"
        ],
        "medio": "ElPais"
    },
    {
        "title": "Diálogo, también social",
        "pubDate": "2024-05-02 03:00:00",
        "link": "https://elpais.com/opinion/2024-05-02/dialogo-tambien-social.html",
        "guid": "https://elpais.com/opinion/2024-05-02/dialogo-tambien-social.html",
        "author": "EL PAÍS",
        "thumbnail": "",
        "description": "Los trabajadores celebraron ayer el Primero de Mayo en un contexto  de buenas cifras económicas y grandes retos para el empleo",
        "content": "España nunca había sumado tanta gente empleada en un comienzo de año como en los tres primeros meses de 2024, con 21,25 millones de trabajadores. Además, la población activa ha registrado un acelerón hasta los 24,22 millones de personas y el número de parados se ha situado por debajo de la barrera de los tres millones, la menor cifra en un primer trimestre desde 2008. De hecho, la economía española ha demostrado una gran fortaleza en este inicio del año, con un crecimiento del PIB del 0,7% frente a los tres últimos meses del año anterior.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/ZoXKIp5H0CINBsTuOXO-OYfSfXU=/arc-anglerfish-eu-central-1-prod-prisa/public/6GM6422AMBEPZKJSOISMVOVWJY.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "Opinión",
            "Empleo",
            "Día internacional trabajo",
            "Sindicatos",
            "Empresas",
            "Patronal",
            "Dialogo social",
            "Productividad laboral",
            "EPA",
            "PIB",
            "Economía",
            "Contratos",
            "Empleo temporal",
            "Administración pública",
            "Salarios",
            "Brecha digital",
            "Educación",
            "Trabajo",
            "Noticias de España"
        ],
        "medio": "ElPais"
    },
    {
        "title": "El aviso de Pedro Sánchez a Puigdemont",
        "pubDate": "2024-05-02 03:00:00",
        "link": "https://elpais.com/opinion/2024-05-02/el-aviso-de-pedro-sanchez-a-puigdemont.html",
        "guid": "https://elpais.com/opinion/2024-05-02/el-aviso-de-pedro-sanchez-a-puigdemont.html",
        "author": "Estefanía Molina",
        "thumbnail": "",
        "description": "El ‘punto y aparte’ del presidente añade un nuevo eje a la campaña catalana: si el PSC hablaba de dejar atrás el ‘procès’ para atraer voto de Ciutadans, ahora se suma la defensa de la democracia, como opa a Comuns-Sumar",
        "content": "Pedro Sánchez lanzó un sutil aviso a Carles Puigdemont con su período reflexivo: si me harto, aquí os quedaréis todos y la amnistía quizás acabe cayendo en saco roto. Y muy probablemente, las elecciones catalanas no alterarán la legislatura tanto como se dice. España podría tener presupuestos, a medio plazo, con el voto favorable de Junts. Y ello no tendrá tanto que ver con el aviso del presidente, si no con la evolución política de Puigdemont.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/T87n5O2s8oYnNx0rXb_QnIxWFjE=/arc-anglerfish-eu-central-1-prod-prisa/public/UVNXJURLXFMWZXT2U2OFR3Y76M.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "Opinión",
            "Noticias de España",
            "Política",
            "Pedro Sánchez",
            "Elecciones",
            "Elecciones Catalanas",
            "Carles Puigdemont",
            "Independentismo",
            "Nacionalismo",
            "JuntsxCat",
            "Procés Independentista Catalán"
        ],
        "medio": "ElPais"
    },
    {
        "title": "España de bulo en bulo",
        "pubDate": "2024-05-02 03:00:00",
        "link": "https://elpais.com/opinion/2024-05-02/espana-de-bulo-en-bulo.html",
        "guid": "https://elpais.com/opinion/2024-05-02/espana-de-bulo-en-bulo.html",
        "author": "Daniel Gascón",
        "thumbnail": "",
        "description": "Uno pensaría que en España no se castigan las difamaciones y las injurias. No es así, como saben todos los periodistas y por supuesto el presidente del Gobierno",
        "content": "Tras meditar durante cinco días si los españoles merecíamos que nos siguiera gobernando, el presidente se ve con ganas de seguir hasta 2031: qué reparador puede ser un puente. Aquellos que pensaban que Pedro Sánchez vivía una verdadera crisis ahora tienen razones para sospechar una maniobra cínica: ha tenido el país en vilo, ha utilizado a su esposa y al rey, e incluso ha hecho llorar a Pedro Almodóvar.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/W2Mp2kVg-hCgICHjSxIUcCYTTOY=/arc-anglerfish-eu-central-1-prod-prisa/public/27J3WFVQIRBKFLBOH5IWPE2VJY.JPG",
            "type": "image/jpeg"
        },
        "categories": [
            "Opinión",
            "Pedro Sánchez",
            "Política",
            "Partidos políticos",
            "PSOE",
            "Medios comunicación",
            "Bulos internet",
            "Fake news",
            "PP",
            "Populismo",
            "Dimisiones políticas"
        ],
        "medio": "ElPais"
    },
    {
        "title": "Juan Palomo",
        "pubDate": "2024-05-02 03:00:00",
        "link": "https://elpais.com/opinion/2024-05-02/juan-palomo.html",
        "guid": "https://elpais.com/opinion/2024-05-02/juan-palomo.html",
        "author": "Idafe Martín Pérez",
        "thumbnail": "",
        "description": "Universidades propiedad de Planeta y la Asociación Católica de Propagandistas conceden honores a periodistas de medios propiedad de Planeta y la Asociación Católica de Propagandistas",
        "content": "Vicente Vallés es el periodista más influyente de España y el presentador del informativo de televisión más visto. Si es que los informativos de televisión tienen todavía la influencia que un día tuvieron. Es un ejemplo a estudiar, una referencia esencial cuando se trata de fiscalizar al poder. Vallés es una guía para las nuevas generaciones de periodistas y desde el pasado viernes es también doctor honoris causa, un honor que alcanzan muy pocos periodistas en el mundo. Trabaja en Antena 3, la televisión del grupo Atresmedia, propiedad del Grupo Planeta. Y fue nombrado honoris causa por la Universidad Internacional de Valencia, propiedad del Grupo Planeta. Casualidades. La VIU (sus siglas son en inglés) es un centro universitario online con 409 profesores y ningún estudiante de doctorado, según datos de un informe de la Fundación BBVA. En la clasificación de universidades españolas de esa misma fundación figura en el puesto 68 de 71. Al borde del descenso a Segunda. Según contó Eldiario.es en febrero del año pasado, la VIU fue creada en 2008, empezó a funcionar en 2010 y la Generalitat valenciana dijo entonces que su puesta en marcha le había costado 34 millones de euros. En 2013, el Grupo Planeta compró el 70% por cuatro millones.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/o409n9diboB0f4MMPXJJQu-rBws=/arc-anglerfish-eu-central-1-prod-prisa/public/MU42ZZGRJDSJOCTLQP3FF67IDY.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "Opinión",
            "Sociedad",
            "Medios comunicación",
            "Medios comunicación nacionales",
            "Periodismo",
            "Prensa",
            "Periodistas",
            "Vicente Vallés",
            "Sonsoles Ónega",
            "USP-CEU",
            "Grupo Planeta",
            "Premio Planeta",
            "Antena 3",
            "Atresmedia",
            "Doctorado",
            "Honoris causa",
            "Universidad",
            "Francisco Marhuenda",
            "La Razón"
        ],
        "medio": "ElPais"
    },
    {
        "title": "Ayuso reivindica Madrid como \"la plaza mayor de todos\" y el PP se vuelca en atacar a Sánchez durante el Dos de Mayo: \"Es el señor bulo\"",
        "pubDate": "2024-05-02 16:48:41",
        "link": "https://elpais.com/espana/madrid/2024-05-02/ayuso-reivindica-madrid-como-la-plaza-mayor-de-todos-y-el-pp-se-vuelca-en-atacar-a-sanchez-durante-el-dos-de-mayo-es-el-senor-bulo.html",
        "guid": "https://elpais.com/espana/madrid/2024-05-02/ayuso-reivindica-madrid-como-la-plaza-mayor-de-todos-y-el-pp-se-vuelca-en-atacar-a-sanchez-durante-el-dos-de-mayo-es-el-senor-bulo.html",
        "author": "Juan José Mateo Ruiz-Gálvez",
        "thumbnail": "",
        "description": "Ausente Feijóo y la plana mayor de la dirección nacional, los conservadores de Madrid usan el acto institucional para criticar al presidente del Gobierno",
        "content": "Mientras Isabel Díaz Ayuso se muerde la lengua, el PP de Madrid habla. Pasa este jueves durante la ceremonia organizada por el Gobierno regional para celebrar el Dos de Mayo, día de la Comunidad de Madrid. Un año después de que la cita quedara marcada por el choque institucional que supuso impedir al ministro Félix Bolaños el acceso a la tribuna de autoridades, los representantes de las dos administraciones optan por la contención. La presidenta Díaz Ayuso hace un discurso sin referencias a Sánchez: \"[Madrid es] la plaza mayor de todos\", dice ante un público entregado que no incluye al líder del PP, Alberto Núñez Feijóo, ni a ningún peso pesado de la dirección nacional. El ministro Ángel Víctor Torres (PSOE), por su parte, propone \"caminar juntos en la cogobernanza\". Pero la mecha del conflicto sigue encendida y no hay quien la apague: otros representantes de los partidos demuestran que el punto y aparte que pidió Pedro Sánchez tras sus cinco días de reflexión es simplemente un punto y seguido en Madrid. La guerra sigue.",
        "enclosure": {
            "link": "https://imagenes.elpais.com/resizer/g1tCJHkD5sBCgO4gggA51jjy9GY=/arc-anglerfish-eu-central-1-prod-prisa/public/ASNUEVUFFVDU3NC2LYTGURUYVY.jpg",
            "type": "image/jpeg"
        },
        "categories": [
            "Comunidad de Madrid",
            "Madrid",
            "Isabel Díaz Ayuso",
            "Gobierno Comunidad de Madrid",
            "Alberto Núñez Feijóo",
            "PP Madrid",
            "Pedro Sánchez",
            "Ángel Víctor Torres",
            "Delegados Gobierno",
            "2 de Mayo"
        ],
        "medio": "ElPais"
    },
    {
        "title": "Jornada surrealista en Territori: machetazo a Rodalies y premio para la exdirectora de Renfe en Catalunya",
        "pubDate": "2024-05-02 15:57:55",
        "link": "https://www.elperiodico.com/es/sociedad/20240502/jornada-surrealista-territori-machetazo-rodalies-premio-amtu-exdirectora-renfe-maye-castillo-101848481?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101848481",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/973eef7e-9e48-4b14-b592-dbd54fed4067_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>Si les gusta el fútbol habrán visto las imágenes del <a href=\"https://www.elperiodico.com/es/opinion/20240413/ese-tipo-hombre-luis-enrique-xavi-hernandez-articulo-agnes-marques-101015343\" target=\"_blank\"><strong>abrazo que se dieron Luis Enrique y Xavi</strong></a><strong> </strong>en los pasillos del estadio del PSG antes del partido de ida de los <strong>cuartos de final de Champions</strong>. Días atrás se habían cruzado incómodos mensajes sobre cuál de los dos representa <a href=\"https://www.elperiodico.com/es/deportes/20240409/luis-enrique-representa-mejor-estilo-100815484\" target=\"_blank\">mejor el espíritu del juego blaugrana</a>. Pero en ese encuentro antes de que sus muchachos saltaran al césped quedó claro que la <strong>relación personal está por encima de los colores</strong> y los clubs. Este jueves ha sucedido un poco lo mismo en Lloret de Mar, con el Govern entregando un premio a una exresponsable de Renfe poco después de<strong> </strong><a href=\"https://www.elperiodico.com/es/sociedad/20240502/govern-convoca-urgencia-renfe-abordar-problemas-venta-abonos-gratuitos-101837025\" target=\"_blank\"><strong>asegurar que Rodalies es un \"desastre\"</strong></a><strong>.</strong> El deporte y la política no están tan alejados.</p>\n<p><a href=\"https://www.elperiodico.com/es/sociedad/20240502/jornada-surrealista-territori-machetazo-rodalies-premio-amtu-exdirectora-renfe-maye-castillo-101848481?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "Si les gusta el fútbol habrán visto las imágenes del abrazo que se dieron Luis Enrique y Xavi en los pasillos del estadio del PSG antes del partido de ida de los cuartos de final de Champions. Días atrás se habían cruzado incómodos mensajes sobre cuál de los dos representa mejor el espíritu del juego blaugrana. Pero en ese encuentro antes de que sus muchachos saltaran al césped quedó claro que la relación personal está por encima de los colores y los clubs. Este jueves ha sucedido un poco lo mismo en Lloret de Mar, con el Govern entregando un premio a una exresponsable de Renfe poco después de asegurar que Rodalies es un \"desastre\". El deporte y la política no están tan alejados. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "Daniel Sancho, al acabar el juicio por la muerte de Edwin Arrieta: \"Siento que unos padres hayan perdido un hijo\"",
        "pubDate": "2024-05-02 15:30:32",
        "link": "https://www.elperiodico.com/es/sociedad/20240502/daniel-sancho-perdon-arrieta-alegato-final-juicio-visto-sentencia-agosto-101848786?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101848786",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/da410296-1101-44ec-a1f8-383fb1f9e5fb_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>A mediodía, con el bochorno castigando la isla de Koh Samui, el <strong>juez dio por concluido </strong><a href=\"https://www.elperiodico.com/es/sucesos/20240502/juicio-daniel-sancho-tailandia-hoy-asesinato-caso-edwin-arrieta-directo-ultima-hora-dv-100566594\"><strong>el juicio contra Daniel Sancho</strong></a><a href=\"https://www.elperiodico.com/es/sucesos/20240502/juicio-daniel-sancho-tailandia-hoy-asesinato-caso-edwin-arrieta-directo-ultima-hora-dv-100566594\"> </a>y emplazó a las partes al <a href=\"https://www.elperiodico.com/es/internacional/20240502/juicio-daniel-sancho-tailandia-visto-sentencia-fallo-29-agosto-101828020\"><strong>29 de agosto para la sentencia</strong></a>. Han sido doce jornadas de las 15 previstas con 35 testigos y abundantes problemas técnicos, desde apagones a traducciones debatidas, pero todas las partes se marchan satisfechas y con sus pretensiones intactas: un asesinato premeditado para una, un homicidio en legítima defensa para la otra.</p>\n<p><a href=\"https://www.elperiodico.com/es/sociedad/20240502/daniel-sancho-perdon-arrieta-alegato-final-juicio-visto-sentencia-agosto-101848786?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "A mediodía, con el bochorno castigando la isla de Koh Samui, el juez dio por concluido el juicio contra Daniel Sancho y emplazó a las partes al 29 de agosto para la sentencia. Han sido doce jornadas de las 15 previstas con 35 testigos y abundantes problemas técnicos, desde apagones a traducciones debatidas, pero todas las partes se marchan satisfechas y con sus pretensiones intactas: un asesinato premeditado para una, un homicidio en legítima defensa para la otra. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "Los Mossos buscan a los sospechosos de cometer un crimen en la Barceloneta",
        "pubDate": "2024-05-02 15:09:22",
        "link": "https://www.elperiodico.com/es/barcelona/20240502/investigan-agresion-mortal-hombre-barcelona-101848759?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101848759",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/82e2bbee-d851-4cd0-adbf-bc1b799aeea0_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>Los Mossos d'Esquadra investigan la <strong>muerte de un hombre en el barrio de la Barceloneta de Barcelona </strong>la noche del miércoles al jueves. Al parecer fue <strong>agredido en plena calle</strong>, poco antes de la medianoche, y quedó mal herido por lo que tuvo que ser trasladado por una ambulancia al hospital, aunque murió poco después. Fuentes policiales señalan que el hombre presentaba varias lesiones en el cuerpo tras haber recibido una paliza y por eso los agentes consideran que fue un crimen.</p>\n<p><a href=\"https://www.elperiodico.com/es/barcelona/20240502/investigan-agresion-mortal-hombre-barcelona-101848759?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "Los Mossos d'Esquadra investigan la muerte de un hombre en el barrio de la Barceloneta de Barcelona la noche del miércoles al jueves. Al parecer fue agredido en plena calle, poco antes de la medianoche, y quedó mal herido por lo que tuvo que ser trasladado por una ambulancia al hospital, aunque murió poco después. Fuentes policiales señalan que el hombre presentaba varias lesiones en el cuerpo tras haber recibido una paliza y por eso los agentes consideran que fue un crimen. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "El Govern quiere que la T-Mobilitat cobre por kilómetros y no por zonas antes de 2027",
        "pubDate": "2024-05-02 14:48:40",
        "link": "https://www.elperiodico.com/es/sociedad/20240502/govern-aspira-poner-marcha-cobro-por-distancia-t-mobilitat-antes-2027-101832436?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101832436",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/0fa17ba6-cb92-48c9-adc0-9a81f334da59_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>La <a href=\"https://www.elperiodico.com/es/temas/t-mobilitat-31391\" target=\"_blank\">T-Mobilitat</a> no es solo un cambio de formato <strong>del magnético al 'contact less',</strong> una tecnología presente desde hace años en muchas otras ciudades del mundo. Tampoco es pasar del plástico a una <strong>aplicación móvil</strong>. O no solo. Lo que hace distinto al <strong>título integrado</strong> de<strong> transporte público de Catalunya</strong>, y en eso sí es pionero, es que el <a href=\"https://www.elperiodico.com/es/sociedad/20230602/cobro-distancia-recorrida-camino-pendiente-tmobilitat-88183392\" target=\"_blank\">viajero pagará por la distancia recorrida</a>, de manera que la <strong>tarifa no vaya atada a las coronas territoriales</strong>. El Govern ha asegurado este jueves que ese momento llegará antes de 2027, unos 13 años después de que, en octubre de 2014, se adjudicara el proyecto a la<strong> </strong><a href=\"https://www.elperiodico.com/es/economia/20220212/soc-mobilitat-rescate-13224365\" target=\"_blank\"><strong>empresa Soc Mobilitat</strong></a><strong>.</strong> </p>\n<p><a href=\"https://www.elperiodico.com/es/sociedad/20240502/govern-aspira-poner-marcha-cobro-por-distancia-t-mobilitat-antes-2027-101832436?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "La T-Mobilitat no es solo un cambio de formato del magnético al 'contact less', una tecnología presente desde hace años en muchas otras ciudades del mundo. Tampoco es pasar del plástico a una aplicación móvil. O no solo. Lo que hace distinto al título integrado de transporte público de Catalunya, y en eso sí es pionero, es que el viajero pagará por la distancia recorrida, de manera que la tarifa no vaya atada a las coronas territoriales. El Govern ha asegurado este jueves que ese momento llegará antes de 2027, unos 13 años después de que, en octubre de 2014, se adjudicara el proyecto a la empresa Soc Mobilitat. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "Me voy pero me quedo",
        "pubDate": "2024-05-02 14:33:02",
        "link": "https://www.elperiodico.com/es/opinion/20240502/quedo-pedro-sanchez-paul-auster-articulo-olga-merino-101847230?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101847230",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/421e5fb6-9ec2-4bda-96ee-bbc470cfbdec_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>Uno de los vecinos del inmueble donde vivo <strong>da un portazo tremebundo cada vez que sale de casa</strong>. Cataplum. Pumba. Slam!’, en los cómics. Un golpazo atroz que sacude el edificio, plagado de grietas en su vejez, dejando en el aire una reverberación desabrida que turba el ánimo. El ímpetu le asegura que la puerta queda bien cerrada, pero el encontrón es de tal magnitud que proclama una despedida irrevocable en el hueco de la escalera, <strong>como si pretendiera también desairar a quienquiera que permanezca dentro del piso</strong>. Hasta luego, Maricarmen. Ahí os quedáis. Salgo a por el tabaco definitivo. El topetazo que uno daría tras un cabreo colosal con la pareja o bien cegado por un arreón de furia, de esos que impelen a salir en tromba de casa para desfacer un grave entuerto. El vecino, por cierto, siempre vuelve. </p>\n<p><a href=\"https://www.elperiodico.com/es/opinion/20240502/quedo-pedro-sanchez-paul-auster-articulo-olga-merino-101847230?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "Uno de los vecinos del inmueble donde vivo da un portazo tremebundo cada vez que sale de casa. Cataplum. Pumba. Slam!’, en los cómics. Un golpazo atroz que sacude el edificio, plagado de grietas en su vejez, dejando en el aire una reverberación desabrida que turba el ánimo. El ímpetu le asegura que la puerta queda bien cerrada, pero el encontrón es de tal magnitud que proclama una despedida irrevocable en el hueco de la escalera, como si pretendiera también desairar a quienquiera que permanezca dentro del piso. Hasta luego, Maricarmen. Ahí os quedáis. Salgo a por el tabaco definitivo. El topetazo que uno daría tras un cabreo colosal con la pareja o bien cegado por un arreón de furia, de esos que impelen a salir en tromba de casa para desfacer un grave entuerto. El vecino, por cierto, siempre vuelve. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "Mamarazzis: María del Monte e Isabel Pantoja unidas, de nuevo, por la actualidad",
        "pubDate": "2024-05-02 14:14:48",
        "link": "https://www.elperiodico.com/es/gente/20240502/maria-del-monte-rechaza-oferta-historica-telecinco-isabel-pantoja-cache-conciertos-exclusiva-mamarazzis-101841330?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101841330",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/64374cb6-73ed-4f83-95fd-5106e0c118d7_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>No hay semana que las <a href=\"https://www.elperiodico.com/es/temas/mamarazzis-1019840\">Mamarazzis</a> no hagan <strong>ruido</strong>. De lo contrario, <strong>Laura Fa </strong>y <strong>Lorena Vázquez </strong>no serían nuestras periodistas del 'cuore' favoritas. ¿O a caso pensabas que porque el <a href=\"https://www.elperiodico.com/es/economia/20240501/reducir-jornada-reformas-pendientes-mercado-laboral-101649688\" target=\"_blank\">Primero de Mayo</a> cayese en miércoles, esta semana no se emitiría el pódcast del corazón de EL PERIÓDICO? Además, las <strong>revistas de papel cuché</strong> salieron el martes para esquivar el <a href=\"https://www.elperiodico.com/es/economia/20240501/primero-de-mayo-manifestacion-barcelona-reduccion-jornada-laboral-101802277\" target=\"_blank\">Día del Trabajador</a>, y la actualidad se amontonaba. Unas novedades en las que, por cierto, las Mamarazzis son las protagonistas. Sí, has leído bien. Fa y Vázquez, expertas en contar todo lo que pasa en el <strong>mundo del famoseo</strong>, se han convertido, aunque sea de manera excepcional, en 'celebrities' y comparten terreno 'gossip' con <strong>María del Monte</strong>, <strong>Isabel Pantoja</strong>, <strong>Iñaki Urdangarin</strong>, <strong>Ainhoa Armentia</strong> y muchos más. </p>\n<p><a href=\"https://www.elperiodico.com/es/gente/20240502/maria-del-monte-rechaza-oferta-historica-telecinco-isabel-pantoja-cache-conciertos-exclusiva-mamarazzis-101841330?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "No hay semana que las Mamarazzis no hagan ruido. De lo contrario, Laura Fa y Lorena Vázquez no serían nuestras periodistas del 'cuore' favoritas. ¿O a caso pensabas que porque el Primero de Mayo cayese en miércoles, esta semana no se emitiría el pódcast del corazón de EL PERIÓDICO? Además, las revistas de papel cuché salieron el martes para esquivar el Día del Trabajador, y la actualidad se amontonaba. Unas novedades en las que, por cierto, las Mamarazzis son las protagonistas. Sí, has leído bien. Fa y Vázquez, expertas en contar todo lo que pasa en el mundo del famoseo, se han convertido, aunque sea de manera excepcional, en 'celebrities' y comparten terreno 'gossip' con María del Monte, Isabel Pantoja, Iñaki Urdangarin, Ainhoa Armentia y muchos más. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "La jugada que nos merecemos",
        "pubDate": "2024-05-02 14:05:14",
        "link": "https://www.elperiodico.com/es/opinion/20240502/jugada-merecemos-pedro-sanchez-emociones-articulo-emma-riverola-101846476?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101846476",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/2667816e-b139-4b7c-b97e-1d88673b0c63_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>Ni más ni menos. Puede encantarnos o desolarnos. Puede emocionarnos, porque<strong> nos creemos el lamento de ese hombre enamorado</strong> o irritarnos, porque le vemos<strong> todas las costuras de su traje impoluto</strong>. Incluso podemos bascular en todos estos estados de ánimo hasta marearnos: vivir con angustia los cinco días en que el capitán del barco se retiró a pensar a su camarote, gritar como lo hicieron esas voces de la Moncloa justo cuando Pedro Sánchez anunció que seguía o sufrir una <strong>resaca de desconfianza</strong>. Tanto da el meneo emocional, la jugada de Sánchez, sea espontánea o premeditada, sea o no particular, se escribe con letras de oro en el ecosistema político y social que hemos creado. Sí, hemos.</p>\n<p><a href=\"https://www.elperiodico.com/es/opinion/20240502/jugada-merecemos-pedro-sanchez-emociones-articulo-emma-riverola-101846476?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "Ni más ni menos. Puede encantarnos o desolarnos. Puede emocionarnos, porque nos creemos el lamento de ese hombre enamorado o irritarnos, porque le vemos todas las costuras de su traje impoluto. Incluso podemos bascular en todos estos estados de ánimo hasta marearnos: vivir con angustia los cinco días en que el capitán del barco se retiró a pensar a su camarote, gritar como lo hicieron esas voces de la Moncloa justo cuando Pedro Sánchez anunció que seguía o sufrir una resaca de desconfianza. Tanto da el meneo emocional, la jugada de Sánchez, sea espontánea o premeditada, sea o no particular, se escribe con letras de oro en el ecosistema político y social que hemos creado. Sí, hemos. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "Atropellan a dos alumnos y a su madre cuando se dirigían hacia una escuela de Sant Cugat",
        "pubDate": "2024-05-02 13:25:25",
        "link": "https://www.elperiodico.com/es/sant-cugat/20240502/atropellan-alumnos-madre-dirigian-escuela-101844793?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101844793",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/0b5da62c-9339-4fd0-945e-7e1ac55f5f0c_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>Dos alumnos y su madre han sido atropellados cuando se dirigían hacia una escuela de Sant Cugat del Vallès, concretamente a la de <strong>Gerbert d'Orlhac </strong>a las 9 h de la mañana (específicamente, a las 8.54 h se ha alertado al Servicio de Emergencias, SEM).</p>\n<p><a href=\"https://www.elperiodico.com/es/sant-cugat/20240502/atropellan-alumnos-madre-dirigian-escuela-101844793?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "Dos alumnos y su madre han sido atropellados cuando se dirigían hacia una escuela de Sant Cugat del Vallès, concretamente a la de Gerbert d'Orlhac a las 9 h de la mañana (específicamente, a las 8.54 h se ha alertado al Servicio de Emergencias, SEM). .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "La crecida del Besòs por la lluvia inunda de basura una zona protegida para aves amenazadas",
        "pubDate": "2024-05-02 12:46:56",
        "link": "https://www.elperiodico.com/es/barcelona/20240502/lluvias-crecida-besos-basura-desembocadura-aves-101842153?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101842153",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/25cdff53-63ee-4cf4-b081-22ceaa89b018_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>La crecida del Besòs por el <a href=\"https://www.elperiodico.com/es/medio-ambiente/20240429/cataluna-dia-lluvioso-seis-meses-lunes-crecida-rios-embalses-101729747\">temporal de lluvia del pasado fin de semana y el lunes</a> -<strong>el más intenso de los últimos tiempos en medio de la persistente sequía</strong>- tiene un reverso ingrato, aún visible en la desembocadura del río. Una maraña de basura enredada con ramas y cañas ha inundado la parte final del delta, justo en un <strong>arenal de acceso prohibido en Sant Adrià de Besòs para que especies de aves amenazadas y protegidas puedan nidificar</strong>. El Ayuntamiento de la localidad barcelonesa ha contactado con administraciones superiores y ha rogado que se actúe de inmediato para limpiar el tramo.</p>\n<p><a href=\"https://www.elperiodico.com/es/barcelona/20240502/lluvias-crecida-besos-basura-desembocadura-aves-101842153?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "La crecida del Besòs por el temporal de lluvia del pasado fin de semana y el lunes -el más intenso de los últimos tiempos en medio de la persistente sequía- tiene un reverso ingrato, aún visible en la desembocadura del río. Una maraña de basura enredada con ramas y cañas ha inundado la parte final del delta, justo en un arenal de acceso prohibido en Sant Adrià de Besòs para que especies de aves amenazadas y protegidas puedan nidificar. El Ayuntamiento de la localidad barcelonesa ha contactado con administraciones superiores y ha rogado que se actúe de inmediato para limpiar el tramo. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "El PP afirma que \"Puigdemont tiene secuestrado a Sánchez\" y ve a Illa como la \"marioneta\" del PSOE",
        "pubDate": "2024-05-02 12:21:53",
        "link": "https://www.elperiodico.com/es/elecciones-catalunya/20240502/pp-puigdemont-secuestrado-sanchez-101832116?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada",
        "guid": "101832116",
        "author": "",
        "thumbnail": "",
        "description": "\n<p><img src=\"https://estaticos-cdn.prensaiberica.es/clip/e6a6c835-55e8-432b-837c-49ce10d0bd1d_thumb-ep-aspect-ratio_default_0.jpg\"></p>\n<p>El candidato del PP a la presidencia de la Generalitat, <strong>Alejandro Fernández</strong>, sigue centrando su campaña en la crítica a los pactos entre socialistas e independentistas. Después de que, el miércoles, Fernández <a href=\"https://www.elperiodico.com/es/elecciones-catalunya/20240501/alejandro-fernandez-pp-descarta-pactar-junts-poco-probable-psc-elecciones-catalanas-101794620\">sentenciara que </a><a href=\"https://www.elperiodico.com/es/elecciones-catalunya/20240501/alejandro-fernandez-pp-descarta-pactar-junts-poco-probable-psc-elecciones-catalanas-101794620\"><strong>no iba a pactar con con el PSC si el presidente del Gobierno, Pedro Sánchez, no rompía sus lazos con el independentismo </strong></a><a href=\"https://www.elperiodico.com/es/elecciones-catalunya/20240501/alejandro-fernandez-pp-descarta-pactar-junts-poco-probable-psc-elecciones-catalanas-101794620\">en la Moncloa</a>, hoy el presidente de Castilla y León, <strong>Alfonso Fernández Mañueco</strong>, ha añadido que el candidato del PSC, Salvador Illa, \"<strong>es solo la cabeza que va a entregar Sánchez a Puigdemont</strong>\" en la Generalitat para continuar en la Moncloa. <strong>\"Carles Puigdemont tiene a Sánchez secuestrado</strong>\", ha espetado en una comparecencia ante los medios de comunicación en <strong>Sant Joan Despí</strong>.</p>\n<p><a href=\"https://www.elperiodico.com/es/elecciones-catalunya/20240502/pp-puigdemont-secuestrado-sanchez-101832116?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada?utm_source=rss-noticias&amp;utm_medium=feed&amp;utm_campaign=portada\">Seguir leyendo...</a>.</p>\n",
        "content": "El candidato del PP a la presidencia de la Generalitat, Alejandro Fernández, sigue centrando su campaña en la crítica a los pactos entre socialistas e independentistas. Después de que, el miércoles, Fernández sentenciara que no iba a pactar con con el PSC si el presidente del Gobierno, Pedro Sánchez, no rompía sus lazos con el independentismo en la Moncloa, hoy el presidente de Castilla y León, Alfonso Fernández Mañueco, ha añadido que el candidato del PSC, Salvador Illa, \"es solo la cabeza que va a entregar Sánchez a Puigdemont\" en la Generalitat para continuar en la Moncloa. \"Carles Puigdemont tiene a Sánchez secuestrado\", ha espetado en una comparecencia ante los medios de comunicación en Sant Joan Despí. .",
        "enclosure": {},
        "categories": [],
        "medio": "ElPeriodico"
    },
    {
        "title": "Biden condena la \"violencia\" en las protestas y dice que no van a cambiar su apoyo a Israel",
        "pubDate": "2024-05-02 16:10:47",
        "link": "https://www.lavanguardia.com/internacional/20240502/9608415/biden-condena-violencia-protestas-dice-cambiar-apoyo-israel.html",
        "guid": "https://www.lavanguardia.com/internacional/20240502/9608415/biden-condena-violencia-protestas-dice-cambiar-apoyo-israel.html",
        "author": "Javier de la Sotilla Puig",
        "thumbnail": "",
        "description": "Consciente de que su papel en Gaza podría frustrarle la reelección, el presidente defiende la “libertad de expresión” a la par que el “estado de derecho”, mientras condena el “antisemitismo” y la “islamofobia”",
        "content": "Decenas de miles de personas en siete estados clave pueden decantar el resultado de las elecciones presidenciales de Estados Unidos de noviembre, que se prevén, al menos, tan disputadas como las del 2020. En esos comicios, el apoyo de los jóvenes universitarios fue esencial para la victoria de Joe Biden, pero cada vez está menos claro que este año vayan a revalidar su confianza en el presidente.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/05/02/6633b9c83ae17.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Internacional"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "Decenas de detenidos en el desmantelamiento del campamento pro Palestina de la UCLA",
        "pubDate": "2024-05-02 10:56:54",
        "link": "https://www.lavanguardia.com/internacional/20240502/9608219/policia-desmantelar-campamento-pro-palestina-ucla-california.html",
        "guid": "https://www.lavanguardia.com/internacional/20240502/9608219/policia-desmantelar-campamento-pro-palestina-ucla-california.html",
        "author": "Autor Agencias",
        "thumbnail": "",
        "description": "Entre 300 y 500 personas se mantenían atrincheradas en una plaza central del campus de California",
        "content": "Agentes de la policía practicaron este jueves decenas de detenciones tras irrumpir en el campamento propalestino instalado en la Universidad de California (UCLA) en Los Ángeles.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/05/02/663377666335c.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Internacional"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "Los empresarios alertan de la pérdida de un banco con sede operativa en Catalunya",
        "pubDate": "2024-05-02 04:00:00",
        "link": "https://www.lavanguardia.com/dinero/20240502/9607816/empresarios-alertan-perdida-banco-sede-operativa-catalunya.html",
        "guid": "https://www.lavanguardia.com/dinero/20240502/9607816/empresarios-alertan-perdida-banco-sede-operativa-catalunya.html",
        "author": "Eduardo Magallón Lecina",
        "thumbnail": "",
        "description": "Foment ve la unión con  “escepticismo” y  considera que se perderá “eficacia”",
        "content": "La pérdida de un banco con sede operativa en Catalunya y especializado en pymes preocupa a la Generalitat, empresarios y sindicatos. La patronal Foment, que preside Josep Sánchez Llibre, dijo ayer que la operación \"la vemos con mucho escepticismo porque no deja de ser una OPA sin pagar efectivo\". La organización añadió que, además, con la integración de los dos entidades \"se perdería la eficacia de un banco muy cercano a las empresas y muy eficiente que tiene una metodología que dudamos se pueda mantener tras la unión\". Foment opinó que \"el plan estratégico del Sabadell aún tiene mucho recorrido\".]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/05/01/66328c3e1bb8a.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Dinero"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "BBVA propone un canje de acciones que dé al Sabadell el 16% del banco",
        "pubDate": "2024-05-01 10:32:06",
        "link": "https://www.lavanguardia.com/dinero/20240501/9607642/bbva-propone-sabadell-canjear-1-accion-4-8-doble-sede-corporativa.html",
        "guid": "https://www.lavanguardia.com/dinero/20240501/9607642/bbva-propone-sabadell-canjear-1-accion-4-8-doble-sede-corporativa.html",
        "author": "Iñaki De las Heras",
        "thumbnail": "",
        "description": "La operación consistiría en una fusión por absorción, con oficinas conjuntas en Madrid y Barcelona, y domicilio social en Bilbao. Promete un hub en Barcelona y respetar la marca en las regiones relevantes",
        "content": "BBVA ha detallado su propuesta de integración con el Sabadell para, según dice, crear el tercer mayor banco cotizado de Europa. Consiste en una fusión por absorción en la que no habría ningún pago en efectivo, sino un canje de acciones que daría al Sabadell lo equivalente al 16% del capital del grupo resultante.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/04/30/6630eaf773327.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Dinero"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "Mazón y la CEV, preocupados por la concentración si se fusionan BBVA y Sabadell",
        "pubDate": "2024-05-02 08:20:38",
        "link": "https://www.lavanguardia.com/local/valencia/20240502/9608068/sabadell-bbva-mazon-cev-empresarios-valencia-sede.html",
        "guid": "https://www.lavanguardia.com/local/valencia/20240502/9608068/sabadell-bbva-mazon-cev-empresarios-valencia-sede.html",
        "author": "Hèctor Sanjuán",
        "thumbnail": "",
        "description": "Ambas entidades podrían aglutinar el 60% del mercado en la Comunitat Valenciana",
        "content": "El presidente de la Generalitat de Valencia, Carlos Mazón, y el presidente de la Confederación Empresarial Valenciana (CEV), Salvador Navarro, han mostrado su \"preocupación\" por la posible fusión entre el BBVA y Sabadell, ya que el nuevo grupo llegaría a concentrar el 60% del mercado bancario en la Comunidad Valenciana y la sede social de la segunda entidad dejaría de estar en Alicante si prospera. Así lo han expuesto antes de un acto organizado por La Vanguardia en València, en el que se analiza el futuro económico valenciano.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/05/02/66338116f0841.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Comunidad Valenciana"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "Mazón anuncia \"importantísimas inversiones\" próximamente en la Comunidad Valenciana",
        "pubDate": "2024-05-02 14:28:34",
        "link": "https://www.lavanguardia.com/local/valencia/20240502/9608311/mazon-anuncia-importantisimas-inversiones-proximamente-comunidad-valenciana.html",
        "guid": "https://www.lavanguardia.com/local/valencia/20240502/9608311/mazon-anuncia-importantisimas-inversiones-proximamente-comunidad-valenciana.html",
        "author": "Neus Navarro",
        "thumbnail": "",
        "description": "El presidente de la Generalitat Valenciana no entra en detalles, pero explica que los proyectos llegarán “a partir del próximo lunes” y que estarán relacionados con investigación biomédica, energía o movilidad",
        "content": "El presidente de la Generalitat Valenciana, Carlos Mazón, ha anunciado este jueves que \"importantísimas inversiones vienen a la Comunidad Valenciana\". Sin entrar en detalles, el jefe del Consell ha hecho este avance durante su intervención de apertura en el foro \"Encuentros Dinero: Especial Comunidad Valenciana\" que La Vanguardia ha celebrado esta mañana en la sede de la Confederació Empresarial de la Comunitat Valenciana (CEV), con patrocinio de Caixabank y Telefónica. ]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/files/fp/uploads/2024/05/02/66339e435d566.r_d.4290-1526-0.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Comunidad Valenciana"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "​La Generalitat estudiará la próxima semana si levanta la emergencia por sequía",
        "pubDate": "2024-05-02 15:07:03",
        "link": "https://www.lavanguardia.com/local/catalunya/20240502/9608355/generalitat-estudiara-proxima-semana-flexibilizar-emergencia-sequia.html",
        "guid": "https://www.lavanguardia.com/local/catalunya/20240502/9608355/generalitat-estudiara-proxima-semana-flexibilizar-emergencia-sequia.html",
        "author": "Autor Agencias",
        "thumbnail": "",
        "description": "Las últimas lluvias han incrementado las reservas del Ter y del Llobregat hasta un 23 %, una cifra que se espera que siga aumentando en los próximos días",
        "content": "La Generalitat valorará la próxima semana si puede levantar la fase de emergencia por la sequía, lo que supondría flexibilizar las restricciones. Es un análisis derivado de las importantes aportaciones de lluvia registradas la última semana, y que han incrementado las reservas de las cuencas internas hasta un 21,7 %, una cifra que se espera que siga aumentando en los próximos días. En el caso, de la región de Barcelona y Girona servida por el Ter y Llobregat han alcanzado el 23% de su nivel máximo, lo que se aproxima al 25%, un umbral que abrigaría las esperanzas de levantar la fase más aguda de la sequía.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/05/02/6633ab4a42723.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Catalunya"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "Ni Barcelona ni Girona limitarán el consumo de agua en los hoteles este verano",
        "pubDate": "2024-05-02 09:07:59",
        "link": "https://www.lavanguardia.com/local/catalunya/20240502/9608017/barcelona-girona-limitaran-consumo-agua-hoteles-verano-rac1.html",
        "guid": "https://www.lavanguardia.com/local/catalunya/20240502/9608017/barcelona-girona-limitaran-consumo-agua-hoteles-verano-rac1.html",
        "author": "RAC1 RAC 1",
        "thumbnail": "",
        "description": "Según ha podido saber RAC1, ninguna de las 10 ciudades más pobladas del país en situación de emergencia por sequía sacará adelante esta medida",
        "content": "A pesar de la lluvia de los últimos días, las medidas para combatir la sequía continúan activas y uno de los miedos que había, especialmente en el sector turístico, era que se aplicara restricciones al consumo de agua a los hoteles. Sin embargo, según puede adelantar RAC1, ni Barcelona ni Girona ni ninguna de las 10 ciudades más pobladas en situación de emergencia por sequía limitarán el gasto de agua en estos establecimientos, al menos, por ahora.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/05/02/66332fe621b27.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Catalunya"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "Salvador Illa no cierra la puerta a pactar con Junts un Govern \"transversal\"",
        "pubDate": "2024-05-02 08:46:16",
        "link": "https://www.lavanguardia.com/politica/20240502/9608089/salvador-illa-abre-puerta-pactar-junts-govern-transversal.html",
        "guid": "https://www.lavanguardia.com/politica/20240502/9608089/salvador-illa-abre-puerta-pactar-junts-govern-transversal.html",
        "author": "Luis B. García García",
        "thumbnail": "",
        "description": "El candidato del PSC asegura que irá a la investidura si gana y tratará de alejar la amenaza de una repetición electoral",
        "content": "El candidato del PSC a las elecciones del 12 de mayo, Salvador Illa, tiene claro que el rival en las urnas es Junts y que el resultado que obtenga Puigdemont junto a la magnitud de la caída que pueda sufrir ERC, puede acabar por decantar la balanza. Illa se sabe ganador, pues así lo señalan todas las encuestas desde hace meses, pero la cuestión está en cuán grande es la distancia con Junts y la suma de los partidos independentistas. Además, la estabilidad del Gobierno de España se sustenta en la formación posconvergente, que ya ha dado muestras de su fluctuación en el Congreso. Bajo estas premisas se entiende que Illa haya apostado hoy por formar un Govern \"transversal\" si gana las elecciones catalanas, del que no ha querido excluir, adrede, al partido de Puigdemont.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/05/02/6633702b48a67.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Política"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "Puigdemont cree que puede ser investido sin mayoría absoluta independentista",
        "pubDate": "2024-05-02 10:33:35",
        "link": "https://www.lavanguardia.com/politica/20240502/9608190/puigdemont-cree-investido-mayoria-absoluta-independentista.html",
        "guid": "https://www.lavanguardia.com/politica/20240502/9608190/puigdemont-cree-investido-mayoria-absoluta-independentista.html",
        "author": "Iñaki Pardo Torregrosa",
        "thumbnail": "",
        "description": "El expresidente catalán asegura que estará presente en el primer debate de investidura, que será como tarde el 25 de junio, y será el candidato de Junts si hay repetición electoral en otoño",
        "content": "Todos los pronósticos prevén un escenario postelectoral complejo en Catalunya, con fragmentación del voto y posibilidad de bloqueo e incluso repetición de los comicios en otoño. Pero el candidato de Junts, Carles Puigdemont, que si hay repetición electoral se volverá a presentar, confía en ser investido en segunda votación, con más votos a favor que en contra, aunque el independentismo no tenga mayoría absoluta. Así se ha pronunciado el expresidente catalán este jueves en una rueda de prensa en Argelers organizada por la Agència Catalana de Notícies, en la que ha reiterado que su intención es pactar el resto de fuerzas independentistas y que los votos de JxCat no facilitarán la investidura de Salvador Illa, candidato del PSC.]]>",
        "enclosure": {
            "link": "https://www.lavanguardia.com/files/og_thumbnail/files/fp/uploads/2024/05/02/66336a2c70c09.r_d.2190-2226-0.jpeg",
            "type": "image/jpeg"
        },
        "categories": [
            "Política"
        ],
        "medio": "LaVanguardia"
    },
    {
        "title": "El alegato final de Daniel Sancho: \"Siento que unos padres hayan perdido un hijo\".",
        "pubDate": "2024-05-02 16:49:00",
        "link": "https://www.lavozdegalicia.es/noticia/internacional/2024/05/02/alegato-final-daniel-sancho-siento-padres-hayan-perdido-hijo/00031714666576842487355.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/internacional/2024/05/02/alegato-final-daniel-sancho-siento-padres-hayan-perdido-hijo/00031714666576842487355.htm",
        "author": "LA VOZ",
        "thumbnail": "",
        "description": "Última jornada del juicio por el asesinato del colombiano Edwin Arrieta. El joven español, hijo del actor Rodolfo Sancho, espera ahora la sentencia, que se conocerá el próximo verano",
        "content": "Última jornada del juicio por el asesinato del colombiano Edwin Arrieta. El joven español, hijo del actor Rodolfo Sancho, espera ahora la sentencia, que se conocerá el próximo verano.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/rzCUTcoYMKnGfyU04jyjSwhLBmw=/768x/2023/09/06/00121694033761626851199/Foto/efe_20230806_031453027.jpg"
        },
        "categories": [
            "Internacional"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "Google elimina 200 puestos clave y trasladará algunas funciones a India y México.",
        "pubDate": "2024-05-02 16:42:00",
        "link": "https://www.lavozdegalicia.es/noticia/economia/2024/05/02/google-elimina-200-puestos-clave-trasladara-funciones-india-mexico/00031714667336953569957.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/economia/2024/05/02/google-elimina-200-puestos-clave-trasladara-funciones-india-mexico/00031714667336953569957.htm",
        "author": "Efe",
        "thumbnail": "",
        "description": "El vicepresidente de la multinacional informó de los despidos por correo electrónico",
        "content": "El vicepresidente de la multinacional informó de los despidos por correo electrónico.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/d2JYQX1wmdCk_LIAc6n7vqxi2Tg=/768x/2024/01/11/00121704966481944118695/Foto/reu_20231219_045800482.jpg"
        },
        "categories": [
            "Economía",
            "Google",
            "despidos"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "Jaime Cantizano se casará en el 2025 con el artista Miguel García Golding.",
        "pubDate": "2024-05-02 16:12:00",
        "link": "https://www.lavozdegalicia.es/noticia/gente/2024/05/02/cantizano-casara-2025-artista-miguel-garcia-golding/00031714661214264768716.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/gente/2024/05/02/cantizano-casara-2025-artista-miguel-garcia-golding/00031714661214264768716.htm",
        "author": "LA VOZ",
        "thumbnail": "",
        "description": "Según confirman varios medios, el presentador jerezano contraerá matrimonio con el artista visual, con quien lleva varios años de relación. En el 2016 fue padre soltero de Leo mediante gestación subrogada en EE.UU.",
        "content": "Según confirman varios medios, el presentador jerezano contraerá matrimonio con el artista visual, con quien lleva varios años de relación. En el 2016 fue padre soltero de Leo mediante gestación subrogada en EE.UU..",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/A4wO-K-NptRM8HjHuUaad_EKqbE=/768x/2024/05/02/00121714666201935139696/Foto/eup_20240502_160400861.jpg"
        },
        "categories": [
            "Gente"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "Arizona Baby: \"Escuchar \"Despacito\" o \"Gangnam Style\" provoca urticaria porque en su momento quedamos saturados\".",
        "pubDate": "2024-05-02 16:01:01",
        "link": "https://www.lavozdegalicia.es/noticia/ourense/2024/05/03/grupo-ortodoxo-influencias/0003_202405O3C6991.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/ourense/2024/05/03/grupo-ortodoxo-influencias/0003_202405O3C6991.htm",
        "author": "María Doallo",
        "thumbnail": "",
        "description": "La banda vallisoletana presenta su nuevo disco, «Salvation», en el café Auriense este viernes por la noche",
        "content": "La banda vallisoletana presenta su nuevo disco, \"Salvation\", en el café Auriense este viernes por la noche.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/6aTybMjXZ-bHVJokG1ew_VGv0Wg=/768x/2024/04/30/00121714497782685104198/Foto/OY3C6F1_1.jpg"
        },
        "categories": [
            "Ourense",
            "Música",
            "Conciertos",
            "A Coruña ciudad",
            "Ourense ciudad"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "El equipo al que habría rechazado Carlos Sainz según Antonio Lobato.",
        "pubDate": "2024-05-02 15:54:00",
        "link": "https://www.lavozdegalicia.es/noticia/escuadra/motor/2024/05/02/equipo-rechazado-carlos-sainz-segun-antonio-lobato/00031714664918186772116.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/escuadra/motor/2024/05/02/equipo-rechazado-carlos-sainz-segun-antonio-lobato/00031714664918186772116.htm",
        "author": "",
        "thumbnail": "",
        "description": "«Decidió no aceptar la oferta y dejar pasar la fecha límite que tenía para contestar», asegura el comentarista",
        "content": "\"Decidió no aceptar la oferta y dejar pasar la fecha límite que tenía para contestar\", asegura el comentarista.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/aEcV1R-cp6TCtHDqWyq0_bTJ9_I=/768x/2024/05/02/00121714664888281977343/Foto/EuropaPress_5871963_sainz_carlos_spa_scuderia_ferrari_sf_24_portrait_during_the_formula_msc-EP.jpg"
        },
        "categories": [
            "Motor",
            "Carlos Sainz Jr.",
            "Antonio Lobato",
            "Audi",
            "Fórmula 1"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "\"Torres de Oeste\", el drakkar de Catoira que saldrá en una película de Amenábar.",
        "pubDate": "2024-05-02 15:42:00",
        "link": "https://www.lavozdegalicia.es/noticia/arousa/catoira/2024/05/02/torres-oeste-drakkar-catoira-saldra-pelicula-amenabar/00031714662426583595468.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/arousa/catoira/2024/05/02/torres-oeste-drakkar-catoira-saldra-pelicula-amenabar/00031714662426583595468.htm",
        "author": "",
        "thumbnail": "",
        "description": "El Concello ha cedido el uso de la embarcación para<em> El Cautivo</em>, un filme sobre Miguel de Cervantes en el que participa Netflix",
        "content": "El Concello ha cedido el uso de la embarcación para El Cautivo, un filme sobre Miguel de Cervantes en el que participa Netflix.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/cC9GpzKDKzPS_gQ8XzKxQiSSDtw=/768x/2024/05/02/00121714667762137498246/Foto/AY3C5F1_183513.jpg"
        },
        "categories": [
            "Catoira"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "Carla Bruni testifica por una investigación abierta contra Nicolas Sarkozy.",
        "pubDate": "2024-05-02 15:39:00",
        "link": "https://www.lavozdegalicia.es/noticia/internacional/2024/05/03/carla-bruni-testifica-investigacion-abierta-marido-sarkozy/0003_202405G3P19994.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/internacional/2024/05/03/carla-bruni-testifica-investigacion-abierta-marido-sarkozy/0003_202405G3P19994.htm",
        "author": "La Voz",
        "thumbnail": "",
        "description": "La ex primera dama francesa ha sido citada a declarar como imputada en el caso de presunta manipulación de testigos en el que está también implicado su marido",
        "content": "La ex primera dama francesa ha sido citada a declarar como imputada en el caso de presunta manipulación de testigos en el que está también implicado su marido.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/KC1ZqgnpKUtPSJXlhStSd1nsxVM=/768x/2024/05/02/00121714663801760405516/Foto/efe_20231112_165049296.jpg"
        },
        "categories": [
            "Internacional",
            "Nicolás Sarkozy",
            "Carla Bruni",
            "Muamar el Gadafi",
            "Corrupción",
            "Francia"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "Muere un joven de Lugo de 21 años en Valladolid tras desplomarse en su facultad.",
        "pubDate": "2024-05-02 15:31:00",
        "link": "https://www.lavozdegalicia.es/noticia/lugo/lugo/2024/05/02/muere-joven-lugo-21-anos-tras-sufrir-ataque-epileptico-valladolid/00031714662034534851649.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/lugo/lugo/2024/05/02/muere-joven-lugo-21-anos-tras-sufrir-ataque-epileptico-valladolid/00031714662034534851649.htm",
        "author": "André S. Zapata",
        "thumbnail": "",
        "description": "El chico, que tenía epilepsia, estudiaba Periodismo en el campus de la UVA. El rector suspendió las clases y la comunidad mostró su «consternación»",
        "content": "El chico, que tenía epilepsia, estudiaba Periodismo en el campus de la UVA. El rector suspendió las clases y la comunidad mostró su \"consternación\".",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/ZdadvMqnGR-_KsGc6gF3MHRhlI4=/768x/2024/05/02/00121714663323702901752/Foto/L_20240502_171756000.jpg"
        },
        "categories": [
            "Lugo ciudad",
            "Sucesos",
            "Valladolid"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "El Gobierno no prevé cambios en la A-57 y mantendrá el trazado \"más próximo a la ciudad\" de Pontevedra.",
        "pubDate": "2024-05-02 15:18:00",
        "link": "https://www.lavozdegalicia.es/noticia/pontevedra/pontevedra/2024/05/03/gobierno-preve-cambios-a-57-mantendra-trazado-proximo-ciudad/0003_202405P3C2993.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/pontevedra/pontevedra/2024/05/03/gobierno-preve-cambios-a-57-mantendra-trazado-proximo-ciudad/0003_202405P3C2993.htm",
        "author": "Serxio Barral",
        "thumbnail": "",
        "description": "El PP lamenta la «respuesta evasiva» obtenida en el Senado a preguntas de Pepa Pardo",
        "content": "El PP lamenta la \"respuesta evasiva\" obtenida en el Senado a preguntas de Pepa Pardo.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/JQAtWVYP2LJdqJYhwlYRe_LgQlI=/768x/2024/05/02/00121714660622074157348/Foto/PY3C2F4_163537.jpg"
        },
        "categories": [
            "Pontevedra ciudad",
            "A-57",
            "Senado"
        ],
        "medio": "LaVozDeGalicia"
    },
    {
        "title": "El nuevo conselleiro de Sanidade avanza que habrá cambios en algunas gerencias de las áreas sanitarias.",
        "pubDate": "2024-05-02 15:07:00",
        "link": "https://www.lavozdegalicia.es/noticia/galicia/2024/05/02/nuevo-conselleiro-sanidade-avanza-habra-cambios-gerencias-areas-sanitarias/00031714656973416600541.htm",
        "guid": "https://www.lavozdegalicia.es/noticia/galicia/2024/05/02/nuevo-conselleiro-sanidade-avanza-habra-cambios-gerencias-areas-sanitarias/00031714656973416600541.htm",
        "author": "La Voz",
        "thumbnail": "",
        "description": "Gómez Caamaño reconoce que tiene «ideas diferentes» a las de su predecesor, aunque elogia el trabajo hecho por García Comesaña",
        "content": "Gómez Caamaño reconoce que tiene \"ideas diferentes\" a las de su predecesor, aunque elogia el trabajo hecho por García Comesaña.",
        "enclosure": {
            "link": "https://cflvdg.avoz.es/sc/KVOiy3Sp51BdcY7QUXCPSvoysRI=/768x/2024/05/02/00121714658281328133833/Foto/eup_20240502_111135235.jpg"
        },
        "categories": [
            "Galicia",
            "Sergas",
            "Sanidad",
            "Consellería de Sanidade"
        ],
        "medio": "LaVozDeGalicia"
    }
]
   # Get the database
   
    dbname = get_database()
    print(dbname.list_collection_names())
    print(len(all_items))
    for e in all_items:
        print(dbname.get_collection("tfg").insert_one(e))