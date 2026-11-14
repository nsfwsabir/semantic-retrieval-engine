import json
from search import search_faqs

def load_test_queries():
    with open("data/holdout_queries.json","r") as file:
        return json.load(file)


def evaluate():
    test_queries= load_test_queries()

    total= len(test_queries)
    correct=0
    failed_queries=[]

    for test in test_queries:
        query= test["query"]
        expected_ids= test["expected_ids"]

        results= search_faqs(query, max_distance=2.0)

        predicted_id= None
        distance=None

        if results:
            distance = results[0]['distance']
            if distance <=0.6:
                predicted_id=results[0]["id"]

        print(f"  Distance: {distance}")

        if not expected_ids:
            is_correct= predicted_id is None
        else:
            is_correct= predicted_id in expected_ids
        
        if is_correct:
            correct+=1
            status="PASS"

        else:
            status="FAIL"
            failed_queries.append({
                "query": query,
                "expected": expected_ids,
                "predicted": predicted_id
            })

        print(f"[{status}] {query}")
        print(f"    Expected: {expected_ids}")
        print(f"    Predicted: {predicted_id}")


    accuracy= (correct/total) *100 if total else 0

    print("\n" + "-" *40)
    print("        EVALUATION RESULTS")
    print("-"* 40)
    print(f"Total queries: {total}")
    print(f"Correct: {correct}")
    print(f"Incorrect: {total-correct}")
    print(f"Hit Rate@1: {accuracy:.2f}%")

    if failed_queries:
        print("\nFailed queries:")
        for item in failed_queries:
            print(f"- {item['query']}")
            print(f" Expected: {item['expected']}")
            print(f" Predicted: {item['predicted']}")

if __name__ =="__main__":
    evaluate()
            

    
            
        
    