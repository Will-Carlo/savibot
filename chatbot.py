import sett
import time
import funcWhap

class chatbot:
    
    list = []
    
    def __init__(self, _text, _number, _messageId, _name):
        self.text = _text
        self.number = _number
        self.messageId = _messageId
        self.name = _name

    # Getters y Setters
    def get_text(self):
        return self.text
    def set_text(self, _text):
        self.text = _text
    def get_number(self):
        return self.number
    def set_number(self, _number):
        self.number = _number
    def get_messageId(self):
        return self.messageId
    def set_messageId(self, _messageId):
        self._messageId = _messageId
    def get_name(self):
        return self.name
    def set_name(self, _name):
        self.name = _name

    def start(self):
        text = text.lower() #mensaje que envio el usuario
        list = []
        print("mensaje del usuario: ",text)

        markRead = funcWhap.markRead_Message(self.messageId)
        list.append(markRead)
        time.sleep(2)


        if "hola" in text:
            # self.sendSimpleText("¡Hola! soy SaviBot 😃")
            body = "¡Hola! 👋 Bienvenido a Savin. ¿Cómo podemos ayudarte hoy?"
            footer = "Savin Team"
            options = ["✅ servicios", "📅 agendar cita"]

            replyButtonData = funcWhap.buttonReply_Message(self.number, options, body, footer, "sed1",self.messageId)
            replyReaction = funcWhap.replyReaction_Message(self.number, self.messageId, "🫡")
            list.append(replyReaction)
            list.append(replyButtonData)
            
        for item in list:
            funcWhap.enviar_Mensaje_whatsapp(item)

    def bienvenida(self):
            self.sendSimpleText("¡Hola! soy SaviBot 😃")
            self.sendSimpleText("Tú asistente virtual")
            
            body = "¡Hola! soy SaviBot 😃"
            footer = "Savin Team"
            options = ["✅ servicios", "📅 agendar cita"]

            replyReaction = funcWhap.replyReaction_Message(self.number, self.messageId, "🫡")
            replyButtonData = funcWhap.buttonReply_Message(self.number, options, body, footer, "sed1",self.messageId)
            list.append(replyReaction)
            list.append(replyButtonData)
    
    def sendSimpleText(self, _message):
        textMessage = funcWhap.text_Message(self.number, _message)
        funcWhap.enviar_Mensaje_whatsapp(textMessage)
        
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

        for item in list:
            funcWhap.enviar_Mensaje_whatsapp(item)
