.. code:: ipython3

    import pandas as pd
    import numpy as np

.. code:: ipython3

    #create data frame
    info={'name':['aliha','mawrah','tabasum','hania'],
         'age':[12,34,56,67],
          'city':['lhr','rwd','sin','cos']}
    df=pd.DataFrame(info)

.. code:: ipython3

    #when need full table
    df




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
        <tr>
          <th>1</th>
          <td>mawrah</td>
          <td>34</td>
          <td>rwd</td>
        </tr>
        <tr>
          <th>2</th>
          <td>tabasum</td>
          <td>56</td>
          <td>sin</td>
        </tr>
        <tr>
          <th>3</th>
          <td>hania</td>
          <td>67</td>
          <td>cos</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #description with no table format
    print(df)


.. parsed-literal::

          name  age city
    0    aliha   12  lhr
    1   mawrah   34  rwd
    2  tabasum   56  sin
    3    hania   67  cos
    

.. code:: ipython3

    #create file of the table you create
    df.to_csv("friend.csv")

.. code:: ipython3

    #create another file with no indexing
    df.to_csv("friends_no_indexing.csv",index=False)

.. code:: ipython3

    #get first five rows(if there is)
    df.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
        <tr>
          <th>1</th>
          <td>mawrah</td>
          <td>34</td>
          <td>rwd</td>
        </tr>
        <tr>
          <th>2</th>
          <td>tabasum</td>
          <td>56</td>
          <td>sin</td>
        </tr>
        <tr>
          <th>3</th>
          <td>hania</td>
          <td>67</td>
          <td>cos</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #only get first two rows
    df.head(2)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
        <tr>
          <th>1</th>
          <td>mawrah</td>
          <td>34</td>
          <td>rwd</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #only get 1st row of the table
    df.head(1)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #get last 2 rows
    df.tail(2)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2</th>
          <td>tabasum</td>
          <td>56</td>
          <td>sin</td>
        </tr>
        <tr>
          <th>3</th>
          <td>hania</td>
          <td>67</td>
          <td>cos</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #get ever row ecept last two
    df.head(-2)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
        <tr>
          <th>1</th>
          <td>mawrah</td>
          <td>34</td>
          <td>rwd</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #descriptipon of all the table
    df.describe()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>age</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>4.000000</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>42.250000</td>
        </tr>
        <tr>
          <th>std</th>
          <td>24.390914</td>
        </tr>
        <tr>
          <th>min</th>
          <td>12.000000</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>28.500000</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>45.000000</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>58.750000</td>
        </tr>
        <tr>
          <th>max</th>
          <td>67.000000</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #naming
    info=pd.read_csv("friend.csv")

.. code:: ipython3

    info




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Unnamed: 0</th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>0</td>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
        <tr>
          <th>1</th>
          <td>1</td>
          <td>mawrah</td>
          <td>34</td>
          <td>rwd</td>
        </tr>
        <tr>
          <th>2</th>
          <td>2</td>
          <td>tabasum</td>
          <td>56</td>
          <td>sin</td>
        </tr>
        <tr>
          <th>3</th>
          <td>3</td>
          <td>hania</td>
          <td>67</td>
          <td>cos</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #indexing
    info["name"][3]




.. parsed-literal::

    'hania'



.. code:: ipython3

    #change name in pposition 3 according to index
    info["name"][3]="bisma"


.. parsed-literal::

    C:\Users\Peace\AppData\Local\Temp\ipykernel_3280\361771329.py:1: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
    You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
    A typical example is when you are setting values in a column of a DataFrame, like:
    
    df["col"][row_indexer] = value
    
    Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    
      info["name"][3]="bisma"
    C:\Users\Peace\AppData\Local\Temp\ipykernel_3280\361771329.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      info["name"][3]="bisma"
    

.. code:: ipython3

    info




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Unnamed: 0</th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>0</td>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
        <tr>
          <th>1</th>
          <td>1</td>
          <td>mawrah</td>
          <td>34</td>
          <td>rwd</td>
        </tr>
        <tr>
          <th>2</th>
          <td>2</td>
          <td>tabasum</td>
          <td>56</td>
          <td>sin</td>
        </tr>
        <tr>
          <th>3</th>
          <td>3</td>
          <td>bisma</td>
          <td>67</td>
          <td>cos</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #providing customize index
    info.index=['A','B','C','D']

.. code:: ipython3

    info




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Unnamed: 0</th>
          <th>name</th>
          <th>age</th>
          <th>city</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>A</th>
          <td>0</td>
          <td>aliha</td>
          <td>12</td>
          <td>lhr</td>
        </tr>
        <tr>
          <th>B</th>
          <td>1</td>
          <td>mawrah</td>
          <td>34</td>
          <td>rwd</td>
        </tr>
        <tr>
          <th>C</th>
          <td>2</td>
          <td>tabasum</td>
          <td>56</td>
          <td>sin</td>
        </tr>
        <tr>
          <th>D</th>
          <td>3</td>
          <td>bisma</td>
          <td>67</td>
          <td>cos</td>
        </tr>
      </tbody>
    </table>
    </div>



