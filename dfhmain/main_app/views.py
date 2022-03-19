from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# REST API

from rest_framework import status

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
    if request.GET :
        dict = request.GET
        if(dict['service_name'] == 'NPK Calculator'):
            try:
                received_data = [dict['nitrogen'], dict['phosphorus'], dict['potassium'], dict['temp'], dict['humidity'], dict['phval'], dict['rainfall']]
                testing_data = [np.array(received_data, dtype='float64')]

                df_crop = pd.read_csv('main_app/csvfiles/npk.csv')
                X = df_crop.drop(columns = 'label')
                y = df_crop['label']

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

                knn = KNeighborsClassifier(n_neighbors=3)
                knn.fit(X_train, y_train)

                final_prediction = knn.predict(testing_data)

                context = {
                    'crop_name':str.capitalize(str(final_prediction[0])),
                    'accuracy': round(knn.score(X_test, y_test) * 100, 2)
                }
                return render(request, 'thanks-1.html', context)
            except:
                return HttpResponse(404)
        else:
            try:
                received_data = [dict['state'], dict['district'], dict['crop'], dict['year'], dict['season']]
                testing_data = [np.array(received_data, dtype='float64')]

                df_yield = pd.read_csv('main_app/csvfiles/yield_processing_1.csv')

                X = df_yield.drop(columns=['Unnamed: 0', 'Yield'], axis=1)
                Y = df_yield['Yield']

                X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20, random_state=42)

                regr = DecisionTreeRegressor(random_state = 42) # Do not use fit_intercept = False if you have removed 1 column after dummy encoding
                regr.fit(X_train, Y_train)
               
                final_prediction = regr.predict(testing_data)

                predictedacc = regr.predict(X_test)
                r2_test = metrics.r2_score(Y_test, predictedacc)

                context = {
                    'yield': round(final_prediction[0], 3),
                    'isYield':True,
                    'netprod':round(float(dict['area']) * float(final_prediction[0])),
                    'accuracy': round(r2_test * 100, 2)
                }
                return render(request, 'thanks-1.html', context)
            except:
                return HttpResponse(404)
    else :
        # Add Prediction Years
        sam = pd.Index(['2020-21', '2021-22'])
        yearsNew = years.append(sam)

        # Send Data to Website
        context = {
            'states':states,
            'districts':districts,
            'crops':cropcats,
            'years':yearsNew,
            'seasons':seasons,
        }
        return render(request, 'index.html', context)

def apiview(request, n, p, k, soilph, humidity, temp, rainfall):
    try:
        received_data = [n, p,k, temp, humidity, soilph, rainfall]
        testing_data = [np.array(received_data, dtype='float64')]

        df_crop = pd.read_csv('main_app/csvfiles/npk.csv')
        X = df_crop.drop(columns = 'label')
        y = df_crop['label']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train, y_train)

        final_prediction = knn.predict(testing_data)

        context = {
            'crop_name':str.capitalize(str(final_prediction[0])),
            'accuracy': round(knn.score(X_test, y_test) * 100, 2)
        }
        return JsonResponse(context, status=status.HTTP_200_OK)
    except:
        return HttpResponse(404)
