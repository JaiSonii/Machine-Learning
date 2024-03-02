def unique_word(sentence):
    words = sentence.split()
    word_counts = dict()
    for word in words:
        word_counts[word] = word_counts.get(word,0 ) + 1 
    return word_counts

sentence = "This is a test sentence test"
frequencies = unique_word(sentence)
for key, value in frequencies.items():
    print(key, value)