import os
import codecs
import json
import argparse
#from feature_extraction.resources.readability import Readability
from feature_extraction.feature_functions import Functions
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


DIRNAME = os.path.dirname('__file__')
TEXT_TYPE = 'title'
MIN_LINKS = 2


def whatsbeendon(filename):
    pids = []
    try:
        with open(filename) as data:
            pids = [line.strip().split(',')[0] for line in data]
        return set(pids)
    except:
        return set(pids)


def make_str(seq):
    return [str(s) for s in seq]

Functions = Functions()
outfile = 'features-title.csv' if TEXT_TYPE == 'title' else 'features-body.csv'
outpath = "./"
done = whatsbeendon(outfile)
articlesDir = 'articles/mbfc/'

sources_dictionary = {}
with open(articlesDir + 'mappings.txt') as f:
    for line in f.readlines():
        array = line.strip().split('\t')
        sources_dictionary.update({array[0]: (array[1], array[2])})

cat_dict, stem_dict, counts_dict = Functions.load_LIWC_dictionaries()
liwc_cats = [cat_dict[cat] for cat in cat_dict]
pos_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD',
            'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB',
            'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'WP$', 'WRB', 'VB', 'VBD',
            'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP']

if len(done) == 0:
    with open(os.path.join(outpath, outfile), 'a') as out:
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
        out.write(','.join(seq) + '\n')

num_features = sum([len(s.split(',')) for s in seq])

num_files = 0
for dirName, subdirList, fileList in os.walk(articlesDir):
    fileList = [file for file in fileList if file[0] != '.']
    if len(fileList) < MIN_LINKS:
        continue
    num_files += len(fileList)

file_count = 0
empty_text_count = 0

for dirName, subdirList, fileList in os.walk(articlesDir):
    path = dirName + '/'
    cat = dirName.split('/')[-1]  # source

    # remove the .DS_Store file
    fileList = [file for file in fileList if file[0] != '.']

    # skip links that has less than the minimum required number of articles
    if len(fileList) < MIN_LINKS:
        continue

    # make sure that "cat" exists in the list of processed links
    assert cat in [sources_dictionary[key][0]
                   for key in sources_dictionary.keys()], 'missing directory'

    print('({}/{})\t'.format(file_count, num_files), 'working on', cat)

    for fn in fileList:
        file_count += 1
        date = 'NA'  # fn.split("--")[1]
        pid = cat + '__' + fn.split('.')[0]

        if pid in done:
            continue

        with codecs.open(path + fn) as f:
            text_content = json.load(f)

        if TEXT_TYPE == 'title':
            text = Functions.fix(text_content['title'].strip())
        else:
            text = Functions.fix(' '.join([line for line in
                                           text_content['text'].split('\n')
                                           if line.strip() != '']))

        if len(text) == 0:
            seq = ['0'] * num_features
            empty_text_count += 1
        else:
            pos_features_path = './temp/'

            quotes, Exclaim, AllPunc, allcaps = \
                Functions.stuff_LIWC_leftout(pid, text)

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

            bias_count, assertives_count, factives_count, hedges_count, \
                implicatives_count, report_verbs_count, positive_op_count, \
                negative_op_count, wneg_count, wpos_count, wneu_count, \
                sneg_count, spos_count, \
                sneu_count = Functions.bias_lexicon_feats(text)

            HarmVirtue, HarmVice, FairnessVirtue, FairnessVice, \
                IngroupVirtue, IngroupVice, AuthorityVirtue, AuthorityVice, \
                PurityVirtue, PurityVice, \
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

        with open(os.path.join(outpath, outfile), 'a') as out:
            seq = make_str(seq)
            feat_str = ','.join(seq)
            out.write(feat_str + '\n')

print('number of items with empty text: {}'.format(empty_text_count))
