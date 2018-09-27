import codecs
import json

def replace_separator(data_file):
    with codecs.open(data_file, 'r') as f:
        with codecs.open(data_file+'-fixed.txt', 'w') as out:
            for line in f:
                line = line.replace(',','\t',1) # replace the first comma separator with a tab separator (only the first occurence)
                out.write(line)
            out.close()
            f.close()

def separate_liwc_lexicons(file):
    with codecs.open(file,'r') as f:
        swear =[]
        hear = []
        sexual =[]
        see =[]
        negations =[]
        number = []
        money =[]
        first_pers_sing =[]
        sec_pers =[]
        for line in f:
            line=line.strip()
            fields= line.split('\t')
            if '121' in fields:
                swear.append(fields[0])
            if '62' in fields:
                hear.append(fields[0])
            if '73' in fields:
                sexual.append(fields[0])
            if '61' in fields:
                see.append(fields[0])
            if '15' in fields:
                negations.append(fields[0])
            if '24' in fields:
                number.append(fields[0])
            if '113' in fields:
                money.append(fields[0])
            if '4' in fields:
                first_pers_sing.append(fields[0])
            if '6' in fields:
                sec_pers.append(fields[0])
        f.close()
        i=1
        for lex in [swear,hear,sexual,see,negations,number,money,first_pers_sing,sec_pers]:
            with codecs.open('../data/lexicons/'+str(i)+'.txt', 'w') as out:
                for word in lex:
                    word=word.replace('*','')
                    out.write(word+'\n')
                out.close()
                i+=1

def separate_subjectives(file):
    with codecs.open(file, 'r') as f:
        weak_subj=[]
        strong_subj=[]
        for line in f:
            line=line.strip()
            fields = line.split(' ')
            subj = fields[0].split('=')
            word_fields = fields[2].split('=')
            word = word_fields[1]
            if subj[1] == 'weaksubj':
                weak_subj.append(word)
            elif subj[1] == 'strongsubj' :
                strong_subj.append(word)
        f.close()
        with codecs.open ('../data/lexicons/weak_subj_wilson.txt','w') as out:
            for sub in weak_subj:
                out.write(sub+'\n')
            out.close()
        with codecs.open('../data/lexicons/strong_subj_wilson.txt','w') as out:
            for sub in strong_subj:
                out.write(sub+'\n')
            out.close()


def from_josn_to_tsv(file):

    articles = json.load(open(file))
    with codecs.open(file+'.converted.tsv', 'w', encoding='utf8') as out:

        for a in articles:
            if a['html_text'].strip() == "":
                continue
            # fixing text (removing new lines and tabs)
            a['gdlt_actionGeo']= a['gdlt_actionGeo'].strip()
            a['gdlt_avgTone'] = a['gdlt_avgTone'].strip()
            a['gdlt_day'] = a['gdlt_day'].strip()
            a['gdlt_id'] = a['gdlt_id'].strip()
            a['gdlt_RL'] = a['gdlt_RL'].strip()
            a['html_authors'] = a['html_authors'].strip()
            a['html_text'] = a['html_text'].strip()
            a['html_text'] = a['html_text'].replace("\n", " ")
            a['html_text'] = a['html_text'].replace("\t", " ")
            a['html_title'] = a['html_title'].strip()
            a['html_title'] = a['html_title'].replace("\n", " ")
            a['html_title'] = a['html_title'].replace("\t", " ")
            a['mbfc_class'] = a['mbfc_class'].strip()
            a['mbfc_link'] = a['mbfc_link'].strip()
            a['mbfc_link'] = a['mbfc_link'].replace("\n", " ")
            a['mbfc_link'] = a['mbfc_link'].replace("\t", " ")
            a['mbfc_name'] = a['mbfc_name'].strip()
            a['mbfc_notes'] = a['mbfc_notes'].strip()
            a['mbfc_notes'] = a['mbfc_notes'].replace("\n", " ")
            a['mbfc_notes'] = a['mbfc_notes'].replace("\t", " ")
            a['mbfc_score'] = a['mbfc_score'].strip()
            a['mbfc_url'] = a['mbfc_url'].strip()
            a['propaganda_label'] = a['propaganda_label'].strip()

            #writing the fixed file to a tsv file
            out.write(a['html_text']+'\t'+a['gdlt_actionGeo']+'\t'+a['gdlt_avgTone']+'\t'+a['gdlt_day']+'\t'+ a['gdlt_id']+'\t'+ a['gdlt_RL']+'\t'+
                      a['html_authors']+'\t'+a['html_title']+'\t'+
                      a['mbfc_class']+'\t'+a['mbfc_link']+'\t'+a['mbfc_name']+'\t'+ a['mbfc_notes']+'\t'+a['mbfc_score']+'\t'+a['mbfc_url']+'\t'+a['propaganda_label']+'\n')

