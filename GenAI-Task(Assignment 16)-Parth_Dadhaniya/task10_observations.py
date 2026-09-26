# Task 10: Technical Observations
# Author: Parth Dadhaniya

import sys

sys.stdout.reconfigure(encoding="utf-8")

print("1. Basic vs Advanced Cleaning:")
print("- Basic cleaning removes punctuation and numbers, but it breaks URLs and HTML tags into leftover garbage words (like 'httpsshopcom' or 'div').")
print("- Advanced cleaning uses regular expressions to completely delete full URLs, emails, HTML tags, and emojis before tokenizing.")

print("\n2. Lemmatization vs Stemming:")
print("- Stemming simply cuts off word endings using fixed rules. It is fast but often makes non-words like 'studies' -> 'studi' and 'leaves' -> 'leav'.")
print("- Lemmatization uses a dictionary and part of speech to find the true root word (lemma), giving real words like 'studies' -> 'study' and 'leaves' -> 'leaf'.")

print("\n3. Why Text Preprocessing is Important:")
print("- It removes noise (URLs, emails, emojis) that do not help in understanding the meaning.")
print("- It lowers vocabulary size, which makes machine learning models faster and saves memory.")
print("- It groups different forms of the same word (running, runs -> run) so the model learns better.")
