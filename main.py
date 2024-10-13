docs = int(input())
documents = []
for _ in range(docs):
    documents.append(input())

qs = int(input())
queries = []
for _ in range(qs):
    queries.append(input())

def process_document(document):
    cleaned_document = "".join([char.lower() if char.isalnum() else " " for char in document])
    return cleaned_document.split()

doc_words = [process_document(doc) for doc in documents]

for query in queries:
    results = []
    query_lower = query.lower()
    for index, words in enumerate(doc_words):
        count = words.count(query_lower)
        if count > 0:
            results.append((index, count))
    
    results.sort(key=lambda x: (-x[1], x[0]))
    
    result_final = [str(result[0]) for result in results]
    print(" ".join(result_final))