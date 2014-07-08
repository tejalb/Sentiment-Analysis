import sys
import json
import collections

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    tags=[]
    json_dict={}
    frequency={}
    tweet_file=open(sys.argv[1])
#Why do I need to declare this again?? If I don't it doesn't read in
    for line in tweet_file:
     json_dict=json.loads(line)
     if 'entities' in json_dict.keys():
      #print json_dict["text"]
      
      tags=json_dict['entities']['hashtags']
      for tag in tags:
        if 'text' in tag: 
           hashtag=tag['text']
           if hashtag not in frequency:
             frequency[hashtag]=1
           elif hashtag in frequency:
             frequency[hashtag]+=1
    print frequency.items()
    sort_tags=sorted(frequency, key=frequency.get, reverse=True)
    #print sort_tags
    for k in sort_tags[:10]:
      print k, frequency[k]
    #topten=Counter(frequency).most_common()[:10]
    
    #print content[2]
    
     
if __name__ == '__main__':
    main()
