import m_20minutos, m_abc, m_cope, m_elconfidencial, sm_elpais, m_lasexta
import html2text

# all_items = []
# for e in m_20minutos.get_news_list():
#     all_items.append(e)
# for e in m_abc.get_news_list():
#     all_items.append(e)
# for e in m_cope.get_news_list():
#     all_items.append(e)
# for e in m_elconfidencial.get_news_list():
#     all_items.append(e)
# for e in sm_elpais.get_news_list():
#     all_items.append(e)
# for e in m_lasexta.get_news_list():
#     all_items.append(e)



# soup=BeautifulSoup(get_news_JSON(rss2json.RRS2JSON+RSS_URL)[0]["content"])
# text=soup.get_text()
    

#sacar categorias

# print(len(all_items))
# for e in all_items:
#     for i in e["categories"]:
#         print(i)
    
# print(len(all_items))

# print(all_items[0]["title"])
# print(all_items[0]["content"])

abccontent="""
 La gala de los Oscar concluyó a las 3.25 horas, aunque en España había terminado dos horas antes, cuando J. A. Bayona y Pablo Berger perdieron cualquier opción de ganar. 'La sociedad de la nieve' se quedó sin premio a mejor película internacional frente a 'La zona de interés' y a maquillaje y peluquería ante 'Pobres criaturas'. ' Robot Dreams ', por su parte, fue derrotada por 'El chico y la garza', del maestro Miyazaki. Ya que no vas a ganar, al menos que quien te quite la gloria sea el último maestro vivo del género.Porque sí, los Oscar son cuestión más de tiempo que de cine. De espectáculo más que de celuloide. Premiar a Christopher Nolan , el director que ha hecho de la cuarta dimensión un protagonista más de sus guiones, tiene algo de poético, de cerrar un círculo, algo que también está en todas sus películas. Total, que 'Oppenheimer' arrasó con siete de las 13 nominaciones, tal y como decían las profecías. Ni 'Pobres criaturas', que se desinfló tras arrancar la noche ganando tres estatuillas -diseño de vestuario, diseño de producción y maquillaje al inicio y Emma Stone como actriz protagonista al final- ni 'Barbie' -que fue menospreciada en el palmarés, aunque alabada durante la gala- ni Martin Scorsese -cero premios para 'Los asesinos de la luna'- hicieron sombra al biopic del padre de la bomba atómica: «El cine tiene poco más de cien años... Ser parte de su historia significa mucho para mí», dijo Christopher Nolan mientras recogía el primer Oscar de su carrera. Al terminar su discurso de ganador, Martin Scorsese, 81 años de cine recorriendo sus venas, lo miró y no hizo ni una mueca ante la que quizá sea la última oportunidad que le quedaba de ganar otro Oscar.La cara de Greta Gerwig fue un poema toda la noche y eso que estaba ahí, en segundo plano, durante el mejor momento de la ceremonia, cuando Ryan Gosling cantó 'I'm Just Ken' . Empezó el actor a cantar detrás de Margot Robbie, que no podía dejar de reír a boca llena, una risa inmensa y genuina; y detrás de ambos Greta Gerwig como pensando que por qué sus protagonistas estaban de fiesta mientras ella vivía un funeral . Pero importó poco porque Ryan Gosling puso al público en pie con una interpretación diviertida, entonada y en la que era imposible no bailar. Incluso un rockero como Slash se subió al escenario y con su mítica guitarra acompañó la canción. Historia desde ya de los Oscar y lo único salvable del sopor de ceremonia que -un año más- firma la primera industria de entretenimiento del mundo. Noticia Relacionada reportaje No Christopher Nolan: el cineasta que domeñó el tiempo y el espacio busca su primer Oscar Fernando MuñozPorque sí, los Oscar son una gala de premios en la que importa tanto quién gana como todo lo que hay alrededor. Y de eso Jimmy Kimmel , presentador de la ceremonia en cuarta ocasión, sabe tanto que comenzó su monólogo inicial repasando uno por uno los nominados con más nombre y mejor planta -«os ha tocado la lotería de la genética», le dijo a los protagonistas de 'Barbie', Ryan Gosling y Margot Robie - pero, sobre todo, homenajeando a los guionistas que estuvieron de huelga 118 días: «No estamos en una ciudad de gente con mucho bótox y que beben batidos 'detox', Los Ángeles es también una ciudad con una gran fuerza sindical», expresó. Y animó a salir al escenario a técnicos, camioneros, electricistas, carpinteros... todos con barbas y pintas de ser más de Trump que de 'Barbie'. Las noches de los Oscar siempre avanzan a ritmo lento, mascado. Saben los organizadores que los ojos del planeta están sobre el escenario y se recrean entre premio y premio como en ninguna otra gala. «Va a ser una noche muy larga, ya vamos con cinco minutos de retraso», dijo Jimmy Kimmel nada más empezar la ceremonia. A la hora, apenas se habían entregado seis de los 23 premios. Eso sí, ya había cantado Billie Eilish, habían homenajeado a estrellas veteranas y el presentador había salido seis veces a animar el cotarro. El cine se abrió paso entre todo ese andamiaje de espectáculo de mano de Justine Triet, la cineasta responsable de ' Anatomía de una caída ', que recogió el Oscar a mejor guion original junto a su marido y coguionista, Arthur Harari. Muy franceses ellos, apenas dijeron mucho ante el patio de butacas. Tampoco dijo nada la pobre Greta Gerwig , responsable de 'Barbie', que veía cómo perdía el primer Oscar al que optaba y que la noche, lejos de pintar de rosa, se tornaba más bien negra para sus intereses. Ryan Gosling durante su actuación en los premios Oscar 2024 EFE / Cortesía de A.M.P.A.S.© 2024Más palmas se llevó minutos después el guionista Cord Jefferson, que adaptó la novela ' American Fiction '. Reclamó que no hace falta hacer películas de 200 millones para hacer buen cine, y entre los asistentes, casi todos ellos intérpretes de algunas de esas megaproducciones, se escuchó una gran ovación. La misma que no pudieron escuchar los españoles nominados. Noticia Relacionada estandar No Consulta la lista completa de premiados Jorge Herrero Desde documentales hasta cortometrajes animados, el catálogo abarca un amplio espectro de géneros y narrativasPolítica antes, durante y despuésAntes, mucho antes, a las afueras del Dolby Theater y en los alrededores de la mastodóntica alfombra roja de los Oscar se juntaron los habituales cazadores de autógrafos con los manifestantes pro-Palestina que recibieron el apoyo de muy pocos nominados, apenas de los franceses de ' Anatomía de una caída '; el resto, en la fiesta de una industria dominada por nombres de ascendencia judía, no hicieron tanto caso a la protesta. Ya en el escenario, solo Jonathan Glazer, director de 'La zona de interés', apoyó a Gaza y comparó la guerra con el Holocausto . Hubo muy poca política, en realidad, nada que ver con esta latitudes. Si en los Goya o en los Cesar todo son reivindicaciones, aquí todo es espectáculo. Y cuando se denuncia algo, todo es 'vía institucional'. Lo demostraron los organizadores al poner un vídeo de Navalny diciendo que lo único que no puede hacer la buena gente es rendirse. Era una escena del documental con el que ganó el Oscar el año pasado y en el que el disidente asesinado habla directamente a cámara. Antes, el director ucraniano Mstyslav Chernov , responsable de ' 20 días en Mariúpol ', recogió el primer Oscar de la historia de Ucrania para decir que cambiaría todo lo que tiene por que Rusia nunca hubiera invadido su país. «Los que están aquí, gente de la más talentosa del mundo, puede intentar que la historia cuente lo que de verdad pasó, que la verdad prevalezca y que los que dieron su vida no sean olvidados», dijo entre aplausos. Emma Stone, ganadora del Oscar a mejor actriz por 'Pobres criaturas' EFEY los premios, que también se dan, claro y dejan algunas curiosidades, como que Wes Anderson ganara anoche el primer Oscar de su carrera -y llevaba ocho nominaciones- con un cortometraje, ' La maravillosa historia de Henry Sugar '. El director de ' El gran hotel Budapest ' o 'Moonrise Kingdom' no le dio la gana ir a la gala a recogerlo. Sí pasaron por allí los japoneses de ' Godzilla: Minus One ', que recogieron el galardón a mejores efectos especiales. Es la primera producción alejada de Hollywood que lo hace en la categoría y es, quizá, el resumen del último cine americano, que ya no gana ni el Oscar que realmente solo ellos saben hacer. También pasó por el escenario Sean Lennon, hijo de Yoko Ono y John Lenon, que se hizo con la estatuilla a mejor corto de animación por ' WAR IS OVER! Inspired by the Music of John and Yoko '.Total, que a las 3.30 hora de España -todo es cuestión de tiempo aquí- los Oscar habían cumplido su horario, desmentido a Jimmy Kimmel y consagrado para siempre a Nolan. El domador del tiempo en pantalla, el autor más comercial, el hombre que moviliza a los amantes del cine que no leen 'Cahiers du Cinéma', ganó su primera estatuilla y puso a Hollywood a sus pies. Nominados a Mejor Película American Fiction Anatomía de una caída Barbie The Holdovers Los asesinos de la luna Maestro GANADOR - Oppenheimer Vidas pasadas Poor Things La zona de interésNominados al Mejor Dirección Anatomía de una caída - Justine Triet Los asesinos de la luna - Martin Scorssese GANADOR - Oppenheimer - Christopher Nolan Poor Things - Yorgos Lanthimos La zona de interés - Jonathan GlazerNominados a Mejor Actor Bradley Cooper - Maestro Colman Domingo - Rustin Paul Giamati - Los que se quedan GANADOR - Cilian Murphy - Oppenheimer Jeffrey Wright - American FictionNominadas a Mejor Actriz Annette Bening - Nyad Lily Gladstone - Asesinos de la luna Sandra Huller - Anatomía de una caída Carey Mulligan - Maestro GANADORA - Emma Stone - Pobres criaturasNominados a Mejor Actor de Reparto Starling K. Brown - American Fiction Ryan Gosling - Barbie GANADOR - Robert Downey Jr - Oppenheimer Mark Ruffalo - Pobres criaturas Robert de Niro - Asesinos de la lunaNominadas a Mejor Actriz de Reparto Emily Blunt - Oppenheimer Danielle Brooks - El color púrpura America Ferrera - Barbie Jodie Foster - Nyad GANADORA - Da'Vine Joy Randolph - Los que se quedanNominadas a Mejor Película Extranjera Io Capitano - Italia Perfect Days - Japón La sociedad de la nieve - España La sala de los profesores - Alemania GANADORA - La zona de interés - Reino UnidoNominadas a mejor Película de Animación GANADOR - El niño y la garza Eklemmental Nimona Robot Dreams Spider-man: a través del metaversoNominadas al mejor Largometraje Documental Bobi wine: el presidente de la gente La memoria eternal Cuatro hijas Matar a un tigre GANADOR - 20 días en MariupolNominadas al mejor Cortometraje Documental El ABC del libro de Banning El barbero de Little Rock La hisla en medio GANADOR - La última tienda de reparación Nai nai y Wai pooNominados a mejor Maquillaje y Peluquería Golda Maestro Oppenheimer GANADORA - Pobres Criaturas La sociedad de la nieveMejor Diseño de Vestuario Barbie Asesinos de la luna Napoleón Oppenheimer GANADOR - Pobres criaturasNominadas a la Mejor Fotografía El Conde Asesinos de la luna Maestro GANADOR - Oppenheimer Pobres criaturasNominadas a mejor Montaje Anatomía de una caída Los que se quedan Los asesinos de la luna GANADOR - Oppenheimer Poor ThingsNominados a mejor Sonido The Creator Maestro Mission Imposible: sentencia mortal parte I Oppenheimer GANADOR - Zona de interésNominadas a mejores Efectos Especiales The Creator GANADOR - Gozilla minus one Guardianes de la Galaxia Vol. 3 Mission Imposible: sentencia mortal parte INominados a mejor Guion Original GANADOR - Anatomía de una caída Los que se quedan Maestro Secretos de un escándalo Vidas pasadasNominados a mejor Guion Adaptado GANADOR - American Fiction Barbie Oppenheimer Pobres Criaturas La zona de interésNominados a mejor Banda Sonora Original American Fiction Indicana Jones y el dial del destino Asesinos en la luna GANADOR - Oppenheimer Poor ThingsNominadas a mejor Canción Original 'The Fire Inside' - Flamin Hot 'Im Just Ken' - Barbie 'It Never Went Away' - American Symphony 'Wahzhahe' - Asesinos de la luna GANADORA - 'What Was I Made For?' - BarbieNominadas a mejor Cortometraje de Animación Carta a un cerdo 99 sentidos Nuestro uniforme Paquidermo GANADOR - ¡La guerra ha acabado! Inspirado en la múisca de John y YokoNominadas a mejor Cortometraje The After Invencible Caballero de Fortuna Rojo, blanco y azul GANADORA - La maravillosa historia de Henry Sugar"
"""


