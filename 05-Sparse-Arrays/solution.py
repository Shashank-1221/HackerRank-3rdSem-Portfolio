import math

def matchingStrings(stringList, queries):
    frequency_map = {}
    
    for word in stringList:
        frequency_map[word] = frequency_map.get(word, 0) + 1
        
    results = []
    for query in queries:
        results.append(frequency_map.get(query, 0))
        
    return results

if __name__ == '__main__':
    sample_strings = ['ab', 'ab', 'abc']
    sample_queries = ['ab', 'abc', 'bc']
    
    result = matchingStrings(sample_strings, sample_queries)
    print("Sparse Arrays Matching Frequencies:", result)