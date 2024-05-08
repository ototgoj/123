import re
from difflib import get_close_matches
import pymorphy3
morph = pymorphy3.MorphAnalyzer()
def preprocess_text(text):
    return text.lower().strip()
def preprocess_query(query_str):
    return re.sub(r'[^\w\s]', '', query_str).lower().strip()
def is_similar_word(word1, word2):
    return bool(get_close_matches(word1, [word2], n=1, cutoff=0.6))
def search(query_str, text):
    text = preprocess_text(text)
    query_str = preprocess_query(query_str)
    sentences = re.split(r'[.!?]', text)
    result = []
    for sentence in sentences:
        words = sentence.split()
        if query_str in words:
            result.append(sentence.strip())
        else:
            for word in words:
                if is_similar_word(query_str, word):
                    result.append(sentence.strip())
                    break

    return result

file_path = 'C:/Users/User/Desktop/mertvye-dushi.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
while True:
    query = input("Введите запрос: ")
    if not query:
        break
    result = search(query, text)
    print("Результат поиска:")
    for sentence in result:
        print(sentence)

