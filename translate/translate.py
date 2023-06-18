import http.client

conn = http.client.HTTPSConnection("text-translator2.p.rapidapi.com")

payload = "source_language=pt&target_language=en&text=Insira%20o%20texto%20para%20ser%20traduzido%3A%20"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Key': "13a3b399b4msh4336ef5ea54cff8p1dcb39jsn34523ec0dcc4",
    'X-RapidAPI-Host': "text-translator2.p.rapidapi.com"
}

conn.request("POST", "/translate", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))