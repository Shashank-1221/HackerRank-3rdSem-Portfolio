import math

def compareTriplets(a, b):
    score_a = 0
    score_b = 0
    
    for i in range(3):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
            
    return [score_a, score_b]

if __name__ == '__main__':
    alice_scores = [5, 6, 7]
    bob_scores = [3, 6, 10]
    
    result = compareTriplets(alice_scores, bob_scores)
    print("Triplets Comparison Scores [Alice, Bob]:", result)