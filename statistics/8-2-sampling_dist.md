[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)


For this file I worked off of a copy of estimation.py
```python
"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import thinkstats2
import thinkplot

import math
import random
import numpy as np


def MeanError(estimates, actual):
    """Computes the mean error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float mean error
    """
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)


def RMSE(estimates, actual):
    """Computes the root mean squared error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float RMSE
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)


def Estimate1(n=7, m=1000):
    """Evaluates RMSE of sample mean and median as estimators.

    n: sample size
    m: number of iterations
    """
    mu = 0
    sigma = 1

    means = []
    medians = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for _ in range(n)]
        xbar = np.mean(xs)
        median = np.median(xs)
        means.append(xbar)
        medians.append(median)

    print('Experiment 1')
    print('rmse xbar', RMSE(means, mu))
    print('rmse median', RMSE(medians, mu))


def Estimate2(n=7, m=1000):
    """Evaluates S and Sn-1 as estimators of sample variance.

    n: sample size
    m: number of iterations
    """
    mu = 0
    sigma = 1

    estimates1 = []
    estimates2 = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for _ in range(n)]
        biased = np.var(xs)
        unbiased = np.var(xs, ddof=1)
        estimates1.append(biased)
        estimates2.append(unbiased)

    print('Experiment 2')
    print('mean error biased', MeanError(estimates1, sigma**2))
    print('mean error unbiased', MeanError(estimates2, sigma**2))


def Estimate3(n=7, m=1000):
    """Evaluates L and Lm as estimators of the exponential parameter.

    n: sample size
    m: number of iterations
    """
    lam = 2

    means = []
    medians = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        Lm = math.log(2) / np.median(xs)
        means.append(L)
        medians.append(Lm)

    print('Experiment 3')
    print('rmse L', RMSE(means, lam))
    print('rmse Lm', RMSE(medians, lam))
    print('mean error L', MeanError(means, lam))
    print('mean error Lm', MeanError(medians, lam))


def SimulateSampleL(lam=2, n=10, m=1000):
    """Plots the sampling distribution of the sample L.

    mu: hypothetical population mean
    sigma: hypothetical population standard deviation
    n: sample size
    m: number of iterations
    """
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    L_estimates = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        L_estimates.append(L)

    stderr = RMSE(L_estimates, lam)
    print('Sample size n=', n)
    print('standard error', stderr)

    cdf = thinkstats2.Cdf(L_estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    VertLine(ci[0])
    VertLine(ci[1])


    # plot the CDF
    if n == 10:
        thinkplot.Cdf(cdf)
        thinkplot.Save(root='/Users/MelanieAppleby/ds/metis/prework/dsp/img/ch8ex2CDF',
                       formats=['jpg'],
                       xlabel='sample lambda',
                       ylabel='CDF',
                       title='Sampling distribution')

    return stderr


def SimulateGame(lam, n):

    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    def one_game(lam):
        count = 0
        xs = np.random.exponential(1.0 / lam, 1)
        while np.sum(xs) <= 1:
            x = np.random.exponential(1.0 / lam, 1)
            xs = np.append(xs, x)
        return xs.size

    lam_list = []
    for _ in range(n):
        num_goals = one_game(lam)
        lam_list.append(num_goals)

    print('mean error at n=%d:' % n, MeanError(lam_list, lam))
    print('RMSE / stderr', RMSE(lam_list, lam))

    cdf = thinkstats2.Cdf(lam_list)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    VertLine(ci[0])
    VertLine(ci[1])

    if n == 1900:
        thinkplot.Cdf(cdf)
        thinkplot.Save(root='/Users/MelanieAppleby/ds/metis/prework/dsp/img/ch8ex2Game',
                       formats=['jpg'],
                       xlabel='goal-scoring rate',
                       ylabel='CDF',
                       title='Sampling distribution at n=%d' % n)


def main():
    thinkstats2.RandomSeed(17)

    # stderrs = []
    # xs = []
    # for i in range(10,1000,100):
    #     xs.append(i)
    #     se = SimulateSampleL(n=i)
    #     stderrs.append(se)
    # thinkplot.Plot(xs, stderrs)
    # thinkplot.Save(root='/Users/MelanieAppleby/ds/metis/prework/dsp/img/ch8ex2stderrs',
    #                formats=['jpg'],
    #                xlabel='n',
    #                ylabel='standard error',
    #                title='Relationship between SE and n')

    SimulateGame(lam=5, n=100)
    SimulateGame(lam=5, n=300)
    SimulateGame(lam=5, n=1000)
    SimulateGame(lam=5, n=10000)

if __name__ == '__main__':
    main()
```
