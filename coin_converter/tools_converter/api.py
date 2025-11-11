
import requests

def obtain_taxes(api_key, base_coin="EUR"):

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_coin}"

    try:
        result = requests.get(url)
        
        if result.status_code != 200:
            raise Exception(f"Error on the API response: (status {result.status_code})")
        
        data = result.json()

        if data.get("result") != "success":
            raise Exception(f"Error on the API response: the result wasn't success")
        
        return data.get("conversion_rates", {})
    
    except requests.RequestException as e:
        raise Exception(f"Connection error with API: {e}")