# You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. The most relevant sentence is the one with the maximum number of matching words with the query.
# Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
# Input:
# Please input your query string
# “Python is”
# Output:
# 3 results found:
# python is not python snake
# python is good
# Python is cool

def macthing_Words(sentence_1, sentence_2):
    words_1 = sentence_1.split(" ")
    words_2 = sentence_2.split(" ")
    matching_score = 0
    for word_1 in words_1:
        for word_2 in words_2:
            # print(f"Matching {word_1} with {word_2}")
            if word_1.lower() == word_2.lower():
                matching_score += 1
    return matching_score

if __name__ == "__main__":
    # macthing_Words("This is good", "python is good")
    sentences = ["python is a good", "this is snake","python is not python snake"]
    query = input("Enter the query string: ")
    total_score = [macthing_Words(query,sentence) for sentence in sentences]
    # print(total_score)
    sorted_sentence_score = [sentence_score for sentence_score in sorted(zip(total_score, sentences), reverse=True) if sentence_score[0] != 0]
    # print(sorted_sentence_score)
    print(f"{len(sorted_sentence_score)} results found!")
    for matching_score, item in sorted_sentence_score:
        print(f"\"{item}\": with a score of {matching_score}")