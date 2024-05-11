import requests

API_KEY = 'fd747e3bd2a67f8afbc5c13d'

# Function to fetch supported currencies from the API
def get_supported_currencies():
  # Fetching data from the API
  response = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD')
  # If the request was successful (status code 200)
  if response.status_code == 200:
      # Extracting data from the response in JSON format
      data = response.json()
      # Extracting currency keys from the JSON data
      return data.get('conversion_rates').keys()
  # If there was an error in fetching data
  else:
      # Raise an exception with an error message
      raise Exception(f"Failed to fetch supported currencies. Status code: {response.status_code}")

# Function to get conversion rate between two currencies
def get_conversion_rate(from_currency, to_currency, amount):
  # Fetching data from the API
  response = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}')
  # If the request was successful (status code 200)
  if response.status_code == 200:
      # Extracting data from the response in JSON format
      data = response.json()
      # Extracting conversion result and rate from the JSON data
      return data.get('conversion_result'), data.get('conversion_rate')
  # If there was an error in fetching data
  else:
      # Raise an exception with an error message
      raise Exception(f"Failed to get conversion rate. Status code: {response.status_code}")

# Main function to run the currency conversion program
def main():
  # Fetching supported currencies from the API
  currencies = get_supported_currencies()

  # Asking the user for input until a valid currency code is entered
  while True:
      from_currency = input('From: ').upper()
      if from_currency in currencies:
          break
      else:
          print('This currency is not supported or the three-letter currency code is not correct')

  # Asking the user for input until a valid currency code is entered
  while True:
      to_currency = input('To: ').upper()
      if to_currency in currencies:
          break
      else:
          print('This currency is not supported or the three-letter currency code is not correct')

  # Asking the user for input until a valid amount is entered
  while True:
      try:
          from_amount = float(input('Amount: '))
          if from_amount <= 0.0:
              raise ValueError()
          break
      except ValueError:
          print('Please enter a valid number that is greater than zero')

  try:
      # Getting conversion result and rate
      conversion_result, conversion_rate = get_conversion_rate(from_currency, to_currency, from_amount)
      # Printing the conversion result and rate
      print(f'{from_amount} {from_currency} is equal to {conversion_result} {to_currency} and the conversion rate is {conversion_rate}')
  except Exception as e:
      # Handling errors and printing an error message
      print(f'There was an error: {str(e)}')

# Entry point of the program
if __name__ == "__main__":
  main()