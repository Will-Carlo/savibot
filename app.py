from flask import Flask, request
from chatbot import ChatBot
import sett 
import funcWhap


app = Flask(__name__)

@app.route('/bienvenido', methods=['GET'])
def  bienvenido():
    return 'Hola mundo.'

@app.route('/webhook', methods=['GET'])
def verificar_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == sett.token and challenge != None:
            return challenge
        else:
            return 'token incorrecto', 403
    except Exception as e:
        return e,403
    
@app.route('/webhook', methods=['POST'])
def recibir_mensajes():

    try:
        body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['messages'][0]
        number = funcWhap.replace_start(message['from'])
        messageId = message['id']
        contacts = value['contacts'][0]
        name = contacts['profile']['name']
        text = funcWhap.obtener_Mensaje_whatsapp(message)
        print(text, number, messageId, name)
        # funcWhap.administrar_chatbot(text, number,messageId,name)
    
        mi_bot = ChatBot(text, number, messageId, name)
        mi_bot.start()
        
        return 'enviado'

    except Exception as e:
        return 'no enviado ' + str(e)

if __name__ == '__main__':
    app.run()
