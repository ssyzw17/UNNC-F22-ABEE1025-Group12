#Author:Ziyu Wang,Su Li
#Date:2023-2-14

import pandas as pd
from cw3_parametric_simulation import run_two_parameter_simulation


class TwoParaSimulation():
    def __init__(self, eplus_run_path, idf_path, out_put_dir):
        self.plot_column_name = 'ZONE ONE:Zone Mean Air Temperature [C](TimeStep) '
        self.eplus_run_path = eplus_run_path
        self.idf_path = idf_path
        self.out_put_dir = out_put_dir
        self.interval = 0.02
        self.val_start_a = None
        self.val_end_a = None
        self.val_start_b = None
        self.val_end_b = None
        self.para_key_a = None
        self.para_key_b = None
        self.highest_value = None
        self.simulation_result = None
        self.result_value = None

    @property
    def interval(self):
        return self.interval

    @interval.setter
    def interval(self, value):
        self._interval = value

    @property
    def val_start_a(self):
        return self.start_a

    @val_start_a.setter
    def val_start_a(self, value):
        self._start_a = value

    @property
    def val_end_a(self):
        return self.val_end_a

    @val_end_a.setter
    def val_end_a(self, value):
        self.val_end_a = value

    @property
    def val_start_b(self):
        return self.val_start_b

    @val_start_b.setter
    def val_start_b(self, value):
        self.val_start_b = value

    @property
    def val_end_b(self):
        return self.val_end_b

    @val_end_b.setter
    def val_end_b(self, value):
        self._val_end_b = value

    @property
    def para_key_a(self):
        return self.para_key_a

    @para_key_a.setter
    def para_key_a(self, value):
        self._para_key_a = value

    @property
    def para_key_b(self):
        return self.para_key_b

    @para_key_b.setter
    def para_key_b(self, value):
        self._para_key_b = value

    def run_two_para_simulation(self):
        results = {}
        n1 = int((self.val_end_a - self.val_start_a) / self.interval) + 1
        n2 = int((self.val_end_b - self.val_start_b) / self.interval) + 1
        val_a = []
        for i in range(n1):
            val_a.append(self.val_start_a + self.interval * i)
        val_b = []
        for i in range(n2):
            val_b.append(self.val_start_b + self.interval * i)
        out_path = run_two_parameter_simulation(self.eplus_run_path, self.idf_path, self.out_put_dir,
                                                self._para_key_a, val_a,
                                                self._para_key_b, val_b)

        for item in out_path.keys():
            tem_csv = pd.read_csv(out_path[item])
            tem_val = tem_csv[self.plot_column_name].values
            results[item] = sum(tem_val / len(tem_val))

        self.simulation_result = results
        return results
