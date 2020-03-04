import csv

input_path = "test-29-02-2020/ScaledData.csv"

thrust_sum = 0  # suma pomiarów ciągu
mesure_num = 0  # liczba pomiarów
burn_time = 0


with open(input_path) as f:
    data = csv.reader(f)
    for sample in data:
        thrust_sum = thrust_sum + float(sample[2])
        mesure_num = mesure_num + 1

# burn_time = (file[len(file)-1]['time'] - file[0]['time']) * 1000
#print(file[0]['time'], file[len(file)-1]['time'])

mass = 3
burn_time = 1.4
avr_thurst = (thrust_sum / mesure_num) * 10  # średni ciąg
impuls = avr_thurst * burn_time  # impuls całkowity
rocket_velocity = impuls / mass  # prędkość rakiety
rocket_altitude = rocket_velocity**2 / (mass*9.81)  # wysokość lotu rakiety

print("Średni ciąg = [N] " + str(avr_thurst))
print("Impuls całkowity [Ns] = " + str(impuls))
print("Prędkość rakiety [m/s] = " + str(rocket_velocity))
print("Liczba macha = ", str(rocket_velocity * 0.00291545))
print("Wysokość lotu rakiety [m] = " + str(rocket_altitude))
print("Czas spalania [s] = " + str(burn_time))


# with open("obliczenia/test_KAL_45", "w") as f:
#     f.write("Średni ciąg = " + str(avr_thurst) + "\n")
#     f.write("Impuls całkowity = " + str(impuls) + "\n")
#     f.write("Prędkość rakiety [m/s] = " + str(rocket_velocity) + "\n")
#     f.write("Wysokość lotu rakiety [m] = " + str(rocket_altitude))
