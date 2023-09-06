from elasticsearch import Elasticsearch
import warnings
warnings.filterwarnings("ignore")

host = 'localhost'
# host = '13.233.103.143'
port = 9200
url = f'http://{host}:{port}'


es = Elasticsearch([url],
                    # http_auth=(username, password),
                   verify_certs=False,timeout=100 
                   )

# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

print(es.ping())