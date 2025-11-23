import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from etl.transform import transform_data

def test_no_null_sales():
    df = transform_data()
    assert df['Global_Sales'].isnull().sum() == 0

def test_year_is_int():
    df = transform_data()
    assert str(df['Year'].dtype) in ["Int64", "int64"]

def test_columns_exist():
    df = transform_data()
    expected = {'Rank','Name','Platform','Year','Genre','Publisher',
                'NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'}
    assert expected.issubset(df.columns)
