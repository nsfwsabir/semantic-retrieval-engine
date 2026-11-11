import numpy as np
from embeddings import generate_embedding

def cosine_similarity(a, b):

    denominator= (np.linalg.norm(a) * (np.linalg.norm(b)))
    
    if denominator == 0:
        return 0.0
        
    cosine= np.dot(a,b) / denominator

    return cosine


sentence_a = "How do I reset my password?"
sentence_b = "I forgot my login credentials."
sentence_c = "What is the weather today?"

embedding_a= generate_embedding(sentence_a)
embedding_b= generate_embedding(sentence_b)
embedding_c= generate_embedding(sentence_c)

print("A vs B", cosine_similarity(embedding_a, embedding_b))
print("A vc C", cosine_similarity(embedding_a, embedding_c))

    

