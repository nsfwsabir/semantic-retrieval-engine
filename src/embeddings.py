from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-V2")

def generate_embedding(text: str):
    vector= model.encode(text)
    return vector.tolist()


if __name__ == "__main__":
    text = "how do I reset my password"

    vector= generate_embedding(text)

    print("Dimensions:", len(vector))
    print("Vector:", vector[:10])