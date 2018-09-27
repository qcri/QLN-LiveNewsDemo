#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:26:09 2018

@author: baly
"""

# -*- coding: utf-8 -*-
import os
import json
import codecs
from feature_extraction.feature_functions import Functions


Functions = Functions()


def make_str(seq):
    return [str(s) for s in seq]


if __name__ == '__main__':

    text_type = 'title'  # could be title or body

    # Note to Israa: this is the directory where articles are stored
    directory = 'XXX'

    if not os.path.exists('features/'):
        os.mkdir('featDir/')

    featFile = 'features/features-title.csv' if text_type == 'title' \
        else '/features/features-body.csv'

    outpath = './'

    cat_dict, stem_dict, counts_dict = Functions.load_LIWC_dictionaries()
    liwc_cats = [cat_dict[cat] for cat in cat_dict]
    pos_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS',
                'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$',
                'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'WP$', 'WRB',
                'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP']

    seq = ('pid, source, date, Happiness, HarmVirtue, HarmVice, ' +
           'FairnessVirtue, FairnessVice, IngroupVirtue, IngroupVice, ' +
           'AuthorityVirtue, AuthorityVice, PurityVirtue, PurityVice, ' +
           'MoralityGeneral, bias_count, assertives_count, ' +
           'factives_count, hedges_count, implicatives_count, ' +
           'report_verbs_count, positive_op_count, negative_op_count, ' +
           'wneg_count, wpos_count, wneu_count, sneg_count, ' +
           'spos_count, sneu_count, TTR, vad_neg, vad_neu, vad_pos, FKE,' +
           'SMOG, stop, wordlen,WC, NB_pobj, NB_psubj, quotes, Exclaim,' +
           'AllPunc, allcaps',
           ','.join(pos_tags),
           ','.join(liwc_cats))

    with open(os.path.join(outpath, featFile), 'a') as out:
        out.write(','.join(seq) + '\n')

    num_features = sum([len(s.split(',')) for s in seq])

    for file in os.listdir(directory):

        # Note to Israa: I made these 'NA' as they relate to web source info
        pid = 'NA'
        cat = 'NA'
        date = 'NA'

        with codecs.open(os.path.join(directory, file)) as f:
            text_content = json.load(f)

        if text_type == 'title':
            text = Functions.fix(text_content['title'].strip())
        else:
            text = text_content['text']
            text = Functions.fix(' '.join([
                    L for L in text.split('\n') if L.strip() != '']))

        if len(text.strip()) == 0:
            # if text is not available, generate a set of zeros
            seq = ['0'] * num_features
        else:
            pos_features_path = './temp/'

            quotes, Exclaim, AllPunc, allcaps = \
                Functions.stuff_LIWC_leftout(cat, text)
            lex_div = Functions.ttr(text)
            counts_norm = \
                Functions.POS_features('input', text, pos_features_path)
            counts_norm = [str(c) for c in counts_norm]
            counts_norm_liwc, liwc_cats = \
                Functions.LIWC(text, cat_dict, stem_dict, counts_dict)
            counts_norm_liwc = [str(c) for c in counts_norm_liwc]
            vadneg, vadneu, vadpos = Functions.vadersent(text)
            fke, SMOG = Functions.readability(text)
            stop, wordlen, WC = Functions.wordlen_and_stop(text)
            NB_pobj, NB_psubj = Functions.subjectivity(text)
            bias_count, assertives_count, factives_count, hedges_count,\
                implicatives_count, report_verbs_count, positive_op_count,\
                negative_op_count, wneg_count, wpos_count, wneu_count,\
                sneg_count, spos_count,\
                sneu_count = Functions.bias_lexicon_feats(text)
            HarmVirtue, HarmVice, FairnessVirtue, FairnessVice,\
                IngroupVirtue, IngroupVice, AuthorityVirtue,\
                AuthorityVice, PurityVirtue, PurityVice,\
                MoralityGeneral = Functions.moral_foundation_feats(text)
            happiness = Functions.happiness_index_feats(text)

            seq = [pid, cat, date, happiness, HarmVirtue, HarmVice,
                   FairnessVirtue, FairnessVice, IngroupVirtue, IngroupVice,
                   AuthorityVirtue, AuthorityVice, PurityVirtue, PurityVice,
                   MoralityGeneral, bias_count, assertives_count,
                   factives_count, hedges_count, implicatives_count,
                   report_verbs_count, positive_op_count, negative_op_count,
                   wneg_count, wpos_count, wneu_count, sneg_count, spos_count,
                   sneu_count, lex_div, vadneg, vadneu, vadpos, fke, SMOG,
                   stop, wordlen, WC, NB_pobj, NB_psubj, quotes, Exclaim,
                   AllPunc, allcaps,
                   ','.join(counts_norm),
                   ','.join(counts_norm_liwc)]

            with open(os.path.join(outpath, featFile), 'a') as out:
                seq = make_str(seq)
                feat_str = ','.join(seq)
                out.write(feat_str + '\n')