from transformers import pipeline # Load the summarization pipeline
summarizer = pipeline("summarization",model="google-t5/t5-base")
text = """\ Your 20 lines of text go here. It's important that the text is coherent and forms a single, well-structured narrative or argument for the best summarization results. The transformer models are trained on a variety of texts, but they perform best when the input text is similar to the data they were trained on, which often includes news articles, essays, and other forms of written content. Keep this in mind when choosing your text for summarization. (Additional text lines would continue here to make up the full 20 lines you want to summarize.) """
text=html2text.html2text("""
<p>El PP no suelta la presa sobre la esposa del presidente del Gobierno, Pedro Sánchez, por las reuniones que mantuvo con la matriz de Air Europa unos días antes de que la aerolínea fuera rescatada con dinero público en 2020. El líder popular, Alberto Núñez Feijóo, avisó este miércoles a Sánchez de que <b>el PP impulsará una "investigación específica" sobre los vínculos Begoña Gómez</b> con esa empresa y su supuesta intermediación para el rescate, una investigación que será "parlamentaria" pero que, amenazó Feijóo, puede terminar llegando a los tribunales si el presidente no ofrece explicaciones.</p><p>En una intervención con un tono algo más sosegado que en las últimas semanas, Feijóo aseguró que Sánchez que "se equivoca" si cree que ha "resuelto las dudas de lo que ha pasado en su Gobierno y en su partido", una referencia muy poco velada a la conocida como trama Koldo, que se habría beneficiado de mordidas en la compra de mascarillas durante la pandemia. Al líder del PP también<b> le genera dudas "lo que ha pasado" en la "casa" del presidente</b>, en referencia a la esposa de Sánchez, a quien no llamó por su nombre.</p><p>"Se equivoca si cree que ha dado carpetazo" a ese asunto, espetó Feijóo, que prometió que si el presidente "vuelve a negarse a dar explicaciones" impulsará "una investigación específica sobre los asuntos que le afectan a su entorno más inmediato".<b> "Parlamentaria seguro, y judicial también</b>, si es necesaria", espetó el líder del PP. En respuesta, Sánchez ironizó con la "paciencia" que, dijo, tiene que tener para responder semanalmente a las mismas preguntas, y exigió a Feijóo que "plante cara a la corrupción" en el PP y "exija la dimisión a la señora [Isabel Díaz] Ayuso como presidenta de la Comunidad de Madrid" por las informaciones sobre el fraude fiscal que habría cometido su pareja.</p>
""")
print(text)


