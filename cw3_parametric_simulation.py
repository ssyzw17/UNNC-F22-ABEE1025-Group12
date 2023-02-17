
#Author:Ziyu Wang,Su Li
#Date:2023-2-13

import json
import os
from StaticEplusEngine import run_eplus_model, convert_json_idf

def run_two_parameter_simulation_helper(eplus_run_path, idf_path, output_dir, parameter_key_a, parameter_val_a,
                                        parameter_key_b, parameter_val_b):
    # convert idf to a JSON dict
    convert_json_idf(eplus_run_path, idf_path)
    eplus_json_path = idf_path.split('.idf')[0] + '.epJSON'
    with open(eplus_json_path) as eplus_JSON:
        eplus_json_dict = json.load(eplus_JSON)

    # change the dict json val
    inner_dict = eplus_json_dict
    for i in range(len(parameter_key_a)):
        if i < len(parameter_key_a) - 1:
            inner_dict = inner_dict[parameter_key_a[i]]
    inner_dict[parameter_key_a[-1]] = parameter_val_a
    for j in range(len(parameter_key_b)):
        if j < len(parameter_key_b) - 1:
            inner_dict = inner_dict[parameter_key_b[j]]
    inner_dict[parameter_key_b[-1]] = parameter_val_b

    # put the JSON dict into idf
    with open(eplus_json_path, 'w') as epjson:
        json.dump(eplus_json_dict, epjson)
    convert_json_idf(eplus_run_path, eplus_json_path)

    # run simulation
    run_eplus_model(eplus_run_path, idf_path, output_dir)
    return output_dir


def run_two_parameter_simulation(eplus_run_path, idf_path, output_dir, parameter_key_a, parameter_val_a,
                                 parameter_key_b, parameter_val_b):
    output = {}
    os.makedirs(output_dir)
    for i in range(len(parameter_val_a)):
        for j in range(len(parameter_val_b)):
            name = str(parameter_val_a[i]) + '_' + str(parameter_val_b[j])
            output_path = output_dir + os.sep + name
            run_two_parameter_simulation_helper(eplus_run_path, idf_path, output_path, parameter_key_a, parameter_val_a[i],
                                                parameter_key_b, parameter_val_b[j])
            output[name] = output_path + os.sep + 'eplusout.csv'
    return output
