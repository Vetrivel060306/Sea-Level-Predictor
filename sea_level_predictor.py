import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy import stats

def draw_plot():
    df=pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots(figsize=(20, 6))
    ax.scatter(df.Year, df['CSIRO Adjusted Sea Level'],c='pink')

    # Create first line of best fit
    slope, intercept,_,_,_ = stats.linregress(df.Year,df['CSIRO Adjusted Sea Level'] )
    x_pred=pd.Series(range(1880,2051))
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, c='green')

    # Create second line of best fit
    dropped_df= df[df['Year']>1999]
    slope, intercept,_,_,_ = stats.linregress(dropped_df.Year,dropped_df['CSIRO Adjusted Sea Level'] )
    x_prediction=pd.Series(range(2000,2051))
    y_prediction = slope * x_prediction + intercept
    plt.plot(x_prediction, y_prediction, c='red')

    # Add labels and title
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlabel('Year')
    ax.set_title('Rise in Sea Level')


    plt.savefig('sea_level_plot.png')
    return plt.gca()