"""
primer parrafo: 94 palabras
segundo parrafo: 96 palabras
tercer parrafo: 114 palabras
"""
texto_ar=[
    """El PP no suelta la presa sobre la esposa del presidente del Gobierno, Pedro Sánchez, por las reuniones que mantuvo con la matriz de Air Europa unos días antes de que la aerolínea fuera rescatada con dinero público en 2020. El líder popular, Alberto Núñez Feijóo, avisó este miércoles a Sánchez de queel PP impulsará una "investigación específica" sobre los vínculos Begoña Gómez con esa empresa y su supuesta intermediación para el rescate, una investigación que será "parlamentaria" pero que, amenazó Feijóo, puede terminar llegando a los tribunales si el presidente no ofrece explicaciones.""", 

    """En una intervención con un tono algo más sosegado que en las últimas semanas, Feijóo aseguró que Sánchez que "se equivoca" si cree que ha "resuelto las dudas de lo que ha pasado en su Gobierno y en su partido", una referencia muy poco velada a la conocida como trama Koldo, que se habría beneficiado de mordidas en la compra de mascarillas durante la pandemia. Al líder del PP también le genera dudas "lo que ha pasado" en la "casa" del presidente, en referencia a la esposa de Sánchez, a quien no llamó por su nombre.""",

    """"Se equivoca si cree que ha dado carpetazo" a ese asunto, espetó Feijóo, que prometió que si el presidente "vuelve a negarse a dar explicaciones" impulsará "una investigación específica sobre los asuntos que le afectan a su entorno más inmediato". "Parlamentaria seguro, y judicial también, si es necesaria", espetó el líder del PP. En respuesta, Sánchez ironizó con la "paciencia" que, dijo, tiene que tener para responder semanalmente a las mismas preguntas, y exigió a Feijóo que "plante cara a la corrupción" en el PP y "exija la dimisión a la señora [Isabel Díaz] Ayuso como presidenta de la Comunidad de Madrid" por las informaciones sobre el fraude fiscal que habría cometido su pareja."""
          ]

