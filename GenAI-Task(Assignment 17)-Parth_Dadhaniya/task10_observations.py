# Task 10: Observations & Insights
# Author: Parth Dadhaniya

print("1. Difference between Basic and Advanced Cleaning:")
print("- Basic cleaning only converts text to lowercase and strips punctuation and numbers. On web text, it leaves broken URL pieces (like 'httpsmoviehubcom') and leftover HTML tag letters ('div' or 'p').")
print("- Advanced cleaning uses regular expressions to remove complete entities like URLs, email addresses, HTML markup tags, and emojis before words are split, keeping the vocabulary free from junk tokens.")

print("\n2. Why Lemmatization is Preferred over Stemming:")
print("- Stemming simply cuts off word endings using fixed rules, which often creates non-words (e.g. 'studies' -> 'studi' and 'leaves' -> 'leav').")
print("- Lemmatization uses vocabulary and parts of speech (POS) to find the true dictionary root (e.g. 'studies' -> 'study', 'leaves' -> 'leaf', 'better' -> 'good').")
print("- In NLP models, lemmatization preserves word meanings and keeps tokens grammatically valid.")

print("\n3. Importance of Preprocessing in NLP Models:")
print("- It removes noise (URLs, emails, emojis) that do not help in understanding meaning.")
print("- It reduces vocabulary size, which makes machine learning models faster and saves RAM.")
print("- It groups different forms of the same word (running, runs -> run) so models learn better patterns.")
