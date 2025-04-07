FROM registry.cn-hangzhou.aliyuncs.com/gerry_ai/deploy_nlp:v20240624_01

# 安装依赖库
RUN /mnt/miniconda3/bin/pip install torch==1.13.1 joblib==1.4.2 uvicorn==0.30.1 scikit-learn==1.4.2 fastapi==0.109.0 numpy==1.24.4 -i http://mirrors.cloud.aliyuncs.com/pypi/simple/ --trusted-host mirrors.cloud.aliyuncs.com

# copy文件夹到/mnt文件夹下
COPY fastapi_text_classify_deploy /mnt/fastapi_text_classify_deploy

# 对外暴露的端口号
EXPOSE 9001

# 执行命令(执行docker run的时候，对应的默认命令)
CMD /mnt/miniconda3/bin/python /mnt/fastapi_text_classify_deploy/deploy_app.py