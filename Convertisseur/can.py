from math import *
from bindec import *



def convertisseur_can(voltage, resolution_bits, input_voltage_range=(0,5), convertion = 0):
    # Calculer la plage de tension Scc
    min_input_voltage , max_input_voltage = input_voltage_range
    Scc = max_input_voltage

    # Tension d'entrée
    Ve = voltage

    # Calculer la valeur de chaque bit delta ou quantum ou bit_value 
    delta = Scc / (2**resolution_bits)

    # Calculer la valeur numérique N
    if convertion == 0:
        digital_value = floor((Ve - min_input_voltage) / delta)
    else:
        digital_value = ceil((Ve - min_input_voltage) / delta)

    
    return digital_value

   

# Exemple d'utilisation

# Scc = 5
# nbreBits = 10
# convert = 1
# Ve = 3.43  # Tension analogique d'entrée à convertir Ve
# digital_value = convertisseur_can(Ve, nbreBits, input_voltage_range=(0,Scc),convertion=convert)
# print("Valeur numérique :", digital_value)
# print("Valeur binaire :", dectobin(digital_value))








# def convertisseur_can(voltage, resolution_bits=12, input_voltage_range=(0, 5)):
#     # Calculer la plage de tension Scc
#     min_voltage, max_voltage = input_voltage_range
#     voltage_range = max_voltage - min_voltage

#     # Calculer la valeur de chaque bit delta ou quantum 
#     bit_value = voltage_range / (2**resolution_bits)

#     # Calculer la valeur numérique N
#     digital_value = int((voltage - min_voltage) / bit_value)

#     return digital_value

# # Exemple d'utilisation
# voltage = 5  # Tension analogique d'entrée à convertir Ve
# nbreBits = 10
# digital_value = convertisseur_can(voltage, nbreBits)
# print("Valeur numérique :", digital_value)