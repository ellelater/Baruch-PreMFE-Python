from waterfall import doWaterfall
import numpy as np


def simulateWaterfall(loan_pool, securities, n_sim):
    n_tranche = len(securities.tr_lst)
    metric_records = np.zeros((n_tranche, 2))  # records DIRR & AL for each tr
    for i in xrange(n_sim):
        securities.reset()
        print "Simulation", i
        tr_metrics, lp_wf, sc_wf, res_amounts = doWaterfall(loan_pool, securities)
        for j, tr_metric in enumerate(tr_metrics):
            metric_records[j] += [tr_metric[1], tr_metric[2]]
    return metric_records / n_sim
