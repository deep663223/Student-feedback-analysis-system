import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def load_data():
    data = pd.read_csv('C:\\Users\\HP\\3D Objects\\feedback\\Feedback.csv')
    return data

def plot_ques1(data):
    ques1 = data['Question 1'].values
