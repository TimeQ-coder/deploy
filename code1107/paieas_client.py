# -*- coding: utf-8 -*-

from eas_prediction import PredictClient, StringResponse
from eas_prediction import StringRequest

if __name__ == '__main__':
    client = PredictClient('http://1757826125271350.cn-shenzhen.pai-eas.aliyuncs.com', 'text_classify_nlp1107')
    client.set_token('NTFmMDZiYjBhNDcwM2JmZDQwMjBhM2FkMTE4ZTIwNGU3ZmNmOGQ0ZA==')
    client.init()

    request = StringRequest('{"text":"我是小明", "k":2}')
    for x in range(0, 1000):
        resp: StringResponse = client.predict(request)
        str_result = str(resp.response_data, encoding='utf-8')
        print(str_result)
