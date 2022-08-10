from datetime import datetime, timedelta
import os
import sys
import time
from bs4 import BeautifulSoup
import bitlyshortener
import boto3
import openpyxl as ox
# import pandas as pd
import requests
import json
import csv
import openpyxl
from openpyxl import Workbook
import pymysql


def parsenumbers() :
    # 메인파일 열어서 시트별로 데이터 가져오기 - 시작
    to_parse_file_name = "kakao_sms.xlsx"
    getsno_file_name = './to_parse/' + to_parse_file_name
    getsno_file_parsing = ox.load_workbook(filename=getsno_file_name, data_only=True)
    getsno_sheet = getsno_file_parsing['시트 1 - kakao_sms']

    getsno_sheet_rows = []

    ### 시트온오프 파싱
    for getsno_sheet_row in getsno_sheet:
        getsno_sheet_row_values = []
        if getsno_sheet_row[0].value is not None:
            for row_value in getsno_sheet_row:
                if row_value.value is not None:
                    getsno_sheet_row_values.append(row_value.value)
                else:
                    continue
        else:
            continue
        getsno_sheet_rows.append(getsno_sheet_row_values)



    snos = ""
    for sno in getsno_sheet_rows :
        snos += str(sno[0]) + ','

    getsno_filename = to_parse_file_name + ".txt"

    with open(getsno_filename, 'w') as f:
        f.write(snos)
    print(getsno_filename + " 저장 완료 ")


parsenumbers()