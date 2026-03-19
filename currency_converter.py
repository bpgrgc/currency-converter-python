# Author: bpgrgc
# License: MIT
# Description: Real-time currency converter using ExchangeRate-API

# Licensed under the MIT License. See LICENSE file in the project root for full license information.


print("Exchange Rates by bpgrgc".center(50, "-"))
print("Powered by: exchangerate-api.com".center(50))

import requests
import json

apiKey= input("Enter your API key, which you can easily get from exchangerate-api.com: ")
if apiKey == "":
    print("No API key entered. Exiting the program.")
    exit()

apiUrl = (f"https://v6.exchangerate-api.com/v6/{apiKey}/latest/")

print("\nTo quit: Type quit as the base currency type.\n")
while True:
    try:
        # 1 - Base currency input and validation
        baseCurrency = input("Base currency to convert: ").upper() # Currency to be converted (e.g., USD, EUR, TRY)
        if baseCurrency == "QUIT":
            print("Exiting the program. Goodbye!")
            break
    
        if len(baseCurrency) != 3 or baseCurrency.isalpha() == False:
            raise ValueError("Invalid currency code. Currency codes must be 3 letters long.")
        
        # 2 - Target currency input and validation
        targetCurrency = input("Target currency: ").upper()
        if len(targetCurrency) != 3 or targetCurrency.isalpha() == False:
            raise ValueError("Invalid currency code. Currency codes must be 3 letters long.")
        
        # 3 - Amount input and validation
        amount = float(input(f"How much {baseCurrency} do you want to exchange for {targetCurrency}?: "))
        if amount <= 0 or amount > 1000000:
            raise ValueError("Amount must be a positive number and a whole number less than or equal to 1,000,000.")
        
        # 4 - API request and response handling
        result = requests.get(apiUrl+baseCurrency)
        result_json = json.loads(result.text)

        if result_json["result"] == "error":
            print("API Error:", result_json["error-type"])
            exit()

        # 5 - Currency conversion and output
        convertedAmount = (result_json["conversion_rates"][targetCurrency] * amount)
        print("{0} {1} = {2} {3}".format(amount, baseCurrency, convertedAmount, targetCurrency))

        # 6 - Exception handling for invalid inputs and API errors
    except ValueError as ve:
        print("Error:", ve)
        continue
    except KeyError:
        print("Error: Invalid currency code. Please enter a valid 3-letter currency code.")
        continue
    except requests.exceptions.RequestException:
        print("Network error. Check your connection.")
        exit()
