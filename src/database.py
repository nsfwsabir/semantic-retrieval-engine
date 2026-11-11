import chromadb
import json
from embeddings import generate_embedding

client= chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="support_faqs",
    metadata={"hnsw:space": "cosine"}
)

def load_faqs():
    with open("data/faqs.json", "r") as file:
        return json.load(file)

def store_faqs():

    faqs= load_faqs()

    ids=[]
    documents=[]
    embeddings=[]
    metadatas=[]

    for faq in faqs:

        faq_id=faq["id"]
        question=faq["question"]
        category=faq["category"]
        answer=faq["answer"]

        vector=generate_embedding(question)

        ids.append(faq_id)
        documents.append(question)
        embeddings.append(vector)

        metadatas.append({
            "category": category,
            "answer": answer
        })


    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    
if __name__ == "__main__":
    store_faqs()
    print("Total Records", collection.count())