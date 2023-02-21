
"""
Computational Work 03 - Combinatorial Optimization
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957
Result Analysis
"""

import json
import numpy as np
import pandas as pd


solvers = {"solve_sa": "Simulated Annealing",
           "solve_mls": "Random Multi-start LS",
           "solve_tabu": "Tabu Search",
           "solve_ma": "Memetic Algorithm"}

problems = ["ch130",
            "ch150",
            "eil101",
            "lin318"]

best_fits = {"ch130": 6110,
             "ch150": 6528,
             "eil101": 629,
             "lin318": 42029}

results = list()

for problem in problems:
    for solver in solvers:

        filename = "results/results_{:s}_{:s}.json".format(solver, problem)

        with open(filename, "r") as f:
            data = json.load(f)

        value_min = np.min(data)

        value_avg = np.mean(data)

        value_median = np.median(data)

        value_max = np.max(data)

        value_std = np.std(data)

        results.append([problem,
                        best_fits[problem],
                        solvers[solver],
                        value_min,
                        value_avg,
                        value_median,
                        value_max,
                        value_std])

df = pd.DataFrame.from_records(np.array(results),
                               columns=["Problem",
                                        "Best known Fit",
                                        "Solver",
                                        "Min Value",
                                        "Mean Value",
                                        "Median Value",
                                        "Max Value",
                                        "STD Dev"])
print(df)
df.to_excel("results/results.xls")
