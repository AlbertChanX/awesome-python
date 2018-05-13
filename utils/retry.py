# coding:utf-8
# http://tenacity.readthedocs.io/en/latest/
# https://www.zhihu.com/question/24590883/answer/201698987
from tenacity import retry, stop_after_attempt, wait_fixed

# wait=wait_exponential(multiplier=1, max=10)
from json.decoder import JSONDecodeError

# @retry(retry=retry_if_exception_type(JSONDecodeError))


@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def extract(url):
    info_json = requests.get(url).content.decode()
    info_dict = json.loads(info_json)
    data = info_dict['data']
