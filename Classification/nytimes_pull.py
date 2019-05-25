import urllib.request
import json

def main(api_key, category, label):
    
    content = []
    for i in range(0,5):
        # print "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:('%s')&api-key=%s&page=%s" % (category, api_key, i)
        h = urllib.request.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:(\"%s\")&api-key=%s&page=%s" % (category, api_key, i))
        print (h)
        try:
            result = json.loads(h.read().decode('utf-8'))
            content.append(result)
        except ValueError:
            print ("Malformed JSON: " + data)
            continue #In the rare cases that JSON refuses to parse

    f = open(label, 'w')
    for line in content:
        try:
            f.write('%s\n' % line)
        except UnicodeEncodeError:
            pass
            
    f.close()

if __name__ == '__main__':
    main("tzkg9t96J58TsFt9HPDhIAzfLP7zP4ez", "Arts","arts2")
    main("tzkg9t96J58TsFt9HPDhIAzfLP7zP4ez", "Sports","sports2")

