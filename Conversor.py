import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["info"]["rate"]
        converted = amount * rate
        print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    else:
        print("Erro ao buscar taxas de câmbio.")

def main():
    print("Conversor de Moedas")
    amount = float(input("Digite o valor: "))
    from_currency = input("De (código da moeda, ex: USD): ").upper()
    to_currency = input("Para (código da moeda, ex: EUR): ").upper()
    convert_currency(amount, from_currency, to_currency)

if __name__ == "__main__":
    main()
