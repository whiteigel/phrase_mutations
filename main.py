from phrase import *
from positions import *

def mutate_seed(seed_phrase, new_positions):
    words = seed_phrase.split()
    original_positions = {word: words.index(word) for word in words}

    # Mutate the seed phrase based on the new positions
    mutated_seed = ' '.join(words[new_pos - 1] for new_pos in new_positions)

    return mutated_seed, original_positions


def revert_seed(mutated_seed, original_positions):
    words = mutated_seed.split()
    # Revert the mutated seed phrase to the original
    reverted_seed = ' '.join(word for word, pos in sorted(original_positions.items(), key=lambda x: x[1]))

    return reverted_seed

# Mutate the seed phrase
mutated_seed, original_positions = (
    mutate_seed(original_seed, new_positions))
print("Mutated Seed Phrase:", mutated_seed)

# Revert changes
reverted_seed = revert_seed(mutated_seed, original_positions)
print("Reverted Seed Phrase:", reverted_seed)
print("Original Seed Phrase:", original_seed)