from waterfall import doWaterfall
import numpy as np
import utils
import logging


def simulateWaterfall(loan_pool, securities, n_sim):
    n_tranche = len(securities.tr_lst)
    metric_records = np.zeros((n_tranche, 2))  # records DIRR & AL for each tr
    for i in xrange(n_sim):
        loan_pool.reset()
        securities.reset()
        # logging.info("Simulation {}".format(i))
        tr_metrics, lp_wf, sc_wf, res_amounts = doWaterfall(loan_pool, securities)
        for j, tr_metric in enumerate(tr_metrics):
            metric_records[j] += [tr_metric[1], tr_metric[2]]
    return metric_records / n_sim


def runMonte(loan_pool, n_sim, tol):
    percents = np.array([0.8, 0.2])
    rates = np.array([0.05, 0.08])
    levels = [0, 1]
    step_sizes = np.array([1.2, 0.8])
    diff = np.inf
    ii = 0
    while np.abs(diff) > tol:
        print "Iteration {}, rates {}".format(ii, rates)
        securities = utils.makeSecurities(loan_pool.totalPrincipal(), percents, rates, levels)
        tr_metrics = simulateWaterfall(loan_pool, securities, n_sim)
        yields = utils.calcYields(tr_metrics[:, 0], tr_metrics[:, 1])
        new_rates = rates + step_sizes * (yields - rates)  # update rates
        diff = np.dot(percents, (rates - new_rates)/rates)
        ii += 1
        rates = new_rates
    print "Done"
    return new_rates