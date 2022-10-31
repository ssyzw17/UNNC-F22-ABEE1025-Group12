from parametric_simulation import run_one_parameter_parametric
from post_processor import plot_1D_results

idf_path = './1ZoneUncontrolled_win_test.idf'
eplus_run_path = './energyplus9.5/energyplus'
parameter_vals=[0.25,0.27,0.29,0.31,0.33,0.35,0.37,0.39,0.41,0.43,0.45,0.47,0.49,0.51,0.53,0.55,0.57,0.59,0.61,0.63,0.65,0.67,0.69,0.71,0.73,0.75]
parameter_key = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient'] 

out_directory = './param_exp_1'

plot_column_name='ZONE ONE:Zone Mean Air Temperature [C](TimeStep) '
y_axis_title='Indoor Air Temperature (C)'
plot_title=' Simulation of Indoor Air Temperature vs. SHGC'

d=run_one_parameter_parametric(eplus_run_path,idf_path,out_directory,parameter_key,parameter_vals)

plot_1D_results(d,plot_column_name,y_axis_title,plot_title)