import numpy as np

file_name = "prueba.csv"

num_iters = 10**3
num_values = 10**8

x = np.arange(1, num_values+1)

# Max, means, lengths

seeds = x.copy()
maxs = x.copy()
means = x.copy()
lengths = np.ones(shape=x.shape)

dicts = []
for i in range(1, num_iters):

    # Add statistics of values equal to 1 to a df
    
    ones = x == 1
    
    terminated_seeds = seeds[ones]
    terminated_maxs = maxs[ones]
    terminated_means = means[ones]
    terminated_lengths = lengths[ones]
    
    terminated_dict = {
        "seed": terminated_seeds,
        "max": terminated_maxs,
        "mean": terminated_means,
        "length": terminated_lengths
    }
    
    dicts.append(terminated_dict)
    
    # Remove values equal to 1
    
    not_ones = ~ones
    seeds = seeds[not_ones]
    maxs = maxs[not_ones]
    means = means[not_ones]
    lengths = lengths[not_ones]
    x = x[not_ones]
    
    # Perform the collatz iteration

    x = np.where(x%2==1,
                (3*x+1)/2,
                x/2)
    
    # Update maxs
    
    stacked = np.vstack([maxs, x])
    maxs = np.amax(stacked, axis=0)
    
    # Update means
    
    means = (i * means + x) / (i + 1)
    
    # Update lengths
    
    lengths = lengths + 1

with open(file_name, "w") as f:
    f.write("seed|max|mean|length\n")

    for df in dicts:
        for seed, _max, mean, length in list(zip(df["seed"],
                                                 df["max"],
                                                 df["mean"],
                                                 df["length"])):
            f.write(f"{seed}|{_max}|{mean}|{length}\n")
