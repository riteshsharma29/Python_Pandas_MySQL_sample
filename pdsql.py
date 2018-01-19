#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Prequesite commands :

pip install mysqlclient
pip install mysql-python

'''

from sqlalchemy import create_engine
import MySQLdb
import pandas as pd

class PandasMysql():

    #Method to import DataFrame into MySQL database in newly created specified Table

    def df_to_new_mysql(self,host,dbusername,dbpassword,port,db,dbtable,dataframe):

        engine = create_engine('mysql://' + dbusername + ":" + dbpassword + "@" + str(host) + ":" + str(port) + "/" + db)

        dataframe.to_sql(name=dbtable,con=engine,if_exists='fail',index=False)

    #Method to import DataFrame into MySQL database in existing specified "NEW" Table will created in the specified Database

    def df_to_exist_mysql(self,host,dbusername,dbpassword,port,db,dbtable,dataframe):

        engine = create_engine('mysql://' + dbusername + ":" + dbpassword + "@" + str(host) + ":" + str(port) + "/" + db)

        dataframe.to_sql(name=dbtable,con=engine,if_exists='append',index=False)

    #Method to import DataFrame into MySQL database in existing specified "NEW" Table will created in the specified Database

    def export_df(self,host,dbusername,dbpassword,port,db,dbtable,exportfilename):

    #Open database connection

        conn = MySQLdb.connect(host = host,port = port,user=dbusername,passwd = dbpassword,db = db)

    #query the database table
        df = pd.read_sql_query('select * from ' + dbtable,conn)

        df.to_csv(exportfilename)








