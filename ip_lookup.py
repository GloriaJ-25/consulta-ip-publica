import requests
import json

resultados = []

print("Ingresa una IP pública para obtener información. Escribe 'exit' para salir.")

while True:
    ip = input("IP pública: ").strip()
    
    if ip.lower() == 'exit':
        break

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            info = {
                "IP": ip,
                "País": data.get("country", "Desconocido"),
                "Región": data.get("regionName", "Desconocido"),
                "ISP": data.get("isp", "Desconocido"),
                "Coordenadas": {
                    "Latitud": data.get("lat", 0),
                    "Longitud": data.get("lon", 0)
                }
            }
            print(json.dumps(info, indent=4, ensure_ascii=False))
            resultados.append(info)
        else:
            print(f"Error: {data.get('message', 'No se pudo obtener información')}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

with open("resultados_ips.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, indent=4, ensure_ascii=False)

print("Resultados guardados en 'resultados_ips.json'.")



