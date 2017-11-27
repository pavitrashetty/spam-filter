# A basic spam-filter
Crude Bayesian spam filter implementation in Python

The aim of this problem is get an idea about how to use Na ̈ıve Bayes Algorithm to build a text classifier from scratch.

Steps followed:
1. Read the essay [A plan for spam](http://www.paulgraham.com/spam.html) by Paul Graham. It will help you appreciate the intent of this assignment.
2. Get the 6 folders from the test data set (contact me for links).
3. Separate out the dataset based on the tags spam and ham.
4. Tokenize the data using some very basic assumptions. You can treat whitespace/newline as word delimiters.
5. Remove punctuation characters like .,;:!?&\/$%‘‘’’() etc. You may choose to keep other characters such as _-’ etc.
6. Now we will reduce our vocabulary(or the dimensionality of our problem). Remove stopwords from the texts. Contact me for a list.
7. Get token-counts for the two tags (ham and spam). Use appropriate data-structure to store this information.
8. Get Term Frequency(tf) and Document Frequency(df) for all tokens. These are basic statistics that will help us identify important words. Remove the tokens which have tf or df less than a certain threshold. Choice of tf or df depends on you.
9. Use some ideas either from the above blog post or your own to reduce the vocabulary further. This is optional.
10. Build a Na ̈ıve Bayes classifier. Use the first 5 folders as training dataset, and the 6th folder as the testing dataset.
11. Report Accuracy, Precision, Recall for the classifier.
