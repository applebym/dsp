[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

```python
import hypothesis
import thinkstats2
import first

class DiffMeansResample(hypothesis.DiffMeansPermute):

    def RunModel(self):
        data = thinkstats2.Resample(self.pool[:self.n]), \
               thinkstats2.Resample(self.pool[self.n:])
        return data

def TestResampling(data):
    ht = DiffMeansResample(data)
    pvalue = ht.PValue(iters=10000)
    print('p-value', pvalue)

def TestPermutation(data):
    ht = hypothesis.DiffMeansPermute(data)
    pvalue = ht.PValue(iters=10000)
    print('p-value', pvalue)

def main():
    live, firsts, others = first.MakeFrames()
    data_preg = firsts.prglngth.values, others.prglngth.values
    data_wgt = firsts.totalwgt_lb.values, others.totalwgt_lb.values

    print('Diff Means by Resampling:')
    print('Diff in preg length:')
    TestResampling(data_preg)
    print('Diff in birth weight:')
    TestResampling(data_wgt)

    print('Diff Means by Permutation:')
    print('Diff in preg length:')
    TestPermutation(data_preg)
    print('Diff in birth weight:')
    TestPermutation(data_wgt)

if __name__ =='__main__':
    main()
```
