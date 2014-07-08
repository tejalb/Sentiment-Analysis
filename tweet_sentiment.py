import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    
    content=[]
    json_dict={}
    tweet_file=open(sys.argv[2])

    for line in tweet_file:
     json_dict=json.loads(line)
     if 'text' in json_dict.keys():
      #print json_dict["text"]
      unicode_str=json_dict['text']
      encoded=unicode_str.encode('utf-8')
      content.append(encoded)
    #print len(content)
    #print content[6]

    affinfile=open(sys.argv[1]) 

    scores={}
    for line in affinfile:
     term,score=line.split("\t")
     scores[term]=int(score)
    #print scores.items()

    score_list=[]
    #print content[2]
    for tweet in content:
     tweet=tweet.lower()
     terms=tweet.split(" ")
     count=0
     for term in terms:
      term=term.strip()
      if term in scores:
        count+=scores[term]
     score_list.append(count)
    #print score_list
    
    for elem in score_list:
     print elem

    

    

if __name__ == '__main__':
    main()
