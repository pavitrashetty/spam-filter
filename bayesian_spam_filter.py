import numpy
import scipy
import os
import collections
'''
STEPS:
- We have preprocessed messages in our test data directory.

- Separate this data using tags `spam` and `ham`.

- Tokenize the data. Whitespace and newline are delimiters.
- Remove special characters, except _ and -
- Remove stopwords using the list in test data directory.
- We get a list of unique tokens.

- Get each token count for Spam and Ham. We can have 2 tables - Spam and Ham. 
1st column is the token, 2nd column is the count. Or 2 arrays of dicts - keys are token and count.

- Calculate TF and DF for each token. We can store it in a 3rd DS, array of dicts - keys are token, TF and DF.
- TF = number of times token appears in entire data set.
- DF = number of documents that contain the token.
- Remove tokens below some threshold - to be determined.

- Baki baad me.
'''

stop_words = []
good_tokens = []
bad_tokens = []


def get_stop_words(path):
    with open(path, 'r') as f:
        for line in f:
            for word in line.split():
                stop_words.append(word)


def list_directory(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def tokenize(folder_path):
    tokens = []
    for filename in list_directory(folder_path):
        with open(os.path.join(folder_path, filename), 'r') as f:
            for line in f:
                for word in line.split():
                    w = word
                    # TODO: remove special characters
                    # w = ''.join(c for c in word if c.isalnum())
                    # re.sub('[^A-Za-z0-9]-_+', '', word)
                    if w not in stop_words:
                        tokens.append(w)
    return tokens


def read_files():
    base_folder = '/Users/pavitra/Practice/spam-filter/test_data/enron'
    for n in range(1, 2):
        folder_path = base_folder + str(n)
        ham_folder = folder_path + '/ham'
        spam_folder = folder_path + '/spam'

        global good_tokens
        good_tokens = tokenize(ham_folder)
        global bad_tokens
        bad_tokens = tokenize(spam_folder)


def build_hash_tables(token_list):
    print token_list
    freq = []
    unique_words = sorted(set(token_list))
    print 'unique words = {0}'.format(unique_words)
    '''
    for word in unique_words:
        freq.append({'token': word, 'count': token_list.count(word)})
    '''
    return freq


if __name__ == "__main__":
    get_stop_words('/Users/pavitra/Practice/spam-filter/test_data/stopwords')
    read_files()
    print 'len1: {0}'.format(len(good_tokens))
    print 'len1: {0}'.format(len(bad_tokens))
    # ham_hash = build_hash_tables(good_tokens)
    spam_hash = build_hash_tables(bad_tokens)
