import thinkstats2
import nsfg
import first
import thinkstats2
import pandas

def main():
    live, firsts, others = first.MakeFrames
    n = 100000
    for i in range(10):
        sample = thinkstats2.SampleRows(live, n)
        Runtests(sample)
        n = n // 2

def RunTests:
    
