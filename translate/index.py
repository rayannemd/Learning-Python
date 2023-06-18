import requests

url = "https://text-translator2.p.rapidapi.com/translate"

payload = {
	"source_language": "pt",
	"target_language": "en",
	"text": "Insira o texto para ser traduzido: "
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "13a3b399b4msh4336ef5ea54cff8p1dcb39jsn34523ec0dcc4",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())