## Predict Customer Churn using Random Forest Classification

Customer retention is one of the primary growth pillars for products with a returning customers and subscription models.

Customer churn (or customer attrition) is a tendency of customers to abandon a brand and stop being a paying client of a particular business. The percentage of customers that discontinue using a company’s products or services during a particular time period is called a customer churn (attrition) rate. 

Churn rate is a health indicator for businesses whose customers are subscribers and paying for services on a recurring basis


# Data Source and Preperation

Dataset is Telecommunication Churn from Kaggle Dataset 

The training dataset contains 4250 samples. Each sample contains 19 features and 1 boolean variable "churn" which indicates the class of the sample. The 19 input features and 1 target variable

In Data cleaning and preparation, We handle the categorical variables into machine learning format (Check the Jupyter notebook)

# Exploratory Data Analysis


1. No of Users per churn (If the churn number is 1 the customer has discontinued)

![image](Images/chrun_count_plot.png)

2. Number of Customer Service Calls made per churn

![image](Images/number customer_service_calls_churn_rate.png)

3. Churn Rate per state in the US

![image](Images/state chrun plot.png)

4. Total Daily calls and how it affects churn rate

![image](Images/total daily calls and churn rate.png)

5. Total Evening Calls and how it affects churn rate

![image](Images/total eve call and churn rate.png)







## Flow

