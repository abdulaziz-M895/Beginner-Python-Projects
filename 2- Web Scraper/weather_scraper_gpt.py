from bs4 import BeautifulSoup
import requests

# Dictionary mapping governorates to their URLs
governorate_urls = {
  'cairo': 'https://weather.com/weather/today/l/21f7c3bea9c3049f9df8e31a25feb5cd81303c461d762d0708b97570bfb7e82b?unit=m',
  'new valley': 'https://weather.com/weather/today/l/ea3d942b2141e4b888fcb75f0e4a1760674e0bb6c6ee9ace9e91b4a682e7692d?unit=m',
  'matruh': 'https://weather.com/weather/today/l/27dbb5c69cf66dc4e3b1d0d20bcb61aa0bf75928c47cdbda21ad28f82e1f69c5?unit=m',
  'red sea': 'https://weather.com/weather/today/l/a2fc8b63b302d7a4bb67efa32e91c4097991354de79ba2657df1f872b549cb51?unit=m',
  'giza': 'https://weather.com/weather/today/l/3416b3a88a2c8d9f77bcb34e485f931b9ee9ef4718522f3eb6b79e1e0b070437?unit=m',
  'sinai': 'https://weather.com/weather/today/l/a2fc8b63b302d7a4bb67efa32e91c4097991354de79ba2657df1f872b549cb51?unit=m',
  'suez': 'https://weather.com/weather/today/l/373ee1a7d17edf6b74ed2b6e10d6f79acb439b0839b3d5623f651483ce05cf9c?unit=m',
  'beheira': 'https://weather.com/weather/today/l/e01555e78fc8a386c5b838d26fd8e8d51ea21657cf24b63a54dd09c017cc33e7?unit=m',
  'helwan': 'https://weather.com/weather/today/l/74d52db826215d934074a054f19a82141a5850a9ed542ab72a7f60bf8a71e716?unit=m',
  'sharqia': 'https://weather.com/weather/today/l/a2fc8b63b302d7a4bb67efa32e91c4097991354de79ba2657df1f872b549cb51?unit=m',
  'alexandria': 'https://weather.com/weather/today/l/bd5efd8d02dacf517fc96f085874156696b5a0b6eabe0651a0840b6a395857e4?unit=m',
  'dakahlia': 'https://weather.com/weather/today/l/a2fc8b63b302d7a4bb67efa32e91c4097991354de79ba2657df1f872b549cb51?unit=m',
  'kafr el-sheikh': 'https://weather.com/weather/today/l/39b6f05ad18a4555985fab64983c338a91ac586fd94ac06fa653f59e0c0e2ae3?unit=m',
  'monufia': 'https://weather.com/weather/today/l/a2fc8b63b302d7a4bb67efa32e91c4097991354de79ba2657df1f872b549cb51?unit=m',
  'minya': 'https://weather.com/weather/today/l/9e9dde032744743355b6251f57e5403a136503bdbea68e523ffd6ea864355b0f?unit=m',
  'gharbia': 'https://weather.com/weather/today/l/a2fc8b63b302d7a4bb67efa32e91c4097991354de79ba2657df1f872b549cb51?unit=m',
  'faiyum': 'https://weather.com/weather/today/l/922ef69883e1d9d1e003ddde053638c68a29eef5d6e119056d60418bb68062c4?unit=m',
  'ismailia': 'https://weather.com/weather/today/l/69c1980a0d9fd436c1ccffb35e6902fc37d22fca002a1e501cbc1545e824f422?unit=m',
  'qena': 'https://weather.com/weather/today/l/f84f580410cba2034a01fdb4341d18f92ec1a1132da59e9f60dd554f19cabc04?unit=m',
  'asyut': 'https://weather.com/weather/today/l/e7a2c19776498bef0c7c1c11ee53a93db1c9d140e8079d3edbd18e258a3eac5e?unit=m',
  'sohag': 'https://weather.com/weather/today/l/5e31ab27cb0d41cea94c9959014429f5fd1eb4ba01471c189ac8d4f518026b4c?unit=m',
  'beni suef': 'https://weather.com/weather/today/l/28b675c7c35e02270c5eb364640b04e2a17b6fb2f9b71dc0bda13cf31b630f84?unit=m',
  'qalyubia': 'https://weather.com/weather/today/l/a2fc8b63b302d7a4bb67efa32e91c4097991354de79ba2657df1f872b549cb51?unit=m',
  'aswan': 'https://weather.com/weather/today/l/cfc848e46b498a85a2123baa3278db56582b79bd1caff6a7295b8e8bca2ed69a?unit=m',
  'damietta': 'https://weather.com/weather/today/l/b9c161a572b82af776cc9c52b684ccd08bcc9934ceef0c3beb47251defef32f1?unit=m',
  'port said': 'https://weather.com/weather/today/l/68774abb034e7cee3fdfb75082a460da35fd0ccab661416a16cffc807f79a5e6?unit=m',
  'luxor': 'https://weather.com/weather/today/l/8196fa6f0b40937648b73058cd821ac4a47c5e3b1b6deb35b0668e2e80e44151?unit=m',
  '6th of october': 'https://weather.com/weather/today/l/1a9aad9ac91d9fddd2c1668148334d8bbb8e27f7b6b0b0d8ed76135bc0718bf8?unit=m'
}

while True:
  governorate = input('The Governorate: ').lower()
  if governorate in governorate_urls:
    break
  else:
    print(f'Please Select one of the Egyptian governorates: {", ".join(governorate_urls.keys())}')

url = governorate_urls[governorate]

request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
temp = soup.find('span', {'data-testid': 'TemperatureValue'}).text

print(f'The temperature in {governorate.capitalize()}, Egypt is {temp}C')