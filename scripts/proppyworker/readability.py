

import math
import nltk.data
import logging
import numpy as np
import string

from nltk import word_tokenize
from sklearn.base import BaseEstimator, TransformerMixin

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class Readability_vectorizer(TransformerMixin):

    # Considering no more than 100 words is recommended for the
    # computation of the Gunning Fog index.
    MAX_CONSIDERED_WORDS = 100

    # We need to split sentences in English and we do it here
    # (the model comes from NLTK)"""
    PATH_TO_ENGLISH_SENTENCE_MODEL = 'tokenizers/punkt/english.pickle'

    def __init__(self):
        self.feature_names = ["lesch_kincaid_grade_level",
                              "flesch_reading_ease",
                              "self.gunning_fog_index"
                              ]

    def transform(self, X):

        features = []
        for doc in X:
            self._process_text(doc)
            # if self.counters['words'] == 0:
            # print doc
            # print self.counters
            features.append([self.flesch_kincaid_grade_level(),
                             self.flesch_reading_ease(),
                             self.gunning_fog_index()])
        vector = np.array(features)
        logging.info("Readability features computed")
        return vector

    def fit(self):
        return self

    def fit_transform(self, X):
        self.fit()
        return self.transform()

    def get_feature_names(self):
        return self.feature_names

    def flesch_kincaid_grade_level(self):
        """
        Implementation of the Flesch Kincaid Grade Level test. It results on a
        number which should be interpreted as US grade level (similar to Gunning).

        More info at https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level
        """
        fkgl = ( (0.39 * self.counters['words'] / self.counters['sentences'])
               + (11.8 * self.counters['syllables'] / self.counters['words'])
               - 15.59 )
        return fkgl

    def flesch_reading_ease(self):
        """
        Flesch reading ease test which measures the difficulty to understand a
        text. Whereas the range of this metric is unbounded, the lower the more
        difficult to read. Typical values are as follows:

        100.-90.00 	5th grade
        90.0–80.0 	6th grade
        80.0–70.0 	7th grade
        70.0–60.0 	8th & 9th grade
        60.0–50.0 	10th to 12th grade
        50.0–30.0 	College
        30.0–0.0 	College graduate

        More info at https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease
        """
        # fres = 206.835 - (1.015 * count_words / count_sentences) - (84.6 * count_syllables / count_words)
        fres = (206.835
                - (1.015 * self.counters['words'] / self.counters['sentences'])
                - (84.6 * self.counters['syllables'] / self.counters['words'])
        )
        return fres

    def gunning_fog_index(self):
        """
        Implementation of the Gunning Fog Index readability text. It estimates the
        years of formal education necessary to understand a given text. The rough
        values are as follows:
            17 	College graduate
            16 	College senior
            15 	College junior
            14 	College sophomore
            13 	College freshman
            12 	High school senior
            11 	High school junior
            10 	High school sophomore
            9 	High school freshman
            8 	Eighth grade
            7 	Seventh grade
            6 	Sixth grade
        More information in https://en.wikipedia.org/wiki/Gunning_fog_index
        """
        gf_index = 0.4 * (
                (self.counters['words'] / self.counters['sentences']) +
                (100 * self.counters['complex_words'] / self.counters['words'])
                )
        return gf_index

    def _get_sentences(self, this_text):
        """
        Splits the free text into sentences.
        Currently it used nltk's punkt model for English
        :param this_text:
        :return: list of sentences
        """
        return self.sentence_splitter.tokenize(this_text)

    def _count_syllables(self, word):
        """
        Adapted from Tersosauros at
        https://stackoverflow.com/questions/405161/detecting-syllables-in-a-word

        Three rules from the Gunning fog index are added: suffixes -es, -ed,
        and -ing are not counted (Tersosauros' original implementation
        discarded es only)
        TODO add a test
        :param word:
        :return: number of syllables in the word
        """
        vowels = "aeiouy"
        numVowels = 0
        lastWasVowel = False
        for wc in word:
            foundVowel = False
            for v in vowels:
                if v == wc:
                    if not lastWasVowel: numVowels+=1   # don't count diphthongs
                    foundVowel = lastWasVowel = True
                    break
            if not foundVowel:  # If full cycle and no vowel found, set lastWasVowel to false
                lastWasVowel = False

        # Originally as the one commented. Added -ed and -ing as for the Gunning computation instructions
        # if len(word) > 2 and word[-2:] == "es": # Remove es - it's "usually" silent (?)
        if len(word) > 3 and word[-3:] == "ing":
            numVowels -= 1
        elif len(word) > 2 and (word[-2:] in ["es", "ed"]):
            numVowels -= 1
        elif len(word) > 1 and word[-1:] == "e":    # remove silent e
            numVowels -= 1
        return numVowels

    def _process_text(self, text):
        self.sentence_splitter = nltk.data.load(self.PATH_TO_ENGLISH_SENTENCE_MODEL)

        count_words, count_sentences, count_complex_words, count_syllables = 0, 0, 0, 0
        sentences = self._get_sentences(text)
        for sentence in sentences:
            if count_words >= self.MAX_CONSIDERED_WORDS:
                break  # We have more than MAX_WORDS_GUNNING. We do not need to consider more text

            count_sentences += 1
            # Tokenize and remove punctuation marks at once.
            tokens = [w for w in word_tokenize(sentence) if w not in string.punctuation]
            count_words += len(tokens)
            count_complex_words += len([w for w in tokens if self._word_is_complex(w)])
            count_syllables += sum([self._count_syllables(token) for token in tokens])

        self.counters = {
            'complex_words': count_complex_words,
            'sentences': count_sentences,
            'words': count_words,
            'syllables': count_syllables
            }

    def _word_is_complex(self, word):
        """
        :param word:
        :return: True if the word contains 3 or more syllables
        """
        return self._count_syllables(word) >= 3


