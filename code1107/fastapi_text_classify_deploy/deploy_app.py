# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI, Body

from predictor import Predict

app = FastAPI()
model = Predict(".")


@app.get("/")
def read_root():
    return "使用fastapi框架搭建一个文本分类的模型预测"


async def predict(
        text: str = Body(..., description="待预测文本text"),
        k: int = Body(1, description="TopK的值", examples=[3, 5])
):
    print("调用predict方法......")
    pred_result = model.predict(x=text, k=k)

    # 拼接返回最终值
    return {'code': 0, 'msg': '成功', 'data': pred_result, 'text': text, 'k': k}


app.post("/predict", summary="Predict预测接口")(predict)

if __name__ == '__main__':
    # http://127.0.0.1:9001/docs
    uvicorn.run(app, host="0.0.0.0", port=9001, log_level="info")
