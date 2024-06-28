import requests
import os
import json
from dotenv import load_dotenv
from requests.structures import CaseInsensitiveDict

load_dotenv()

url = " https://graph.facebook.com/v19.0/115394881465051/messages"

headers = CaseInsensitiveDict()

headers["Authorization"] = "Bearer " + os.getenv('TOKEN_ACCESS')
headers["Content-Type"] = "application/json"

# Função para enviar mensagem de alerta de temperatura de sensor monitorado
# Function to send temperature alert message from monitored sensor
def sendRequestAlert(phone, sensor, temperatura):
   
    data = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "pt_BR"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": sensor
                        },
                        {
                            "type": "text",
                            "text": f"{temperatura} C"
                        }
                    ]
                }
            ]
        }
    }


    data_json = json.dumps(data)
    
    resp = requests.post(url, headers=headers, data=data_json)
    print(resp)

# Função para enviar mensagem de alerta de bateria de sensor monitorado
# Function to send battery alert message from monitored sensor
def sendRequestBattery(phone, sensor, bateria):
   
    data = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "template",
        "template": {
            # name of the template to be used (previously created in the Facebook Business Manager)
            "name": "bateria",
            "language": {
                "code": "pt_BR"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": sensor
                        },
                        {
                            "type": "text",
                            "text": bateria
                        }
                    ]
                }
            ]
        }
    }

    data_json = json.dumps(data)    
    resp = requests.post(url, headers=headers, data=data_json)
    print(resp)

# Função para enviar mensagem de teste
# Function to send test message
def sendBasicMessage(phone):

    data = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            },
        }
    }

    data_json = json.dumps(data)
    resp = requests.post(url, headers=headers, data=data_json)
    print(resp)

# Exemplo de uso
sendBasicMessage(os.getenv('PHONE_NUMBER'))