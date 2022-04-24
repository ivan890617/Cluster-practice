# Cluster-practice Report

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

## My Report Experience

In this two case,I think I spend a lot of time on data preprocessing and LSTM model,I will discuss it in the following.

For the case one,I continue working with clustering.This time,I try to clust in 1 dimension, to cluster each group into 3 sub-clusters and so I will have small 9 
clusters.During the process,I met some problem.I found that KMeans could not clust by the size of cluster_centers.For example,if the size of cluster_centers 
is 1000,2000,3000,the output category may be 0,2,1,not 0,1,2.So I define a function to solve this problem.Because in my case,size of categorical numbers is important.

After I solve this problem,I enter the next step,clust each group into 3 sub-clusters.First,I divided the data into three part by category which I clust in previous part.Based on each part,I clusted in 3 sub-clusters again.Now,I have small 9 clusters and output the result.

For the case two,I used the data which outputed from case one which had been labeled(category).In this case,my propose is to use the LSTM model for time series classification.I studied a lot of information and courses and try to achieve porpose.In the pervious report,I had tried time series prediction by LSTM model.Compare with pradiction and classification.The output of the former is the energy consumption,and the output of the latter is the predicted classification result.So I modified the model which I used in the previous report.

Because this is the problem of classification,I choose the CroosEntropy as my loss.In pytorch,CrossEntropy included Softmax,so I had not to set the Softmax function again as my model output.I just set the linear layer in the output.I thought about this question for a long time.I also met another question,that when calculated CrossEntropy,I need put the LSTM model output and training data label into loss function.I set the label from 1 to 9 at first,but the bug is appear.Because the definition of the CrossEntropy in Pytorch the label should be [0:category-1].That means,in my case,I should adjust my label from 0 to 8.Finally,I solved this question.

After I adjusted the Hyperparameters,my model accuracy could achieve nearly 80%,I think it can be more higher,I will try to improve it.

Thanks for reading my report
