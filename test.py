import scipy.stats as sts 
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 100)

norm_dist = sts.norm(loc = np.mean(x), scale = np.std(x))

plt.plot(norm_dist.pdf(x))
plt.savefig("Test Distribution")