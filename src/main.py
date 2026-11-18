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

        if len(results)>=2:
            gap=results[1]["distance"] - results[0]["distance"]

            if gap<0.10:
                print("\nYour query could mean a few different things.")
                print("Did you mean one of these?")

                for index, result in enumerate(results, start=1):
                    print(f"\n{index}. {result['question']}")

                while(True):
                    choice=input("\n Enter your choice (1-3) or 0 to cancel: ")
    
                    if not choice.isdigit():
                        print("Invalid input, please enter a digit")
                        continue

                    choice=int(choice)
    
                    if choice == 0:
                        print("Search cancelled.")
                        break
                        
                    elif 1 <= choice <= len(results):
                        selected = results[choice - 1]
                        print("\nAnswer:", selected["answer"])
                        break
                        
                    else:
                        print(f"Invalid choice. Please select a number between 1 and {len(results)}.")
    
                    continue


if __name__ =="__main__":
    main()