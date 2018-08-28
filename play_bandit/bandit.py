#import statistics as stats
import numpy as np
from scipy import stats 
import matplotlib.pyplot as plt 
#import pymc

# init the beta parameters with equal prob.
prior_a = 1. # aka successes 
prior_b = 1. # aka failures
K = 100
estimated_beta_params = np.zeros((K,2))
estimated_beta_params[:,0] += prior_a # allocating the initial conditions
estimated_beta_params[:,1] += prior_b


def raw_beta():
    n = 10
    # k = 5
    p = np.linspace(0, 1, 100)
    # pbeta = stats.beta.pdf(p, k+1, n-k+1)
    # plt.plot(p, pbeta, label="k=5", lw=2)
     
    for k in range(2,9):
        pbeta = stats.beta.pdf(p, k+1, n-k+1)
        plt.plot(p, pbeta, label="k={}".format(k), lw=2)

    plt.xlabel("$p$")
    plt.legend(loc="best");
    plt.show()


def naive(estimated_beta_params,number_to_explore=100):
    totals = estimated_beta_params.sum(1) # totals
    if np.any(totals < number_to_explore): # if current explored less than specified
        least_explored = np.argmin(totals) # return the one least explored
        return least_explored
    else: # return the best mean forever
        successes = estimated_beta_params[:,0] # successes
        estimated_means = successes/totals # the current means
        best_mean = np.argmax(estimated_means) # the best mean (naive)
        return best_mean


def Thompson_sampling(estimated_beta_params,number_to_explore=100):
    totals = estimated_beta_params.sum(1) # totals
    if np.any(totals < number_to_explore): # if current explored less than specified
        least_explored = np.argmin(totals) # return the one least explored
        return least_explored
    else: # return the best mean forever
        successes = estimated_beta_params[:,0] # successes
        estimated_means = successes/totals # the current means
        best_mean = np.argmax(pymc.rbeta(1 + successes, 1 + totals - successes)) # the best mean with Thompson sampling
        return best_mean




## UBC: Upper Confidence Bound(置信区间上界)
## 先对每一个臂都试一遍
## 之后，每次选择以下值最大的那个臂
## 均值越大，标准差越小，被选中的概率会越来越大，起到了exploit的作用；同时哪些被选次数较少的臂也会得到试验机会，起到了explore的作用。
## 
## 	每个item的回报均值都有个置信区间，随着试验次数增加，置信区间会变窄（逐渐确定了到底回报丰厚还是可怜）。
## 	每次选择前，都根据已经试验的结果重新估计每个item的均值及置信区间。
## 	选择置信区间上限最大的那个item。
## 
## “选择置信区间上界最大的那个item”这句话反映了几个意思：
##     1. 如果item置信区间很宽（被选次数很少，还不确定），那么它会倾向于被多次选择，这个是算法冒风险的部分；
##     2. 如果item置信区间很窄（备选次数很多，比较确定其好坏了），那么均值大的倾向于被多次选择，这个是算法保守稳妥的部分；
##     3. UCB是一种乐观的算法，选择置信区间上界排序，如果时悲观保守的做法，是选择置信区间下界排序。
def UBC(estimated_beta_params,number_to_explore=100):
    t = float(estimated_beta_params.sum()) # total number of rounds 
    totals = estimated_beta_params.sum(1)  #The number of experiments per arm
    successes = estimated_beta_params[:,0]
    estimated_means = successes/totals # earnings mean
    estimated_variances = estimated_means - estimated_means**2    
    UCB = estimated_means + np.sqrt( np.minimum( estimated_variances + np.sqrt(2*np.log(t)/totals), 0.25 ) * np.log(t)/totals )
    return np.argmax(UCB)


## Epsilon-Greedy算法
## 选一个(0,1)之间较小的数epsilon
## 每次以概率epsilon（产生一个[0,1]之间的随机数，比epsilon小）做一件事：所有臂中随机选一个。否则，选择截止当前，平均收益最大的那个臂。
## 是不是简单粗暴？epsilon的值可以控制对Exploit和Explore的偏好程度。越接近0，越保守，只想花钱不想挣钱。

#def Epsilon-Greedy(estimated_beta_params,number_to_explore=100):


if __name__=="__main__":
    raw_beta()
