#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pdsql

mysqldb = pdsql.PandasMysql()

df = pd.read_csv('titanic_data.csv')

mysqldb.df_to_new_mysql("localhost","root","mypassword",21,"test","Titanic_Data",df)

mysqldb.df_to_exist_mysql("localhost","root","mypassword",21,"test","Titanic",df)

mysqldb.export_df("localhost","root","mypassword",21,"test","Titanic","export.csv")