es_en_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
en_es_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
summ=[]

for e in texto_ar:

    summ.append(summarizer(es_en_translator(e)[0]['translation_text'], max_length=100, min_length=70, do_sample=False)[0]['summary_text'])

resumen=""
for e in summ:
    resumen+=en_es_translator(e)[0]['translation_text']+"\n\n"

# Summarize the text, attempting to target around 5 lines.
# Note: Adjust 'max_length' and 'min_length' as needed to get closer to your desired output size.
print(resumen)



"""
*******CON min_length=30, max_length=100********
el PP no libera la presa sobre la esposa del presidente del gobierno, Pedro Sánchez . el líder popular, Alberto Nez Feijóo, advierte al presidente que promoverá una "investigación específica"

Feijóo dice que Sánchez "está equivocado" si cree que ha "resuelto las dudas" de lo que ha sucedido. Plantea dudas "qué ha sucedido" en la "casa" del presidente

si el presidente "regresa a negarse a dar explicaciones" promoverá "una investigación específica", dice . "Parlamento seguro y judicial también, si es necesario", añade el líder del PP.


********CON min_length=50, max_length=100********
el PP no libera la presa sobre la esposa del presidente del gobierno, Pedro Sánchez . el líder popular, Alberto Nez Feijóo, advierte al presidente que promoverá una "investigación específica"

Feijóo dice que Sánchez "está equivocado" si cree que ha "resuelto las dudas" de lo que ha sucedido. Plantea dudas "qué ha sucedido" en la "casa" del presidente

si el presidente "regresa a negarse a dar explicaciones" promoverá "una investigación específica", dice . "Parlamento seguro, y judicial también, si es necesario", añade el líder del PP. en respuesta, 
plancha con la "paciencia" que tiene que responder las mismas preguntas semanalmente .


********CON min_length=70, max_length=100********
el PP no libera la presa a la esposa del presidente del gobierno, Pedro Sánchez . el líder popular, Alberto Nez Feijóo, advierte al presidente que promoverá una "investigación específica" sobre los enlaces a la aerolínea . si el presidente no ofrece explicaciones, la investigación puede terminar llegando a los tribunales .

Feijóo dice que Sánchez "está equivocado" si cree que ha "resuelto las dudas" de lo que ha sucedido. Plantea dudas "qué ha sucedido" en la "casa" del presidente en referencia a su esposa, a quien no llamó por su nombre.  

si el presidente "regresa a negarse a dar explicaciones" promoverá "una investigación específica", dice . "Parlamento seguro, y judicial también, si es necesario", añade el líder del PP. en respuesta, plancha con la "paciencia" que tiene que responder las mismas preguntas semanalmente .
"""