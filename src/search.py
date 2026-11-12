from embeddings import generate_embedding
from database import collection

def search_faqs(
    query: str,
    top_k:int =1,
    max_distance: float=0.5,
    category: str | None = None
):

    query_embedding=generate_embedding(query)

    query_args={
        "query_embeddings": [query_embedding],
        "n_results": top_k
    }

    if category:
        query_args["where"] = {"category": category}
        
    results = collection.query(**query_args)
    ids=results["ids"][0]
    documents=results["documents"][0]
    metadatas=results["metadatas"][0]
    distances=results["distances"][0]

    search_results=[]


    for faq_id, doc, metadata, distance in zip(ids, documents, metadatas, distances):
        result={
            "id": faq_id,
            "question": doc,
            "answer": metadata["answer"],
            "category": metadata["category"],
            "distance": distance
        }

        if(distance<=max_distance):
            search_results.append(result)

    return search_results
        
