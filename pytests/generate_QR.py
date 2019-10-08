# -*- coding: utf-8 -*-
# Created on: Thu 13 Sep 2018 01:25:13 PM CST

# @author: Helin Liu

import os
import time

import qrcode

_PATH_QR_DIR = r'/usr/local/factory/py/test/pytests/generate_QR_static/'

_QRSIZE = 500

_HTML_QR = '''
<div align="center">
<img src="qcn_sn.png" width="550" height="550"/>
'''


class QCNTest(test_case.TestCase):

  def setUp(self):
    self.dut = device_utils.CreateDUTInterface()
    self.CheckPathDir()
    self.GenerateQR()

  def runTest(self):
    self.ui.SetHTML(_HTML_QR, id=None)
    time.sleep(30)

  def CheckPathDir(self):
    _path_dir = os.path.exists(_PATH_QR_DIR)
    if not _path_dir:
      os.makedirs(_PATH_QR_DIR)
    else:
      return False

  def GenerateQR(self):
    qcn_sn = str(device_data.GetDeviceData('factory.qcn_sn'))
    session.console.info('QCN Serail Number is %s', qcn_sn)
    # cmd_qcn = 'SET qcn_sn=' + qcn_sn
    session.console.info('CMD for QCN is %s', qcn_sn)

    qr = qrcode.QRCode(
      version=1, error_correction=qrcode.ERROR_CORRECT_L, box_size=18)

    if qcn_sn != '':
      qr.add_data(qcn_sn)
      # qr.add_data(cmd_qcn)
      qr.make(fit=True)
      orig_img = qr.make_image()
      new_img = orig_img.resize((_QRSIZE, _QRSIZE))
      new_img.save("%sqcn_sn.png" % (_PATH_QR_DIR))
    else:
      raise Exception("Get QCN Serial Number Fail!")
