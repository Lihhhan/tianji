#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import jieba
import jieba.analyse
import re

def run(name, number):
    i = 0
    wordcount = { }
    while i < number/20 :
        i = i + 1
        #数据抓取
        url = 'http://www.zhihu.com/people/' + name + '/answers?page=' + str(i) 
        print url
        req = urllib2.Request(url)
        req.add_header("User-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36")
        c = urllib2.urlopen(req)

        #数据处理
        content = BeautifulSoup(c.read())
        answers = content.find(id = "zh-profile-answer-list")
        answer = answers.div
        if answer == None:
            break
       
        while True:
            #被折叠的回答～
            if answer.textarea != None:
                #print answer
                tag_as = answer.find_all('a')
                for a in tag_as:
                    try:
                        #点赞数
                        if a['class'] == 'zm-item-vote-count js-expand js-vote-count':
                            if 'K' in a.string:
                                k = (float(re.sub('K', '', a.string))*1000) ** 0.5
                            elif 'W' in a.string:
                                k = (float(re.sub('W', '', a.string))*10000) ** 0.5    
                            else:
                                k = float(a.string)**0.5
                        #问题标题
                        if a['class'] == 'question_link' :
                            answer_string = a.string + ' '
                    except:
                        #跳过无效的a标签
                        continue
                #回答
                answer_string += answer.textarea.get_text()
                answer_string = re.sub('[A-Za-z0-9]', '', answer_string)

                #分词提取关键字
                keywords = jieba.analyse.extract_tags(answer_string, 100, True)
                for keyword in keywords:
                    if keyword[0] in wordcount:
                        wordcount[keyword[0]] += keyword[1]*k
                    else:
                        wordcount[keyword[0]] = keyword[1]*k

            answer = answer.next_sibling.next_sibling
            if answer == None:
                break

    #for word in wordcount:
    #    print word,wordcount[word]
    return wordcount



