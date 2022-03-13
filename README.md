# Covid-19-Dashboard

How to run-<br>
1- download the files <br>
2- run index.py on pycharm or any IDE<br>
3- the link to web app should come up<br>
NOTE- due to some complications , I could not upload the app to Heroku or on web.<br>

File Structure-
1- assets - contains css file(I used it from the web itself) and images to upload if any
2- pages - contains codes for all the pages in the web app.
3- datasets - two datasets - extracted and cleaned using web crawler(data_crawler.py).
4- main folder - contains index file of main page, plotting functions(containing graph objects used for plotting) , combine.py to combine the two datasets received. 

References used -  snippets were taken and concepts from these resources.
1- plotly documentation - 
2- video lectures - charming data - 
3- dash documentation - https://dash.plotly.com/
4- app reference- 
5- css files and Standard reference- 

Dataset used-
Kaggle data- https://www.kaggle.com/imdevskp/corona-virus-report
Github repository - 

Libraries used-
Dash , Plotly, Heroku . language used - python.


Future improvements - TODO
1- fix the minor issues to enable the live update of data everyday
2- improve the speed of webapp by storing dataset on the browser.
3- include 2 more pages - forecasting and vaccination update. The code was simple but there was a lack of time.
4- learn more about forecasting models on pandemics - simply machine learning may not capture correct trends.

Description of the project-
This interactive data visualisation webapp illustrates what is possible using the Open Source Plotly Dash library and very little code.
Note that this is app development: not intended for 'production', and more for prototyping and example purpose. Think of it as a completely free Tableau, with the power of python for data science & machine learning directly accessible. 
The source code is in the GitHub.
The dashboard is optimised for desktop, laptop and tablet/mobile average sized screens - it may or may not work on small sized mobile screen.
All plots are interactive - hit play on the map, hover over bubbles, lines & points for dynamic annotations.
You can zoom using your mouse (drag to select area to zoom into), mouse wheel or trackpad, and double click to zoom out & reset . Click lines in legends to hide & show, or double-click to show only one line. Be sure to use zoom on the map because the bubbles overlap & become a lot clearer on zooming.

To maximise any plot to fill the window, use the expand icon in top left.

To filter the bottom middle timeline to a country, hover over a horizontal bar in the rightmost plot.
To switch between Confirmed, Active & Recorded, and Per Capita/Actual, use the radio buttons in the control panel, top right.
The code is entirely Open Source, and is intended as a showcase of what is possible in very few lines of python Plotly Dash code. For example, take a look in the github repo for the single line of Plotly Express code to generate the scatter_mapbox with animating timeline.

We use Global Kaggle Data which is web crawled & cleaned from the - CSSEGISandData/COVID-19 dataset (also on GitHub) also known as “John Hopkins data set”

The dataset gets updated everyday with covid data - so the app is live. 

Per Capita numbers are number / Population * 100,000 - intended to remove the size of country factor.

It was rapid to develop so there are many possible improvements and bugs. 
Enjoy!!.
