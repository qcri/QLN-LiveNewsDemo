
from sklearn.base import TransformerMixin
from nltk.tokenize import word_tokenize
import numpy as np
import codecs


# this is a custom transformer that does the following:

# finds the number of lexical occurences for each lexicon
# final output (return value ) will look like:
#________________________________________________________________________
# doc   occurences from:  lexicon1   lexicon2   lexicon3 , .....
# doc1                    12         2          0
# doc2                    0          5          20
# doc3                    4          2          0
# ...
#________________________________________________________________________
class counts_vectorizer(TransformerMixin): # any custom transformer needs to inherit sklearn transformMixin or any python class that implements .fit method
    def __init__(self,lexicons):
        self.lexicons =[]
        for lexicon in lexicons:
            self.lexicons.append(self.load_lexicon(lexicon))
        self.feature_names = ['action_adverbs','assertives','comparatives','first_person','hear','hedges','manner_adverbs','modal_adverbs','money','negations','number','second_person','see','sexual','strong_subjective','superlatives','swear','weak_subjective']
    def transform(self,X):
        counts = []
        vects =[]

        for doc in X:
            for lexicon in self.lexicons:
                counts.append(self.extract_lexical_counts(doc,lexicon))
            vects.append([counts])
            counts = []
        matrix = np.array(vects).reshape(len(X),len(self.lexicons))
        return matrix


    def fit(self):
        return self

    def fit_transform(self,X):
        self.fit()
        return self.transform(X)

    def get_feature_names(self):
        return self.feature_names

    def extract_lexical_counts(self,doc, lexicon):
        tokens = word_tokenize(doc.lower())
        count = 0
        for vocab in lexicon:
            count += tokens.count(vocab)  # count the number of all vocab in the whole document (document = a list of tokens)
        return count

    def load_lexicon(self,file):
        #print('Loading lexicon from ' + file + ' ...')
        lexicon = []
        with codecs.open(file, 'r', 'utf-8') as f:
            for line in f:
                line = line.strip()
                lexicon.append(line)
            f.close()
            return lexicon





