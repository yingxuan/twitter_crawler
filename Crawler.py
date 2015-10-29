## keep calling twitter search api
## 100 pages per call, use the since id as the max id for the next call
## perfect match on the keyword for now
import time

class Crawler:
    def __init__(self):
        self.user_text = {}

    def form_query(self, keyword, last_max_id, result_type):
        if last_max_id:
            return 'twurl "/1.1/search/tweets.json?max_id=" + last_max_id + "&q=" + keyword + "&count=100&include_entities=1&result_type=" + result_type + """';
        else:
            return 'twurl "/1.1/search/tweets.json?q=" + keyword + "&count=100&include_entities=1&result_type=" + result_type + """';

    def parse(self, data):
        for tweet in data['statuses']:
            text = tweet['text']
            if not text.startswith('RT'):
                user = tweet['user']['screen_name']
                self.user_text[user] = text

    def search_req(self, keyword, result_type):
        attempt = 0
        sleep_times = 0;
        last_max_id = None
        fw = open('crawl','wb')
        while sleep_times <=10:
            try:
                print "1"
                cmd = form_query(keyword, last_max_id, result_type)
                print "===================" + attempt + "======================"
                print cmd
                (status, output) = commands.getstatusoutput(cmd)
                if status:
                    sys.stderr.write(output)
                    sys.exit(1)

                data = json.loads(output)
                parse(data, self.user_text)
                ##parse search_metadata
                last_max_id = data['search_metadata']['max_id_str']
            except:
                print "exception!"
                time.sleep(1200)
                sleep_times+=1

        for user, text in self.user_text.items():
            fw.write("\n[" + user + "]\t", text)
        fw.close()




if __name__ == "__main__":
    Crawler().search_req("bought a car", "mixed")