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
#Why do I need to declare this again?? If I don't it doesn't read in
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
#If I use sent_file above, it prints an empty dict. Why?? 
    scores={}
    for line in affinfile:
     term,score=line.split("\t")
     scores[term]=int(score)
    #print scores.items()

    score_list=[]
    non_sentiment={}
    
    #print content[2]
    for tweet in content:
     tweet=tweet.lower()
     terms=tweet.split(" ")
     count=0
     for term in terms:
      term=term.strip()
      if term in scores:
        count+=scores[term]
      elif term not in scores:
        if term not in non_sentiment:
         non_sentiment[term]=[0,1] #score, number of tweets it appears in
        else: non_sentiment[term][1]+=1
        
     score_list.append(count)
    #print len(non_sentiment.items())

    tweet_number= 0
    for tweet in content:
     tweet=tweet.lower()
     terms=tweet.split(" ")
     
     for term in terms:
      term=term.strip()
      if term in non_sentiment:
        non_sentiment[term][0]+=score_list[tweet_number]
     tweet_number+=1

    #print len(non_sentiment.items())
    
    for item in non_sentiment:
      non_sentiment[item][0]=non_sentiment[item][0]/non_sentiment[item][1]
    for key in non_sentiment:
      print key, non_sentiment[key][0]

    
     
    
    

if __name__ == '__main__':
    main()
