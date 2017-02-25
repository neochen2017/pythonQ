
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

print sort_sentence('chen')
