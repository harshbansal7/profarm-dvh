from django.http import HttpResponse
from django.shortcuts import render

# IMPORTS

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor 
from sklearn import metrics

# Data Frame for 2nd Service

ndf = pd.read_csv('main_app/csvfiles/yield_cleaned_2.csv')

ndf['Year'] = pd.Categorical(ndf['Year'], ordered = True)
ndf['State'] = pd.Categorical(ndf['State'], ordered = True)
ndf['District'] = pd.Categorical(ndf['District'], ordered = True)
ndf['Season'] = pd.Categorical(ndf['Season'], ordered = True)
ndf['Crop'] = pd.Categorical(ndf['Crop'], ordered = True)

years = (ndf['Year'].cat.categories)
states = (ndf['State'].cat.categories)
districts = (ndf['District'].cat.categories)
seasons = (ndf['Season'].cat.categories)
cropcats = (ndf['Crop'].cat.categories)

# Create your views here.
def home(request):
        return render(request, 'index.html')