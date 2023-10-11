import tkinter as tk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

# Function to preprocess text
def preprocess_text(text):
    
    # Tokenize the text and preprocess it
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]  # Filter out non-alphabetic tokens
    tokens = [token for token in tokens if token not in stopwords.words('english')]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize tokens
    tokens = [token for token in tokens if wn.synsets(token)]  # Filter out non-English words
    return tokens

# Function to calculate similarity between two texts
def calculate_similarity(tokens1, tokens2):
    
    # Calculate the similarity based on the intersection and union of tokens
    intersection = len(set(tokens1) & set(tokens2))
    union = len(set(tokens1) | set(tokens2))
    similarity_percentage = (intersection / union) * 100
    return similarity_percentage

# Function to find repeated sentences between two texts
def find_repeated_sentences(text1, text2):
    sentences1 = sent_tokenize(text1)
    sentences2 = sent_tokenize(text2)
    repeated_sentences = [sentence for sentence in sentences1 if sentence in sentences2]
    return repeated_sentences

# Function to compare two texts and display the results
def compare_texts(text1, text2):
    tokens1 = preprocess_text(text1)
    tokens2 = preprocess_text(text2)

    similarity_percentage = calculate_similarity(tokens1, tokens2)
    matched_words = list(set(tokens1) & set(tokens2))
    repeated_sentences = find_repeated_sentences(text1, text2)
    
    return similarity_percentage, matched_words, repeated_sentences

# Function to trigger text comparison
def check_similarity():
    text1 = entry1.get("1.0", "end-1c")
    text2 = entry2.get("1.0", "end-1c")
    
    similarity_percentage, matched_words, repeated_sentences = compare_texts(text1, text2)
    
    result_label.config(text=f"Similarity: {similarity_percentage:.2f}%")
    words_label.config(text=f"Repeated words: {', '.join(matched_words)}" if matched_words else "No repeated words")
    sentences_label.config(text=f"Repeated sentences: {', '.join(repeated_sentences)}" if repeated_sentences else "No repeated sentences")

# Create a GUI window
window = tk.Tk()
window.title("Plagiarism Checker")

# Create text entry fields
entry1 = tk.Text(window, height=10, width=40)
entry2 = tk.Text(window, height=10, width=40)

# Create labels to display the results
result_label = tk.Label(window, text="", bg="black", fg="green", font=("", 15), wraplength=200)
words_label = tk.Label(window, text="", bg="black", fg="red", font=("", 11), wraplength=200)
sentences_label = tk.Label(window, text="", bg="black", fg="red", font=("", 13), wraplength=200)

# Create a comparison button
compare_button = tk.Button(window, text="Check Plagiarism", command=check_similarity, font=("", 15))

# Arrange widgets using grid layout
tk.Label(window, text="Text 1", bg="black", fg="white", font=("", 15)).grid(row=0, column=0, pady=10)
tk.Label(window, text="Text 2", bg="black", fg="white", font=("", 15)).grid(row=0, column=1, pady=10)
entry1.grid(row=1, column=0, padx=10)
entry2.grid(row=1, column=1, padx=10)
compare_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2)
sentences_label.grid(row=4, column=0, columnspan=2)
words_label.grid(row=5, column=0, columnspan=2)

# add background color to the window
window.configure(bg='black')

# Start the GUI main loop
window.mainloop()