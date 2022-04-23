# Cluster-practice

Hourly Energy Consumption Data Classification

Data:Provided by PJM in Megawatts

This practice included three file:

    README.md
    
    all_data.csv
    
    result.csv

    kmeans.ipynb

    LSTM_classification.ipynb

We can diveded this practice into two case 

## Case 1:
### Clust time series data into 3 group and each group can clust into 3 sub-cluster,so we will get 9 clusters.
In this case,first,clust the time series data by kmeans algorithm into three group(three Energy-Consumption-Level)

Next step,cluste each group into three sub-cluster(three sub-Energy-Consumption-Level)

The detail code can see the **kmeans.ipynb**
## Case 2:
### time series classification with LSTM model
In this case,we use the LSTM model last time we report.

First step,we get the data which have be labeled by case 1.

Next,we preprocess the data before training model.

Modified the hyperparameters time series classification by LSTM model.

Show the result and accuracy.

The detail code can see the **LSTM_classification.ipynb**
