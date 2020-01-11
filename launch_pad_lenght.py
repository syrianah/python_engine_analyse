# http://rakiety.org.pl/forum/viewtopic.php?t=2120

exit_velocity = 13

rocket_velocity = 343
rocket_mass = 3.5       # masa startowa rakiety

grain_mass = 0.6        # masa paliwa
burn_time = 1.2

acceleration = (grain_mass * rocket_velocity) / (rocket_mass * burn_time)

launch_pad_lenght = exit_velocity**2 / (2 * acceleration)

print(launch_pad_lenght)
