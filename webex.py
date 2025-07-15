import requests


access_token = 'MWNmY2U4ZjUtMzhhZi00ODdmLWIxMDMtNDQyMWJkY2QwN2E1ODg5Mjk3ZTctM2Zh_P0A1_e5840657-a59b-4c71-a507-6ac685cd8fcf'
room_id = 'e5840657-a59b-4c71-a507-6ac685cd8fcf'
mensaje = 'QUE CHSM EL AMERICA'

url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
data = {
    'roomId': room_id,
    'text': mensaje
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Mensaje enviado con éxito.")
else:
    print(f"Error al enviar mensaje: {response.status_code}\n{response.text}")
