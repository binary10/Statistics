import scipy.stats              as s
import numpy                    as np
import matplotlib.pyplot        as pl

# Hypothesis Testing: Proportions #####################################

class ProportionTest:

    # Simulation of proportionality estimation
    def __init__(self):
        self.rv         = s.binom(1000, .35)    # Define a binomial random variable
        self.b          = None                  # Store samples from binomial variable
        self.b_se       = None                  # Store standard errors of sample
        self.b_ci_max   = None                  # Store max endpoint of confidence interval

    def loop(self):
        z_confidence = s.norm.ppf(.97)
        self.b          = self.rv.rvs(1000)     # Pull 1000 samples from binomial
        # Calculate S.E. for each sample
        self.b_se       = np.sqrt( (self.b/1000. * (1-(self.b/1000.)))/1000.)
        # Calculate endpoint of CI for each sample
        self.b_ci_max   = self.b/1000. + z_confidence * self.b_se 
        return len([a for a in self.b_ci_max if a < .35])

    def test(self):
        return self.loop()

        
p = ProportionTest()
p.test()/1000. - 1



# Running a sequence of the same test #################################
#
# Take a sample of size 'n' from a normal distribution (collect data).
# Test if this sample is normal.
# Store the p-value of the test.
# Repeat the process above 'T' number of times.
# Calculate how many tests reject the null hypothesis with confidence level 'alpha'.
# The Law of Large Numbers predicts that our tests will converge to 95% confidence.
#

# Initialize Variables
n_test = []     # Store p-values for each normal test done
n = 1000        # Size of samples from Normal distribution
T = 1000        # Number of tests to perform
alpha = 0.05    # Type I error level

for i in range(T):
    sample_data = s.norm.rvs(size=n)                    # Collect some data
    n_test.append(s.normaltest(sample_data)[1])         # Test if the data is normal

#    
# Calculate the percentage of failed tests in our 
# experiment with significance level alpha.
# Should find that the proportion of rejected tests is close to alpha
100 * len([p_value for p_value in n_test if p_value < alpha]) / T




# Q-Q Plots ###########################################################

# Sample n=100 from Normal distribution and sort values
n_samp = scipy.stats.norm.rvs(size=100)
n_samp.sort()

# Plot
plt.scatter(n_samp, q)
plt.show()

