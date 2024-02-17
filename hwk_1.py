#The objective is to learn to differentiate:
'''
- When can we estimate causal effects?
- Do we need to apply the adjustment formula?
- If yes, what variable should we adjust for?
'''
## Packages
import numpy as np
from numpy.random import binomial, normal, seed

seed (1234)
n = 10000

# ------------------------------------------------------------------------------
#EXAMPLE - RCT or AB Test
T = np.random.binomial(1,0.5,size=n)
O = np.random.binomial(1,0.3,size=n)*(T) + np.random.binomial(1,0.5,size=n)*(1-T)

#condition_prob_diff = mean(outcome[treatment==1]) - mean(outcome[treatment==0])
conditional_prob_diff = np.mean(O[T==1]) - np.mean(O[T==0])
print(conditional_prob_diff)
#-0.1810218929047634

#Adjustment
#?

#Theoretical ATE
theoretic_ATE = np.mean(O*1) - np.mean(O*(1-T))
print(theoretic_ATE)


#| Question                                        | Result |
#| --------                                        | ------- |
#| Estimated E(O\|T=1) - E(O\|T=0)                 |  -0.18 |
#| adjustment(1) - adjustment(0)                   |  ? |
#| Theoretical ATE = E(O\|do(T=1)) - E(O\|do(T=0)) |  -0.2 |
#| Estimated ATE from data                         |  -0.18 |


# ------------------------------------------------------------------------------
#EXERCISE A 

# 𝜀 ~N(0,1)
epsilon = normal(0,1)

#EXAMPLE - RCT or AB Test
C = np.random.binomial(1,0.8,size=n)
#Z := B(0.6) C + B(0.1) (1-C)
Z = np.random.binomial(1,0.6,size=n)*C + np.random.binomial(1,0.1,size=n)*(1-C)
#T := B(0.6) Z + B(0.2)(1-Z)
T = np.random.binomial(1,0.6,size=n)*Z + np.random.binomial(1,0.2,size=n)*(1-Z)
#O := B(0.3) T + B(0.5) (1-T) + C + 𝜀
O = np.random.binomial(1,0.3,size=n)*(T) + np.random.binomial(1,0.5,size=n)*(1-T) + C + epsilon

#condition_prob_diff = mean(outcome[treatment==1]) - mean(outcome[treatment==0])
conditional_prob_diff = np.mean(O[T==1]) - np.mean(O[T==0])
print(conditional_prob_diff)
#-0.1810218929047634

#Adjustment
#?

#Theoretical ATE
theoretic_ATE = np.mean(O*1) - np.mean(O*(1-T))
print(theoretic_ATE)

#| Question                                        | Result |
#| --------                                        | ------- |
#| Estimated E(O\|T=1) - E(O\|T=0)                 |  -0.063 |
#| adjustment(1) - adjustment(0)                   |  ? |
#| Theoretical ATE = E(O\|do(T=1)) - E(O\|do(T=0)) |  -0.2 |
#| Estimated ATE from data                         |  -0.18 |