def rashkan_statistics(ds_file):
    with codecs.open(ds_file+'.filtered.txt','w', encoding='utf8') as out:
        with codecs.open(ds_file, 'r', encoding='utf8') as f:
            count=0
            for line in f:
                line = line.strip()
                line = line.lower()
                if 'youtube' in line and len(line)<150:
                    count+=1
                    print (line)
                else:
                    out.write(line+'\n')

            print ('estimation of number of bad examples in dataset: '+ str(count))


def remove_redundants(ds_file):
    ids=[]
    with codecs.open(ds_file+'.filtered.txt', 'w', encoding='utf8') as out:
        with codecs.open(ds_file, 'r', encoding ='utf8') as f:
            lines = f.readlines()
            print ('Number of articles before filtering ='+str(len(lines)))
            for line in lines:
                line=line.strip()
                fields= line.split('\t')
                if fields[4] not in ids:
                    out.write(line+'\n')
                    ids.append(fields[4])
            print ('Number of articles after filtering = '+ str(len(ids)))


def distribute_sources(train_file,dev_file,test_file):
    sources = dict()
    with codecs.open(train_file,'r',encoding='utf8') as f_train:
        with codecs.open(dev_file,'r',encoding='utf8') as f_dev:
            with codecs.open(test_file,'r',encoding='utf8') as f_test:
                with codecs.open('train.dist.converted.txt', 'w', encoding='utf8') as train_out:
                    with codecs.open('dev.dist.converted.txt','w', encoding='utf8') as dev_out:
                        with codecs.open('test.dist.converted.txt','w',encoding='utf8') as test_out:
                            train_lines = f_train.readlines()
                            dev_lines = f_dev.readlines()
                            test_lines = f_test.readlines()
                            all_lines= train_lines+dev_lines+test_lines
                            for line in all_lines:
                                line =line.strip()
                                fields = line.split('\t')
                                if fields[-2] not in sources:         #fields[-2] is the source of the article
                                    sources[fields[-2]] =[]
                                    sources[fields[-2]].append(line)
                                else:
                                    sources[fields[-2]].append(line)
                            train_articles = []
                            test_articles =[]
                            dev_articles =[]
                            for article_set in sources:
                                seventy_percent = len(sources[article_set]) * 0.7
                                eighty_percent = len(sources[article_set]) * 0.8
                                print ('source: (' +article_set+') has '+ str(len(sources[article_set])) + ' articles')
                                print('70% of those is : ' + str(seventy_percent))
                                for i, article in enumerate(sources[article_set]):
                                    train_articles.append(article)
                                    i += 1
                                    if i >= seventy_percent:
                                        break

                                print('10% of those is : ' + str(eighty_percent - seventy_percent))
                                for i, article in enumerate(sources[article_set]):
                                    if i > seventy_percent and i <= eighty_percent:
                                        dev_articles.append(article)
                                    i += 1

                                print('20% of those is : ' + str(len(sources[article_set]) - eighty_percent))
                                for i, article in enumerate(sources[article_set]):
                                    if i > eighty_percent:
                                        test_articles.append(article)
                                    i += 1
                            for a in train_articles:
                                train_out.write(a+'\n')
                            train_out.close()
                            for a in dev_articles:
                                dev_out.write(a+'\n')
                            dev_out.close()
                            for a in test_articles:
                                test_out.write(a+'\n')
                            test_out.close()





distribute_sources('../data/train.json.converted.txt','../data/dev.json.converted.txt','../data/test.json.converted.txt')
#remove_redundants('../data/train.json.converted.txt')
#rashkan_statistics('../data/test.txtconverted.txt')
#from_josn_to_tsv('../data/test.json')
#separate_liwc_lexicons('../data/lexicons/LIWC/LIWC2015_English.txt')
#separate_subjectives('../data/lexicons/subjectivity_clues_hltemnlp05/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.txt')