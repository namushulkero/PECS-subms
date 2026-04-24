# - Create a program that generates a random number with the following distributions
#   - Uniformly distributed (int) discrete random number
#   - Between a min and a max values (int)

import random
import numpy as np
import matplotlib.pyplot as plt

def generate_unifdist_random_number(min_value, max_value):
    if min_value > max_value:
        raise ValueError("min_value should be less than or equal to max_value")
    
    return random.randint(min_value, max_value)

def run_simulation(num_of_val, dist_type, seed, min_value=None, max_value=None):
    random.seed(seed)

    if dist_type == "uniform_int":
        return [generate_unifdist_random_number(min_value, max_value) for _ in range(num_of_val)]

    if dist_type == "uniform_real":
        return [generate_unifrealdist_random_number(min_value, max_value) for _ in range(num_of_val)]

    if dist_type == "normal":
        mean = 0
        stddev = 0.75 
        return [random.gauss(mean, stddev) for _ in range(num_of_val)]

    if dist_type == "exponential":
        lambda_param = 2.0
        return [random.expovariate(lambda_param) for _ in range(num_of_val)]

    if dist_type == "geometric":
        p = 0.3
        return [np.random.geometric(p) for _ in range(num_of_val)]
        
    else:
        raise ValueError("Unsupported distribution type")


def generate_unifrealdist_random_number(min_value, max_value):
    if min_value > max_value:
        raise ValueError("min_value should be less than or equal to max_value")
    
    return random.uniform(min_value, max_value)

# Example usage

if __name__ == "__main__":
    for num_of_val in [10, 100, 1000, 10000]:
        data = run_simulation(num_of_val, dist_type="geometric", seed=2, min_value=1.0, max_value=3.0)
        # plot the histogram

        # title = f"Uniform Distribution (real) (1.0 to 3.0) - {num_of_val} Values"
        # title = f"Normal Distribution (mean=0, stddev=0.75) - {num_of_val} Values"
        # title = f"Exponential Distribution (lambda=2.0) - {num_of_val} Values"
        title = f"Geometric Distribution (p=0.3) - {num_of_val} Values"

        plt.figure(figsize=(10, 6))

        plt.title(title)

        plt.hist(data, bins="auto", density=True, edgecolor='black')

        # write to file the numbers

        filename = title.replace(" ", "_") + ".txt"

        with open(filename, "w") as f:
            for number in data:
                f.write(f"{number}, ")

        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.grid(axis='y', alpha=0.75)
        plt.savefig(title.replace(" ", "_") + ".png")






