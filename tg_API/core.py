import requests

url = "https://numbersapi.p.rapidapi.com/1729/math"

querystring = {"fragment":"true","json":"true"}

headers = {
	"X-RapidAPI-Key": "8cfc4c02bcmsh01167662013ce43p132b4bjsn2c2e2d396a36",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())