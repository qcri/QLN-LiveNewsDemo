
from sklearn.base import TransformerMixin
from feature_extraction.feature_functions import Functions
import numpy as np

class nela_vectorizer(TransformerMixin): # any custom transformer needs to inherit sklearn transformMixin or any python class that implements .fit method
    def __init__(self):
        self. Functions = Functions()
        self.cat_dict, self.stem_dict, self.counts_dict = self.Functions.load_LIWC_dictionaries('feature_extraction/resources/')
        self.liwc_cats = [self.cat_dict[cat] for cat in self.cat_dict]
        self.pos_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS',
                    'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$',
                    'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'WP$', 'WRB',
                    'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP']

        self.seq = ('Happiness, HarmVirtue, HarmVice, ' +
               'FairnessVirtue, FairnessVice, IngroupVirtue, IngroupVice, ' +
               'AuthorityVirtue, AuthorityVice, PurityVirtue, PurityVice, ' +
               'MoralityGeneral, bias_count, assertives_count, ' +
               'factives_count, hedges_count, implicatives_count, ' +
               'report_verbs_count, positive_op_count, negative_op_count, ' +
               'wneg_count, wpos_count, wneu_count, sneg_count, ' +
               'spos_count, sneu_count, TTR, vad_neg, vad_neu, vad_pos, FKE,' +
               'SMOG, stop, wordlen,WC, NB_pobj, NB_psubj, quotes, Exclaim,' +
               'AllPunc, allcaps',
               ','.join(self.pos_tags),
               ','.join(self.liwc_cats))

        self.num_features = sum([len(s.split(',')) for s in self.seq])
        self.feature_names = self.seq

    def transform(self,X):
        vects = []
        for article in X:

            #article = Functions.fix(' '.join([L for L in article.split('\n') if L.strip() != '']))
            if len(article.strip()) == 0:
                # if text is not available, generate a set of zeros
                seq = ['0'] * self.num_features
            else:
                pos_features_path = 'feature_extraction/temp/'

                quotes, Exclaim, AllPunc, allcaps = self.Functions.stuff_LIWC_leftout('ERROR',article)
                lex_div = float(self.Functions.ttr(article))
                counts_norm = self.Functions.POS_features('input', article, pos_features_path)
                #counts_norm = [str(c) for c in counts_norm]
                counts_norm_liwc, liwc_cats = self.Functions.LIWC(article, self.cat_dict, self.stem_dict, self.counts_dict)
                #counts_norm_liwc = [str(c) for c in counts_norm_liwc]
                vadneg, vadneu, vadpos = self.Functions.vadersent(article)
                fke, SMOG = self.Functions.readability(article)
                stop, wordlen, WC = self.Functions.wordlen_and_stop(article)
                NB_pobj, NB_psubj = self.Functions.subjectivity(article)
                bias_count, assertives_count, factives_count, hedges_count, \
                implicatives_count, report_verbs_count, positive_op_count, \
                negative_op_count, wneg_count, wpos_count, wneu_count, \
                sneg_count, spos_count, \
                sneu_count = self.Functions.bias_lexicon_feats(article)
                HarmVirtue, HarmVice, FairnessVirtue, FairnessVice, \
                IngroupVirtue, IngroupVice, AuthorityVirtue, \
                AuthorityVice, PurityVirtue, PurityVice, \
                MoralityGeneral = self.Functions.moral_foundation_feats(article)
                happiness = float(self.Functions.happiness_index_feats(article))

                seq = [happiness, HarmVirtue, HarmVice,
                       FairnessVirtue, FairnessVice, IngroupVirtue, IngroupVice,
                       AuthorityVirtue, AuthorityVice, PurityVirtue, PurityVice,
                       MoralityGeneral, bias_count, assertives_count,
                       factives_count, hedges_count, implicatives_count,
                       report_verbs_count, positive_op_count, negative_op_count,
                       wneg_count, wpos_count, wneu_count, sneg_count, spos_count,
                       sneu_count, lex_div, vadneg, vadneu, vadpos, fke, SMOG,
                       stop, wordlen, WC, NB_pobj, NB_psubj, quotes, Exclaim,
                       AllPunc, allcaps]+ counts_norm+counts_norm_liwc
                       # ','.join(counts_norm),
                       # ','.join(counts_norm_liwc)]
            vects.append(seq)
        matrix = np.array(vects).reshape(len(X),len(seq))
        return matrix


    def fit(self):
        return self

    def fit_transform(self,X):
        self.fit()
        return self.transform(X)

    def get_feature_names(self):
        return self.feature_names

    def make_str(seq):
        return [str(s) for s in seq]




