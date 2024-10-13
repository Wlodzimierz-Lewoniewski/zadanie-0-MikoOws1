docs = int(input("liczba dokumentow: "))
documents = []
for i in range(docs):
    documents.append(input(f"dokument {i + 1}: "))

qs = int(input("liczba zapytan: "))
queries = []
for i in range(qs):
    queries.append(input(f"zapytanie {i + 1}: "))

def process_document(document):
    cleaned_document = "".join([char.lower() if char.isalnum() else " " for char in document])
    return cleaned_document.split()

doc_words = [process_document(doc) for doc in documents]

for query in queries:
    results = []
    query_lower = query.lower()
    index = 0
    for words in doc_words:
        count = words.count(query_lower)
        if count > 0:
            results.append((index, count))
        index += 1
    
    results.sort(key=lambda x: (-x[1], x[0]))
    
    result_final = [str(result[0]) for result in results]
    print("wynik dla '", query, "':", " ".join(result_final))