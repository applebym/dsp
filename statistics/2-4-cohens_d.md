[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> ```python
import nsfg
import sys
import math

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

def main(script):
    df = nsfg.ReadFemPreg()

    firsts = df[df.birthord == 1]
    others = df[df.birthord > 1]

    d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print d


if __name__ == '__main__':
    main(*sys.argv)
```
