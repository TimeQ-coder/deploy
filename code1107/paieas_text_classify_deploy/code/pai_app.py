# -*- coding: utf-8 -*-
import json
import logging
import os

import allspark


class MyProcessor(allspark.BaseProcessor):
    def initialize(self):
        """
            模型恢复初始化的相关方法，仅执行一次
        """
        from predictor import Predict

        # 通过环境变量给定模型所在文件夹
        model_dir = os.path.abspath(os.environ['MODEL_DIR'])
        self.model = Predict(model_dir)
        print(f"模型初始化完成:{model_dir}")

    def process(self, data):
        """
            每次请求传递过来的数据，进行推理，并返回结果,
            假定data入参为json字符串，包含了两个值，text和k
        """
        try:
            data = str(data, encoding='utf-8')
            data = json.loads(data)
            text = data['text']
            k = int(str(data.get('k', '1')))
            pred_result = self.model.predict(x=text, k=k)
            output = {'code': 0, 'msg': '成功', 'data': pred_result, 'text': text, 'k': k}
            result = json.dumps(output, ensure_ascii=False)
            return bytes(result, encoding='utf8'), 200
        except Exception as e:
            logging.error(f"服务器异常:{e} - {data}", exc_info=e)
            result = json.dumps({'code': 1, 'msg': '服务器异常'}, ensure_ascii=False)
            return bytes(result, encoding='utf8'), 200


if __name__ == '__main__':
    # allspark.default_properties().put('rpc.keepalive', '10000')
    # 设置服务计算超时时间为10s, 默认为5秒
    # parameter worker_threads indicates concurrency of processing
    endpoint = os.environ['PAI_ENDPOINT']
    runner = MyProcessor(worker_threads=10, endpoint=endpoint)
    runner.run()
