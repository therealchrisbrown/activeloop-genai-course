import numpy as np

probabilities = np.array([0.4,0.27,0.55,0.79])
sentence_probabilities = probabilities.prod()
sentence_probabilities_normalized = sentence_probabilities ** (1/len(probabilities))
perplexity = 1 / sentence_probabilities_normalized

print(perplexity)

# Suppose we further train the LLM, and the probabilities of the next best word become higher. How would the final perplexity be, higher or lower?
# Would become lower