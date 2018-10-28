import pandas as pd
import sqlite3
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def check(uID,Data)
    conn = sqlite3.connect('db.sqlite3')

    query = "SELECT * FROM haxtor_userprog;"

    df=pd.read_sql_query(query,conn)

    df2=pd.read_sql_query("select * from haxtor_topic",conn)

    df3=pd.read_sql_query("select * from haxtor_questions",conn)


    li=list(df['topicID_id'])
    lis=[]
    for i in range(999):
    if(li[i]=="1"):
        lis.append(1)
    elif(li[i]=="2"):
        lis.append(1)
    elif(li[i]=="3"):
        lis.append(2)
    elif(li[i]=="4"):
        lis.append(2)

    df['TopDiff']=lis
    lis=[]
    for i in range(999):
    if(li[i]=="1"):
        lis.append(1)
    elif(li[i]=="2"):
        lis.append(1)
    elif(li[i]=="3"):
        lis.append(1)
    elif(li[i]=="4"):
        lis.append(1)

    df['QuesDiff']=lis

    batch_size = 5

    m = tf.Variable(0.5)
    b = tf.Variable(1.0)

    xph = tf.placeholder(tf.float32,[batch_size])
    yph = tf.placeholder(tf.float32,[batch_size])

    def normalize(array): 
    return (array - array.mean()) / array.std()

    x_data = df.drop(['id','uID_id','currEvolution','topicID_id'],axis=1)

    df['Diffprid']=0

    y_val = df['Diffprid']

    X_train, X_test, y_train, y_test = train_test_split(x_data,y_val,test_size=0.2,random_state=101)

    scaler = MinMaxScaler()
    scaler.fit(X_train)
    X_train = pd.DataFrame(data=scaler.transform(X_train),columns = X_train.columns,index=X_train.index)

    X_test = pd.DataFrame(data=scaler.transform(X_test),columns = X_test.columns,index=X_test.index)


    prog_sc= tf.feature_column.numeric_column('progScore')
    Topd= tf.feature_column.numeric_column('TopDiff')   
    Quesd= tf.feature_column.numeric_column('QuesDiff')

    feat_cols = [Topd,Quesd,prog_sc]

    input_func = tf.estimator.inputs.pandas_input_fn(x=X_train,y=y_train ,batch_size=10,num_epochs=1000,shuffle=True)

    model = tf.estimator.DNNRegressor(hidden_units=[40,10,10,10],feature_columns=feat_cols)

    model.train(input_fn=input_func,steps=2500)


    





