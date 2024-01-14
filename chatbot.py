import sett
import time
import funcWhap

class ChatBot:
    
    list = []
    listCity = ["La Paz", "El Alto", "Cochabamba", "Santa Cruz", "Tarija", "Sucre", "Oruro", "Potosí"]
    listArea = ["Impresoras 3D", "Fotocopiadoras", "Sublimación", "Cortadora láser", "Computadoras", "Bioseguridad", "Impresoras", "Papel", "Novedades", "Otros"]
    listMenu = ["📦 Productos y precios", "🗺️ Dirección", "💰 Promociones y ofertas", "📖 Ver catálogos", "🙋🏻‍♂️ Chatear con un asesor"]
    listAreaSupport = ["🙋🏻‍♂️ Impresoras 3D", "🙋🏻‍♂️ Máquinas láser", "🙋🏻‍♂️ Computadoras", "🙋🏻‍♂️ Sublimación", "🙋🏻‍♂️ Atención general"]
    listCitySupport = ["➡️ La Paz", "➡️ El Alto", "➡️ Cochabamba", "➡️ Santa Cruz", "➡️ Tarija", "➡️ Sucre", "➡️ Oruro", "➡️ Potosí"]
    listAreaCatalog = ["📰 Impresoras 3D", "📰 Fotocopiadoras", "📰 Sublimación", "📰 Cortadora láser", "📰 Computadoras", "📰 Bioseguridad", "📰 Impresoras", "📰 Papel", "📰 Novedades", "📰 Otros"]

    
    def __init__(self, _text, _number, _messageId, _name):
        self.text = _text
        self.number = _number
        self.messageId = _messageId
        self.name = _name

    # Getters y Setters
    def get_text(self):
        return self.text
    def get_number(self):
        return self.number
    def get_messageId(self):
        return self.messageId
    def get_name(self):
        return self.name
    def set_text(self, _text):
        self.text = _text
    def set_number(self, _number):
        self.number = _number
    def set_messageId(self, _messageId):
        self._messageId = _messageId
    def set_name(self, _name):
        self.name = _name

    def start(self):
        # #mensaje que envio el usuario
        # text = self.text.lower() 
        text = self.text
        self.list = []
        markRead = funcWhap.markRead_Message(self.messageId)
        
        self.list.append(markRead)
        time.sleep(2)

        if "🤖 Empezar" == text:
            self.welcome("🫡")
        elif "Hola" in text:
            self.welcome("👋🏻")
        elif "✅ Menú" == text:
            self.menu()
        elif "📅 Horarios" == text:
            self.attentionSchedule()
        elif "✅ Sí" == text:
            self.menu()
        elif "⛔ No" == text:
            self.goodbye()
        # Flujo del menú principal
        elif "📦 Productos y precios" == text:
            self.productsAndPrices()
        elif "🗺️ Dirección" == text:
            self.address()
        elif "💰 Promociones y ofertas" == text:
            self.promotionsAndOffers()
        elif "📖 Ver catálogos" == text:
            self.seeCatalogs()
        elif "🙋🏻‍♂️ Chatear con un asesor" == text:
            self.chatWithAnAdvisor()
        # FLUJO DE 📦 PRODUCTOS Y PRECIOS
        # el flujo se manda automáticamente a error para integrar la IA más adelante
        elif text in self.listArea:
            self.searchForArea()  
        # elif "notFound" == text:
            self.notFound()
        elif "📦 Productos" == text:
            self.productsAndPrices()
        elif "📑 Menú" == text:
            self.menu()
        
        # FLUJO DE 🗺️ DIRECCIÓN
        elif text in self.listCity:
            self.addressForCity()
        # FLUJO DE 💰 Promociones y ofertas

        # FLUJO DE 📖 Ver catálogos
        elif text in self.listAreaCatalog:
            self.catalog()
        # FLUJO DE 🙋🏻‍♂️ Chatear con un asesor
        elif text in self.listAreaSupport:
            self.customerSupport()
        elif text in self.listCitySupport:
            self.customerSupportByCity()
        
        else:
            self.errorMessage()

            
        for item in self.list:
            funcWhap.enviar_Mensaje_whatsapp(item)

    def welcome(self, emoji):
        self.sendEmojiReactionMessage(emoji)
        self.sendSimpleText("🤖 ¡Hola "+ self.name +"! Soy SaviBot")
        self.sendSimpleText("Tú asistente virtual")
        self.sendTwoOptions("¿Cómo podemos ayudarte hoy? 😃", "✅ Menú", "📅 Horarios")

    def menu(self):
        # options = ["📦 Productos y precios", "🗺️ Dirección", "💰 Promociones y ofertas", "📖 Ver catálogos", "🙋🏻‍♂️ Chatear con un asesor"]
        self.sendSimpleText("¿En qué puedo ayudarte? 🤔")
        self.sendMenuOptions("Selecciona una opción 👇🏻", self.listMenu)
    
    def attentionSchedule(self):
        self.sendSimpleText("Nuestros horarios de atención en tiendas son:\n" \
                    "✅ Lunes a Viernes\n" \
                    "    ➡ de 8:30am a 12:30pm\n" \
                    "    ➡ de 2:30pm a 7:00pm\n" \
                    "✅ Sábados\n" \
                    "    ➡ de 9:00am a 1:00pm")
        self.menuPreEnd()
        
    def menuPreEnd(self):
        self.sendTwoOptions("¿Te puedo ayudar con algo más? 🤔", "✅ Sí", "⛔ No")
    
    def goodbye(self):
        self.sendSimpleText("🤖 Ha sido un placer atenderte")
        self.sendSimpleText("No olvides revisar nuestra página web y nuestros productos aquí 👇🏻")
        self.sendSimpleText("https://savin.com.bo/")
        
    def errorMessage(self):
        self.sendSimpleText("Lo siento, no entendí lo que dijiste 👀")
        self.sendSimpleButton("Pulsa aquí para iniciar el asistente virtual 👇🏻", "🤖 Empezar")
        
    def buildArea(self):
        self.sendEmojiReactionMessage("🛠️")
        self.sendSimpleText("Lo siento, esta área esta en construcción 🛠️")
        
    # FUNCIONES DEL MENÚ PRINCIPAL
    def productsAndPrices(self):
        # options = ["🖥️ Impresoras 3D", "🗺️ Fotocopiadoras", "💰 Sublimación", "📖 Cortadora láser", "🙋🏻‍♂️ Computadoras", "Bioseguridad", "Impresoras", "Papel", "Encuadernación", "Plastificado", "Novedades", "Otros"]
        # options = ["Impresoras 3D", "Fotocopiadoras", "Sublimación", "Cortadora láser", "Computadoras", "Bioseguridad", "Impresoras", "Papel", "Novedades", "Otros"]
        self.sendMenuOptions("Escoge el área del producto que buscas 👇🏻", self.listArea)
    
    def address(self):
        # options = ["La Paz", "El Alto", "Cochabamba", "Santa Cruz", "Tarija", "Sucre", "Oruro", "Potosí"]
        self.sendMenuOptions("Excelente, indícame de que ciudad me escribes... 👀", self.listCity)
        
    def promotionsAndOffers(self):
        self.sendSimpleText("Mantente al pendiente de nuestras ofertas 😉")
        self.menuPreEnd()
        
    def seeCatalogs(self):
        # options = ["🖥️ Impresoras 3D", "🗺️ Fotocopiadoras", "💰 Sublimación", "📖 Cortadora láser", "🙋🏻‍♂️ Computadoras", "Bioseguridad", "Impresoras", "Papel", "Encuadernación", "Plastificado", "Novedades", "Otros"]
        # options = ["Impresoras 3D", "Fotocopiadoras", "Sublimación", "Cortadora láser", "Computadoras", "Bioseguridad", "Impresoras", "Papel", "Novedades", "Otros"]
        self.sendMenuOptions("Excelente, escoge el área del catálogo que quieres ver 👇🏻", self.listAreaCatalog)
    
    def chatWithAnAdvisor(self):
        self.sendSimpleText("Muy bien ¿En qué área necesitas la atención al cliente? 🤔")
        self.sendMenuOptions("Selecciona un área 👇🏻", self.listAreaSupport)
        
    # FUNCIONES DE PRODUCTOS POR ÁREA
    
    def searchForArea(self):
        self.sendSimpleText("¿Qué producto estás buscando en el área " + self.text + "?")
    def notFound(self):
        self.sendSimpleText("Lo siento no encontré el producto " + self.text)
        self.buildArea()
        self.otherProduct()
        
    def otherProduct(self):
        self.sendTwoOptions("¿Quieres consultar otro producto? 🤔", "📦 Productos", "📑 Menú")
        
    # FUNCIONES DE DIRECCIÓN POR CIUDAD
    
    def addressForCity(self):
        self.sendSimpleText("En "+ self.text +" atendemos en: 👇🏻")
        
        if "La Paz" == self.text:
            address1 = "🏢 Calle Loayza # 349, local 3 (Frente a la facultad de Derecho UMSA)"
            address1 += "\n📲 72030101"
            address1 += "\n📌 https://maps.app.goo.gl/tNsAqrArK2NfGnM47"

            address2 = "🏢 Calle Zapata # 141 (frente Monoblock UMSA)"
            address2 += "\n📲 72030107"
            address2 += "\n📌 https://maps.app.goo.gl/vnP2W9hk2oJZMSwx5"

            address3 = "🏢 Calle 2 de obrajes entre Av. Hernando Siles y Av. 14 de Septiembre (Frente Universidad Catolica)"
            address3 += "\n📲 71545171"
            address3 += "\n📌 https://maps.app.goo.gl/Vvw4BjAnpP6MFnwa8"
            
            self.sendSimpleText(address1)
            self.sendSimpleText(address2)
            self.sendSimpleText(address3)            
            
        elif "El Alto" == self.text:
            address1 = "🏢 Av. Juan Pablo II Edif. EI Ceibo Local A-15 (Final Autopista casi esq. Rene Dorado)"
            address1 += "\n📲 72029023"
            address1 += "\n📌 https://maps.app.goo.gl/vTUrQCpyNQmC24hH6"

            address2 = "🏢 Avenida Satélite # 668 (Cerca al Banco Mercantil Santa Cruz)"
            address2 += "\n📲 71543980"
            address2 += "\n📌 https://maps.app.goo.gl/bagfMNGR4GSmpom9A"
            
            self.sendSimpleText(address1)
            self.sendSimpleText(address2)
        elif "Cochabamba" == self.text:
            address1 = "🏢 Calle Sucre # 882 (Casi esquina Oquendo)"
            address1 += "\n📲 72030102"
            address1 += "\n📌 https://maps.app.goo.gl/6MfeLnrtaiAk9p6y9"
            
            self.sendSimpleText(address1)
        elif "Santa Cruz" == self.text:
            address1 = "🏢 Avenida Centenario # 113 casi esquina Palermo (entre primer y segundo anillo)"
            address1 += "\n📲 72030103"
            address1 += "\n📌 https://maps.app.goo.gl/1xw1r9zfBwv1pQJK6"
            
            self.sendSimpleText(address1)
        elif "Tarija" == self.text:
            address1 = "🏢 Calle Alejandro del Carpio # 258 entre Suipacha y Méndez (Zona Las Panosas)"
            address1 += "\n📲 72030105"
            address1 += "\n📌 https://maps.app.goo.gl/rHxKVwKALUQev44QA"
            
            self.sendSimpleText(address1)
        elif "Sucre" == self.text:
            address1 = "🏢 Calle Regimiento Campos # 174 Esquina Ricardo Andrade (Frente a la Facultad Técnica)"
            address1 += "\n📲 72030104"
            address1 += "\n📌 https://maps.app.goo.gl/bcK8XhSmjCk9daXt7"
            
            self.sendSimpleText(address1)
        elif "Oruro" == self.text:
            address1 = "🏢 Calle Potosí # 5507 Esquina Montecinos (Diagonal al Col. Juan Misael Saracho)"
            address1 += "\n📲 72030106"
            address1 += "\n📌 https://maps.app.goo.gl/5ARt9qRxZoRzadc89"
            
            self.sendSimpleText(address1)
        elif "Potosí" == self.text:
            address1 = "🏢 Avenida Prado San Clemente # 29 entre las calles Camargo y 13 de Mayo"
            address1 += "\n📲 68868684"
            address1 += "\n📌 https://maps.app.goo.gl/mzG5tcuqNpD9NcLDA"
            
            self.sendSimpleText(address1)
        
        self.menuPreEnd()


    # FUNCIONES PARA VER LOS CATÁLOGOS
    def catalog(self):
        self.buildArea()
        self.menuPreEnd()
    


    # FUNCIONES DE ATECIÓN AL CLIENTE
    def customerSupport(self):
        if self.text == "🙋🏻‍♂️ Impresoras 3D" or type == "🙋🏻‍♂️ Máquinas láser":
            adviser = "Nuestro asesor Rodri te atenderá con gusto 😊"
            phone = "📲 68068883"
            self.sendSimpleText(adviser)
            self.sendSimpleText(phone)
            
            self.menuPreEnd()
        elif self.text == "🙋🏻‍♂️ Computadoras":
            adviser = "Nuestro asesor Iván te atenderá con gusto 😊"
            phone = "📲 74040348"
            self.sendSimpleText(adviser)
            self.sendSimpleText(phone)
            
            self.menuPreEnd()
        elif self.text == "🙋🏻‍♂️ Sublimación":
            adviser = "Nuestra asesora Mafer te atenderá con gusto 😊"
            phone = "📲 72507000"
            self.sendSimpleText(adviser)
            self.sendSimpleText(phone)
            
            self.menuPreEnd()
        elif self.text == "🙋🏻‍♂️ Atención general":
            self.sendMenuOptions("Bien, indícame de que ciudad me escribes... 👀", self.listCitySupport)
        
    def customerSupportByCity(self):
        
        if self.text == "➡️ La Paz":
            phone = "📲 72030101 'Loayza' \n📲 72030107 'Zapata' \n📲 71545171 'Obrajes' "
        elif self.text == "➡️ El Alto":
            phone = "📲 72029023 'Ceibo' \n📲 71543980 'Satélite' "
        elif self.text == "➡️ Cochabamba":
            phone = "📲 72030102"
        elif self.text == "➡️ Santa Cruz":
            phone = "📲 72030103"
        elif self.text == "➡️ Tarija":
            phone = "📲 72030105"
        elif self.text == "➡️ Sucre":
            phone = "📲 72030104"
        elif self.text == "➡️ Oruro":
            phone = "📲 72030106"
        elif self.text == "➡️ Potosí":
            phone = "📲 68868684"
        
        self.sendSimpleText("Nuestro asesor en la tienda de " + self.text + " te atenderá con gusto. 😊")
        self.sendSimpleText(phone)
        
        self.menuPreEnd()
        
    # FUNCIONES PARA ENVIAR MENSAJES
    
    
    def sendSimpleText(self, _message):
        textMessage = funcWhap.text_Message(self.number, _message)
        self.list.append(textMessage)
        # funcWhap.enviar_Mensaje_whatsapp(textMessage)
        
    def sendMenuOptions(self, message, multipleChoice):
        body = message
        options = multipleChoice
        listReplyData = funcWhap.listReply_Message(self.number, options, body, "", "sed2",self.messageId)
        self.list.append(listReplyData)
        
    def sendTwoOptions(self, message, optionOne, optionTwo):
        body = message
        options = [optionOne, optionTwo]
        replyButtonData = funcWhap.buttonReply_Message(self.number, options, body, "", "sed1", self.messageId)
        self.list.append(replyButtonData)
    
    def sendEmojiReactionMessage(self, emoji):
        replyReaction = funcWhap.replyReaction_Message(self.number, self.messageId, emoji)
        self.list.append(replyReaction)
            
    def sendSimpleButton(self, message, option):
        body = message
        options = [option]
        replyButtonData = funcWhap.buttonReply_Message(self.number, options, body, "", "sed1", self.messageId)
        self.list.append(replyButtonData)
        
    def sendUrl(self, url):
        replyData = funcWhap.document_Message(self.number, url, "Listo 👍🏻", "Inteligencia de Negocio.pdf")
        self.list.append(replyData)
    
    def sendContact(self, number):
        replyData = funcWhap.replyContact_Message(number)
        self.list.append(replyData)
        
    def start2(self):
        text = text.lower() #mensaje que envio el usuario
        list = []
        print("mensaje del usuario: ",text)

        markRead = funcWhap.markRead_Message(self.messageId)
        list.append(markRead)
        time.sleep(2)


        if "hola" in text:
            self.bienvenida()
            # body = "¡Hola! 👋 Bienvenido a Savin. ¿Cómo podemos ayudarte hoy?"
            # footer = "Savin Team"
            # options = ["✅ servicios", "📅 agendar cita"]

            # replyButtonData = funcWhap.buttonReply_Message(self.number, options, body, footer, "sed1",self.messageId)
            # replyReaction = funcWhap.replyReaction_Message(self.number, self.messageId, "🫡")
            # list.append(replyReaction)
            # list.append(replyButtonData)
        elif "servicios" in text:
            body = "Tenemos varias áreas de consulta para elegir. ¿Cuál de estos servicios te gustaría explorar?"
            footer = "Equipo Bigdateros"
            options = ["Analítica Avanzada", "Migración Cloud", "Inteligencia de Negocio"]

            listReplyData = funcWhap.listReply_Message(self.number, options, body, footer, "sed2",self.messageId)
            sticker = funcWhap.sticker_Message(self.number, funcWhap.get_media_id("perro_traje", "sticker"))

            list.append(listReplyData)
            list.append(sticker)
        elif "inteligencia de negocio" in text:
            body = "Buenísima elección. ¿Te gustaría que te enviara un documento PDF con una introducción a nuestros métodos de Inteligencia de Negocio?"
            footer = "Equipo Bigdateros"
            options = ["✅ Sí, envía el PDF.", "⛔ No, gracias"]

            replyButtonData = funcWhap.buttonReply_Message(self.number, options, body, footer, "sed3",self.messageId)
            list.append(replyButtonData)
        elif "sí, envía el pdf" in text:
            sticker = funcWhap.sticker_Message(self.number, funcWhap.get_media_id("pelfet", "sticker"))
            textMessage = funcWhap.text_Message(self.number,"Genial, por favor espera un momento.")

            funcWhap.enviar_Mensaje_whatsapp(sticker)
            funcWhap.enviar_Mensaje_whatsapp(textMessage)
            time.sleep(3)

            document = funcWhap.document_Message(self.number, sett.document_url, "Listo 👍🏻", "Inteligencia de Negocio.pdf")
            funcWhap.enviar_Mensaje_whatsapp(document)
            time.sleep(3)

            body = "¿Te gustaría programar una reunión con uno de nuestros especialistas para discutir estos servicios más a fondo?"
            footer = "Equipo Bigdateros"
            options = ["✅ Sí, agenda reunión", "No, gracias." ]

            replyButtonData = funcWhap.buttonReply_Message(self.number, options, body, footer, "sed4",self.messageId)
            list.append(replyButtonData)
        elif "sí, agenda reunión" in text :
            body = "Estupendo. Por favor, selecciona una fecha y hora para la reunión:"
            footer = "Equipo Bigdateros"
            options = ["📅 10: mañana 10:00 AM", "📅 7 de junio, 2:00 PM", "📅 8 de junio, 4:00 PM"]

            listReply = funcWhap.listReply_Message(self.number, options, body, footer, "sed5",self.messageId)
            list.append(listReply)
        elif "7 de junio, 2:00 pm" in text:
            body = "Excelente, has seleccionado la reunión para el 7 de junio a las 2:00 PM. Te enviaré un recordatorio un día antes. ¿Necesitas ayuda con algo más hoy?"
            footer = "Equipo Bigdateros"
            options = ["✅ Sí, por favor", "❌ No, gracias."]


            buttonReply = funcWhap.buttonReply_Message(self.number, options, body, footer, "sed6",self.messageId)
            list.append(buttonReply)
        elif "no, gracias." in text:
            textMessage = funcWhap.text_Message(self.number,"Perfecto! No dudes en contactarnos si tienes más preguntas. Recuerda que también ofrecemos material gratuito para la comunidad. ¡Hasta luego! 😊")
            list.append(textMessage)
        else :
            data = funcWhap.text_Message(self.number,"Lo siento, no entendí lo que dijiste. ¿Quieres que te ayude con alguna de estas opciones?")
            list.append(data)

 
