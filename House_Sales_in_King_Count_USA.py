{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "prev_pub_hash": "8e1b9a014f4d5dd1f594f0f84b9e2a27c098aabf3c393aa0062e8aef51a297d0"
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "<p style=\"text-align:center\">\n    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01\" target=\"_blank\">\n    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"300\" alt=\"Skills Network Logo\">\n    </a>\n</p>\n\n<h1 align=\"center\"><font size=\"5\">Final Project: House Sales in King County, USA </font></h1>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>Table of Contents</h2>\n<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n    <ul>\n    <li><a href=\"#Instructions\">Instructions</a></li>\n    <li><a href=\"#About-the-Dataset\">About the Dataset</a></li>\n    <li><a href=\"#Module-1:-Importing-Data-Sets\">Module 1: Importing Data </a></li>\n    <li><a href=\"#Module-2:-Data-Wrangling\">Module 2: Data Wrangling</a> </li>\n    <li><a href=\"#Module-3:-Exploratory-Data-Analysis\">Module 3: Exploratory Data Analysis</a></li>\n    <li><a href=\"#Module-4:-Model-Development\">Module 4: Model Development</a></li>\n    <li><a href=\"#Module-5:-Model-Evaluation-and-Refinement\">Module 5: Model Evaluation and Refinement</a></li>\n</a></li>\n</div>\n<p>Estimated Time Needed: <strong>75 min</strong></p>\n</div>\n\n<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "# Instructions\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In this assignment, you are a Data Analyst working at a Real Estate Investment Trust. The Trust would like to start investing in Residential real estate. You are tasked with determining the market price of a house given a set of features. You will analyze and predict housing prices using attributes or features such as square footage, number of bedrooms, number of floors, and so on. This is a template notebook; your job is to complete the ten questions. Some hints to the questions are given.\n\nAs you are completing this notebook, take and save the **screenshots** of the final outputs of your solutions (e.g., final charts, tables, calculation results etc.). They will need to be shared in the following Peer Review section of the Final Project module.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "# About the Dataset\n\nThis dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015. It was taken from [here](https://www.kaggle.com/harlfoxem/housesalesprediction?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01). It was also slightly modified for the purposes of this course. \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "| Variable      | Description                                                                                                 |\n| ------------- | ----------------------------------------------------------------------------------------------------------- |\n| id            | A notation for a house                                                                                      |\n| date          | Date house was sold                                                                                         |\n| price         | Price is prediction target                                                                                  |\n| bedrooms      | Number of bedrooms                                                                                          |\n| bathrooms     | Number of bathrooms                                                                                         |\n| sqft_living   | Square footage of the home                                                                                  |\n| sqft_lot      | Square footage of the lot                                                                                   |\n| floors        | Total floors (levels) in house                                                                              |\n| waterfront    | House which has a view to a waterfront                                                                      |\n| view          | Has been viewed                                                                                             |\n| condition     | How good the condition is overall                                                                           |\n| grade         | overall grade given to the housing unit, based on King County grading system                                |\n| sqft_above    | Square footage of house apart from basement                                                                 |\n| sqft_basement | Square footage of the basement                                                                              |\n| yr_built      | Built Year                                                                                                  |\n| yr_renovated  | Year when house was renovated                                                                               |\n| zipcode       | Zip code                                                                                                    |\n| lat           | Latitude coordinate                                                                                         |\n| long          | Longitude coordinate                                                                                        |\n| sqft_living15 | Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area |\n| sqft_lot15    | LotSize area in 2015(implies-- some renovations)                                                            |\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## **Import the required libraries**\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# All Libraries required for this lab are listed below. The libraries pre-installed on Skills Network Labs are commented.\n# !mamba install -qy pandas==1.3.4 numpy==1.21.4 seaborn==0.9.0 matplotlib==3.5.0 scikit-learn==0.20.1\n# Note: If your environment doesn't support \"!mamba install\", use \"!pip install\"",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "# Surpress warnings:\ndef warn(*args, **kwargs):\n    pass\nimport warnings\nwarnings.warn = warn",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 1
    },
    {
      "cell_type": "code",
      "source": "# !pip install seaborn",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 7
    },
    {
      "cell_type": "code",
      "source": "import piplite\nawait piplite.install('seaborn')",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 9
    },
    {
      "cell_type": "code",
      "source": "import pandas as pd\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport seaborn as sns\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler,PolynomialFeatures\nfrom sklearn.linear_model import LinearRegression\n%matplotlib inline",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 10
    },
    {
      "cell_type": "markdown",
      "source": "# Module 1: Importing Data Sets\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Download the dataset by running the cell below.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "from pyodide.http import pyfetch\n\nasync def download(url, filename):\n    response = await pyfetch(url)\n    if response.status == 200:\n        with open(filename, \"wb\") as f:\n            f.write(await response.bytes())",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 11
    },
    {
      "cell_type": "code",
      "source": "filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 12
    },
    {
      "cell_type": "code",
      "source": "await download(filepath, \"housing.csv\")\nfile_name=\"housing.csv\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 13
    },
    {
      "cell_type": "markdown",
      "source": "Load the csv:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df = pd.read_csv(file_name)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 14
    },
    {
      "cell_type": "markdown",
      "source": "> Note: This version of the lab is working on JupyterLite, which requires the dataset to be downloaded to the interface.While working on the downloaded version of this notebook on their local machines(Jupyter Anaconda), the learners can simply **skip the steps above,** and simply use the URL directly in the `pandas.read_csv()` function. You can uncomment and run the statements in the cell below.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'\n#df = pd.read_csv(filepath, header=None)",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": "We use the method <code>head</code> to display the first 5 columns of the dataframe.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df.head()",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 15,
          "output_type": "execute_result",
          "data": {
            "text/plain": "   Unnamed: 0          id             date     price  bedrooms  bathrooms  \\\n0           0  7129300520  20141013T000000  221900.0       3.0       1.00   \n1           1  6414100192  20141209T000000  538000.0       3.0       2.25   \n2           2  5631500400  20150225T000000  180000.0       2.0       1.00   \n3           3  2487200875  20141209T000000  604000.0       4.0       3.00   \n4           4  1954400510  20150218T000000  510000.0       3.0       2.00   \n\n   sqft_living  sqft_lot  floors  waterfront  ...  grade  sqft_above  \\\n0         1180      5650     1.0           0  ...      7        1180   \n1         2570      7242     2.0           0  ...      7        2170   \n2          770     10000     1.0           0  ...      6         770   \n3         1960      5000     1.0           0  ...      7        1050   \n4         1680      8080     1.0           0  ...      8        1680   \n\n   sqft_basement  yr_built  yr_renovated  zipcode      lat     long  \\\n0              0      1955             0    98178  47.5112 -122.257   \n1            400      1951          1991    98125  47.7210 -122.319   \n2              0      1933             0    98028  47.7379 -122.233   \n3            910      1965             0    98136  47.5208 -122.393   \n4              0      1987             0    98074  47.6168 -122.045   \n\n   sqft_living15  sqft_lot15  \n0           1340        5650  \n1           1690        7639  \n2           2720        8062  \n3           1360        5000  \n4           1800        7503  \n\n[5 rows x 22 columns]",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>id</th>\n      <th>date</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>0</td>\n      <td>7129300520</td>\n      <td>20141013T000000</td>\n      <td>221900.0</td>\n      <td>3.0</td>\n      <td>1.00</td>\n      <td>1180</td>\n      <td>5650</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>7</td>\n      <td>1180</td>\n      <td>0</td>\n      <td>1955</td>\n      <td>0</td>\n      <td>98178</td>\n      <td>47.5112</td>\n      <td>-122.257</td>\n      <td>1340</td>\n      <td>5650</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>6414100192</td>\n      <td>20141209T000000</td>\n      <td>538000.0</td>\n      <td>3.0</td>\n      <td>2.25</td>\n      <td>2570</td>\n      <td>7242</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>7</td>\n      <td>2170</td>\n      <td>400</td>\n      <td>1951</td>\n      <td>1991</td>\n      <td>98125</td>\n      <td>47.7210</td>\n      <td>-122.319</td>\n      <td>1690</td>\n      <td>7639</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2</td>\n      <td>5631500400</td>\n      <td>20150225T000000</td>\n      <td>180000.0</td>\n      <td>2.0</td>\n      <td>1.00</td>\n      <td>770</td>\n      <td>10000</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>6</td>\n      <td>770</td>\n      <td>0</td>\n      <td>1933</td>\n      <td>0</td>\n      <td>98028</td>\n      <td>47.7379</td>\n      <td>-122.233</td>\n      <td>2720</td>\n      <td>8062</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>3</td>\n      <td>2487200875</td>\n      <td>20141209T000000</td>\n      <td>604000.0</td>\n      <td>4.0</td>\n      <td>3.00</td>\n      <td>1960</td>\n      <td>5000</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>7</td>\n      <td>1050</td>\n      <td>910</td>\n      <td>1965</td>\n      <td>0</td>\n      <td>98136</td>\n      <td>47.5208</td>\n      <td>-122.393</td>\n      <td>1360</td>\n      <td>5000</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>4</td>\n      <td>1954400510</td>\n      <td>20150218T000000</td>\n      <td>510000.0</td>\n      <td>3.0</td>\n      <td>2.00</td>\n      <td>1680</td>\n      <td>8080</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>8</td>\n      <td>1680</td>\n      <td>0</td>\n      <td>1987</td>\n      <td>0</td>\n      <td>98074</td>\n      <td>47.6168</td>\n      <td>-122.045</td>\n      <td>1800</td>\n      <td>7503</td>\n    </tr>\n  </tbody>\n</table>\n<p>5 rows × 22 columns</p>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 15
    },
    {
      "cell_type": "markdown",
      "source": "### Question 1\n\nDisplay the data types of each column using the function dtypes. Take a screenshot of your code and output. You will need to submit the screenshot for the final project. \n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\ndf.dtypes",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 19,
          "output_type": "execute_result",
          "data": {
            "text/plain": "Unnamed: 0         int64\nid                 int64\ndate              object\nprice            float64\nbedrooms         float64\nbathrooms        float64\nsqft_living        int64\nsqft_lot           int64\nfloors           float64\nwaterfront         int64\nview               int64\ncondition          int64\ngrade              int64\nsqft_above         int64\nsqft_basement      int64\nyr_built           int64\nyr_renovated       int64\nzipcode            int64\nlat              float64\nlong             float64\nsqft_living15      int64\nsqft_lot15         int64\ndtype: object"
          },
          "metadata": {}
        }
      ],
      "execution_count": 19
    },
    {
      "cell_type": "markdown",
      "source": "We use the method describe to obtain a statistical summary of the dataframe.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df.describe()",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 20,
          "output_type": "execute_result",
          "data": {
            "text/plain": "        Unnamed: 0            id         price      bedrooms     bathrooms  \\\ncount  21613.00000  2.161300e+04  2.161300e+04  21600.000000  21603.000000   \nmean   10806.00000  4.580302e+09  5.400881e+05      3.372870      2.115736   \nstd     6239.28002  2.876566e+09  3.671272e+05      0.926657      0.768996   \nmin        0.00000  1.000102e+06  7.500000e+04      1.000000      0.500000   \n25%     5403.00000  2.123049e+09  3.219500e+05      3.000000      1.750000   \n50%    10806.00000  3.904930e+09  4.500000e+05      3.000000      2.250000   \n75%    16209.00000  7.308900e+09  6.450000e+05      4.000000      2.500000   \nmax    21612.00000  9.900000e+09  7.700000e+06     33.000000      8.000000   \n\n        sqft_living      sqft_lot        floors    waterfront          view  \\\ncount  21613.000000  2.161300e+04  21613.000000  21613.000000  21613.000000   \nmean    2079.899736  1.510697e+04      1.494309      0.007542      0.234303   \nstd      918.440897  4.142051e+04      0.539989      0.086517      0.766318   \nmin      290.000000  5.200000e+02      1.000000      0.000000      0.000000   \n25%     1427.000000  5.040000e+03      1.000000      0.000000      0.000000   \n50%     1910.000000  7.618000e+03      1.500000      0.000000      0.000000   \n75%     2550.000000  1.068800e+04      2.000000      0.000000      0.000000   \nmax    13540.000000  1.651359e+06      3.500000      1.000000      4.000000   \n\n       ...         grade    sqft_above  sqft_basement      yr_built  \\\ncount  ...  21613.000000  21613.000000   21613.000000  21613.000000   \nmean   ...      7.656873   1788.390691     291.509045   1971.005136   \nstd    ...      1.175459    828.090978     442.575043     29.373411   \nmin    ...      1.000000    290.000000       0.000000   1900.000000   \n25%    ...      7.000000   1190.000000       0.000000   1951.000000   \n50%    ...      7.000000   1560.000000       0.000000   1975.000000   \n75%    ...      8.000000   2210.000000     560.000000   1997.000000   \nmax    ...     13.000000   9410.000000    4820.000000   2015.000000   \n\n       yr_renovated       zipcode           lat          long  sqft_living15  \\\ncount  21613.000000  21613.000000  21613.000000  21613.000000   21613.000000   \nmean      84.402258  98077.939805     47.560053   -122.213896    1986.552492   \nstd      401.679240     53.505026      0.138564      0.140828     685.391304   \nmin        0.000000  98001.000000     47.155900   -122.519000     399.000000   \n25%        0.000000  98033.000000     47.471000   -122.328000    1490.000000   \n50%        0.000000  98065.000000     47.571800   -122.230000    1840.000000   \n75%        0.000000  98118.000000     47.678000   -122.125000    2360.000000   \nmax     2015.000000  98199.000000     47.777600   -121.315000    6210.000000   \n\n          sqft_lot15  \ncount   21613.000000  \nmean    12768.455652  \nstd     27304.179631  \nmin       651.000000  \n25%      5100.000000  \n50%      7620.000000  \n75%     10083.000000  \nmax    871200.000000  \n\n[8 rows x 21 columns]",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>id</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>21613.00000</td>\n      <td>2.161300e+04</td>\n      <td>2.161300e+04</td>\n      <td>21600.000000</td>\n      <td>21603.000000</td>\n      <td>21613.000000</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>...</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>10806.00000</td>\n      <td>4.580302e+09</td>\n      <td>5.400881e+05</td>\n      <td>3.372870</td>\n      <td>2.115736</td>\n      <td>2079.899736</td>\n      <td>1.510697e+04</td>\n      <td>1.494309</td>\n      <td>0.007542</td>\n      <td>0.234303</td>\n      <td>...</td>\n      <td>7.656873</td>\n      <td>1788.390691</td>\n      <td>291.509045</td>\n      <td>1971.005136</td>\n      <td>84.402258</td>\n      <td>98077.939805</td>\n      <td>47.560053</td>\n      <td>-122.213896</td>\n      <td>1986.552492</td>\n      <td>12768.455652</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>6239.28002</td>\n      <td>2.876566e+09</td>\n      <td>3.671272e+05</td>\n      <td>0.926657</td>\n      <td>0.768996</td>\n      <td>918.440897</td>\n      <td>4.142051e+04</td>\n      <td>0.539989</td>\n      <td>0.086517</td>\n      <td>0.766318</td>\n      <td>...</td>\n      <td>1.175459</td>\n      <td>828.090978</td>\n      <td>442.575043</td>\n      <td>29.373411</td>\n      <td>401.679240</td>\n      <td>53.505026</td>\n      <td>0.138564</td>\n      <td>0.140828</td>\n      <td>685.391304</td>\n      <td>27304.179631</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>0.00000</td>\n      <td>1.000102e+06</td>\n      <td>7.500000e+04</td>\n      <td>1.000000</td>\n      <td>0.500000</td>\n      <td>290.000000</td>\n      <td>5.200000e+02</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>1.000000</td>\n      <td>290.000000</td>\n      <td>0.000000</td>\n      <td>1900.000000</td>\n      <td>0.000000</td>\n      <td>98001.000000</td>\n      <td>47.155900</td>\n      <td>-122.519000</td>\n      <td>399.000000</td>\n      <td>651.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>5403.00000</td>\n      <td>2.123049e+09</td>\n      <td>3.219500e+05</td>\n      <td>3.000000</td>\n      <td>1.750000</td>\n      <td>1427.000000</td>\n      <td>5.040000e+03</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1190.000000</td>\n      <td>0.000000</td>\n      <td>1951.000000</td>\n      <td>0.000000</td>\n      <td>98033.000000</td>\n      <td>47.471000</td>\n      <td>-122.328000</td>\n      <td>1490.000000</td>\n      <td>5100.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>10806.00000</td>\n      <td>3.904930e+09</td>\n      <td>4.500000e+05</td>\n      <td>3.000000</td>\n      <td>2.250000</td>\n      <td>1910.000000</td>\n      <td>7.618000e+03</td>\n      <td>1.500000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1560.000000</td>\n      <td>0.000000</td>\n      <td>1975.000000</td>\n      <td>0.000000</td>\n      <td>98065.000000</td>\n      <td>47.571800</td>\n      <td>-122.230000</td>\n      <td>1840.000000</td>\n      <td>7620.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>16209.00000</td>\n      <td>7.308900e+09</td>\n      <td>6.450000e+05</td>\n      <td>4.000000</td>\n      <td>2.500000</td>\n      <td>2550.000000</td>\n      <td>1.068800e+04</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>8.000000</td>\n      <td>2210.000000</td>\n      <td>560.000000</td>\n      <td>1997.000000</td>\n      <td>0.000000</td>\n      <td>98118.000000</td>\n      <td>47.678000</td>\n      <td>-122.125000</td>\n      <td>2360.000000</td>\n      <td>10083.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>21612.00000</td>\n      <td>9.900000e+09</td>\n      <td>7.700000e+06</td>\n      <td>33.000000</td>\n      <td>8.000000</td>\n      <td>13540.000000</td>\n      <td>1.651359e+06</td>\n      <td>3.500000</td>\n      <td>1.000000</td>\n      <td>4.000000</td>\n      <td>...</td>\n      <td>13.000000</td>\n      <td>9410.000000</td>\n      <td>4820.000000</td>\n      <td>2015.000000</td>\n      <td>2015.000000</td>\n      <td>98199.000000</td>\n      <td>47.777600</td>\n      <td>-121.315000</td>\n      <td>6210.000000</td>\n      <td>871200.000000</td>\n    </tr>\n  </tbody>\n</table>\n<p>8 rows × 21 columns</p>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 20
    },
    {
      "cell_type": "markdown",
      "source": "# Module 2: Data Wrangling\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "### Question 2\n\nDrop the columns <code>\"id\"</code>  and <code>\"Unnamed: 0\"</code> from axis 1 using the method <code>drop()</code>, then use the method <code>describe()</code> to obtain a statistical summary of the data. Make sure the <code>inplace</code> parameter is set to <code>True</code>. Take a screenshot of your code and output. You will need to submit the screenshot for the final project. \n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\ndf.drop(['Unnamed: 0', 'id'], axis=1, inplace=True)\ndf.describe()",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 21,
          "output_type": "execute_result",
          "data": {
            "text/plain": "              price      bedrooms     bathrooms   sqft_living      sqft_lot  \\\ncount  2.161300e+04  21600.000000  21603.000000  21613.000000  2.161300e+04   \nmean   5.400881e+05      3.372870      2.115736   2079.899736  1.510697e+04   \nstd    3.671272e+05      0.926657      0.768996    918.440897  4.142051e+04   \nmin    7.500000e+04      1.000000      0.500000    290.000000  5.200000e+02   \n25%    3.219500e+05      3.000000      1.750000   1427.000000  5.040000e+03   \n50%    4.500000e+05      3.000000      2.250000   1910.000000  7.618000e+03   \n75%    6.450000e+05      4.000000      2.500000   2550.000000  1.068800e+04   \nmax    7.700000e+06     33.000000      8.000000  13540.000000  1.651359e+06   \n\n             floors    waterfront          view     condition         grade  \\\ncount  21613.000000  21613.000000  21613.000000  21613.000000  21613.000000   \nmean       1.494309      0.007542      0.234303      3.409430      7.656873   \nstd        0.539989      0.086517      0.766318      0.650743      1.175459   \nmin        1.000000      0.000000      0.000000      1.000000      1.000000   \n25%        1.000000      0.000000      0.000000      3.000000      7.000000   \n50%        1.500000      0.000000      0.000000      3.000000      7.000000   \n75%        2.000000      0.000000      0.000000      4.000000      8.000000   \nmax        3.500000      1.000000      4.000000      5.000000     13.000000   \n\n         sqft_above  sqft_basement      yr_built  yr_renovated       zipcode  \\\ncount  21613.000000   21613.000000  21613.000000  21613.000000  21613.000000   \nmean    1788.390691     291.509045   1971.005136     84.402258  98077.939805   \nstd      828.090978     442.575043     29.373411    401.679240     53.505026   \nmin      290.000000       0.000000   1900.000000      0.000000  98001.000000   \n25%     1190.000000       0.000000   1951.000000      0.000000  98033.000000   \n50%     1560.000000       0.000000   1975.000000      0.000000  98065.000000   \n75%     2210.000000     560.000000   1997.000000      0.000000  98118.000000   \nmax     9410.000000    4820.000000   2015.000000   2015.000000  98199.000000   \n\n                lat          long  sqft_living15     sqft_lot15  \ncount  21613.000000  21613.000000   21613.000000   21613.000000  \nmean      47.560053   -122.213896    1986.552492   12768.455652  \nstd        0.138564      0.140828     685.391304   27304.179631  \nmin       47.155900   -122.519000     399.000000     651.000000  \n25%       47.471000   -122.328000    1490.000000    5100.000000  \n50%       47.571800   -122.230000    1840.000000    7620.000000  \n75%       47.678000   -122.125000    2360.000000   10083.000000  \nmax       47.777600   -121.315000    6210.000000  871200.000000  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>condition</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>2.161300e+04</td>\n      <td>21600.000000</td>\n      <td>21603.000000</td>\n      <td>21613.000000</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>5.400881e+05</td>\n      <td>3.372870</td>\n      <td>2.115736</td>\n      <td>2079.899736</td>\n      <td>1.510697e+04</td>\n      <td>1.494309</td>\n      <td>0.007542</td>\n      <td>0.234303</td>\n      <td>3.409430</td>\n      <td>7.656873</td>\n      <td>1788.390691</td>\n      <td>291.509045</td>\n      <td>1971.005136</td>\n      <td>84.402258</td>\n      <td>98077.939805</td>\n      <td>47.560053</td>\n      <td>-122.213896</td>\n      <td>1986.552492</td>\n      <td>12768.455652</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>3.671272e+05</td>\n      <td>0.926657</td>\n      <td>0.768996</td>\n      <td>918.440897</td>\n      <td>4.142051e+04</td>\n      <td>0.539989</td>\n      <td>0.086517</td>\n      <td>0.766318</td>\n      <td>0.650743</td>\n      <td>1.175459</td>\n      <td>828.090978</td>\n      <td>442.575043</td>\n      <td>29.373411</td>\n      <td>401.679240</td>\n      <td>53.505026</td>\n      <td>0.138564</td>\n      <td>0.140828</td>\n      <td>685.391304</td>\n      <td>27304.179631</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>7.500000e+04</td>\n      <td>1.000000</td>\n      <td>0.500000</td>\n      <td>290.000000</td>\n      <td>5.200000e+02</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>1.000000</td>\n      <td>1.000000</td>\n      <td>290.000000</td>\n      <td>0.000000</td>\n      <td>1900.000000</td>\n      <td>0.000000</td>\n      <td>98001.000000</td>\n      <td>47.155900</td>\n      <td>-122.519000</td>\n      <td>399.000000</td>\n      <td>651.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>3.219500e+05</td>\n      <td>3.000000</td>\n      <td>1.750000</td>\n      <td>1427.000000</td>\n      <td>5.040000e+03</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>3.000000</td>\n      <td>7.000000</td>\n      <td>1190.000000</td>\n      <td>0.000000</td>\n      <td>1951.000000</td>\n      <td>0.000000</td>\n      <td>98033.000000</td>\n      <td>47.471000</td>\n      <td>-122.328000</td>\n      <td>1490.000000</td>\n      <td>5100.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>4.500000e+05</td>\n      <td>3.000000</td>\n      <td>2.250000</td>\n      <td>1910.000000</td>\n      <td>7.618000e+03</td>\n      <td>1.500000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>3.000000</td>\n      <td>7.000000</td>\n      <td>1560.000000</td>\n      <td>0.000000</td>\n      <td>1975.000000</td>\n      <td>0.000000</td>\n      <td>98065.000000</td>\n      <td>47.571800</td>\n      <td>-122.230000</td>\n      <td>1840.000000</td>\n      <td>7620.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>6.450000e+05</td>\n      <td>4.000000</td>\n      <td>2.500000</td>\n      <td>2550.000000</td>\n      <td>1.068800e+04</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>4.000000</td>\n      <td>8.000000</td>\n      <td>2210.000000</td>\n      <td>560.000000</td>\n      <td>1997.000000</td>\n      <td>0.000000</td>\n      <td>98118.000000</td>\n      <td>47.678000</td>\n      <td>-122.125000</td>\n      <td>2360.000000</td>\n      <td>10083.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>7.700000e+06</td>\n      <td>33.000000</td>\n      <td>8.000000</td>\n      <td>13540.000000</td>\n      <td>1.651359e+06</td>\n      <td>3.500000</td>\n      <td>1.000000</td>\n      <td>4.000000</td>\n      <td>5.000000</td>\n      <td>13.000000</td>\n      <td>9410.000000</td>\n      <td>4820.000000</td>\n      <td>2015.000000</td>\n      <td>2015.000000</td>\n      <td>98199.000000</td>\n      <td>47.777600</td>\n      <td>-121.315000</td>\n      <td>6210.000000</td>\n      <td>871200.000000</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 21
    },
    {
      "cell_type": "markdown",
      "source": "We can see we have missing values for the columns <code> bedrooms</code>  and <code> bathrooms </code>\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "print(\"number of NaN values for the column bedrooms :\", df['bedrooms'].isnull().sum())\nprint(\"number of NaN values for the column bathrooms :\", df['bathrooms'].isnull().sum())\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "number of NaN values for the column bedrooms : 13\nnumber of NaN values for the column bathrooms : 10\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 22
    },
    {
      "cell_type": "markdown",
      "source": "We can replace the missing values of the column <code>'bedrooms'</code> with the mean of the column  <code>'bedrooms' </code> using the method <code>replace()</code>. Don't forget to set the <code>inplace</code> parameter to <code>True</code>\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "mean=df['bedrooms'].mean()\ndf['bedrooms'].replace(np.nan,mean, inplace=True)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 23
    },
    {
      "cell_type": "markdown",
      "source": "We also replace the missing values of the column <code>'bathrooms'</code> with the mean of the column  <code>'bathrooms' </code> using the method <code>replace()</code>. Don't forget to set the <code> inplace </code>  parameter top <code> True </code>\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "mean=df['bathrooms'].mean()\ndf['bathrooms'].replace(np.nan,mean, inplace=True)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 24
    },
    {
      "cell_type": "code",
      "source": "print(\"number of NaN values for the column bedrooms :\", df['bedrooms'].isnull().sum())\nprint(\"number of NaN values for the column bathrooms :\", df['bathrooms'].isnull().sum())",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "number of NaN values for the column bedrooms : 0\nnumber of NaN values for the column bathrooms : 0\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 25
    },
    {
      "cell_type": "markdown",
      "source": "# Module 3: Exploratory Data Analysis\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "### Question 3\n\nUse the method <code>value_counts</code> to count the number of houses with unique floor values, use the method <code>.to_frame()</code> to convert it to a data frame. Take a screenshot of your code and output. You will need to submit the screenshot for the final project. \n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\nfloor_counts = df['floors'].value_counts().to_frame()\nfloor_counts",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 28,
          "output_type": "execute_result",
          "data": {
            "text/plain": "        count\nfloors       \n1.0     10680\n2.0      8241\n1.5      1910\n3.0       613\n2.5       161\n3.5         8",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>count</th>\n    </tr>\n    <tr>\n      <th>floors</th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1.0</th>\n      <td>10680</td>\n    </tr>\n    <tr>\n      <th>2.0</th>\n      <td>8241</td>\n    </tr>\n    <tr>\n      <th>1.5</th>\n      <td>1910</td>\n    </tr>\n    <tr>\n      <th>3.0</th>\n      <td>613</td>\n    </tr>\n    <tr>\n      <th>2.5</th>\n      <td>161</td>\n    </tr>\n    <tr>\n      <th>3.5</th>\n      <td>8</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 28
    },
    {
      "cell_type": "markdown",
      "source": "### Question 4\n\nUse the function <code>boxplot</code> in the seaborn library  to  determine whether houses with a waterfront view or without a waterfront view have more price outliers. Take a screenshot of your code and boxplot. You will need to submit the screenshot for the final project. \n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "sns.boxplot(x='waterfront', y='price', data=df)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 29,
          "output_type": "execute_result",
          "data": {
            "text/plain": "<AxesSubplot:xlabel='waterfront', ylabel='price'>"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 640x480 with 1 Axes>",
            "image/png": "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UJGkI0eOeMdC1fQDAASei76iIkk9evTQn//8Z23cuFFDhgxR69atfc7PnDmzXopD03b06NF67QcA8D+XFFSWLVumdu3aadu2bdq2bZvPOYfDQVBBvajZFbl79+7KzMzU22+/rUOHDikqKkrjxo3T9OnT9c0337B7MgAEsEsKKmfP+qmZouxwOOqnIuD/1Wx86XK5FBwc7DMF2ePxeBdTqm2DTABAYLikMSrSj1dV+vXrpxYtWqhFixbq16+f/vrXv9ZnbWjiasLvV199VeumhDVL6BOSASBwXdIVlUceeUQLFy7UjBkzlJCQIEnKzc3Vgw8+qKKiIv35z3+u1yLRNA0cOFCvvPKKYmJilJ+fr+TkZO+5iIgIxcTEqKioSAMHDrSvSABAg7qkoJKVlaUXXnhBEydO9Lb9+te/Vnx8vGbMmEFQQb0YOHCg2rVrp6KiIl199dW68847veuobN68WZs2bVL79u0JKgAQwC4pqJw+fVpDhw49p33IkCE6c+bMZRcFSJLT6dTs2bOVmpqq7du3a9OmTd5zLpdLDodDDz74oJxOp41VAgAa0iWNUfnd736nrKysc9qXLl2qpKSkyy4KqJGYmKi0tDS1b9/epz0sLExpaWlKTEy0qTIAQGO4pCsq0o+DaT/88ENdffXVkqTNmzerqKhId911l2bPnu3tt3DhwsuvEk1aYmKihg0bpueff17fffedunTpoj/84Q9q2bKl3aUBABrYJQWVnTt3avDgwZKk/Px8SVKHDh3UoUMH7dy509uP2RioD88995xWr17tXYn2s88+09tvv60JEyboj3/8o83VAQAa0iUFlU8++aS+6wBq9dxzz2nlypVq37697rnnHiUkJCg3N1fLli3TypUrJYmwAgAB7JLXUQEaWnV1tVavXq327dtr5cqV6ty5s3bs2KHOnTt7w8vq1atVXV1td6kAgAZyyWNUgIa2du1aud1ujRw5UpMnT1ZJSYn3XEREhEaOHKm33npLa9eu9Vm1FgAQOAgqMNahQ4ckSW+//baGDx+uESNGqLq6WsHBwTp48KDefvttn34AgMBDUIGxIiIiJEkhISHasmWLPB6P91xQUJBCQkJUVlbm7QcACDwEFRgrLi5OklRWVlbrYNpjx4759AMABB4G08JYpaWl3q89Ho8sy/IeZ19dObsfACCwcEUFxtq9e7ckqXfv3tq9e7eeeuop7zmHw6FevXppz5492r17t2666Sa7ygQANCCuqMB4hYWF57RZlqWioiIbqgEANCaCCozVuXNnSdLJkyclSb169dLkyZPVq1cvn/aafgCAwENQgbGuu+4679dBQUHas2ePXnrpJe3Zs0dBQUG19gMABBaCCox19piUoKAgXXvttZo+fbquvfZan6Bydj8AQGBhMC2MVbOQW4cOHVRaWqqPP/5YH3/8sSTJ6XSqQ4cOOnr0KAu+AUAA44oKjNW6dWtJUrNmzXymI0uS2+1Ws2bNfPoBAAIPQQXGGjt2rCSppKREDofD55zD4fDu/VPTDwAQeAgqMFanTp28X1uWpWHDhumZZ57RsGHDZFlWrf0AAIGFMSowVn5+vqQfr55YlqWtW7dq69at3vM17fn5+Ro2bJhdZQIAGpCtV1SysrIUHx+vkJAQhYSEKCEhQe+9956dJcEgO3fulCSfqydnq2mv6QcACDy2BpUuXbro8ccf17Zt2/TZZ5/p2muv1W233aZdu3bZWRYM0bJly3rtBwDwP7YGlXHjxunmm29Wjx491LNnT6Wnp6tNmzbatGmTnWXBEImJifXaDwDgf4wZTOt2u7Vy5UqdOHFCCQkJtfapqqpSeXm5z4HA9e677/o8bt26tSIiIs6ZjvzTfgCAwGH7YNovv/xSCQkJOnXqlNq0aaM1a9aoT58+tfbNyMhQWlpaI1cIu3zzzTc+j0+cOKETJ05csB8AIHDYfkXlyiuv1I4dO7R582ZNmzZNkydP1ldffVVr37lz56qsrMx7HDhwoJGrRWOqqKio134AAP9j+xWV4OBgXXHFFZKkIUOGaOvWrXr66af1/PPPn9PX5XLJ5XI1domwSatWrbw7JEtSz5491blzZx08eFD79u3z6QcACEy2B5Wf8ng8qqqqsrsMGOD06dM+j/ft2+cTUM7XDwAQOGwNKnPnztXYsWMVExOjiooKvfrqq1q/fr0++OADO8uCIU6dOlWv/QAA/sfWoHLkyBHdddddKi4uVmhoqOLj4/XBBx/ohhtusLMsGCIoqG5DqOraDwDgf2wNKsuWLbPz28NwXbt21Z49e+rUDwAQmPhTFMa65ZZb6rUfAMD/EFRgLMaoAAAIKjBWmzZt6rUfAMD/EFRgrPMt/Hep/QAA/oegAmPl5+fXaz8AgP8hqMBYP/zwQ732AwD4H4IKjNWiRQvv1w6Hw+fc2Y/P7gcACCzGLaEP1GjXrp0KCwsl/ThgtlOnTqqurlZwcLCOHDni3YywXbt2NlYJAGhIBBUY6+wVZysqKs67SzIr0wJA4OI3PIxV112R2T0ZAAIXQQXG6t27d732AwD4H4IKjHXw4MF67QcA8D8EFRhr48aN9doPAOB/CCowVmVlZb32AwD4H4IKjOXxeOq1HwDA/xBUAACAsQgqAADAWAQVAABgLIIKAAAwFkEFAAAYi6ACAACMRVCBsVq3bl2v/QAA/oegAmOdOXOmXvsBAPwPQQXGqqqqqtd+AAD/Q1ABAADGIqgAAABjEVQAAICxmtldAADY6fDhwyorK7O7jCavsLDQ51/YKzQ0VOHh4XaXIYmgAqAJO3z4sCb97i6drmZAtinS09PtLgGSmge7tOKVl40IKwQVAE1WWVmZTldX6V9xo+RpEWp3OYARgk6VSd9sUFlZGUEFAEzgaREqT+sOdpcBoBYMpoWxgoLq9r9nXfsBAPwPv+FhLJfLVa/9AAD+x9agkpGRoWHDhqlt27bq1KmTxo8fr71799pZEgzCXj8AAFuDyoYNG5ScnKxNmzbpo48+0unTp3XjjTfqxIkTdpYFQ7DXDwDA1sG077//vs/j5cuXq1OnTtq2bZsSExNtqgqmsCyrXvsBAPyPUbN+ahZdCgsLq/V8VVWVzwZ05eXljVIX7FHXRbhYrAsAApcxg2k9Ho9mzZqlESNGqF+/frX2ycjIUGhoqPeIjo5u5CoBAEBjMiaoJCcna+fOnVq5cuV5+8ydO1dlZWXe48CBA41YIQAAaGxG3Pq5//779c477ygnJ0ddunQ5bz+Xy8VUVAAAmhBbg4plWZoxY4bWrFmj9evXKzY21s5yAACAYWwNKsnJyXr11Ve1du1atW3bViUlJZJ+3LWxZcuWdpYGAAAMYOsYlaysLJWVlWn06NGKjIz0HqtWrbKzLAAAYAjbb/0AAACcjzGzfgAAAH6KoAIAAIxFUAEAAMYiqAAAAGMRVAAAgLEIKgAAwFgEFQAAYCyCCgAAMBZBBQAAGIugAgAAjEVQAQAAxiKoAAAAYxFUAACAsQgqAADAWAQVAABgLIIKAAAwFkEFAAAYi6ACAACMRVABAADGamZ3AQBgt6B/Hbe7BMAYpr0fCCoAmryWBTl2lwDgPAgqAJq8f8UmytOynd1lAEYI+tdxo8I7QQVAk+dp2U6e1h3sLgNALRhMCwAAjEVQAQAAxiKoAAAAYxFUAACAsQgqAADAWAQVAABgLIIKAAAwFkEFAAAYiwXfmohTp06pqKjI7jIazL59++wu4aLFxMSoRYsWdpcBAEYjqDQRRUVFuu++++wuo8H448+2dOlS9ezZ0+4yAMBotgaVnJwcLViwQNu2bVNxcbHWrFmj8ePH21lSwIqJidHSpUvtLuOiXEz48LefTfrxvwkA4OfZGlROnDihAQMGaOrUqbr99tvtLCXgtWjRwu/+el+8eLFmzpxZp37+9rMBAOrG1qAyduxYjR071s4SYLD4+Ph67QcA8D9+NeunqqpK5eXlPgcC2/r16y/rPADAv/lVUMnIyFBoaKj3iI6OtrskNIL169dr8eLFPm2LFy8mpABAE+BXQWXu3LkqKyvzHgcOHLC7JDSS+Ph474DZpUuXcrsHAJoIv5qe7HK55HK57C4DAAA0Er+6ogIAAJoWW6+oVFZW6uuvv/Y+Ligo0I4dOxQWFsYaEwAAwN6g8tlnn2nMmDHex7Nnz5YkTZ48WcuXL7epKgAAYApbg8ro0aNlWZadJQAAAIMxRgUAABiLoAIAAIxFUAEAAMbyq3VUAKAhBJ0qs7sEwBimvR8IKgCarNDQUDUPdknfbLC7FMAozYNdCg0NtbsMSQQVAE1YeHi4VrzyssrKzPoLsikqLCxUenq65s2bp65du9pdTpMXGhqq8PBwu8uQRFAB0MSFh4cb8wsZUteuXdWzZ0+7y4BBGEwLAACMxRWVOjh8+DCXhg1QWFjo8y/sZdKlYQCBi6ByAYcPH9ak392l09VVdpeC/5eenm53CdCPg+1WvPIyYQVAgyKoXEBZWZlOV1fpX3Gj5GlhxghowG5Bp8qkbzaorKyMoAKgQRFU6sjTIlSe1h3sLgMAgCaFwbQAAMBYBBUAAGAsggoAADAWQQUAABiLwbR1FPSv43aXABiD9wOAxkJQqaOWBTl2lwAAQJNDUKmjf8UmytOynd1lAEYI+tdxwjuARkFQqSNPy3asowIAQCNjMC0AADAWQQUAABiLWz91FHSK3ZOBGrwfADQWgsoFhIaGqnmwS/pmg92lAEZpHuxSaCgbdQJoWASVCwgPD9eKV15WWRl/QdqtsLBQ6enpmjdvnrp27Wp3OU1eaGgoOycb4tSpUyoqKrK7jMtSWFjo86+/i4mJUYsWLewuIyAQVOogPDycX8gG6dq1q3r27Gl3GYAxioqKdN9999ldRr1IT0+3u4R6sXTpUn5P1ROCCgD4uZiYGC1dutTuMnCWmJgYu0sIGAQVAPBzLVq04K93BCymJwMAAGMRVAAAgLEIKgAAwFgEFQAAYCyCCgAAMJbts34yMzO1YMEClZSUaMCAAXrmmWd01VVX2V1WwGFBKPOwIBQAXJjDsizLrm++atUq3XXXXXruuec0fPhwLVq0SKtXr9bevXvVqVOnCz6/vLxcoaGhKisrU0hISCNU7L/27dsXMAtCBQoWhALQVF3M57etQWX48OEaNmyYnn32WUmSx+NRdHS0ZsyYoTlz5lzw+QSVuguEKyqBhisqAJqqi/n8tu3WT3V1tbZt26a5c+d624KCgnT99dcrNze31udUVVWpqqrK+7i8vLzB6wwULAgFAPBHtg2mPXr0qNxu9zl76ISHh6ukpKTW52RkZCg0NNR7REdHN0apAADAJn4162fu3LkqKyvzHgcOHLC7JAAA0IBsu/XToUMHOZ1OHT582Kf98OHDioiIqPU5LpdLLperMcoDAAAGsO2KSnBwsIYMGaJ169Z52zwej9atW6eEhAS7ygIAAAaxdR2V2bNna/LkyRo6dKiuuuoqLVq0SCdOnNDdd99tZ1kAAMAQtgaVO+64Q99//70eeeQRlZSUaODAgXr//ffPGWALAACaJlvXUblcrKMCAID/uZjPb7+a9QMAAJoWggoAADAWQQUAABiLoAIAAIxFUAEAAMYiqAAAAGPZuo7K5aqZWc0uygAA+I+az+26rJDi10GloqJCkthFGQAAP1RRUaHQ0NCf7ePXC755PB4dOnRIbdu2lcPhsLscNLDy8nJFR0frwIEDLPAHBBje302LZVmqqKhQVFSUgoJ+fhSKX19RCQoKUpcuXewuA40sJCSEX2RAgOL93XRc6EpKDQbTAgAAYxFUAACAsQgq8Bsul0upqalyuVx2lwKgnvH+xvn49WBaAAAQ2LiiAgAAjEVQAQAAxiKoAAAAYxFU4DcyMzPVrVs3tWjRQsOHD9eWLVvsLgnAZcrJydG4ceMUFRUlh8OhN9980+6SYBiCCvzCqlWrNHv2bKWmpurzzz/XgAEDdNNNN+nIkSN2lwbgMpw4cUIDBgxQZmam3aXAUMz6gV8YPny4hg0bpmeffVbSj9snREdHa8aMGZozZ47N1QGoDw6HQ2vWrNH48ePtLgUG4YoKjFddXa1t27bp+uuv97YFBQXp+uuvV25uro2VAQAaGkEFxjt69KjcbrfCw8N92sPDw1VSUmJTVQCAxkBQAQAAxiKowHgdOnSQ0+nU4cOHfdoPHz6siIgIm6oCADQGggqMFxwcrCFDhmjdunXeNo/Ho3Xr1ikhIcHGygAADa2Z3QUAdTF79mxNnjxZQ4cO1VVXXaVFixbpxIkTuvvuu+0uDcBlqKys1Ndff+19XFBQoB07digsLEwxMTE2VgZTMD0ZfuPZZ5/VggULVFJSooEDB2rx4sUaPny43WUBuAzr16/XmDFjzmmfPHmyli9f3vgFwTgEFQAAYCzGqAAAAGMRVAAAgLEIKgAAwFgEFQAAYCyCCgAAMBZBBQAAGIugAgAAjEVQAQAAxiKoAPAbJSUluuGGG9S6dWu1a9fO7nIANAKCCoAGM3r0aM2aNaveXu8vf/mLiouLtWPHDu3bt6/eXrc269evl8Ph0PHjxxv0+wD4eWxKCMB41dXVCg4OVn5+voYMGaIePXqct+/p06fVvHnzRqwOQEPiigoAr3feeUft2rWT2+2WJO3YsUMOh0Nz5szx9rn33ns1adIk/fDDD5o4caI6d+6sVq1aqX///nrttde8/aZMmaINGzbo6aeflsPhkMPh0LfffitJ2rlzp8aOHas2bdooPDxcv/vd73T06FHvc0ePHq37779fs2bNUocOHXTTTTepW7duev311/Xyyy/L4XBoypQpkiSHw6GsrCz9+te/VuvWrZWeni5JysrKUvfu3RUcHKwrr7xSr7zyis/P6nA49Ne//lW/+c1v1KpVK/Xo0UNvvfWWJOnbb7/1bpTXvn17n+8HoJFZAPD/jh8/bgUFBVlbt261LMuyFi1aZHXo0MEaPny4t88VV1xhvfDCC9Z3331nLViwwNq+fbuVn59vLV682HI6ndbmzZu9r5WQkGD9/ve/t4qLi63i4mLrzJkz1rFjx6yOHTtac+fOtXbv3m19/vnn1g033GCNGTPG+z1GjRpltWnTxvrTn/5k7dmzx9qzZ4915MgR61e/+pX129/+1iouLraOHz9uWZZlSbI6depk/e1vf7Py8/OtwsJC64033rCaN29uZWZmWnv37rWeeuopy+l0Wh9//LH3e0iyunTpYr366qvW/v37rZkzZ1pt2rSxfvjhB+vMmTPW66+/bkmy9u7d6/P9ADQuggoAH4MHD7YWLFhgWZZljR8/3kpPT7eCg4OtiooK67vvvrMkWfv27av1ubfccov1X//1X97Ho0aNsh544AGfPo899ph14403+rQdOHDAGwpqnjdo0KBzXv+2226zJk+e7NMmyZo1a5ZP2y9/+Uvr97//vU/bhAkTrJtvvtnneSkpKd7HlZWVliTrvffesyzLsj755BNLknXs2LFaf1YAjYNbPwB8jBo1SuvXr5dlWfrHP/6h22+/Xb1799Y///lPbdiwQVFRUerRo4fcbrcee+wx9e/fX2FhYWrTpo0++OADFRUV/ezrf/HFF/rkk0/Upk0b79GrVy9JUn5+vrffkCFD6lzz0KFDfR7v3r1bI0aM8GkbMWKEdu/e7dMWHx/v/bp169YKCQnRkSNH6vx9ATQ8BtMC8DF69Gj97W9/0xdffKHmzZurV69eGj16tNavX69jx45p1KhRkqQFCxbo6aef1qJFi9S/f3+1bt1as2bNUnV19c++fmVlpcaNG6cnnnjinHORkZHer1u3bl3nmi+m79l+OujW4XDI4/Fc0msBaBhcUQHgY+TIkaqoqNBf/vIXbyipCSrr16/X6NGjJUkbN27UbbfdpkmTJmnAgAGKi4s7Z8pwcHCwd2BujcGDB2vXrl3q1q2brrjiCp/jUgPHT/Xu3VsbN270adu4caP69OlT59cIDg6WpHPqB9C4CCoAfLRv317x8fHKzs72hpLExER9/vnn2rdvnze89OjRQx999JE+/fRT7d69W3/4wx90+PBhn9fq1q2bNm/erG+//VZHjx6Vx+NRcnKySktLNXHiRG3dulX5+fn64IMPdPfdd9dbKPjTn/6k5cuXKysrS/v379fChQv1xhtv6KGHHqrza3Tt2lUOh0PvvPOOvv/+e1VWVtZLbQAuDkEFwDlGjRolt9vtDSphYWHq06ePIiIidOWVV0qSUlJSNHjwYN10000aPXq0IiIiNH78eJ/Xeeihh+R0OtWnTx917NhRRUVFioqK0saNG+V2u3XjjTeqf//+mjVrltq1a6egoPr5lTR+/Hg9/fTTevLJJ9W3b189//zzevHFF70/T1107txZaWlpmjNnjsLDw3X//ffXS20ALo7DsizL7iIAAABqwxUVAABgLIIKAAAwFkEFAAAYi6ACAACMRVABAADGIqgAAABjEVQAAICxCCoAAMBYBBUAAGAsggoAADAWQQUAABiLoAIAAIz1fybta6vjIMcaAAAAAElFTkSuQmCC"
          },
          "metadata": {}
        }
      ],
      "execution_count": 29
    },
    {
      "cell_type": "markdown",
      "source": "### Question 5\n\nUse the function <code>regplot</code>  in the seaborn library  to  determine if the feature <code>sqft_above</code> is negatively or positively correlated with price. Take a screenshot of your code and scatterplot. You will need to submit the screenshot for the final project. \n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\nsns.regplot(x=\"sqft_above\", y=\"price\", data=df)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 31,
          "output_type": "execute_result",
          "data": {
            "text/plain": "<AxesSubplot:xlabel='sqft_above', ylabel='price'>"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 640x480 with 1 Axes>",
            "image/png": "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vUm++93vrvjaH//xH8vrrrtOSkmvRTNblkc/lmXhmWeewVVXXVX6GuccV111FR577LE6XtnykUqlAABtbW0AgJdeegmDg4MVz3kymcRFF11Ues6feeYZ2LZdcZszzzwTa9asKd3mscceQ0tLC84///zSba666ipwzvHEE08s+u/VTG6++Wa86U1vqng+AXotltKPf/xjnH/++Xjb296Grq4unHfeebjrrrtK36fXYulccsklePjhh7F3714AwHPPPYdHH30U11xzDQB6LZpZU8/6mc7IyAhc18WKFSsqvr5ixQq8+OKLdbqq5UMIgQ9/+MO49NJLsXnzZgDA4OAgAFR9zoPvDQ4OQtd1tLS0zHibrq6uiu+rqoq2trbSbQhw33334Xe/+x2eeuqpKd+j12LpHDx4ENu2bcMtt9yC2267DU899RQ++MEPQtd1XH/99fRaLKGPfexjSKfTOPPMM6EoClzXxWc/+1lcd911AOjfRTNbloEKWVw333wzdu7ciUcffbTel3JSOnz4MD70oQ/hF7/4BUKhUL0v56QmhMD555+Pz33ucwCA8847Dzt37sQ///M/4/rrr6/z1Z1c7r//fnz3u9/F9773PWzatAnPPvssPvzhD6Onp4deiya3LI9+Ojo6oCjKlEztY8eOobu7u05XtTy8//3vx09+8hP8+te/rphcHTyvMz3n3d3dsCwL4+PjM95maGio4vuO42B0dJReO98zzzyDoaEhvOpVr4KqqlBVFdu3b8f/+T//B6qqlj4x0mux+FauXImzzjqr4msbN27EoUP/f3v3H1NV/cdx/HkFofRCl2wDVOCKaYLeOZByVzdbwhTc2A23FGQE9oebVqPSnFv1R7/M2dAa85/akj/C5Wqgqy2LLlnJkl9xqfQKDkeXP66uwpuQrYz7+f7ROuuG3y/1FS8X93ps549zPu/7OZ9zPgNenHPPvQFAPxfR9PTTT7Nnzx7Ky8txuVxUVVXx5JNP8sorrwCai+nslgwqCQkJrFixAq/Xa20Lh8N4vV7cbvcUjmz6Msbw2GOP0dzcTGtrKwsWLIhoX7BgAWlpaRHn/MqVK7S3t1vnfMWKFcycOTOipq+vj0AgYNW43W5CoRDd3d1WTWtrK+FwmJUrV97MQ5w2CgsL+eabb/D5fNZSUFBAZWUlPp+P7OxszUWUrF69etxj+v39/WRlZQH6uYimq1evMmNG5J+0uLg4wuEwoLmY1qb63bw3yzvvvGMSExNNQ0ODOXv2rNm2bZtxOBzm4sWLUz20aWn79u3mjjvuMCdPnjTBYNBarl69atXs27fPOBwOc/z4cfP1118bj8dz3Uf/MjMzTWtrq+nq6jJut9u43e6IfRUXF5u8vDzT3t5uTp06ZRYtWqRH/ybw16d+jNFcREtHR4eJj483L7/8sjl//rxpbGw0s2bNMm+//bZVo7mIjurqajNv3jzr8eSmpiZz1113md27d1s1movp6ZYNKsYYU19fbzIzM01CQoK57777zOnTp6d6SNMWcN3l8OHDVk04HDbPPfecSU1NNYmJiaawsND09fVF9PPLL7+YHTt2mJSUFDNr1ixTVlZmgsFgRM2PP/5oKioqjN1uN8nJyWbr1q1mZGQkGoc5bf09qGguouf99983y5YtM4mJiWbJkiXmjTfeiGjXXETHlStXTG1trcnMzDS33Xabyc7ONs8884z59ddfrRrNxfSkb08WERGRmHVLvkdFREREbg0KKiIiIhKzFFREREQkZimoiIiISMxSUBEREZGYpaAiIiIiMUtBRURERGKWgoqIiIjELAUVEZkUxhi2bdvGnXfeic1mw+fz3ZT9OJ1OXnvttZvSt4jEHgUVEZkUJ06coKGhgQ8++IBgMMiyZcuw2WwcO3ZsqocmItNY/FQPQERuDQMDA6Snp7Nq1aqpHoqI3EJ0RUVELO+99x4ul4vbb7+dOXPmUFRUxM8//8zY2BhPPfUUDoeDOXPmsHv3bqqrq3nwwQcBqKmp4fHHHycQCGCz2XA6nTidTgDKysqsbRMZGBjA4/GQmpqK3W7n3nvv5ZNPPhlXNzIyQkVFBbNnz2bevHkcOnQooj0QCODxeLDb7SQnJ7Np0yYuXboEQH9/PzabjXPnzkW85uDBgyxcuNBa//bbbykpKcFut5OamkpVVRU//PDDvzibIjIZFFREBIBgMEhFRQWPPPIIfr+fkydPsnHjRowx1NXV0dDQwFtvvcWpU6cYHh6mubnZeu3rr7/OCy+8wPz58wkGg3R2dtLZ2QnA4cOHrW0TGR0dZcOGDXi9Xnp6eiguLqa0tJRAIBBR9+qrr7J8+XJ6enrYs2cPtbW1tLS0ABAOh/F4PAwPD/PZZ5/R0tLChQsX2Lx5MwCLFy+moKCAxsbGiD4bGxvZsmULAKFQiLVr15KXl0dXVxcnTpzg0qVLbNq06f8/wSLy/5naL28WkVjR3d1tADM4ODiuLT093ezfv99av3btmpk/f77xeDzWtoMHD5qsrKyI1wGmubn5hsa1dOlSU19fb61nZWWZ4uLiiJrNmzebkpISY4wxH3/8sYmLizOBQMBqP3PmjAFMR0eHNdaFCxda7X19fQYwfr/fGGPMiy++aNatWxexj6GhIQOYvr6+GzoeEfl3dEVFRABYvnw5hYWFuFwuHnroId58800uX77MTz/9RDAYZOXKlVZtfHw8BQUFkz6G0dFRdu3aRU5ODg6HA7vdjt/vH3dFxe12j1v3+/0A+P1+MjIyyMjIsNpzc3NxOBxWTXl5OYODg5w+fRr442pKfn4+S5YsAaC3t5dPP/0Uu91uLX+2DQwMTPpxi8h/p6AiIgDExcXR0tLChx9+SG5uLvX19dxzzz0MDg5GbQy7du2iubmZvXv38sUXX+Dz+XC5XPz222+Tup+0tDTWrl3LkSNHADhy5AiVlZVW++joKKWlpfh8vojl/PnzrFmzZlLHIiL/m4KKiFhsNhurV6/m+eefp6enh4SEBLxeL+np6bS3t1t1v//+O93d3RP2N3PmTMbGxv7x/tva2qipqaGsrAyXy0VaWtp1g9KfV0L+up6TkwNATk4OQ0NDDA0NWe1nz54lFAqRm5trbausrOTo0aN8+eWXXLhwgfLycqstPz+fM2fO4HQ6ufvuuyOW2bNn/+PjEZEbp6AiIgC0t7ezd+9eurq6CAQCNDU18f3335OTk0NtbS379u3j2LFjnDt3jh07dhAKhSbs0+l04vV6uXjxIpcvX56wftGiRTQ1NeHz+ejt7WXLli2Ew+FxdW1tbezfv5/+/n4OHTrEu+++S21tLQBFRUW4XC4qKyv56quv6Ojo4OGHH+b++++PuF21ceNGRkZG2L59Ow888ABz58612h599FGGh4epqKigs7OTgYEBPvroI7Zu3fqvgpeI3DgFFREBIDk5mc8//5wNGzawePFinn32Werq6igpKWHnzp1UVVVRXV2N2+0mKSmJsrKyCfusq6ujpaWFjIwM8vLyJqw/cOAAKSkprFq1itLSUtavX09+fv64up07d9LV1UVeXh4vvfQSBw4cYP369cAfV4WOHz9OSkoKa9asoaioiOzsbI4ePRrRR1JSEqWlpfT29kbc9gGYO3cubW1tjI2NsW7dOlwuF0888QQOh4MZM/RrUySabMYYM9WDEJHpp6amhlAopE+eFZGbSv8aiIiISMxSUBGRqFm6dGnEI79/Xf7+AWwiIqBbPyISRd999x3Xrl27bltqaipJSUlRHpGIxDoFFREREYlZuvUjIiIiMUtBRURERGKWgoqIiIjELAUVERERiVkKKiIiIhKzFFREREQkZimoiIiISMxSUBEREZGY9R8BPWTaYumAXQAAAABJRU5ErkJggg=="
          },
          "metadata": {}
        }
      ],
      "execution_count": 31
    },
    {
      "cell_type": "markdown",
      "source": "We can use the Pandas method <code>corr()</code>  to find the feature other than price that is most correlated with price.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# df.corr()['price'].sort_values()",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 33
    },
    {
      "cell_type": "markdown",
      "source": "# Module 4: Model Development\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "We can Fit a linear regression model using the  longitude feature <code>'long'</code> and  caculate the R^2.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "X = df[['long']]\nY = df['price']\nlm = LinearRegression()\nlm.fit(X,Y)\nlm.score(X, Y)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 34,
          "output_type": "execute_result",
          "data": {
            "text/plain": "0.00046769430149007363"
          },
          "metadata": {}
        }
      ],
      "execution_count": 34
    },
    {
      "cell_type": "markdown",
      "source": "### Question  6\n\nFit a linear regression model to predict the <code>'price'</code> using the feature <code>'sqft_living'</code> then calculate the R^2. Take a screenshot of your code and the value of the R^2. You will need to submit it for the final project.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\nX = df[['sqft_living']]\nY = df['price']\nlm = LinearRegression()\nlm.fit(X,Y)\nlm.score(X, Y)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 35,
          "output_type": "execute_result",
          "data": {
            "text/plain": "0.4928532179037931"
          },
          "metadata": {}
        }
      ],
      "execution_count": 35
    },
    {
      "cell_type": "markdown",
      "source": "### Question 7\n\nFit a linear regression model to predict the <code>'price'</code> using the list of features:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "features =[\"floors\", \"waterfront\",\"lat\" ,\"bedrooms\" ,\"sqft_basement\" ,\"view\" ,\"bathrooms\",\"sqft_living15\",\"sqft_above\",\"grade\",\"sqft_living\"]     ",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": "Then calculate the R^2. Take a screenshot of your code and the value of the R^2. You will need to submit it for the final project.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\nZ = df[[\"floors\", \"waterfront\",\"lat\" ,\"bedrooms\" ,\"sqft_basement\" ,\"view\" ,\"bathrooms\",\"sqft_living15\",\"sqft_above\",\"grade\",\"sqft_living\"]]\nlm.fit(Z,Y)\nlm.score(Z, Y)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 37,
          "output_type": "execute_result",
          "data": {
            "text/plain": "0.6576890354915759"
          },
          "metadata": {}
        }
      ],
      "execution_count": 37
    },
    {
      "cell_type": "markdown",
      "source": "### This will help with Question 8\n\nCreate a list of tuples, the first element in the tuple contains the name of the estimator:\n\n<code>'scale'</code>\n\n<code>'polynomial'</code>\n\n<code>'model'</code>\n\nThe second element in the tuple  contains the model constructor\n\n<code>StandardScaler()</code>\n\n<code>PolynomialFeatures(include_bias=False)</code>\n\n<code>LinearRegression()</code>\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": "### Question 8\n\nUse the list to create a pipeline object to predict the 'price', fit the object using the features in the list <code>features</code>, and calculate the R^2. Take a screenshot of your code and the value of the R^2. You will need to submit it for the final project.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\nfrom sklearn.metrics import mean_squared_error, r2_score\nInput=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]\npipe=Pipeline(Input)\nZ = Z.astype(float)\npipe.fit(Z,Y)\nypipe=pipe.predict(Z)\nprint(r2_score(Y,ypipe))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0.7512051345272872\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 39
    },
    {
      "cell_type": "markdown",
      "source": "# Module 5: Model Evaluation and Refinement\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Import the necessary modules:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "from sklearn.model_selection import cross_val_score\nfrom sklearn.model_selection import train_test_split\nprint(\"done\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "done\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 40
    },
    {
      "cell_type": "markdown",
      "source": "We will split the data into training and testing sets:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "features =[\"floors\", \"waterfront\",\"lat\" ,\"bedrooms\" ,\"sqft_basement\" ,\"view\" ,\"bathrooms\",\"sqft_living15\",\"sqft_above\",\"grade\",\"sqft_living\"]    \nX = df[features]\nY = df['price']\n\nx_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)\n\n\nprint(\"number of test samples:\", x_test.shape[0])\nprint(\"number of training samples:\",x_train.shape[0])",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "number of test samples: 3242\nnumber of training samples: 18371\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 41
    },
    {
      "cell_type": "markdown",
      "source": "### Question 9\n\nCreate and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data. Take a screenshot of your code and the value of the R^2. You will need to submit it for the final project.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "from sklearn.linear_model import Ridge",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 43
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\nRidgeModel=Ridge(alpha=0.1)\nRidgeModel.fit(x_train, y_train)\nyhat = RidgeModel.predict(x_test)\nprint(r2_score(y_test,yhat))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0.647875916393907\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 44
    },
    {
      "cell_type": "markdown",
      "source": "### Question 10\n\nPerform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided. Take a screenshot of your code and the R^2. You will need to submit it for the final project.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\npr = PolynomialFeatures(degree=2)\nx_train_pr = pr.fit_transform(x_train)\nx_test_pr = pr.fit_transform(x_test)\nRidgeModel.fit(x_train_pr, y_train)\ny_hat = RidgeModel.predict(x_test_pr)\nprint(r2_score(y_test,y_hat))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0.7002744263583341\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 45
    },
    {
      "cell_type": "markdown",
      "source": "<p>Once you complete your notebook you will have to share it. You can download the notebook by navigating to \"File\" and clicking on \"Download\" button.\n        <p><img width=\"600\" src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Module%206/images/DA0101EN_FA_Image21.png\" alt=\"share notebook\" style=\"display: block; margin-left: auto; margin-right: auto;\"></p>\n        <p></p>\n<p>This will save the (.ipynb) file on your computer. Once saved, you can upload this file in the \"My Submission\" tab, of the \"Peer-graded Assignment\" section.  \n          \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>About the Authors:</h2> \n\n<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Other contributors: <a href=\"https://www.linkedin.com/in/michelleccarey/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01\">Michelle Carey</a>, <a href=\"https://www.linkedin.com/in/jiahui-mavis-zhou-a4537814a?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01\">Mavis Zhou</a>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "\n## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n<!--## Change Log\n\n| Date (YYYY-MM-DD) | Version | Changed By      | Change Description                           |\n| ----------------- | ------- | --------------- | -------------------------------------------- |\n| 2020-12-01        | 2.2     | Aije Egwaikhide | Coverted Data describtion from text to table |\n| 2020-10-06        | 2.1     | Lakshmi Holla   | Changed markdown instruction of Question1    |\n| 2020-08-27        | 2.0     | Malika Singla   | Added lab to GitLab                          |\n| 2022-06-13        | 2.3     | Svitlana Kramar | Updated Notebook sharing instructions        |\n| <hr>              |         |                 |                                              |\n\n\n--!>\n<p>\n",
      "metadata": {}
    }
  ]
}