
def coin_converter(value, original_coin, destination_coin, taxes):

    if original_coin not in taxes or destination_coin not in taxes:
        raise ValueError("Coin not supported!")
    
    value_in_euro = value / taxes[original_coin]
    converted_value = value_in_euro * taxes[destination_coin]

    return converted_value 

