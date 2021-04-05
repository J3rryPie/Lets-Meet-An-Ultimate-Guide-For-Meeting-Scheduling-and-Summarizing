from django.shortcuts import render
from .forms import TextForm
from .models import Text
from django.core.files import File
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Create your views here.
def welcome_view(request):
    return render(request,'fileupload/index.html')
def text_paste_view(request):
    if request.method== 'POST':
        text_form=TextForm(request.POST)
        if text_form.is_valid():
            text_form.save(commit=False)
            text_form.name = 'mini-project'
            text_form.save()
            trans=text_form.cleaned_data['transcript']
            context={
                'trans':trans
            }
            with open('mini_project.txt', 'w') as f:
                myfile = File(f)
                myfile.write(trans)
            from nltk.cluster.util import cosine_distance
            import numpy as np
            import networkx as nx
            def sentence_similarity(sent1, sent2): 
                sent1 = [w.lower() for w in sent1]
                sent2 = [w.lower() for w in sent2]
            
                all_words = list(set(sent1 + sent2))
            
                vector1 = [0] * len(all_words)
                vector2 = [0] * len(all_words)
            
                # build the vector for the first sentence
                for w in sent1:
                    if w in stopwords:
                        continue
                    vector1[all_words.index(w)] += 1
            
                # build the vector for the second sentence
                for w in sent2:
                    if w in stopwords:
                        continue
                    vector2[all_words.index(w)] += 1
            
                return 1 - cosine_distance(vector1, vector2)
            
            # ARTIFICIAL INTELLIGENCE PROJECT - Automatic Story Summarization 

            # ALGORITHM NAME - Automatic summarization based on weighting

            #OWN
            import os
            import math
            # from os import listdir, system
            # print(os.getcwd())
            # os.system('cd sample_data')
            # os.chdir('sample_data')
            import nltk
            from nltk.tokenize import RegexpTokenizer, sent_tokenize
            from nltk.corpus import stopwords
            from nltk.stem.snowball import SnowballStemmer
            import operator
            import matplotlib.pyplot as plt

            stopwords = stopwords.words('english')

            tokenizer = RegexpTokenizer(r'\w+')

            stemmer = SnowballStemmer('english')
            # print(os.system('ls -lS'))
            # print(os.getcwd())
            f1 = open('mini_project.txt')
            # f2 = open('the-skylight-room.txt')
            # f3 = open('the-cactus.txt')

            # OWN - read the files
            text1 = f1.read()
            text2 = f1.read()
            text3 = f1.read()

            # OWN - tokenize and form nltk objects
            tk1 = nltk.Text(tokenizer.tokenize(text1))
            tk2 = nltk.Text(tokenizer.tokenize(text2))
            tk3 = nltk.Text(tokenizer.tokenize(text3))

            # OWN - remove punctuations and digits and change to lower case
            tk1 = [w.lower() for w in tk1 if w.isalpha() and not w.isdigit()]
            tk2 = [w.lower() for w in tk2 if w.isalpha() and not w.isdigit()]
            tk3 = [w.lower() for w in tk3 if w.isalpha() and not w.isdigit()]

            # OWN - remove stop words and stem the words
            tk1 = [stemmer.stem(w) for w in tk1 if w not in stopwords]
            tk2 = [stemmer.stem(w) for w in tk2 if w not in stopwords]
            tk3 = [stemmer.stem(w) for w in tk3 if w not in stopwords]

            # OWN - find word frequencies
            index1 = nltk.FreqDist(tk1)
            index2 = nltk.FreqDist(tk2)
            index3 = nltk.FreqDist(tk3)
            # print('lol')
            # print(index1['maggi'])
            # print('lol ends')
            # OWN - document frequencies
            comb = list(index1.keys())
            comb.extend(index2.keys())
            comb.extend(index3.keys())
            cindex = nltk.FreqDist(comb)
            # print(cindex['maggi'])
            # OWN - split document into sentences
            sent1 = sent_tokenize(text1)
            tsent=len(sent1)
            # print(tsent)
            idf={}
            for sentence in sent1:
                words = tokenizer.tokenize(sentence)
                # words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]
            for word in words:
                cnt_idf=index1[word]
                cnt_idf=(math.log(1+tsent/1+cnt_idf)+1)*index1[word]
                # print(cnt_idf)
                if(word in idf):
                    idf[word]+=cnt_idf
                else:
                    idf[word]=cnt_idf
            # print(idf)
            sent2 = sent_tokenize(text2)
            sent3 = sent_tokenize(text3)

            # OWN - create word list of title
            t1 = 'gift of magi'
            t2 = 'the skylight room'
            t3 = 'the cactus'
            title1 = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(t1) if w.isalpha() and w not in stopwords]
            title2 = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(t2) if w.isalpha() and w not in stopwords]
            title3 = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(t3) if w.isalpha() and w not in stopwords]

            similarity_matrix = np.zeros((len(sent1), len(sent1)))
            for idx1 in range(len(sent1)):
                for idx2 in range(len(sent1)):
                    if idx1 == idx2: #ignore if both are same sentences
                        continue 
                    similarity_matrix[idx1][idx2] = sentence_similarity(sent1[idx1], sent1[idx2])
            sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)
            scores = nx.pagerank(sentence_similarity_graph)
            print(scores)
            # Step 4 - Sort the rank and pick top sentences
            ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sent1)), reverse=True)

            # OWN - calculate score for every sentence

            scores1 = {}
            sentence_lengths = []
            for sentence in sent1:
                sentence_lengths.append(len(sentence))
                if len(sentence) < 81 and len(sentence)>10:
                    # OWN - find all words in the sentence
                    words = tokenizer.tokenize(sentence)
                    words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]
                # score = 0.0
                    score = 0.0
                    titlewords = 0.0
                # idf_score=0.0
                    idf_score = 0.0
                    cnt=-1
                    for word in words:
                        cnt+=1     
                        score = score + index1[word] / (1+cindex[word])
                        if(cnt==0):     
                            factor=score/scores[1]        
                        if word in title1:
                            titlewords += 1
                        if word in idf:
                            # print(word)
                            idf_score += (idf[word]*idf[word])
                    # idf_score += idf[word]*idf[word]
                    # OWN - number of words in sentence / number of those words present in title
                    titlewords = 0.1 * titlewords / len(title1)
                    # scores1.add(sentence,score + titlewords + math.sqrt(idf_score)+scores[cnt]*factor)
                    # print('lollll')
                    # print(cnt)
                    # print(scores.get(cnt))
                    scores1[sentence] = score + titlewords + math.sqrt(idf_score)#+scores.get(cnt)*factor
                    # scores1.get(sentence) = score + titlewords + math.sqrt(idf_score)+scores[cnt]*factor
                    # print('idf_score') 
                    # print(math.sqrt(idf_score))
            # print('score1')
            # print(scores1)
            # print('score one ends')

            scores2 = {}
            sentence_lengths2 = []
            for sentence in sent2:
                sentence_lengths2.append(len(sentence))
                if len(sentence) < 120:
                    # OWN - find all words in the sentence
                    words = tokenizer.tokenize(sentence)
                    words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]

                    # OWN - sum of term frequencies and doc frequencies
                    score = 0.0
                    titlewords = 0.0
                    for word in words:
                        score = score + index2[word] / (1+cindex[word])
                        if word in title2:
                            titlewords += 1

                    # OWN - number of words in sentence / number of those words present in title
                    titlewords = 0.1 * titlewords / len(title2)
                    scores2[sentence] = score + titlewords
            # print(scores2)

            scores3 = {}
            sentence_lengths3 = []
            for sentence in sent3:
                sentence_lengths3.append(len(sentence))
                if len(sentence) < 90:
                    # OWN - find all words in the sentence
                    words = tokenizer.tokenize(sentence)
                    words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]

                    # OWN - sum of term frequencies and doc frequencies
                    score = 0.0
                    titlewords = 0.0
                    for word in words:
                        score = score + index3[word] / (1+cindex[word])
                        if word in title3:
                            titlewords += 1


                    # OWN - number of words in sentence / number of those words present in title
                    titlewords = 0.1 * titlewords / len(title3)
                    scores3[sentence] = score + titlewords

            # print(scores3)
            # similarity_matrix = np.zeros((len(sent1), len(sent1)))
            # for idx1 in range(len(sent1)):
            #     for idx2 in range(len(sent1)):
            #         if idx1 == idx2: #ignore if both are same sentences
            #             continue 
            #         similarity_matrix[idx1][idx2] = sentence_similarity(sent1[idx1], sent1[idx2])
            # sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)
            # scores = nx.pagerank(sentence_similarity_graph)
            # # print(scores)
            # # Step 4 - Sort the rank and pick top sentences
            # ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sent1)), reverse=True)    
            # print("Indexes of top ranked_sentence order are ", ranked_sentence)    
            summarize_text = []
            for i in range(2):
                summarize_text.append("".join(ranked_sentence[i][1]))

            # Step 5 - Offcourse, output the summarize texr
            # print("Summarize Text: \n", ". ".join(summarize_text))
            context={
                'summary': summarize_text,
            }
            #to-do
            # max (of rec (calculated below) should equals iska max score sentence)


            '''
            print scores1
            sorted1 = sorted(scores1.items(), key = operator.itemgetter(1))
            print sorted1[-10:]
            f, axarr = plt.subplots(2, 2)
            axarr[0, 0].hist(scores1.values(), bins = 30)
            axarr[0, 0].set_title("Sentence lengths histogram")
            # axarr[0, 0].xlabel('Number of characters')
            # axarr[0, 0].ylabel('Number of sentences')
            # axarr[0, 0].show()
            axarr[0, 1].hist(scores2.values(), bins = 30)
            axarr[0, 1].set_title("Sentence lengths histogram")
            # axarr[0, 1].xlabel('Number of characters')
            # axarr[0, 1].ylabel('Number of sentences')
            # axarr[0, 1].show()
            axarr[1, 0].hist(scores3.values(), bins = 30)
            axarr[1, 0].set_title("Sentence lengths histogram")
            # axarr[1, 0].xlabel('Number of characters')
            # axarr[1, 0].ylabel('Number of sentences')
            plt.show()
            '''

            # OWN - print the summary generated for each story
            res = 0
            max=0
            for val in scores1.values():
                if(val > max):
                    max=val
                    res += val
            
            # using len() to get total keys for mean computation
            if(len(scores1)!=0):
               res = res / len(scores1)
            res=res+(max-res)/2
            # print(res)
            #

            # print(scores1)
            # print('gift of magi')

            for sentence in scores1.keys():
                if scores1[sentence] >= res:
                    print(sentence)

            #print('\n\nthe skylight room')
            for sentence in scores2.keys():
                if scores2[sentence] >= 20:
                    print(sentence)

            #print('\n\nthe cactus')
            for sentence in scores3.keys():
                if scores3[sentence] >= 8:
                    print(sentence)
            return render(request,'fileupload/output.html',context)
    else:
        form=TextForm()
        context={
            'form':form
        }
        return render(request,"fileupload/input.html",context)
