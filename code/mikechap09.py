import thinkstats2
import hypothesis
import nsfg
import first
import thinkstats2
import pandas

def RunTests(sample):
    n = len(sample)
    print(n)
    ht = hypothesis.DiffMeansPermute(sample)

def main():
    live, firsts, others = first.MakeFrames()
    n = len(live)
    for i in range(10):
        sample = thinkstats2.SampleRows(live, n)
        RunTests(sample)
        n = n // 2

if __name__ == '__main__':
    main()

