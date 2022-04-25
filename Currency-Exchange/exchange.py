def exchange_money(budget, exchange_rate):
    """
 
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate
# exchange_money()'s outputs
money = exchange_money(127.5, 1.2)
print(f'Exchange money is {money}')

def get_change(budget, exchanging_value):
    """
 
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value

# get_change()'s outputs
money = get_change(127.5, 120)
print(f'Your change is {money}')

def get_value_of_bills(denomination, number_of_bills):
    """
 
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return denomination * number_of_bills

# get_value_of_bills()'s outputs
value = get_value_of_bills(5, 128)
print(f'Your value of bills is {value}')

def get_number_of_bills(budget, denomination):
    """
 
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget / denomination)

# get_number_of_bills()'s outputs
bills = get_number_of_bills(127.5, 5)
print(f'Your number of bills is {bills}')

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
 
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    actual_rate = (exchange_rate * (spread / 100)) + exchange_rate
    new_currency = budget / actual_rate
    exchanged_number = new_currency / denomination
    max_value = int(exchanged_number) * denomination
    return max_value

# exchangeable_value()'s outputs
exchangeable = exchangeable_value(127.25, 1.20, 10, 20)
print(f'Your exchangeable value is {exchangeable}')

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
 
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    actual_rate = (exchange_rate * (spread / 100)) + exchange_rate
    new_currency = budget / actual_rate
    exchanged_number = new_currency / denomination
    max_value = int(exchanged_number) * denomination
    return int(new_currency - max_value)

# non_exchangeable_value()'s outputs
non_exchangeable = non_exchangeable_value(127.25, 1.20, 10, 20)
print(f'Your non exchangeable value is {non_exchangeable}')