import sys
import json

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

    content=[]
    json_dict={}
    tweet_file=open(sys.argv[1])

    for line in tweet_file:
     json_dict=json.loads(line)
     if 'text' in json_dict.keys():
      #print json_dict["text"]
      unicode_str=json_dict['text']
      encoded=unicode_str.encode('utf-8')
      content.append(encoded)
    
    frequency={}
    
    #print content[2]
    total_count=0
    for tweet in content:
     tweet=tweet.lower()
     newtweet=tweet.replace('\n',"")
     terms=newtweet.split(" ")
     for term in terms:
      total_count+=1
      term=term.strip()
      if term in frequency:
        frequency[term]+=1
      elif term not in frequency:
        frequency[term]=1
     
        
        
    #print frequency.values()
    #print total_count
    for k in sorted(frequency, key=frequency.get, reverse=True):
      print('%s %.6f' %(k, frequency[k]/total_count))

    
     
    
    

if __name__ == '__main__':
    main()
