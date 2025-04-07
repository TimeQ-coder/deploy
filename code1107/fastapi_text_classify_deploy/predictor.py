# -*- coding: utf-8 -*-
import os

import numpy as np

import torch


class Predict(object):
    def __init__(self, output_dir):
        super(Predict, self).__init__()
        # 1. 加载恢复模型
        save_obj = torch.load(os.path.join(output_dir, "best.pkl"), map_location='cpu')
        net = save_obj['net']  # 此时就是网络对象
        vectorizer = save_obj['vec']
        target_names = save_obj['target_names']
        net.eval()  # 让模型进入推理阶段: 针对某些特殊API进行特殊执行逻辑，eg: Dropout、BN.....

        self.net = net
        self.vectorizer = vectorizer
        self.target_names = target_names
        print(f"模型恢复成功:{output_dir}")

    # noinspection DuplicatedCode
    def predict(self, x, k=1):
        """
        对给定样本x进行推理预测，并返回概率最大的前k个预测结果
        :param x:
        :param k:
        :return:
        """
        org_x = x
        if isinstance(x, str):
            org_x = [org_x]

        # 2. 按照训练的相同方式对待预测数据进行处理转换
        x = self.vectorizer.transform(org_x)
        x = x.toarray()
        print(f"待预测数据shape:{x.shape}")

        # 3. 调用模型对应的predict方法获取结果
        x_tensor = torch.tensor(x, dtype=torch.float32)
        score = self.net(x_tensor)
        print(score)
        # detach: 梯度截断
        proba = torch.softmax(score, dim=1).detach().numpy()
        print(type(proba), proba.shape)

        # 4. 后处理
        sorted_pred_class_ids = np.argsort(proba, axis=1)[:, ::-1]
        print(proba)
        result = []
        k = max(1, min(k, sorted_pred_class_ids.shape[1]))
        for sorted_pred_ids, prob, _x in zip(sorted_pred_class_ids, proba, org_x):
            result_per_sample = []
            for i in range(k):
                cid = sorted_pred_ids[i]
                result_per_sample.append({
                    'id': int(cid),
                    'class_name': self.target_names[int(cid)],
                    'proba': float(f'{prob[cid]:.3f}'),
                })
            result.append(result_per_sample)

        return result
