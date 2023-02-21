"""
Computational Work 03 - Combinatorial Optimization
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957
Solvers to TSP
"""

import json

from solvers import *

algorithms = {"solve_sa": {"tsp_files/ch130.tsp": {"image_file": "latex/images/solve_sa_ch130_{:d}.png",
                                                   "results_file": "results/results_solve_sa_ch130.json",
                                                   "exec_time_file": "results/exec_timer_solve_sa_ch130.json"},
                           "tsp_files/ch150.tsp": {"image_file": "latex/images/solve_sa_ch150_{:d}.png",
                                                   "results_file": "results/results_solve_sa_ch150.json",
                                                   "exec_time_file": "results/exec_timer_solve_sa_ch150.json"},
                           "tsp_files/eil101.tsp": {"image_file": "latex/images/solve_sa_eil101_{:d}.png",
                                                    "results_file": "results/results_solve_sa_eil101.json",
                                                    "exec_time_file": "results/exec_timer_solve_sa_eil101.json"},
                           "tsp_files/lin318.tsp": {"image_file": "latex/images/solve_sa_lin318_{:d}.png",
                                                    "results_file": "results/results_solve_sa_lin318.json",
                                                    "exec_time_file": "results/exec_timer_solve_sa_lin318.json"}},
              "solve_mls": {"tsp_files/ch130.tsp": {"image_file": "latex/images/solve_mls_ch130_{:d}.png",
                                                    "results_file": "results/results_solve_mls_ch130.json",
                                                    "exec_time_file": "results/exec_timer_solve_mls_ch130.json"},
                            "tsp_files/ch150.tsp": {"image_file": "latex/images/solve_mls_ch150_{:d}.png",
                                                    "results_file": "results/results_solve_mls_ch150.json",
                                                    "exec_time_file": "results/exec_timer_solve_mls_ch150.json"},
                            "tsp_files/eil101.tsp": {"image_file": "latex/images/solve_mls_eil101_{:d}.png",
                                                     "results_file": "results/results_solve_mls_eil101.json",
                                                     "exec_time_file": "results/exec_timer_solve_mls_eil101.json"},
                            "tsp_files/lin318.tsp": {"image_file": "latex/images/solve_mls_lin318_{:d}.png",
                                                     "results_file": "results/results_solve_mls_lin318.json",
                                                     "exec_time_file": "results/exec_timer_solve_mls_lin318.json"}},
              "solve_tabu": {"tsp_files/ch130.tsp": {"image_file": "latex/images/solve_tabu_ch130_{:d}.png",
                                                     "results_file": "results/results_solve_tabu_ch130.json",
                                                     "exec_time_file": "results/exec_timer_solve_tabu_ch130.json"},
                             "tsp_files/ch150.tsp": {"image_file": "latex/images/solve_tabu_ch150_{:d}.png",
                                                     "results_file": "results/results_solve_tabu_ch150.json",
                                                     "exec_time_file": "results/exec_timer_solve_tabu_ch150.json"},
                             "tsp_files/eil101.tsp": {"image_file": "latex/images/solve_tabu_eil101_{:d}.png",
                                                      "results_file": "results/results_solve_tabu_eil101.json",
                                                      "exec_time_file": "results/exec_timer_solve_tabu_eil101.json"},
                             "tsp_files/lin318.tsp": {"image_file": "latex/images/solve_tabu_lin318_{:d}.png",
                                                      "results_file": "results/results_solve_tabu_lin318.json",
                                                      "exec_time_file": "results/exec_timer_solve_tabu_lin318.json"}},
              "solve_ma": {"tsp_files/ch130.tsp": {"image_file": "latex/images/solve_ma_ch130_{:d}.png",
                                                   "results_file": "results/results_solve_ma_ch130.json",
                                                   "exec_time_file": "results/exec_timer_solve_ma_ch130.json"},
                           "tsp_files/ch150.tsp": {"image_file": "latex/images/solve_ma_ch150_{:d}.png",
                                                   "results_file": "results/results_solve_ma_ch150.json",
                                                   "exec_time_file": "results/exec_timer_solve_ma_ch150.json"},
                           "tsp_files/eil101.tsp": {"image_file": "latex/images/solve_ma_eil101_{:d}.png",
                                                    "results_file": "results/results_solve_ma_eil101.json",
                                                    "exec_time_file": "results/exec_timer_solve_ma_eil101.json"},
                           "tsp_files/lin318.tsp": {"image_file": "latex/images/solve_ma_lin318_{:d}.png",
                                                    "results_file": "results/results_solve_ma_lin318.json",
                                                    "exec_time_file": "results/exec_timer_solve_ma_lin318.json"}}}

solvers = {"solve_sa": solve_sa,
           "solve_mls": solve_mls,
           "solve_tabu": solve_tabu,
           "solve_ma": solve_ma}

for solver in solvers:

    problems = algorithms[solver]
    solver = solvers[solver]

    for problem in problems:
        exec_time, results = solver(problem, problems[problem]["image_file"])

        with open(problems[problem]["results_file"], "w") as f:
            json.dump(results, f, indent=4)

        with open(problems[problem]["exec_time_file"], "w") as f:
            json.dump(exec_time, f, indent=4)
