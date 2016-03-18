[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
import sys
import chap01soln as ch1
import thinkstats2
import thinkplot as tp

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

def plot_pmfs(pmf1, pmf2):
    tp.PrePlot(2)
    tp.Pmfs([pmf1, pmf2])
    tp.Save(root='/Users/MelanieAppleby/ds/metis/prework/dsp/img/ch3ex1',
            formats=['jpg'],
            xlabel='Number of Children',
            ylabel='PMF')

def main(script):
    resp = ch1.ReadFemResp()
    pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
    biased_pmf = BiasPmf(pmf, label='biased')
    print 'The mean of the unbiased pmf is %f and the mean of the biased pmf is %f' \
          % (pmf.Mean(), biased_pmf.Mean())
    plot_pmfs(pmf, biased_pmf)

if __name__ == '__main__':
    main(*sys.argv)
```