class LexicalStyle_vectorizer(TransformerMixin):

    # TODO perhaps we should limit the lengths of the texts here as well
    def __init__(self):
        self.feature_names = ["ttr",
                              "hapax_legomena",
                              "hapax_dislegomena",
                              "honore_R",
                              "yule_K"]

    def transform(self, X):
        # COMPUTE THE FEATURES
        print('Computing lexical style features...')
        counts = []
        for doc in X:
            # on row; in my case a matrix [5x16000]
            # first try with a vector and then with features
            self._process_text(doc)
            counts.append([self.ttr(),
                           self.hapax_legomena(),
                           self.hapax_dislegomena(),
                           self.honore_R(),
                           self.yule_K()])
        # return transformations (value for each documen).
        # (16,000 array for training)
        # print(counts)
        vect = np.array(counts)#.reshape(-1,1)
        logging.info("Lexical features computed")
        return vect

    def fit(self):
        return self

    def fit_transform(self, X):
        self.fit()
        return self.transform(X)

    def get_feature_names(self):
        return self.feature_names

    def ttr(self):
        """
        Type-token ratio (types/tokens). The number of types id divided by the number of
        tokens. Described in Stamatatos' 2.1
        :return:
        """
        try:
            return float(self.counter['types']) / self.counter['tokens']
        except ZeroDivisionError:
            return 0

    def hapax_legomena(self):
        """
        We compute the number of hapax_legomena and normalize by the
        number of types.

        :return: number of types appearing only once in the text (normalized)
        """
        try:
            return float(self.counter['hapax_legomena']) / self.counter['types']
        except ZeroDivisionError:
            return 0

    def hapax_dislegomena(self):
        """
        We compute the number of hapax_dislegomena and normalize by the
        number of types.

        :return: number of types appearing twice in the text (normalized)
        """
        return float(self.counter['hapax_dislegomena']) / self.counter['types']

    def honore_R(self):
        """
        Computes Honore's Function R:
              100 * log(|tokens\)
           ------------------------
            1 - \hapax_leg\/\types\
        The higher the value of R, the richer the vocabulary. According
        to [1] Honoré considers that |tokens| should be 1300 for the
        computation to stabilize.

        [1] https://www.physics.smu.edu/pseudo/ScienceReligion/MormonStylometric.pdf
        :return:
        """
        try:
            return 100 * math.log(self.counter['tokens']) / (
                    1 - (self.counter['hapax_legomena'] / self.counter['types']))
        except ZeroDivisionError:
            return 0

    def yule_K(self):
        """
        Yule's K, defined as
        K = 10^4 (\sum i^2V_i - N) / N^2 for i=1,2,...
        According to [1]
        [1] https://www.physics.smu.edu/pseudo/ScienceReligion/MormonStylometric.pdf
        :return:
        """

        summ = sum([i**2 * self.counter['all'][i] for i in self.counter['all']])
        k = 10**4 * (summ - self.counter['tokens']) / self.counter['tokens']**2
        return k

    def _get_tokens(self, text):
        return [w for w in word_tokenize(text) if w not in string.punctuation]

    def _process_text(self, text):
        """
        Produces counters for tokens, types, and legomena.
        In this implementation punctuation marks are discarded.
        :param text:
        :return:
        """
        #print (text)
        #print ('---------------')
        tokens = [w for w in word_tokenize(text) if w not in string.punctuation]
        type_freqs = {}
        for token in tokens:
            try:
                type_freqs[token] += 1
            except KeyError:
                type_freqs[token] = 1

        # Counting the number of types appearing i times for all i
        counter_all = {}

        for i in range(1, max(max(type_freqs.values()) + 1, 3) ):
            counter_all[i] = 0.0
            counter_all[i] += sum([1 for x in type_freqs if type_freqs[x] == i])

        self.counter = {
            'tokens': float(len(tokens)),
            'types': float(len(type_freqs)),
            'hapax_legomena': counter_all[1],   # hapax_legomena_count,
            'hapax_dislegomena': counter_all[2],# hapax_dislegomena_count
            'all': counter_all
        }


