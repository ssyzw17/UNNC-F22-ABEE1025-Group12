
#Author:Ziyu Wang,Su Li
#Date:2023-2-16

from two_para_simulation import TwoParaSimulation

eplus_run_path = './EnergyPlus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_test.idf'
out_put_dir = './simulation_output'
para_keys_a = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient']
para_keys_b = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'u_factor']
val_start_a = 0.25
val_end_a = 0.75
val_start_b = 1.0
val_end_b = 2.5
interval = 0.02

#  Initialize an TwoParaSimulation
simulation = TwoParaSimulation(eplus_run_path, idf_path, out_put_dir)
simulation.val_end_a = val_end_a
simulation.val_start_a = val_start_a
simulation.val_start_b = val_start_b
simulation.val_end_b = val_end_b
simulation.interval = interval
simulation.para_key_a = para_keys_a
simulation.para_key_b = para_keys_b

# run two parameter simulation
result = simulation.run_two_para_simulation()
simulation.result_value = max(result, key=result.get)
simulation.highest_value = result[max(result, key=result.get)]
result = result.split('_')
print(result)
print(para_keys_a[2]+"value:"+result[0]+"     "+para_keys_b[2]+"value:"+result[1])
