import math

def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    result_answers = []
    
    for query_type, x_val, y_val in queries:
        target_index = (x_val ^ last_answer) % n
        
        if query_type == 1:
            seq_list[target_index].append(y_val)
        elif query_type == 2:
            element_index = y_val % len(seq_list[target_index])
            last_answer = seq_list[target_index][element_index]
            result_answers.append(last_answer)
            
    return result_answers

if __name__ == '__main__':
    n = 2
    sample_queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ]
    
    result = dynamicArray(n, sample_queries)
    print("Dynamic Array Result:", result)