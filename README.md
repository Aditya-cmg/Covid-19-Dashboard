# Covid-19-Dashboard

How to run-<br>
1- download the files <br>
2- run index.py on pycharm or any IDE<br>
3- the link to web app should come up<br>
NOTE- due to some complications , I could not upload the app to Heroku or on web.<br>
<br>
File Structure-<br>
1- assets - contains css file(I used it from the web itself) and images to upload if any<br>
2- pages - contains codes for all the pages in the web app.<br>
3- datasets - two datasets - extracted and cleaned using web crawler(data_crawler.py).<br>
4- main folder - contains index file of main page, plotting functions(containing graph objects used for plotting) , combine.py to combine the two datasets received. <br>

References used -  snippets were taken and concepts from these resources.<br>
1- plotly documentation  <br>
2- video lectures - charming data - <br>
3- dash documentation - https://dash.plotly.com/<br>
4- app references  <br>
5- css files and Standard references <br>

Dataset used-<br>
Kaggle data- https://www.kaggle.com/imdevskp/corona-virus-report<br>


Libraries used-<br>
Dash , Plotly, Heroku . language used - python.<br>


Future improvements - TODO<br>
1- fix the minor issues to enable the live update of data everyday<br>
2- improve the speed of webapp by storing dataset on the browser.<br>
3- include 2 more pages - forecasting and vaccination update. The code was simple but there was a lack of time.<br>
4- learn more about forecasting models on pandemics - simply machine learning may not capture correct trends.<br>

Description of the project-<br>
This interactive data visualisation webapp illustrates what is possible using the Open Source Plotly Dash library and very little code.<br>
Note that this is app development: not intended for 'production', and more for prototyping and example purpose. Think of it as a completely free Tableau, with the power of python for data science & machine learning directly accessible. <br>
The source code is in the GitHub.<br>
The dashboard is optimised for desktop, laptop and tablet/mobile average sized screens - it may or may not work on small sized mobile screen.<br>
All plots are interactive - hit play on the map, hover over bubbles, lines & points for dynamic annotations.<br>
You can zoom using your mouse (drag to select area to zoom into), mouse wheel or trackpad, and double click to zoom out & reset . Click lines in legends to hide & show, or <br>double-click to show only one line. Be sure to use zoom on the map because the bubbles overlap & become a lot clearer on zooming.<br>

To maximise any plot to fill the window, use the expand icon in top left.<br>

To filter the bottom middle timeline to a country, hover over a horizontal bar in the rightmost plot.<br>
To switch between Confirmed, Active & Recorded, and Per Capita/Actual, use the radio buttons in the control panel, top right.<br>
The code is entirely Open Source, and is intended as a showcase of what is possible in very few lines of python Plotly Dash code. For example, take a look in the github repo for the single line of Plotly Express code to generate the scatter_mapbox with animating timeline.<br>

We use Global Kaggle Data which is web crawled & cleaned from the - CSSEGISandData/COVID-19 dataset (also on GitHub) also known as “John Hopkins data set”<br>

The dataset gets updated everyday with covid data - so the app is live. <br>

Per Capita numbers are number / Population * 100,000 - intended to remove the size of country factor.<br>

It was rapid to develop so there are many possible improvements and bugs. <br>
Enjoy!!.
