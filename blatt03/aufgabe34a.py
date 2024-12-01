import itertools

# Define the sample space
omega1 = range(1, 181)  # 1 to 180 minutes
omega2 = range(1, 121)  # 1 to 120 minutes
sample_space = list(itertools.product(omega1, omega2))

# Calculate the probability P(tilde{X} < tilde{Y})
count_X_less_Y = sum(1 for (x, y) in sample_space if x < y)
total_outcomes = len(sample_space)
prob_X_less_Y = count_X_less_Y / total_outcomes

print(f"P(tilde{{X}} < tilde{{Y}}) = {prob_X_less_Y:.4f}")