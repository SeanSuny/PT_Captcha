#!/usr/bin/env python
# -*- coding:utf-8 -*-
############################################################
# @Author       : Sean
# @Date         : 2022-03-01 14:00:23
# @LastEditors  : Sean
# @LastEditTime : 2022-03-03 15:06:40
# @Description  : 这是由 Sean 创建
# @FilePath     : d:/我的文件/0-项目/Python/pt_captcha/captcha_app/ocrvendor/tencent.py
# @Copyright    : Copyright ©2019-2022 Sean,Inc
############################################################

import re
import sys
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

DEFAULT_REGION = 'ap-guangzhou'


class tencent(object):
    """
    tencent cloud ocr class
    """

    def __init__(self, apikey, secret, region):
        cred = credential.Credential(apikey, secret)
        httpProfile = HttpProfile(reqMethod="POST", reqTimeout=60)
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.signMethod = "TC3-HMAC-SHA256"
        clientProfile.httpProfile = httpProfile
        self.client = ocr_client.OcrClient(cred, region, clientProfile)

    def recog_img(self, image):
        req = models.GeneralAccurateOCRRequest()
        req.from_json_string(json.dumps({"ImageBase64": image.decode()}))
        try:
            resp = self.client.GeneralAccurateOCR(req)
        except TencentCloudSDKException as err:
            print(err)
            print('ERROR: cannot get recognition from tencentcloud')
            sys.exit(1)
        result = "".join([a.DetectedText for a in resp.TextDetections])
        result = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)
        return '"recognition":"%s"' % result
