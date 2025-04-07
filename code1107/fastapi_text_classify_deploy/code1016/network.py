# -*- coding: utf-8 -*-

import torch.nn as nn


class TextClassifyNetWorkV0(nn.Module):
    def __init__(self, in_features, num_classes):
        super(TextClassifyNetWorkV0, self).__init__()
        self.features = nn.Sequential(
            nn.Linear(in_features=in_features, out_features=512),
            nn.Tanh(),
            nn.Linear(in_features=512, out_features=256),
            nn.Tanh(),
        )
        self.classify = nn.Sequential(
            nn.Linear(in_features=256, out_features=num_classes)
        )

    def forward(self, x):
        feature = self.features(x)  #
        return self.classify(feature)  #
