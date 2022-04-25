""" Meltdown Mitigation exercise """
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
 
    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not
 
    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
#is_criticality_balanced()'s outputs
answer = is_criticality_balanced(750, 600)
print(f'The criticality conditions are met? {answer}')

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.
 
    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'
 
    Efficiency can be grouped into 4 bands:
 
    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.
 
    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    efficiency = voltage * current / theoretical_max_power
    if efficiency >= 0.8:
        return 'green'
    if 0.6 <= efficiency < 0.8:
        return 'orange'
    if 0.3 <= efficiency < 0.6:
        return 'red'
    return 'black'
#reactor_efficiency()'s outputs
colour = reactor_efficiency(200,50,15000)
print(f'the efficiency band of the reactor : {colour}')

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.
 
    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'
 
    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    ratio_product_threshold = temperature * neutrons_produced_per_second / threshold
    if ratio_product_threshold < 0.9:
        return 'LOW'
    if 0.9 <= ratio_product_threshold < 1.1:
        return 'NORMAL'
    return 'DANGER'

#fail_safe()'s outputs
status = fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
print(f'status for the reactor : {status}')