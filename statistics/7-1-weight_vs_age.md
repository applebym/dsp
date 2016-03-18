[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```python
"""
Using data from the NSFG, make a scatter plot of birth weight
versus mother's age. Plot percentiles of birth weight versus
mother's age. Compute Pearson's and Spearman's correlations.
How would you characterize the relationship between these
variables?
"""

import first
import thinkstats2 as ts
import thinkplot as tp
import numpy as np


def scatter_plot(weights, ages):
    tp.Scatter(weights, ages, alpha=0.1)
    tp.Save(root='/Users/MelanieAppleby/ds/metis/prework/dsp/img/ch7ex1scatter',
            formats=['jpg'],
            xlabel='Weight (lb)',
            ylabel="Mother's Age",
            axis=[0, 15, 10, 50],
            legend=False)


def plot_percentiles(df):
    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [ts.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    tp.PrePlot(num=3)
    for percent in [75, 50 , 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        tp.Plot(ages, weights, label=label)

    tp.Save(root='/Users/MelanieAppleby/ds/metis/prework/dsp/img/ch7ex1binned',
            formats=['jpg'],
            xlabel="Mother's Age (Years)",
            ylabel='Birth Weight (lbs)')

def main():
    ts.RandomSeed(17)

    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

    scatter_plot(live.birthwgt_lb, live.agepreg)

    plot_percentiles(live)

    print("Pearson's Correlation: ",
           ts.Corr(live.agepreg, live.totalwgt_lb))
    print("Spearman's Correlation: ",
           ts.SpearmanCorr(live.agepreg, live.totalwgt_lb))
    print("Pearson's Correlation with log-weight",
          ts.Corr(live.agepreg, np.log(live.totalwgt_lb)))
    print("Pearson's Correlation with log-age",
          ts.Corr(np.log(live.agepreg), live.totalwgt_lb))
    print("Pearson's Correlation with log-weight, log-age",
          ts.Corr(np.log(live.agepreg), np.log(live.totalwgt_lb)))

    pdf = ts.EstimatedPdf(live.agepreg)
    tp.Pdf(pdf, label="Mother's Age")
    tp.Save(root='/Users/MelanieAppleby/ds/metis/prework/dsp/img/ch7ex1PDF',
            formats=['jpg'])


if __name__ == '__main__':
    main()
```
