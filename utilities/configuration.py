from elasticsearch import Elasticsearch
import warnings
warnings.filterwarnings("ignore")

host = 'localhost'
port = 9200
url = f'http://{host}:{port}'


es = Elasticsearch([url],
                   verify_certs=False,timeout=30
                   )

print(es.ping())