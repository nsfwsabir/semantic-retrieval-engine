from search import search_faqs



def main():
    print("-" *40)
    print("         Semantic Retrieval Engine")
    print("-" *40)

    while True:

        query=input("\nEnter your search query: ").strip()

        if(query.lower()=="exit"):
            print("Goodbye!")
            break
        if(query == "" ):
            print("Query empty, enter something")
            continue

        results=search_faqs(query)
        if not results:
            print("No relevant results found. Try rephrasing your query.")

        for index, result in enumerate(results, start=1):
            print(f"\n{index}, {result['question']} \nCategory: {result['category']} \nDistance: {result['distance']} \nAnswer: {result['answer']}")
            


if __name__ =="__main__":
    main()