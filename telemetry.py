import json

thrust_sum = 0  # suma pomiarów ciągu
mesure_num = 0  # liczba pomiarów
burn_time = 0

with open('pomiary/read.json') as f:
    file = json.load(f)
    for data in file:
        thrust_sum = thrust_sum + data['thrust']
        mesure_num = mesure_num + 1

burn_time = (file[len(file)-1]['time'] - file[0]['time']) * 1000
#print(file[0]['time'], file[len(file)-1]['time'])

mass = 2
burn_time = 1.43
# avr_thurst = (thrust_sum / mesure_num) * 10  # średni ciąg
impuls = 1047.09  # avr_thurst * burn_time  # impuls całkowity
rocket_velocity = impuls / mass  # prędkość rakiety
rocket_altitude = rocket_velocity**2 / (mass*9.81)  # wysokość lotu rakiety

# print("Średni ciąg = " + str(avr_thurst))
print("Impuls całkowity = " + str(impuls))
print("Prędkość rakiety = " + str(rocket_velocity))
print("Wysokość lotu rakiety = " + str(rocket_altitude))
print("Czas spalania = " + str(burn_time))


# with open("obliczenia/test_KAL_45", "w") as f:
#     f.write("Średni ciąg = " + str(avr_thurst) + "\n")
#     f.write("Impuls całkowity = " + str(impuls) + "\n")
#     f.write("Prędkość rakiety = " + str(rocket_velocity) + "\n")
#     f.write("Wysokość lotu rakiety = " + str(rocket_altitude))
