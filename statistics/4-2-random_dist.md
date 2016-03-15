[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
import random
import thinkstats2 as ts
import thinkplot as tp

def make_pmf_cdf():
    randoms = [random.random() for x in range(1000)]
    pmf = ts.Pmf(randoms)
    cdf = ts. Cdf(randoms)
    return pmf, cdf

def plot(pmf, cdf):
    tp.PrePlot(cols=2)
    tp.Pmf(pmf)
    tp.Config(xlabel='random numbers',
              ylabel='PMF',
              linewidth=0.5,
              width=2,
              axis=[0, 1, 0, 0.0012])

    tp.SubPlot(2)
    tp.Cdf(cdf)
    tp.Config(xlabel='random number',
            ylabel='CDF')
    tp.Show()


def main():
    pmf, cdf = make_pmf_cdf()
    plot(pmf, cdf)

if __name__ == '__main__':
    main()
```