1. Understand the business problem.
2. Load the provided notebook into the Watson Studio platform.
3. [Telco customer churn data set](https://community.watsonanalytics.com/wp-content/uploads/2015/03/WA_Fn-UseC_-Telco-Customer-Churn.csv) is loaded into the Jupyter Notebook.
4. Describe, analyze and visualize data in the notebook.
5. Preprocess the data, build machine learning models and test them.
6. Deploy a selected machine learning model into production.
7. Interact and consume your model using a frontend application.

## Included components

* [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio): Analyze data using RStudio, Jupyter, and Python in a configured, collaborative environment that includes IBM value-adds, such as managed Spark.
* [IBM Cloud Foundry](https://cloud.ibm.com/dashboard/cloudfoundry/overview): Deploy and run your applications without managing servers or clusters. Cloud Foundry automatically transforms source code into containers, scales them on demand, and manages user access and capacity.

## Featured technologies

* [Jupyter Notebooks](https://jupyter.org/): An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and explanatory text.
* [Pandas](https://pandas.pydata.org/):  An open source library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
* [Seaborn](https://seaborn.pydata.org/): A Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
* [Scikit-Learn](https://scikit-learn.org/): Machine Learning in Python. Simple and efficient tools for data mining and data analysis.
* [Watson Machine Learning Client](https://pypi.org/project/watson-machine-learning-client/): A library that allows working with Watson Machine Learning service on [IBM Cloud](https://cloud.ibm.com/catalog/services/machine-learning). Train, test and deploy your models as APIs for application development, share with colleagues using this python library.
* [NodeJS](https://nodejs.org/): A JavaScript runtime built on Chrome's V8 JavaScript engine, used for building full stack Javascript web applications.
* [ExpressJS](https://expressjs.com/): A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.

# Watch the Video

[![](https://i.ytimg.com/vi/qchkktwMA6U/0.jpg)](https://youtu.be/qchkktwMA6U)

# Steps

1. [Sign up for Watson Studio](#1-sign-up-for-watson-studio)
2. [Create a new Project](#2-create-a-new-project)
3. [Upload the dataset](#3-upload-the-dataset)
4. [Import notebook to Watson Studio](#4-import-notebook-to-watson-studio)
5. [Import dataset into the notebook](#5-import-dataset-into-the-notebook)
6. [Create Watson Machine Learning Service instance](#6-create-watson-machine-learning-service-instance)
7. [Follow the steps in the notebook](#7-follow-the-steps-in-the-notebook)
8. [Either Deploy to IBM Cloud or Deploy locally](#8-either-deploy-to-ibm-cloud-or-deploy-locally)

    8a. [Deploy to IBM Cloud](#8a-deploy-to-ibm-cloud)

    8b. [Deploy locally](#8b-deploy-locally)

### 1. Sign up for Watson Studio

Sign up for IBM's [Watson Studio](https://dataplatform.cloud.ibm.com/). By creating a project in Watson Studio a free tier Object Storage service will be created in your IBM Cloud account. Take note of your service names as you will need to select them in the following steps.

> Note: When creating your Object Storage service, select the Free storage type to avoid having to pay an upgrade fee.

### 2. Create a new Project

> Note: By creating a project in Watson Studio a free tier `Object Storage` service will be created in your IBM Cloud account. Take note of your service names as you will need to select them in the following steps.

* On Watson Studio's Welcome Page select `New Project`.

![](https://github.com/IBM/pattern-utils/blob/master/watson-studio/StudioStartCreateProject.png)

* Choose the `Data Science` option and click `Create Project`.

![](https://github.com/IBM/pattern-utils/blob/master/watson-studio/CreateDataScienceProject.png)

* Name your project, select the Cloud Object Storage service instance and click `Create`

![](doc/source/images/CreateProject.jpg)

### 3. Upload the dataset

* Download the dataset we will use in this pattern from the following link: [https://community.watsonanalytics.com/wp-content/uploads/2015/03/WA_Fn-UseC_-Telco-Customer-Churn.csv](https://community.watsonanalytics.com/wp-content/uploads/2015/03/WA_Fn-UseC_-Telco-Customer-Churn.csv)


* Drag and drop the dataset (`csv`) file you just downloaded to Watson Studio's dashboard to upload it to Cloud Object Storage.

![](doc/source/images/uploadData.jpg)

### 4. Import notebook to Watson Studio

* Create a **New Notebook**.

![](https://github.com/IBM/pattern-utils/blob/master/watson-studio/StudioAddToProjectNotebook.png)

* Import the notebook found in this repository inside the notebook folder by copying and pasting this URL in the relevant field `https://raw.githubusercontent.com/IBM/customer-churn-prediction/master/notebooks/customer-churn-prediction.ipynb`

* Give a name to the notebook and select a `Python 3.5` runtime environment, then click `Create`.

![](https://github.com/IBM/pattern-utils/blob/master/watson-studio/notebook_with_url_py35.png)

### 5. Import dataset into the notebook

To make the dataset available in the notebook, we need to refer to where it lives. Watson Studio automatically generates a connection to your Cloud Object Storage instance and gives access to your data.

* Click in the cell below `2. Loading Our Dataset`
* Then go to the Files section to the right of the notebook and click `Insert to code` for the data you have uploaded. Choose `Insert pandas DataFrame`.

### 6. Create Watson Machine Learning Service instance


* From [IBM Cloud Catalog](https://cloud.ibm.com/catalog/), under the Watson category, select `Machine Learning` or use the Search bar to find `Machine Learning`.

![](doc/source/images/chooseMachineLearning.jpg)

* Keep the setting as they are and click `Create`.

![](https://github.com/IBM/pattern-utils/blob/master/machine-learning/create-machine-learning.png)

* Once the service instance is created, navigate to the `Service credentials` tab on the left, view credentials and make a note of them.

> Note: If you can't see any credentials available, you can create a `New credential`.

![](https://github.com/IBM/pattern-utils/blob/master/machine-learning/ML-service-credentials.png)

* In the notebook available with this pattern, there is a cell with the WML credentials available after `14. ROC Curve and models comparisons`. You will need to replace the code inside with your credentials.

![](doc/source/images/insertCreds.jpg)

* Keep this tab open, or copy the credentials to a file to use later if you deploy the web app.

### 7. Follow the steps in the notebook

The steps should allow you to understand the dataset, analyze and visualize it. You will then go through the preprocessing and feature engineering processes to make the data suitable for modeling. Finally, you will build some machine learning models and test them to compare their performances.

### 8. Either Deploy to IBM Cloud or Deploy locally

#### 8a. Deploy to IBM Cloud

Click on the following button to clone the repo for this frontend app and create a toolchain to start deploying the app from there.

[![Deploy to IBM Cloud](https://cloud.ibm.com/devops/setup/deploy/button.png)](https://cloud.ibm.com/devops/setup/deploy?repository=https://github.com/IBM/customer-churn-prediction)

* Under `IBM Cloud API Key:` choose `Create+`, and then click on ``Deploy``.

To monitor the deployment, in Toolchains click on `Delivery Pipeline`  and view the logs while the apps are being deployed.

* Once the app has deployed, Click on `Runtime` on the menu and navigate to the `Environment variables` tab.

![](doc/source/images/customerChurnENVvariables.png)

* Update the 5 environment variables with the `WML_INSTANCE_NAME`, `USERNAME`, `PASSWORD`, `INSTANCE_ID`, and `URL`, that you saved at the end of [Create Watson Machine Learning Service instance](#6-create-watson-machine-learning-service-instance). Add the `MODEL_URL` that you created in the Notebook as the variable `scoring_endpoint`.
The app will automatically restart and be ready for use.

### 8b. Deploy locally

For developing the UI locally and testing it:

* `cd frontend/`

* Create a `.env` file in frontend folder (frontend/.env) to hold your credentials.

`cp env.example .env `

For our purposes here, our `.env` file will look like the following:

```
WML_INSTANCE_NAME=**Enter with your Watson Machine Learning service instance name**
USERNAME=**Enter your WML username found in credentials**
PASSWORD=**Enter your WML password found in credentials**
INSTANCE_ID=**Enter your WML instance_id found in credentials**
URL=**Enter your WML url found in credentials**
MODEL_URL=**Change with your model URL after deploying it to the cloud as in step 8**

```
* Copy the variable for the .env file using the variables obtained at the end of [Create Watson Machine Learning Service instance](#6-create-watson-machine-learning-service-instance). Add the `MODEL_URL` that you created in the Notebook.

* Run the application.

```
cd frontend/
npm install
npm start
```

You can view the application in any browser by navigating to [http://localhost:3000](http://localhost:3000). Feel free to test it out.

# Sample output

* Using Postman:

![](doc/source/images/sample_output.png)

* Using the UI app:

![](doc/source/images/sample_output2.jpg)

# Links
* [Demo video on Youtube](https://youtu.be/qchkktwMA6U)
* [Read more about CRISPDM](https://www.ibm.com/support/knowledgecenter/en/SS3RA7_15.0.0/com.ibm.spss.crispdm.help/crisp_overview.htm)

# Learn more
* **Artificial Intelligence Code Patterns**: Enjoyed this Code Pattern? Check out our other [AI Code Patterns](https://developer.ibm.com/technologies/artificial-intelligence/).
* **Data Analytics Code Patterns**: Enjoyed this Code Pattern? Check out our other [Data Analytics Code Patterns](https://developer.ibm.com/technologies/data-science/)
* **AI and Data Code Pattern Playlist**: Bookmark our [playlist](https://www.youtube.com/playlist?list=PLzUbsvIyrNfknNewObx5N7uGZ5FKH0Fde) with all of our Code Pattern videos
* **With Watson**: Want to take your Watson app to the next level? Looking to utilize Watson Brand assets? [Join the With Watson program](https://www.ibm.com/watson/with-watson/) to leverage exclusive brand, marketing, and tech resources to amplify and accelerate your Watson embedded commercial solution.
* **IBM Watson Studio**: Master the art of data science with IBM's [Watson Studio](https://www.ibm.com/cloud/watson-studio)

# License
This code pattern is licensed under the Apache Software License, Version 2.  Separate third party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1 (DCO)](https://developercertificate.org/) and the [Apache Software License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache Software License (ASL) FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)
