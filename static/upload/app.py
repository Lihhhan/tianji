#coding=utf-8
import login, conf, spider
import sys, logging

reload(sys)
sys.setdefaultencoding( "utf-8" )

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='myapp.log',
    filemode='w')

login.login()

res = {}
wordlist = {}
for person in conf.persons:
    res[person] = spider.run(person, 1000)
    logging.info('%s\tdownloaded!'%person)
    f = open('./data/'+person, 'w')
    for word in res[person]:
        #写入临时文件
        f.write('%s\t' % word)
        f.write('%f\n' % res[person][word])
         
        #总词数统计
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1
    f.close()

#筛选重复率高和低的词
for word, count in wordlist.items():
    if float(count)/len(res) < 0.1 or float(count)/len(res) > 0.5:
        wordlist.pop(word)

#把计数矩阵写入文件
f = open('./data/data.txt', 'w')
f.write('Word')
for word in wordlist:
    f.write('\t%s'%word)
f.write('\n')
        


for person, wc in res.items():
    f.write(person)
    for word in wordlist:
        if word in wc:
            f.write('\t%f'%wc[word]) 
        else:
            f.write('\t0')
    f.write('\n')
f.close()





