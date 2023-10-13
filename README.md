# Plagiarism Checker using Natural Language Processing

## Overview

The Plagiarism Checker is a Python-based application that uses Natural Language Processing (NLP) techniques to compare and analyze two text documents for similarities, helping to identify potential plagiarism. This project provides a user-friendly Graphical User Interface (GUI) for users to input two text documents and receive a plagiarism similarity score, a list of repeated words, and a list of repeated sentences between the texts.

The project consists of the following key components:

1. **Text Preprocessing**: The application preprocesses the input texts by tokenizing, removing non-alphabetic characters, eliminating stopwords, lemmatizing words, and ensuring that the remaining words are valid English words. This preprocessing step prepares the text for further analysis.

2. **Similarity Calculation**: The application calculates the similarity between the two preprocessed texts using the Jaccard similarity coefficient, which measures the intersection and union of words in the texts. The similarity is expressed as a percentage.

3. **Repeated Words and Sentences**: The application identifies and displays the words that are repeated in both texts and the sentences that are repeated verbatim in the two documents.

4. **User Interface**: The application features a Tkinter-based GUI that allows users to input two text documents, trigger the comparison, and view the results.

![image](https://github.com/virajp4/CodeClauseInternship_Plagiarism-Checker/assets/122785879/0e4aad02-65cb-4e71-bc23-655525b888d5)

## How It Works

The Plagiarism Checker operates in the following manner:

1. **Text Input**: Users input two text documents (Text 1 and Text 2) using the provided text entry fields in the GUI.

2. **Text Comparison**: Clicking the "Check Plagiarism" button triggers the comparison process. The application analyzes the input texts to find similarities and repeated content.

3. **Results Display**: The application displays the following results on the GUI:
    - **Similarity Score**: The similarity score as a percentage, indicating how similar the two texts are.
    - **Repeated Words**: A list of words that are found in both texts.
    - **Repeated Sentences**: A list of sentences that are repeated verbatim in both texts.

## Dependencies

To run this project, you need the following Python libraries:

- **NLTK**: The Natural Language Toolkit is used for tokenization, stopwords removal, lemmatization, and wordnet access.
- **Tkinter**: Tkinter is used for building the graphical user interface.

You can install these dependencies using pip:

```bash
pip install nltk tkinter
```

## Usage

To use the Plagiarism Checker:

1. Run the script `plagiarism_checker.py`.
2. The GUI window will open, allowing you to input two text documents.
3. Click the "Check Plagiarism" button to compare the texts.
4. The application will display the similarity score, repeated words, and repeated sentences on the GUI.

## Conclusion

The Plagiarism Checker is a useful tool for identifying potential plagiarism and similarities between two text documents. By leveraging NLP techniques and a user-friendly GUI, this project offers an accessible way to analyze and compare textual content for academic, research, or content management purposes.