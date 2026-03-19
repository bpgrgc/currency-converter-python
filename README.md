# 💱 Currency Converter CLI by bpgrgc

A robust and user-friendly Command Line Interface (CLI) tool to check real-time exchange rates and convert currencies using the [ExchangeRate-API](https://www.exchangerate-api.com/).

## 🚀 Features
- **Real-time Conversion:** Fetches the latest market data directly via API.

- **Advanced Error Handling:** - Validates currency codes (3 letters, alphabetic check).
  - Catches invalid numeric inputs (prevents `ValueError`).
  - Displays specific API errors like `invalid-key` or `unsupported-code`.
  - Handles network connection issues gracefully.

- **Interactive UI:** Simple prompts with a quick `QUIT` command to exit.

## 🛠️ Setup & Usage
1. **Clone the repository:**
   `git clone https://github.com/bpgrgc/currency-converter-python.git`
2. **Install requirements:**
   `pip install requests`
3. **Run the script:**
   `python currency_converter.py`

When prompted, enter your **API Key**, specify the **Base Currency** (e.g., USD), the **Target Currency** (e.g., TRY), and the **Amount**. The script will handle the rest!

## 🛡️ Error Handling in Action
The script is designed to be "crash-proof". If you enter a string instead of a number for the amount, or if you provide an invalid currency code, the program will catch the error, notify you, and allow you to try again without closing.

## 📝 License
Distributed under the MIT License.
