import pdfplumber
import nltk
from nltk.corpus import wordnet
import pandas as pd
import os

# Download NLTK data (safe to call repeatedly)
nltk.download('wordnet')
nltk.download('punkt')

pdf_path = r"W:\item.pdf"

output_file = r"W:\item.txt"

results = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()

        if not text:
            continue  # skip empty pages

        print(f"\n--- Page {page_num} ---")
        print(text[:200])  # preview only

        # Tokenize
        words = nltk.word_tokenize(text)
        unique_words = set(words)

        for word in unique_words:
            synsets = wordnet.synsets(word)
            synonyms = set()

            for syn in synsets:
                for lemma in syn.lemmas():
                    synonyms.add(lemma.name())

            # Limit output to keep readable
            if synonyms:
                synonyms_list = list(synonyms)[:5]  # first 5 only

                results.append({
                    "page": page_num,
                    "word": word,
                    "synonyms": ", ".join(synonyms_list)
                })

# Convert to DataFrame
df = pd.DataFrame(results)

# Save output
df.to_csv(output_file, index=False)

print(f"\n✅ Output saved to: {output_file}")
print(df.head())
