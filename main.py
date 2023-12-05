from phrase import original_phrase
from positions import new_positions

def mutate_phrase(phrase, new_positions):
    words = phrase.split()
    original_positions = {word: words.index(word) for word in words}

    # Mutate the phrase based on the new positions
    mutated_phrase = ' '.join(words[new_pos - 1] for new_pos in new_positions)

    return mutated_phrase, original_positions


def revert_phrase(mutated_phrase, original_positions):
    words = mutated_phrase.split()
    # Revert the mutated phrase to the original
    reverted_phrase = ' '.join(word for word, pos in sorted(original_positions.items(), key=lambda x: x[1]))

    return reverted_phrase

# Mutate the phrase
mutated_phrase, original_positions = (mutate_phrase(original_phrase, new_positions))
print("Mutated Phrase:", mutated_phrase)

# Revert changes
reverted_phrase = revert_phrase(mutated_phrase, original_positions)
print("Reverted Phrase:", reverted_phrase)