#
# document = \
# """Subfossil lemurs are primates from Madagascar, especially the extinct giant lemurs,
# represented by subfossils (partially fossilized remains) dating from nearly 26,000 to around
# 560 years ago. Almost all of these species, including the sloth lemurs, koala lemurs and monkey
# lemurs, were living around 2,000 years ago, when humans first arrived on the island. The extinct
# species are estimated to have ranged in size from slightly over 10 kg (22 lb) to roughly 160 kg
# (350 lb). The subfossil sites found around most of the island demonstrate that most giant lemurs
# had wide distributions. Like living lemurs, they had poor day vision and relatively small brains,
# and developed rapidly, but they relied less on leaping, and more on terrestrial locomotion, slow
# climbing, and suspension. Although no recent remains of giant lemurs have been found, oral
# traditions and reported recent sightings by Malagasy villagers suggest that there may be lingering
# populations or very recent extinctions. """
#
# lexstyle = LexicalStyle_vectorizer(document)
# print "Type/token ratio:", lexstyle.ttr(document)
# print "Hapax legomena:", lexstyle.hapax_legomena()
# print "Hapax dislegomena:", lexstyle.hapax_dislegomena()
# print "Honore's R:", lexstyle.honore_R()
# print "Yule's K:", lexstyle.yule_K()


# document = \
# """Subfossil lemurs are primates from Madagascar, especially the extinct giant lemurs,
# represented by subfossils (partially fossilized remains) dating from nearly 26,000 to around
# 560 years ago. Almost all of these species, including the sloth lemurs, koala lemurs and monkey
# lemurs, were living around 2,000 years ago, when humans first arrived on the island. The extinct
# species are estimated to have ranged in size from slightly over 10 kg (22 lb) to roughly 160 kg
# (350 lb). The subfossil sites found around most of the island demonstrate that most giant lemurs
# had wide distributions. Like living lemurs, they had poor day vision and relatively small brains,
# and developed rapidly, but they relied less on leaping, and more on terrestrial locomotion, slow
# climbing, and suspension. Although no recent remains of giant lemurs have been found, oral
# traditions and reported recent sightings by Malagasy villagers suggest that there may be lingering
# populations or very recent extinctions. """
#
# readability = Readability(document)
# print "Gunning Fog Index:", readability.gunning_fog_index(document)
# print "FK grade level:", readability.flesch_kincaid_grade_level(document)
# print "F reading ease", readability.flesch_reading_ease(document)