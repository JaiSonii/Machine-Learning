def counts(corpus):
    words = []
    word_counts = {}
    for document in corpus:
        words = document.split()
        
        for word in words:
            if word not in word_counts:
                word_counts[word] = {'total_count' : 1, 'documents' : {document : 1}}
            else:
                word_counts[word]['total_count'] += 1
                if document in word_counts[word]['documents']:
                    word_counts[word]['documents'][document] += 1
                else:
                    word_counts[word]['documents'][document] = 1
    
    return word_counts
    
corpus = [
    "This is the multidimensional dictionary.",
    "This dictionary stores the sub dictionary.",
    "And this is the third containing the word and count.",
    "Is this the first level of dictionary?"
]

data = counts(corpus)

for key in data.keys():
    print(key, end=': ')
    print(" "*3)
    print(' '*3, 'Total Count:', data[key]['total_count'])
    print(' '*3, 'Documents:')
    for document in data[key]['documents'].keys():
        print(' '*5, document)
    
    