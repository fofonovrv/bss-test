import requests

def get_weather() -> None:
	headers = {'content-type' : 'application/json'}
	target_url = 'https://api.weatherbit.io/v2.0/current'
	params = {
		'key': 'ed6dfd8dfa334a6b869c3eb3be0e30de',
		'lang': 'ru',
		'units': 'M',
		'city': 'Москва',
	}
	try:
		response = requests.get(url=target_url, headers=headers, params=params)
		data = response.json()['data'][0]
		print(f'''
Город: {data['city_name']}
Температура: {data['temp']}
Ветер: {data['wind_spd']}, {data['wind_cdir_full']}
{data['weather']['description']}
		''')
	except requests.exceptions.ConnectionError as ex:
		print(f"Не удалось получить ответ от {target_url}: {ex}")
	except Exception as ex:
		print(f"Ошибка: {ex}")
	


if __name__ == "__main__":
	get_weather()