import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7

## Task 2: About 14,9% (0.14900277967433773)
print(stats.poisson.pmf(7,7))

## Task 3: About 17,2% (0.17299160788207146)

print(stats.poisson.cdf(4,7))

## Task 4: About 27,09% (0.2709087322619176)
bad_day = 1- stats.poisson.cdf(9,7)
print(bad_day)

### Task Group 2 ###

## Task 5:

year_defects = stats.poisson.rvs(7,size = 365)
#print(year_defects)

## Task 6:
print(year_defects[0:21])

## Task 7:Total number of defects we expected over 365 days: 2555
print(lam*365)

## Task 8: Compare to 2644 (Pretty Close to 2555)
print(sum(year_defects))

## Task 9:  AVG 6.8 - Pretty close to lam = 7
print(np.mean(year_defects))

## Task 10: MAX Defects on a Day: 17
print(np.max(year_defects))

## Task 11: 0.00036178431660227606
print(1- stats.poisson.cdf(17,7))

### Extra Bonus ###
# Task 12 =  Fewer than 10 Defects in 90% of Days
percentile = stats.poisson.ppf(0.90,7)
print(percentile)

# Task 13 0.1780821917808219 (about 17,80%) of Values from dataset are equal or greater to percentile
proportion = sum(year_defects >= percentile ) / len(year_defects)
print(proportion)