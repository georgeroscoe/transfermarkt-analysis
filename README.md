# transfermarkt-analysis

Firstly, transfermarktscrape.py scrapes all of the games a player has played in, given the URL of their page, 
along with the number of goals scored, the date of the game, and the number of minutes played in it. It then saves 
it to a .csv file.

transfermarktpens.py scrapes all of the games in which a player has scored a penalty, along with the date of the game, 
and saves it to a .csv file.

Finally, penremover.py removes all of the penalty goals from the former .csv file by looking through the dates in the latter file.

Using these python scripts, I was able to collect all of the non-penalty goals scored by Ronaldo and Messi in the 
league + champions league throughout their career.

After combining the now formatted .csv files for both players, I used the package ggplot2 in R to produce a plot 
of their scoring rates over their entire career. This can be found in the file MessiRonaldoPlot.png, Messi in blue and Ronaldo in red.
