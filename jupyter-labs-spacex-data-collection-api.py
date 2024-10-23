{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\">\n",
    "    </a>\n",
    "</p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **SpaceX  Falcon 9 first stage Landing Prediction**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Lab 1: Collecting the data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Estimated time needed: **45** minutes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this capstone, we will predict if the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch. In this lab, you will collect and make sure the data is in the correct format from an API. The following is an example of a successful and launch.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Several examples of an unsuccessful landing are shown here:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/crash.gif)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most unsuccessful landings are planned. Space X performs a controlled landing in the oceans. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objectives\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this lab, you will make a get request to the SpaceX API. You will also do some basic data wrangling and formating. \n",
    "\n",
    "- Request to the SpaceX API\n",
    "- Clean the requested data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "----\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import Libraries and Define Auxiliary Functions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will import the following libraries into the lab\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Requests allows us to make HTTP requests which we will use to get data from an API\n",
    "import requests\n",
    "# Pandas is a software library written for the Python programming language for data manipulation and analysis.\n",
    "import pandas as pd\n",
    "# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays\n",
    "import numpy as np\n",
    "# Datetime is a library that allows us to represent dates\n",
    "import datetime\n",
    "\n",
    "# Setting this option will print all collumns of a dataframe\n",
    "pd.set_option('display.max_columns', None)\n",
    "# Setting this option will print all of the data in a feature\n",
    "pd.set_option('display.max_colwidth', None)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Below we will define a series of helper functions that will help us use the API to extract information using identification numbers in the launch data.\n",
    "\n",
    "From the <code>rocket</code> column we would like to learn the booster name.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Takes the dataset and uses the rocket column to call the API and append the data to the list\n",
    "def getBoosterVersion(data):\n",
    "    for x in data['rocket']:\n",
    "       if x:\n",
    "        response = requests.get(\"https://api.spacexdata.com/v4/rockets/\"+str(x)).json()\n",
    "        BoosterVersion.append(response['name'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the <code>launchpad</code> we would like to know the name of the launch site being used, the logitude, and the latitude.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Takes the dataset and uses the launchpad column to call the API and append the data to the list\n",
    "def getLaunchSite(data):\n",
    "    for x in data['launchpad']:\n",
    "       if x:\n",
    "         response = requests.get(\"https://api.spacexdata.com/v4/launchpads/\"+str(x)).json()\n",
    "         Longitude.append(response['longitude'])\n",
    "         Latitude.append(response['latitude'])\n",
    "         LaunchSite.append(response['name'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the <code>payload</code> we would like to learn the mass of the payload and the orbit that it is going to.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Takes the dataset and uses the payloads column to call the API and append the data to the lists\n",
    "def getPayloadData(data):\n",
    "    for load in data['payloads']:\n",
    "       if load:\n",
    "        response = requests.get(\"https://api.spacexdata.com/v4/payloads/\"+load).json()\n",
    "        PayloadMass.append(response['mass_kg'])\n",
    "        Orbit.append(response['orbit'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From <code>cores</code> we would like to learn the outcome of the landing, the type of the landing, number of flights with that core, whether gridfins were used, wheter the core is reused, wheter legs were used, the landing pad used, the block of the core which is a number used to seperate version of cores, the number of times this specific core has been reused, and the serial of the core.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Takes the dataset and uses the cores column to call the API and append the data to the lists\n",
    "def getCoreData(data):\n",
    "    for core in data['cores']:\n",
    "            if core['core'] != None:\n",
    "                response = requests.get(\"https://api.spacexdata.com/v4/cores/\"+core['core']).json()\n",
    "                Block.append(response['block'])\n",
    "                ReusedCount.append(response['reuse_count'])\n",
    "                Serial.append(response['serial'])\n",
    "            else:\n",
    "                Block.append(None)\n",
    "                ReusedCount.append(None)\n",
    "                Serial.append(None)\n",
    "            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))\n",
    "            Flights.append(core['flight'])\n",
    "            GridFins.append(core['gridfins'])\n",
    "            Reused.append(core['reused'])\n",
    "            Legs.append(core['legs'])\n",
    "            LandingPad.append(core['landpad'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's start requesting rocket launch data from SpaceX API with the following URL:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "spacex_url=\"https://api.spacexdata.com/v4/launches/past\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "response = requests.get(spacex_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Check the content of the response\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# print(response.content)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You should see the response contains massive information about SpaceX launches. Next, let's try to discover some more relevant information for this project.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 1: Request and parse the SpaceX launch data using the GET request\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To make the requested JSON results more consistent, we will use the following static response object for this project:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We should see that the request was successfull with the 200 status response code\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'response' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_494/160151258.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus_code\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'response' is not defined"
     ]
    }
   ],
   "source": [
    "response.status_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response = requests.get(static_json_url)\n",
    "response.status_code"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we decode the response content as a Json using <code>.json()</code> and turn it into a Pandas dataframe using <code>.json_normalize()</code>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Use json_normalize meethod to convert the json result into a dataframe\n",
    "data_mass = response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = pd.json_normalize(data_mass)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the dataframe <code>data</code> print the first 5 rows\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>static_fire_date_utc</th>\n",
       "      <th>static_fire_date_unix</th>\n",
       "      <th>tbd</th>\n",
       "      <th>net</th>\n",
       "      <th>window</th>\n",
       "      <th>rocket</th>\n",
       "      <th>success</th>\n",
       "      <th>details</th>\n",
       "      <th>crew</th>\n",
       "      <th>ships</th>\n",
       "      <th>capsules</th>\n",
       "      <th>payloads</th>\n",
       "      <th>launchpad</th>\n",
       "      <th>auto_update</th>\n",
       "      <th>failures</th>\n",
       "      <th>flight_number</th>\n",
       "      <th>name</th>\n",
       "      <th>date_utc</th>\n",
       "      <th>date_unix</th>\n",
       "      <th>date_local</th>\n",
       "      <th>date_precision</th>\n",
       "      <th>upcoming</th>\n",
       "      <th>cores</th>\n",
       "      <th>id</th>\n",
       "      <th>fairings.reused</th>\n",
       "      <th>fairings.recovery_attempt</th>\n",
       "      <th>fairings.recovered</th>\n",
       "      <th>fairings.ships</th>\n",
       "      <th>links.patch.small</th>\n",
       "      <th>links.patch.large</th>\n",
       "      <th>links.reddit.campaign</th>\n",
       "      <th>links.reddit.launch</th>\n",
       "      <th>links.reddit.media</th>\n",
       "      <th>links.reddit.recovery</th>\n",
       "      <th>links.flickr.small</th>\n",
       "      <th>links.flickr.original</th>\n",
       "      <th>links.presskit</th>\n",
       "      <th>links.webcast</th>\n",
       "      <th>links.youtube_id</th>\n",
       "      <th>links.article</th>\n",
       "      <th>links.wikipedia</th>\n",
       "      <th>fairings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2006-03-17T00:00:00.000Z</td>\n",
       "      <td>1.142554e+09</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>False</td>\n",
       "      <td>Engine failure at 33 seconds and loss of vehicle</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[5eb0e4b5b6c3bb0006eeb1e1]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>True</td>\n",
       "      <td>[{'time': 33, 'altitude': None, 'reason': 'merlin engine failure'}]</td>\n",
       "      <td>1</td>\n",
       "      <td>FalconSat</td>\n",
       "      <td>2006-03-24T22:30:00.000Z</td>\n",
       "      <td>1143239400</td>\n",
       "      <td>2006-03-25T10:30:00+12:00</td>\n",
       "      <td>hour</td>\n",
       "      <td>False</td>\n",
       "      <td>[{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>5eb87cd9ffd86e000604b32a</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>[]</td>\n",
       "      <td>https://images2.imgbox.com/3c/0e/T8iJcSN3_o.png</td>\n",
       "      <td>https://images2.imgbox.com/40/e3/GypSkayF_o.png</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>None</td>\n",
       "      <td>https://www.youtube.com/watch?v=0a_00nJ_Y88</td>\n",
       "      <td>0a_00nJ_Y88</td>\n",
       "      <td>https://www.space.com/2196-spacex-inaugural-falcon-1-rocket-lost-launch.html</td>\n",
       "      <td>https://en.wikipedia.org/wiki/DemoSat</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>None</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>False</td>\n",
       "      <td>Successful first stage burn and transition to second stage, maximum altitude 289 km, Premature engine shutdown at T+7 min 30 s, Failed to reach orbit, Failed to recover first stage</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[5eb0e4b6b6c3bb0006eeb1e2]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>True</td>\n",
       "      <td>[{'time': 301, 'altitude': 289, 'reason': 'harmonic oscillation leading to premature engine shutdown'}]</td>\n",
       "      <td>2</td>\n",
       "      <td>DemoSat</td>\n",
       "      <td>2007-03-21T01:10:00.000Z</td>\n",
       "      <td>1174439400</td>\n",
       "      <td>2007-03-21T13:10:00+12:00</td>\n",
       "      <td>hour</td>\n",
       "      <td>False</td>\n",
       "      <td>[{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>5eb87cdaffd86e000604b32b</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>[]</td>\n",
       "      <td>https://images2.imgbox.com/4f/e3/I0lkuJ2e_o.png</td>\n",
       "      <td>https://images2.imgbox.com/be/e7/iNqsqVYM_o.png</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>None</td>\n",
       "      <td>https://www.youtube.com/watch?v=Lk4zQ2wP-Nc</td>\n",
       "      <td>Lk4zQ2wP-Nc</td>\n",
       "      <td>https://www.space.com/3590-spacex-falcon-1-rocket-fails-reach-orbit.html</td>\n",
       "      <td>https://en.wikipedia.org/wiki/DemoSat</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>None</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>False</td>\n",
       "      <td>Residual stage 1 thrust led to collision between stage 1 and stage 2</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[5eb0e4b6b6c3bb0006eeb1e3, 5eb0e4b6b6c3bb0006eeb1e4]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>True</td>\n",
       "      <td>[{'time': 140, 'altitude': 35, 'reason': 'residual stage-1 thrust led to collision between stage 1 and stage 2'}]</td>\n",
       "      <td>3</td>\n",
       "      <td>Trailblazer</td>\n",
       "      <td>2008-08-03T03:34:00.000Z</td>\n",
       "      <td>1217734440</td>\n",
       "      <td>2008-08-03T15:34:00+12:00</td>\n",
       "      <td>hour</td>\n",
       "      <td>False</td>\n",
       "      <td>[{'core': '5e9e289ef3591814873b2625', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>5eb87cdbffd86e000604b32c</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>[]</td>\n",
       "      <td>https://images2.imgbox.com/3d/86/cnu0pan8_o.png</td>\n",
       "      <td>https://images2.imgbox.com/4b/bd/d8UxLh4q_o.png</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>None</td>\n",
       "      <td>https://www.youtube.com/watch?v=v0w9p3U8860</td>\n",
       "      <td>v0w9p3U8860</td>\n",
       "      <td>http://www.spacex.com/news/2013/02/11/falcon-1-flight-3-mission-summary</td>\n",
       "      <td>https://en.wikipedia.org/wiki/Trailblazer_(satellite)</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2008-09-20T00:00:00.000Z</td>\n",
       "      <td>1.221869e+09</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>True</td>\n",
       "      <td>Ratsat was carried to orbit on the first successful orbital launch of any privately funded and developed, liquid-propelled carrier rocket, the SpaceX Falcon 1</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[5eb0e4b7b6c3bb0006eeb1e5]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>True</td>\n",
       "      <td>[]</td>\n",
       "      <td>4</td>\n",
       "      <td>RatSat</td>\n",
       "      <td>2008-09-28T23:15:00.000Z</td>\n",
       "      <td>1222643700</td>\n",
       "      <td>2008-09-28T11:15:00+12:00</td>\n",
       "      <td>hour</td>\n",
       "      <td>False</td>\n",
       "      <td>[{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>5eb87cdbffd86e000604b32d</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>[]</td>\n",
       "      <td>https://images2.imgbox.com/e9/c9/T8CfiSYb_o.png</td>\n",
       "      <td>https://images2.imgbox.com/e0/a7/FNjvKlXW_o.png</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>None</td>\n",
       "      <td>https://www.youtube.com/watch?v=dLQ2tZEH6G0</td>\n",
       "      <td>dLQ2tZEH6G0</td>\n",
       "      <td>https://en.wikipedia.org/wiki/Ratsat</td>\n",
       "      <td>https://en.wikipedia.org/wiki/Ratsat</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>None</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>True</td>\n",
       "      <td>None</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>[5eb0e4b7b6c3bb0006eeb1e6]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>True</td>\n",
       "      <td>[]</td>\n",
       "      <td>5</td>\n",
       "      <td>RazakSat</td>\n",
       "      <td>2009-07-13T03:35:00.000Z</td>\n",
       "      <td>1247456100</td>\n",
       "      <td>2009-07-13T15:35:00+12:00</td>\n",
       "      <td>hour</td>\n",
       "      <td>False</td>\n",
       "      <td>[{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>5eb87cdcffd86e000604b32e</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>[]</td>\n",
       "      <td>https://images2.imgbox.com/a7/ba/NBZSw3Ho_o.png</td>\n",
       "      <td>https://images2.imgbox.com/8d/fc/0qdZMWWx_o.png</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>http://www.spacex.com/press/2012/12/19/spacexs-falcon-1-successfully-delivers-razaksat-satellite-orbit</td>\n",
       "      <td>https://www.youtube.com/watch?v=yTaIDooc8Og</td>\n",
       "      <td>yTaIDooc8Og</td>\n",
       "      <td>http://www.spacex.com/news/2013/02/12/falcon-1-flight-5</td>\n",
       "      <td>https://en.wikipedia.org/wiki/RazakSAT</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       static_fire_date_utc  static_fire_date_unix    tbd    net  window  \\\n",
       "0  2006-03-17T00:00:00.000Z           1.142554e+09  False  False     0.0   \n",
       "1                      None                    NaN  False  False     0.0   \n",
       "2                      None                    NaN  False  False     0.0   \n",
       "3  2008-09-20T00:00:00.000Z           1.221869e+09  False  False     0.0   \n",
       "4                      None                    NaN  False  False     0.0   \n",
       "\n",
       "                     rocket  success  \\\n",
       "0  5e9d0d95eda69955f709d1eb    False   \n",
       "1  5e9d0d95eda69955f709d1eb    False   \n",
       "2  5e9d0d95eda69955f709d1eb    False   \n",
       "3  5e9d0d95eda69955f709d1eb     True   \n",
       "4  5e9d0d95eda69955f709d1eb     True   \n",
       "\n",
       "                                                                                                                                                                                details  \\\n",
       "0                                                                                                                                      Engine failure at 33 seconds and loss of vehicle   \n",
       "1  Successful first stage burn and transition to second stage, maximum altitude 289 km, Premature engine shutdown at T+7 min 30 s, Failed to reach orbit, Failed to recover first stage   \n",
       "2                                                                                                                  Residual stage 1 thrust led to collision between stage 1 and stage 2   \n",
       "3                        Ratsat was carried to orbit on the first successful orbital launch of any privately funded and developed, liquid-propelled carrier rocket, the SpaceX Falcon 1   \n",
       "4                                                                                                                                                                                  None   \n",
       "\n",
       "  crew ships capsules                                              payloads  \\\n",
       "0   []    []       []                            [5eb0e4b5b6c3bb0006eeb1e1]   \n",
       "1   []    []       []                            [5eb0e4b6b6c3bb0006eeb1e2]   \n",
       "2   []    []       []  [5eb0e4b6b6c3bb0006eeb1e3, 5eb0e4b6b6c3bb0006eeb1e4]   \n",
       "3   []    []       []                            [5eb0e4b7b6c3bb0006eeb1e5]   \n",
       "4   []    []       []                            [5eb0e4b7b6c3bb0006eeb1e6]   \n",
       "\n",
       "                  launchpad  auto_update  \\\n",
       "0  5e9e4502f5090995de566f86         True   \n",
       "1  5e9e4502f5090995de566f86         True   \n",
       "2  5e9e4502f5090995de566f86         True   \n",
       "3  5e9e4502f5090995de566f86         True   \n",
       "4  5e9e4502f5090995de566f86         True   \n",
       "\n",
       "                                                                                                            failures  \\\n",
       "0                                                [{'time': 33, 'altitude': None, 'reason': 'merlin engine failure'}]   \n",
       "1            [{'time': 301, 'altitude': 289, 'reason': 'harmonic oscillation leading to premature engine shutdown'}]   \n",
       "2  [{'time': 140, 'altitude': 35, 'reason': 'residual stage-1 thrust led to collision between stage 1 and stage 2'}]   \n",
       "3                                                                                                                 []   \n",
       "4                                                                                                                 []   \n",
       "\n",
       "   flight_number         name                  date_utc   date_unix  \\\n",
       "0              1    FalconSat  2006-03-24T22:30:00.000Z  1143239400   \n",
       "1              2      DemoSat  2007-03-21T01:10:00.000Z  1174439400   \n",
       "2              3  Trailblazer  2008-08-03T03:34:00.000Z  1217734440   \n",
       "3              4       RatSat  2008-09-28T23:15:00.000Z  1222643700   \n",
       "4              5     RazakSat  2009-07-13T03:35:00.000Z  1247456100   \n",
       "\n",
       "                  date_local date_precision  upcoming  \\\n",
       "0  2006-03-25T10:30:00+12:00           hour     False   \n",
       "1  2007-03-21T13:10:00+12:00           hour     False   \n",
       "2  2008-08-03T15:34:00+12:00           hour     False   \n",
       "3  2008-09-28T11:15:00+12:00           hour     False   \n",
       "4  2009-07-13T15:35:00+12:00           hour     False   \n",
       "\n",
       "                                                                                                                                                                                              cores  \\\n",
       "0  [{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "1  [{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "2  [{'core': '5e9e289ef3591814873b2625', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "3  [{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "4  [{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "\n",
       "                         id fairings.reused fairings.recovery_attempt  \\\n",
       "0  5eb87cd9ffd86e000604b32a           False                     False   \n",
       "1  5eb87cdaffd86e000604b32b           False                     False   \n",
       "2  5eb87cdbffd86e000604b32c           False                     False   \n",
       "3  5eb87cdbffd86e000604b32d           False                     False   \n",
       "4  5eb87cdcffd86e000604b32e           False                     False   \n",
       "\n",
       "  fairings.recovered fairings.ships  \\\n",
       "0              False             []   \n",
       "1              False             []   \n",
       "2              False             []   \n",
       "3              False             []   \n",
       "4              False             []   \n",
       "\n",
       "                                 links.patch.small  \\\n",
       "0  https://images2.imgbox.com/3c/0e/T8iJcSN3_o.png   \n",
       "1  https://images2.imgbox.com/4f/e3/I0lkuJ2e_o.png   \n",
       "2  https://images2.imgbox.com/3d/86/cnu0pan8_o.png   \n",
       "3  https://images2.imgbox.com/e9/c9/T8CfiSYb_o.png   \n",
       "4  https://images2.imgbox.com/a7/ba/NBZSw3Ho_o.png   \n",
       "\n",
       "                                 links.patch.large links.reddit.campaign  \\\n",
       "0  https://images2.imgbox.com/40/e3/GypSkayF_o.png                  None   \n",
       "1  https://images2.imgbox.com/be/e7/iNqsqVYM_o.png                  None   \n",
       "2  https://images2.imgbox.com/4b/bd/d8UxLh4q_o.png                  None   \n",
       "3  https://images2.imgbox.com/e0/a7/FNjvKlXW_o.png                  None   \n",
       "4  https://images2.imgbox.com/8d/fc/0qdZMWWx_o.png                  None   \n",
       "\n",
       "  links.reddit.launch links.reddit.media links.reddit.recovery  \\\n",
       "0                None               None                  None   \n",
       "1                None               None                  None   \n",
       "2                None               None                  None   \n",
       "3                None               None                  None   \n",
       "4                None               None                  None   \n",
       "\n",
       "  links.flickr.small links.flickr.original  \\\n",
       "0                 []                    []   \n",
       "1                 []                    []   \n",
       "2                 []                    []   \n",
       "3                 []                    []   \n",
       "4                 []                    []   \n",
       "\n",
       "                                                                                           links.presskit  \\\n",
       "0                                                                                                    None   \n",
       "1                                                                                                    None   \n",
       "2                                                                                                    None   \n",
       "3                                                                                                    None   \n",
       "4  http://www.spacex.com/press/2012/12/19/spacexs-falcon-1-successfully-delivers-razaksat-satellite-orbit   \n",
       "\n",
       "                                 links.webcast links.youtube_id  \\\n",
       "0  https://www.youtube.com/watch?v=0a_00nJ_Y88      0a_00nJ_Y88   \n",
       "1  https://www.youtube.com/watch?v=Lk4zQ2wP-Nc      Lk4zQ2wP-Nc   \n",
       "2  https://www.youtube.com/watch?v=v0w9p3U8860      v0w9p3U8860   \n",
       "3  https://www.youtube.com/watch?v=dLQ2tZEH6G0      dLQ2tZEH6G0   \n",
       "4  https://www.youtube.com/watch?v=yTaIDooc8Og      yTaIDooc8Og   \n",
       "\n",
       "                                                                  links.article  \\\n",
       "0  https://www.space.com/2196-spacex-inaugural-falcon-1-rocket-lost-launch.html   \n",
       "1      https://www.space.com/3590-spacex-falcon-1-rocket-fails-reach-orbit.html   \n",
       "2       http://www.spacex.com/news/2013/02/11/falcon-1-flight-3-mission-summary   \n",
       "3                                          https://en.wikipedia.org/wiki/Ratsat   \n",
       "4                       http://www.spacex.com/news/2013/02/12/falcon-1-flight-5   \n",
       "\n",
       "                                         links.wikipedia  fairings  \n",
       "0                  https://en.wikipedia.org/wiki/DemoSat       NaN  \n",
       "1                  https://en.wikipedia.org/wiki/DemoSat       NaN  \n",
       "2  https://en.wikipedia.org/wiki/Trailblazer_(satellite)       NaN  \n",
       "3                   https://en.wikipedia.org/wiki/Ratsat       NaN  \n",
       "4                 https://en.wikipedia.org/wiki/RazakSAT       NaN  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the head of the dataframe\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You will notice that a lot of the data are IDs. For example the rocket column has no information about the rocket just an identification number.\n",
    "\n",
    "We will now use the API again to get information about the launches using the IDs given for each launch. Specifically we will be using columns <code>rocket</code>, <code>payloads</code>, <code>launchpad</code>, and <code>cores</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(107, 42)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_1040/2127768683.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Lets take a subset of our dataframe keeping only the features we want and the flight number, and date_utc.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'rocket'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'payloads'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'launchpad'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'cores'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'flight_number'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'date_utc'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# data.head()\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets take a subset of our dataframe keeping only the features we want and the flight number, and date_utc.\n",
    "data = data[['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]\n",
    "data.shape\n",
    "# data.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rocket</th>\n",
       "      <th>payloads</th>\n",
       "      <th>launchpad</th>\n",
       "      <th>cores</th>\n",
       "      <th>flight_number</th>\n",
       "      <th>date_utc</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>[5eb0e4b5b6c3bb0006eeb1e1]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>[{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-24T22:30:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>[5eb0e4b6b6c3bb0006eeb1e2]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>[{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>2</td>\n",
       "      <td>2007-03-21T01:10:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>[5eb0e4b7b6c3bb0006eeb1e5]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>[{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>4</td>\n",
       "      <td>2008-09-28T23:15:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>[5eb0e4b7b6c3bb0006eeb1e6]</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>[{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>5</td>\n",
       "      <td>2009-07-13T03:35:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5e9d0d95eda69973a809d1ec</td>\n",
       "      <td>[5eb0e4b7b6c3bb0006eeb1e7]</td>\n",
       "      <td>5e9e4501f509094ba4566f84</td>\n",
       "      <td>[{'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]</td>\n",
       "      <td>6</td>\n",
       "      <td>2010-06-04T18:45:00.000Z</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     rocket                    payloads  \\\n",
       "0  5e9d0d95eda69955f709d1eb  [5eb0e4b5b6c3bb0006eeb1e1]   \n",
       "1  5e9d0d95eda69955f709d1eb  [5eb0e4b6b6c3bb0006eeb1e2]   \n",
       "3  5e9d0d95eda69955f709d1eb  [5eb0e4b7b6c3bb0006eeb1e5]   \n",
       "4  5e9d0d95eda69955f709d1eb  [5eb0e4b7b6c3bb0006eeb1e6]   \n",
       "5  5e9d0d95eda69973a809d1ec  [5eb0e4b7b6c3bb0006eeb1e7]   \n",
       "\n",
       "                  launchpad  \\\n",
       "0  5e9e4502f5090995de566f86   \n",
       "1  5e9e4502f5090995de566f86   \n",
       "3  5e9e4502f5090995de566f86   \n",
       "4  5e9e4502f5090995de566f86   \n",
       "5  5e9e4501f509094ba4566f84   \n",
       "\n",
       "                                                                                                                                                                                              cores  \\\n",
       "0  [{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "1  [{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "3  [{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "4  [{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "5  [{'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}]   \n",
       "\n",
       "   flight_number                  date_utc  \n",
       "0              1  2006-03-24T22:30:00.000Z  \n",
       "1              2  2007-03-21T01:10:00.000Z  \n",
       "3              4  2008-09-28T23:15:00.000Z  \n",
       "4              5  2009-07-13T03:35:00.000Z  \n",
       "5              6  2010-06-04T18:45:00.000Z  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# # We will remove rows with multiple cores because those are falcon rockets with 2 extra rocket boosters and rows that have multiple payloads in a single rocket.\n",
    "data = data[data['cores'].map(len)==1]\n",
    "\n",
    "data = data[data['payloads'].map(len)==1]\n",
    "data.shape\n",
    "data.head()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rocket</th>\n",
       "      <th>payloads</th>\n",
       "      <th>launchpad</th>\n",
       "      <th>cores</th>\n",
       "      <th>flight_number</th>\n",
       "      <th>date_utc</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b5b6c3bb0006eeb1e1</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-24T22:30:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b6b6c3bb0006eeb1e2</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>2</td>\n",
       "      <td>2007-03-21T01:10:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e5</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>4</td>\n",
       "      <td>2008-09-28T23:15:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e6</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>5</td>\n",
       "      <td>2009-07-13T03:35:00.000Z</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5e9d0d95eda69973a809d1ec</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e7</td>\n",
       "      <td>5e9e4501f509094ba4566f84</td>\n",
       "      <td>{'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>6</td>\n",
       "      <td>2010-06-04T18:45:00.000Z</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     rocket                  payloads  \\\n",
       "0  5e9d0d95eda69955f709d1eb  5eb0e4b5b6c3bb0006eeb1e1   \n",
       "1  5e9d0d95eda69955f709d1eb  5eb0e4b6b6c3bb0006eeb1e2   \n",
       "3  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e5   \n",
       "4  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e6   \n",
       "5  5e9d0d95eda69973a809d1ec  5eb0e4b7b6c3bb0006eeb1e7   \n",
       "\n",
       "                  launchpad  \\\n",
       "0  5e9e4502f5090995de566f86   \n",
       "1  5e9e4502f5090995de566f86   \n",
       "3  5e9e4502f5090995de566f86   \n",
       "4  5e9e4502f5090995de566f86   \n",
       "5  5e9e4501f509094ba4566f84   \n",
       "\n",
       "                                                                                                                                                                                            cores  \\\n",
       "0  {'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "1  {'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "3  {'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "4  {'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "5  {'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "\n",
       "   flight_number                  date_utc  \n",
       "0              1  2006-03-24T22:30:00.000Z  \n",
       "1              2  2007-03-21T01:10:00.000Z  \n",
       "3              4  2008-09-28T23:15:00.000Z  \n",
       "4              5  2009-07-13T03:35:00.000Z  \n",
       "5              6  2010-06-04T18:45:00.000Z  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# # Since payloads and cores are lists of size 1 we will also extract the single value in the list and replace the feature.\n",
    "data['cores'] = data['cores'].map(lambda x : x[0])\n",
    "data.shape\n",
    "# data.head()\n",
    "data['payloads'] = data['payloads'].map(lambda x : x[0])\n",
    "data.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rocket</th>\n",
       "      <th>payloads</th>\n",
       "      <th>launchpad</th>\n",
       "      <th>cores</th>\n",
       "      <th>flight_number</th>\n",
       "      <th>date_utc</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b5b6c3bb0006eeb1e1</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-24T22:30:00.000Z</td>\n",
       "      <td>2006-03-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b6b6c3bb0006eeb1e2</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>2</td>\n",
       "      <td>2007-03-21T01:10:00.000Z</td>\n",
       "      <td>2007-03-21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e5</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>4</td>\n",
       "      <td>2008-09-28T23:15:00.000Z</td>\n",
       "      <td>2008-09-28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e6</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>5</td>\n",
       "      <td>2009-07-13T03:35:00.000Z</td>\n",
       "      <td>2009-07-13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5e9d0d95eda69973a809d1ec</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e7</td>\n",
       "      <td>5e9e4501f509094ba4566f84</td>\n",
       "      <td>{'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>6</td>\n",
       "      <td>2010-06-04T18:45:00.000Z</td>\n",
       "      <td>2010-06-04</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     rocket                  payloads  \\\n",
       "0  5e9d0d95eda69955f709d1eb  5eb0e4b5b6c3bb0006eeb1e1   \n",
       "1  5e9d0d95eda69955f709d1eb  5eb0e4b6b6c3bb0006eeb1e2   \n",
       "3  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e5   \n",
       "4  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e6   \n",
       "5  5e9d0d95eda69973a809d1ec  5eb0e4b7b6c3bb0006eeb1e7   \n",
       "\n",
       "                  launchpad  \\\n",
       "0  5e9e4502f5090995de566f86   \n",
       "1  5e9e4502f5090995de566f86   \n",
       "3  5e9e4502f5090995de566f86   \n",
       "4  5e9e4502f5090995de566f86   \n",
       "5  5e9e4501f509094ba4566f84   \n",
       "\n",
       "                                                                                                                                                                                            cores  \\\n",
       "0  {'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "1  {'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "3  {'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "4  {'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "5  {'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "\n",
       "   flight_number                  date_utc        date  \n",
       "0              1  2006-03-24T22:30:00.000Z  2006-03-24  \n",
       "1              2  2007-03-21T01:10:00.000Z  2007-03-21  \n",
       "3              4  2008-09-28T23:15:00.000Z  2008-09-28  \n",
       "4              5  2009-07-13T03:35:00.000Z  2009-07-13  \n",
       "5              6  2010-06-04T18:45:00.000Z  2010-06-04  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# # We also want to convert the date_utc to a datetime datatype and then extracting the date leaving the time\n",
    "data['date'] = pd.to_datetime(data['date_utc']).dt.date\n",
    "data.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rocket</th>\n",
       "      <th>payloads</th>\n",
       "      <th>launchpad</th>\n",
       "      <th>cores</th>\n",
       "      <th>flight_number</th>\n",
       "      <th>date_utc</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b5b6c3bb0006eeb1e1</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-24T22:30:00.000Z</td>\n",
       "      <td>2006-03-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b6b6c3bb0006eeb1e2</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>2</td>\n",
       "      <td>2007-03-21T01:10:00.000Z</td>\n",
       "      <td>2007-03-21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e5</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>4</td>\n",
       "      <td>2008-09-28T23:15:00.000Z</td>\n",
       "      <td>2008-09-28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e6</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>5</td>\n",
       "      <td>2009-07-13T03:35:00.000Z</td>\n",
       "      <td>2009-07-13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5e9d0d95eda69973a809d1ec</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e7</td>\n",
       "      <td>5e9e4501f509094ba4566f84</td>\n",
       "      <td>{'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>6</td>\n",
       "      <td>2010-06-04T18:45:00.000Z</td>\n",
       "      <td>2010-06-04</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     rocket                  payloads  \\\n",
       "0  5e9d0d95eda69955f709d1eb  5eb0e4b5b6c3bb0006eeb1e1   \n",
       "1  5e9d0d95eda69955f709d1eb  5eb0e4b6b6c3bb0006eeb1e2   \n",
       "3  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e5   \n",
       "4  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e6   \n",
       "5  5e9d0d95eda69973a809d1ec  5eb0e4b7b6c3bb0006eeb1e7   \n",
       "\n",
       "                  launchpad  \\\n",
       "0  5e9e4502f5090995de566f86   \n",
       "1  5e9e4502f5090995de566f86   \n",
       "3  5e9e4502f5090995de566f86   \n",
       "4  5e9e4502f5090995de566f86   \n",
       "5  5e9e4501f509094ba4566f84   \n",
       "\n",
       "                                                                                                                                                                                            cores  \\\n",
       "0  {'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "1  {'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "3  {'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "4  {'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "5  {'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "\n",
       "   flight_number                  date_utc        date  \n",
       "0              1  2006-03-24T22:30:00.000Z  2006-03-24  \n",
       "1              2  2007-03-21T01:10:00.000Z  2007-03-21  \n",
       "3              4  2008-09-28T23:15:00.000Z  2008-09-28  \n",
       "4              5  2009-07-13T03:35:00.000Z  2009-07-13  \n",
       "5              6  2010-06-04T18:45:00.000Z  2010-06-04  "
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Using the date we will restrict the dates of the launches\n",
    "data = data[data['date'] <= datetime.date(2020, 11, 13)]\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(94, 7)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rocket</th>\n",
       "      <th>payloads</th>\n",
       "      <th>launchpad</th>\n",
       "      <th>cores</th>\n",
       "      <th>flight_number</th>\n",
       "      <th>date_utc</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b5b6c3bb0006eeb1e1</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-24T22:30:00.000Z</td>\n",
       "      <td>2006-03-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b6b6c3bb0006eeb1e2</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>2</td>\n",
       "      <td>2007-03-21T01:10:00.000Z</td>\n",
       "      <td>2007-03-21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e5</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>4</td>\n",
       "      <td>2008-09-28T23:15:00.000Z</td>\n",
       "      <td>2008-09-28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5e9d0d95eda69955f709d1eb</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e6</td>\n",
       "      <td>5e9e4502f5090995de566f86</td>\n",
       "      <td>{'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>5</td>\n",
       "      <td>2009-07-13T03:35:00.000Z</td>\n",
       "      <td>2009-07-13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5e9d0d95eda69973a809d1ec</td>\n",
       "      <td>5eb0e4b7b6c3bb0006eeb1e7</td>\n",
       "      <td>5e9e4501f509094ba4566f84</td>\n",
       "      <td>{'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}</td>\n",
       "      <td>6</td>\n",
       "      <td>2010-06-04T18:45:00.000Z</td>\n",
       "      <td>2010-06-04</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     rocket                  payloads  \\\n",
       "0  5e9d0d95eda69955f709d1eb  5eb0e4b5b6c3bb0006eeb1e1   \n",
       "1  5e9d0d95eda69955f709d1eb  5eb0e4b6b6c3bb0006eeb1e2   \n",
       "3  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e5   \n",
       "4  5e9d0d95eda69955f709d1eb  5eb0e4b7b6c3bb0006eeb1e6   \n",
       "5  5e9d0d95eda69973a809d1ec  5eb0e4b7b6c3bb0006eeb1e7   \n",
       "\n",
       "                  launchpad  \\\n",
       "0  5e9e4502f5090995de566f86   \n",
       "1  5e9e4502f5090995de566f86   \n",
       "3  5e9e4502f5090995de566f86   \n",
       "4  5e9e4502f5090995de566f86   \n",
       "5  5e9e4501f509094ba4566f84   \n",
       "\n",
       "                                                                                                                                                                                            cores  \\\n",
       "0  {'core': '5e9e289df35918033d3b2623', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "1  {'core': '5e9e289ef35918416a3b2624', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "3  {'core': '5e9e289ef3591855dc3b2626', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "4  {'core': '5e9e289ef359184f103b2627', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "5  {'core': '5e9e289ef359185f2b3b2628', 'flight': 1, 'gridfins': False, 'legs': False, 'reused': False, 'landing_attempt': False, 'landing_success': None, 'landing_type': None, 'landpad': None}   \n",
       "\n",
       "   flight_number                  date_utc        date  \n",
       "0              1  2006-03-24T22:30:00.000Z  2006-03-24  \n",
       "1              2  2007-03-21T01:10:00.000Z  2007-03-21  \n",
       "3              4  2008-09-28T23:15:00.000Z  2008-09-28  \n",
       "4              5  2009-07-13T03:35:00.000Z  2009-07-13  \n",
       "5              6  2010-06-04T18:45:00.000Z  2010-06-04  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* From the <code>rocket</code> we would like to learn the booster name\n",
    "\n",
    "* From the <code>payload</code> we would like to learn the mass of the payload and the orbit that it is going to\n",
    "\n",
    "* From the <code>launchpad</code> we would like to know the name of the launch site being used, the longitude, and the latitude.\n",
    "\n",
    "* **From <code>cores</code> we would like to learn the outcome of the landing, the type of the landing, number of flights with that core, whether gridfins were used, whether the core is reused, whether legs were used, the landing pad used, the block of the core which is a number used to seperate version of cores, the number of times this specific core has been reused, and the serial of the core.**\n",
    "\n",
    "The data from these requests will be stored in lists and will be used to create a new dataframe.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Global variables \n",
    "BoosterVersion = []\n",
    "PayloadMass = []\n",
    "Orbit = []\n",
    "LaunchSite = []\n",
    "Outcome = []\n",
    "Flights = []\n",
    "GridFins = []\n",
    "Reused = []\n",
    "Legs = []\n",
    "LandingPad = []\n",
    "Block = []\n",
    "ReusedCount = []\n",
    "Serial = []\n",
    "Longitude = []\n",
    "Latitude = []"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These functions will apply the outputs globally to the above variables. Let's take a looks at <code>BoosterVersion</code> variable. Before we apply  <code>getBoosterVersion</code> the list is empty:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "BoosterVersion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's apply <code> getBoosterVersion</code> function method to get the booster version\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Call getBoosterVersion\n",
    "getBoosterVersion(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "the list has now been update \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Falcon 1', 'Falcon 1', 'Falcon 1', 'Falcon 1', 'Falcon 9']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "BoosterVersion[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "we can apply the rest of the  functions here:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Call getLaunchSite\n",
    "getLaunchSite(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Call getPayloadData\n",
    "getPayloadData(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Call getCoreData\n",
    "getCoreData(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally lets construct our dataset using the data we have obtained. We we combine the columns into a dictionary.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "launch_dict = {'FlightNumber': list(data['flight_number']),\n",
    "'Date': list(data['date']),\n",
    "'BoosterVersion':BoosterVersion,\n",
    "'PayloadMass':PayloadMass,\n",
    "'Orbit':Orbit,\n",
    "'LaunchSite':LaunchSite,\n",
    "'Outcome':Outcome,\n",
    "'Flights':Flights,\n",
    "'GridFins':GridFins,\n",
    "'Reused':Reused,\n",
    "'Legs':Legs,\n",
    "'LandingPad':LandingPad,\n",
    "'Block':Block,\n",
    "'ReusedCount':ReusedCount,\n",
    "'Serial':Serial,\n",
    "'Longitude': Longitude,\n",
    "'Latitude': Latitude}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then, we need to create a Pandas data frame from the dictionary launch_dict.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create a data from launch_dict\n",
    "df = pd.DataFrame(launch_dict)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Show the summary of the dataframe\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>Date</th>\n",
       "      <th>BoosterVersion</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Orbit</th>\n",
       "      <th>LaunchSite</th>\n",
       "      <th>Outcome</th>\n",
       "      <th>Flights</th>\n",
       "      <th>GridFins</th>\n",
       "      <th>Reused</th>\n",
       "      <th>Legs</th>\n",
       "      <th>LandingPad</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Serial</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Latitude</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-24</td>\n",
       "      <td>Falcon 1</td>\n",
       "      <td>20.0</td>\n",
       "      <td>LEO</td>\n",
       "      <td>Kwajalein Atoll</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Merlin1A</td>\n",
       "      <td>167.743129</td>\n",
       "      <td>9.047721</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2007-03-21</td>\n",
       "      <td>Falcon 1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LEO</td>\n",
       "      <td>Kwajalein Atoll</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Merlin2A</td>\n",
       "      <td>167.743129</td>\n",
       "      <td>9.047721</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>2008-09-28</td>\n",
       "      <td>Falcon 1</td>\n",
       "      <td>165.0</td>\n",
       "      <td>LEO</td>\n",
       "      <td>Kwajalein Atoll</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Merlin2C</td>\n",
       "      <td>167.743129</td>\n",
       "      <td>9.047721</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5</td>\n",
       "      <td>2009-07-13</td>\n",
       "      <td>Falcon 1</td>\n",
       "      <td>200.0</td>\n",
       "      <td>LEO</td>\n",
       "      <td>Kwajalein Atoll</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Merlin3C</td>\n",
       "      <td>167.743129</td>\n",
       "      <td>9.047721</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>6</td>\n",
       "      <td>2010-06-04</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0003</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   FlightNumber        Date BoosterVersion  PayloadMass Orbit  \\\n",
       "0             1  2006-03-24       Falcon 1         20.0   LEO   \n",
       "1             2  2007-03-21       Falcon 1          NaN   LEO   \n",
       "2             4  2008-09-28       Falcon 1        165.0   LEO   \n",
       "3             5  2009-07-13       Falcon 1        200.0   LEO   \n",
       "4             6  2010-06-04       Falcon 9          NaN   LEO   \n",
       "\n",
       "        LaunchSite    Outcome  Flights  GridFins  Reused   Legs LandingPad  \\\n",
       "0  Kwajalein Atoll  None None        1     False   False  False       None   \n",
       "1  Kwajalein Atoll  None None        1     False   False  False       None   \n",
       "2  Kwajalein Atoll  None None        1     False   False  False       None   \n",
       "3  Kwajalein Atoll  None None        1     False   False  False       None   \n",
       "4     CCSFS SLC 40  None None        1     False   False  False       None   \n",
       "\n",
       "   Block  ReusedCount    Serial   Longitude   Latitude  \n",
       "0    NaN            0  Merlin1A  167.743129   9.047721  \n",
       "1    NaN            0  Merlin2A  167.743129   9.047721  \n",
       "2    NaN            0  Merlin2C  167.743129   9.047721  \n",
       "3    NaN            0  Merlin3C  167.743129   9.047721  \n",
       "4    1.0            0     B0003  -80.577366  28.561857  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Show the head of the dataframe\n",
    "df.head()\n",
    "# df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 2: Filter the dataframe to only include `Falcon 9` launches\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally we will remove the Falcon 1 launches keeping only the Falcon 9 launches. Filter the data dataframe using the <code>BoosterVersion</code> column to only keep the Falcon 9 launches. Save the filtered data to a new dataframe called <code>data_falcon9</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>Date</th>\n",
       "      <th>BoosterVersion</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Orbit</th>\n",
       "      <th>LaunchSite</th>\n",
       "      <th>Outcome</th>\n",
       "      <th>Flights</th>\n",
       "      <th>GridFins</th>\n",
       "      <th>Reused</th>\n",
       "      <th>Legs</th>\n",
       "      <th>LandingPad</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Serial</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Latitude</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>6</td>\n",
       "      <td>2010-06-04</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0003</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>8</td>\n",
       "      <td>2012-05-22</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>525.0</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0005</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>10</td>\n",
       "      <td>2013-03-01</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>677.0</td>\n",
       "      <td>ISS</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0007</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>11</td>\n",
       "      <td>2013-09-29</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>500.0</td>\n",
       "      <td>PO</td>\n",
       "      <td>VAFB SLC 4E</td>\n",
       "      <td>False Ocean</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1003</td>\n",
       "      <td>-120.610829</td>\n",
       "      <td>34.632093</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>12</td>\n",
       "      <td>2013-12-03</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>3170.0</td>\n",
       "      <td>GTO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1004</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>89</th>\n",
       "      <td>102</td>\n",
       "      <td>2020-09-03</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>KSC LC 39A</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>2</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>12</td>\n",
       "      <td>B1060</td>\n",
       "      <td>-80.603956</td>\n",
       "      <td>28.608058</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90</th>\n",
       "      <td>103</td>\n",
       "      <td>2020-10-06</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>KSC LC 39A</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>3</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>13</td>\n",
       "      <td>B1058</td>\n",
       "      <td>-80.603956</td>\n",
       "      <td>28.608058</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>91</th>\n",
       "      <td>104</td>\n",
       "      <td>2020-10-18</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>KSC LC 39A</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>6</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>12</td>\n",
       "      <td>B1051</td>\n",
       "      <td>-80.603956</td>\n",
       "      <td>28.608058</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>92</th>\n",
       "      <td>105</td>\n",
       "      <td>2020-10-24</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>3</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3033383ecbb9e534e7cc</td>\n",
       "      <td>5.0</td>\n",
       "      <td>12</td>\n",
       "      <td>B1060</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93</th>\n",
       "      <td>106</td>\n",
       "      <td>2020-11-05</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>3681.0</td>\n",
       "      <td>MEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>1</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>8</td>\n",
       "      <td>B1062</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>90 rows × 17 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    FlightNumber        Date BoosterVersion  PayloadMass Orbit    LaunchSite  \\\n",
       "4              6  2010-06-04       Falcon 9          NaN   LEO  CCSFS SLC 40   \n",
       "5              8  2012-05-22       Falcon 9        525.0   LEO  CCSFS SLC 40   \n",
       "6             10  2013-03-01       Falcon 9        677.0   ISS  CCSFS SLC 40   \n",
       "7             11  2013-09-29       Falcon 9        500.0    PO   VAFB SLC 4E   \n",
       "8             12  2013-12-03       Falcon 9       3170.0   GTO  CCSFS SLC 40   \n",
       "..           ...         ...            ...          ...   ...           ...   \n",
       "89           102  2020-09-03       Falcon 9      15600.0  VLEO    KSC LC 39A   \n",
       "90           103  2020-10-06       Falcon 9      15600.0  VLEO    KSC LC 39A   \n",
       "91           104  2020-10-18       Falcon 9      15600.0  VLEO    KSC LC 39A   \n",
       "92           105  2020-10-24       Falcon 9      15600.0  VLEO  CCSFS SLC 40   \n",
       "93           106  2020-11-05       Falcon 9       3681.0   MEO  CCSFS SLC 40   \n",
       "\n",
       "        Outcome  Flights  GridFins  Reused   Legs                LandingPad  \\\n",
       "4     None None        1     False   False  False                      None   \n",
       "5     None None        1     False   False  False                      None   \n",
       "6     None None        1     False   False  False                      None   \n",
       "7   False Ocean        1     False   False  False                      None   \n",
       "8     None None        1     False   False  False                      None   \n",
       "..          ...      ...       ...     ...    ...                       ...   \n",
       "89    True ASDS        2      True    True   True  5e9e3032383ecb6bb234e7ca   \n",
       "90    True ASDS        3      True    True   True  5e9e3032383ecb6bb234e7ca   \n",
       "91    True ASDS        6      True    True   True  5e9e3032383ecb6bb234e7ca   \n",
       "92    True ASDS        3      True    True   True  5e9e3033383ecbb9e534e7cc   \n",
       "93    True ASDS        1      True   False   True  5e9e3032383ecb6bb234e7ca   \n",
       "\n",
       "    Block  ReusedCount Serial   Longitude   Latitude  \n",
       "4     1.0            0  B0003  -80.577366  28.561857  \n",
       "5     1.0            0  B0005  -80.577366  28.561857  \n",
       "6     1.0            0  B0007  -80.577366  28.561857  \n",
       "7     1.0            0  B1003 -120.610829  34.632093  \n",
       "8     1.0            0  B1004  -80.577366  28.561857  \n",
       "..    ...          ...    ...         ...        ...  \n",
       "89    5.0           12  B1060  -80.603956  28.608058  \n",
       "90    5.0           13  B1058  -80.603956  28.608058  \n",
       "91    5.0           12  B1051  -80.603956  28.608058  \n",
       "92    5.0           12  B1060  -80.577366  28.561857  \n",
       "93    5.0            8  B1062  -80.577366  28.561857  \n",
       "\n",
       "[90 rows x 17 columns]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Hint data['BoosterVersion']!='Falcon 1'\n",
    "data_falcon9 = df[df['BoosterVersion']!='Falcon 1']\n",
    "data_falcon9"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have removed some values we should reset the FlgihtNumber column\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/jupyterlab/conda/envs/python/lib/python3.7/site-packages/pandas/core/indexing.py:1773: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  self._setitem_single_column(ilocs[0], value, pi)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>Date</th>\n",
       "      <th>BoosterVersion</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Orbit</th>\n",
       "      <th>LaunchSite</th>\n",
       "      <th>Outcome</th>\n",
       "      <th>Flights</th>\n",
       "      <th>GridFins</th>\n",
       "      <th>Reused</th>\n",
       "      <th>Legs</th>\n",
       "      <th>LandingPad</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Serial</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Latitude</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>2010-06-04</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0003</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2</td>\n",
       "      <td>2012-05-22</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>525.0</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0005</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3</td>\n",
       "      <td>2013-03-01</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>677.0</td>\n",
       "      <td>ISS</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0007</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4</td>\n",
       "      <td>2013-09-29</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>500.0</td>\n",
       "      <td>PO</td>\n",
       "      <td>VAFB SLC 4E</td>\n",
       "      <td>False Ocean</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1003</td>\n",
       "      <td>-120.610829</td>\n",
       "      <td>34.632093</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>5</td>\n",
       "      <td>2013-12-03</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>3170.0</td>\n",
       "      <td>GTO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>None</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1004</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>89</th>\n",
       "      <td>86</td>\n",
       "      <td>2020-09-03</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>KSC LC 39A</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>2</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>12</td>\n",
       "      <td>B1060</td>\n",
       "      <td>-80.603956</td>\n",
       "      <td>28.608058</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90</th>\n",
       "      <td>87</td>\n",
       "      <td>2020-10-06</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>KSC LC 39A</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>3</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>13</td>\n",
       "      <td>B1058</td>\n",
       "      <td>-80.603956</td>\n",
       "      <td>28.608058</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>91</th>\n",
       "      <td>88</td>\n",
       "      <td>2020-10-18</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>KSC LC 39A</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>6</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>12</td>\n",
       "      <td>B1051</td>\n",
       "      <td>-80.603956</td>\n",
       "      <td>28.608058</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>92</th>\n",
       "      <td>89</td>\n",
       "      <td>2020-10-24</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>15600.0</td>\n",
       "      <td>VLEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>3</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3033383ecbb9e534e7cc</td>\n",
       "      <td>5.0</td>\n",
       "      <td>12</td>\n",
       "      <td>B1060</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93</th>\n",
       "      <td>90</td>\n",
       "      <td>2020-11-05</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>3681.0</td>\n",
       "      <td>MEO</td>\n",
       "      <td>CCSFS SLC 40</td>\n",
       "      <td>True ASDS</td>\n",
       "      <td>1</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>5e9e3032383ecb6bb234e7ca</td>\n",
       "      <td>5.0</td>\n",
       "      <td>8</td>\n",
       "      <td>B1062</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>90 rows × 17 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    FlightNumber        Date BoosterVersion  PayloadMass Orbit    LaunchSite  \\\n",
       "4              1  2010-06-04       Falcon 9          NaN   LEO  CCSFS SLC 40   \n",
       "5              2  2012-05-22       Falcon 9        525.0   LEO  CCSFS SLC 40   \n",
       "6              3  2013-03-01       Falcon 9        677.0   ISS  CCSFS SLC 40   \n",
       "7              4  2013-09-29       Falcon 9        500.0    PO   VAFB SLC 4E   \n",
       "8              5  2013-12-03       Falcon 9       3170.0   GTO  CCSFS SLC 40   \n",
       "..           ...         ...            ...          ...   ...           ...   \n",
       "89            86  2020-09-03       Falcon 9      15600.0  VLEO    KSC LC 39A   \n",
       "90            87  2020-10-06       Falcon 9      15600.0  VLEO    KSC LC 39A   \n",
       "91            88  2020-10-18       Falcon 9      15600.0  VLEO    KSC LC 39A   \n",
       "92            89  2020-10-24       Falcon 9      15600.0  VLEO  CCSFS SLC 40   \n",
       "93            90  2020-11-05       Falcon 9       3681.0   MEO  CCSFS SLC 40   \n",
       "\n",
       "        Outcome  Flights  GridFins  Reused   Legs                LandingPad  \\\n",
       "4     None None        1     False   False  False                      None   \n",
       "5     None None        1     False   False  False                      None   \n",
       "6     None None        1     False   False  False                      None   \n",
       "7   False Ocean        1     False   False  False                      None   \n",
       "8     None None        1     False   False  False                      None   \n",
       "..          ...      ...       ...     ...    ...                       ...   \n",
       "89    True ASDS        2      True    True   True  5e9e3032383ecb6bb234e7ca   \n",
       "90    True ASDS        3      True    True   True  5e9e3032383ecb6bb234e7ca   \n",
       "91    True ASDS        6      True    True   True  5e9e3032383ecb6bb234e7ca   \n",
       "92    True ASDS        3      True    True   True  5e9e3033383ecbb9e534e7cc   \n",
       "93    True ASDS        1      True   False   True  5e9e3032383ecb6bb234e7ca   \n",
       "\n",
       "    Block  ReusedCount Serial   Longitude   Latitude  \n",
       "4     1.0            0  B0003  -80.577366  28.561857  \n",
       "5     1.0            0  B0005  -80.577366  28.561857  \n",
       "6     1.0            0  B0007  -80.577366  28.561857  \n",
       "7     1.0            0  B1003 -120.610829  34.632093  \n",
       "8     1.0            0  B1004  -80.577366  28.561857  \n",
       "..    ...          ...    ...         ...        ...  \n",
       "89    5.0           12  B1060  -80.603956  28.608058  \n",
       "90    5.0           13  B1058  -80.603956  28.608058  \n",
       "91    5.0           12  B1051  -80.603956  28.608058  \n",
       "92    5.0           12  B1060  -80.577366  28.561857  \n",
       "93    5.0            8  B1062  -80.577366  28.561857  \n",
       "\n",
       "[90 rows x 17 columns]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_falcon9.loc[:,'FlightNumber'] = list(range(1, data_falcon9.shape[0]+1))\n",
    "data_falcon9"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Wrangling\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see below that some of the rows are missing values in our dataset.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "FlightNumber       0\n",
       "Date               0\n",
       "BoosterVersion     0\n",
       "PayloadMass        5\n",
       "Orbit              0\n",
       "LaunchSite         0\n",
       "Outcome            0\n",
       "Flights            0\n",
       "GridFins           0\n",
       "Reused             0\n",
       "Legs               0\n",
       "LandingPad        26\n",
       "Block              0\n",
       "ReusedCount        0\n",
       "Serial             0\n",
       "Longitude          0\n",
       "Latitude           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_falcon9.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Before we can continue we must deal with these missing values. The <code>LandingPad</code> column will retain None values to represent when landing pads were not used.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 3: Dealing with Missing Values\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate below the mean for the <code>PayloadMass</code> using the <code>.mean()</code>. Then use the mean and the <code>.replace()</code> function to replace `np.nan` values in the data with the mean you calculated.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/jupyterlab/conda/envs/python/lib/python3.7/site-packages/ipykernel_launcher.py:6: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  \n"
     ]
    }
   ],
   "source": [
    "# Calculate the mean value of PayloadMass column\n",
    "mean_payload_mass = data_falcon9['PayloadMass'].mean()\n",
    "\n",
    "\n",
    "# Replace the np.nan values with its mean value\n",
    "data_falcon9['PayloadMass'] = data_falcon9['PayloadMass'].fillna(mean_payload_mass)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "FlightNumber       0\n",
       "Date               0\n",
       "BoosterVersion     0\n",
       "PayloadMass        0\n",
       "Orbit              0\n",
       "LaunchSite         0\n",
       "Outcome            0\n",
       "Flights            0\n",
       "GridFins           0\n",
       "Reused             0\n",
       "Legs               0\n",
       "LandingPad        26\n",
       "Block              0\n",
       "ReusedCount        0\n",
       "Serial             0\n",
       "Longitude          0\n",
       "Latitude           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_falcon9.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You should see the number of missing values of the <code>PayLoadMass</code> change to zero.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we should have no missing values in our dataset except for in <code>LandingPad</code>.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can now export it to a <b>CSV</b> for the next section,but to make the answers consistent, in the next lab we will provide data in a pre-selected date range. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<code>data_falcon9.to_csv('dataset_part_1.csv', index=False)</code>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "data_falcon9.to_csv('dataset_part_1.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Authors\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Directory contents:\n",
      ".ipynb_checkpoints\n",
      "dataset_part_1.csv\n",
      "jupyter-labs-spacex-data-collection-api.ipynb\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "# Specify the directory path (use '.' for the current directory)\n",
    "directory_path = '.'\n",
    "\n",
    "# List contents of the directory\n",
    "contents = os.listdir(directory_path)\n",
    "\n",
    "print(\"Directory contents:\")\n",
    "for item in contents:\n",
    "    print(item)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<!--## Change Log\n",
    "-->\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<!--\n",
    "\n",
    "|Date (YYYY-MM-DD)|Version|Changed By|Change Description|\n",
    "|-|-|-|-|\n",
    "|2020-09-20|1.1|Joseph|get result each time you run|\n",
    "|2020-09-20|1.1|Azim |Created Part 1 Lab using SpaceX API|\n",
    "|2020-09-20|1.0|Joseph |Modified Multiple Areas|\n",
    "-->\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Copyright © 2021 IBM Corporation. All rights reserved.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "prev_pub_hash": "9fae682d673088bca20f23531422d88c5d45eddda6c66ca390a960fb8e99c74e"
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
