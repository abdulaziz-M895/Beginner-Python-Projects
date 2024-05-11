# السلام عليكم
# I couldn't use the API that E.Ahmed used so I used another one. hope this doesn't make a problem
import requests

response_rates = requests.get(f'https://v6.exchangerate-api.com/v6/fd747e3bd2a67f8afbc5c13d/latest/USD')
data_rates = response_rates.json()

currencies = data_rates['conversion_rates'].keys()

while True:
  while True:
    from_currency = input('From: ').upper()
    if from_currency in currencies:
      break
    else:
      print('This Currency is not Supported or The Three Letter Currency Code is not Correct')

  while True:
    to_currency = input('To: ').upper()
    if to_currency in currencies:
      break
    else:
      print('This Currency is not Supported or The Three Letter Currency Code is not Correct')

  while True:
    try:
      from_amount = float(input('Amount: '))
      if from_amount <= 0.0:
        raise ValueError()
      break
    except ValueError:
      print('Please Enter a Valid Number that is Greater than Zero')

  response_conv = requests.get(f'https://v6.exchangerate-api.com/v6/fd747e3bd2a67f8afbc5c13d/pair/{from_currency}/{to_currency}/{from_amount}')
  data_conv = response_conv.json()

  if response_conv.status_code == 200:
    print(f'{from_amount} {from_currency} is equal to {data_conv['conversion_result']} {to_currency} and the conversion rate is {data_conv['conversion_rate']}')
    exit()
  else:
    print(f'There Was an Error Please Try Again (response code: {response_conv.status_code})')