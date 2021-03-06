Synopsis
=============
This is our solutions for the python exercise about Homicide Reports US 1980-2014. 
The github repo contains all python files, all charts generated as images and 2 txt files.

Questions asked
-------
 * Q1:Which ethnicity is it most common for the victims and perpetrators to be?
 * Q2:Which weapon is most used by men?
 * Q3:Which weapon is most used by women?
 * Q4:What is the age of the youngest victim and the oldest victim?
 * Q5:Average age of victims?
 * Q6:Male to female ratio of perpetrators?
 * Q7:Top 10 states with most homicides? display it with bars (barchart) or similar
 * Q8:Are younger perpetrators (age 15-25) more likely to get caught then older ones (25+)?

Solutions
-------
## 1.Which ethnicity is it most common for the victims and perpetrators to be?  
There is a lot of "unknowns" in both graphs, which makes it harder to make it harder to analyze.  
Hispanic are more involved in crimes than non-hispanic(Both victims and perpetrators).  
Less unknown ethnicity in victim's graph. Probably easier to document the ethnicity of victims than perpetrators for unsolved cases.  

![picture alt](http://i.imgur.com/lqvISgY.png)
![picture alt](http://i.imgur.com/kiTMhvX.png)



## 2.Which weapon is most used by men?
 * First thing to note is the numbers between the two graphs. Men are more often killers than women.  
 * Women tend to use "Knife" or "Blunt objects" more often than men.  
 * Women use "Knife" 0.80 for every 1.0 time they use "Handgun". (1:0.8)  
 * Men use "Knife" 0.30 for every 1.0 time they use "Handgun". (1:0.3)
 * Women use "Blunt Object" 0.33 for every 1.0 time they use "Handgun". (1:0.33)  
 * Men use "Blunt Object" 0.23 for every 1.0 time they use "Handgun". (1:0.23)
This might be because women isn't as gang-related as men and therefore doesn't have Handgun as often.  
Their murders might be more in the heat of the moment. 
![picture alt](http://i.imgur.com/9f7HiSa.png)

## 3.Which weapon is most used by women?
![picture alt](http://i.imgur.com/nyvX1Q7.png)

## 4.What is the age of the youngest victim and the oldest victim?
We added TXT file to the project. Didn't see any reason to display with a graph.  
Here is a snippet of the code getting the age of the youngest and the oldest victim and writing to a txt file.  
Youngest victim was 0 years old. Oldest guy was 998 years old. Seemed like an error in the csv file or documentation.
 ![picture alt](http://i.imgur.com/Zu0pSLS.jpg)

## 5.Average age of victims?
We added TXT file to the project. Didn't see any reason to display with a graph.  
Here is a snippet of the code getting the average age of victims and writing to a txt file.  
Average age was 35.0.  
![picture alt](http://i.imgur.com/Ti46wIl.jpg)

## 6. Male to female ratio of perpetrators?
90% male to 10% female (9:1) We used masks to remove all the "unknown", which was 70% of the perpetrators.
![picture alt](http://i.imgur.com/hOn1crU.png)

## 7. Top 10 states with most homicides? display it with bars (barchart) or similar
This graph needs to compare with population numbers of the states.  
e.g. "Top 10 states with most homicides per citizen"  
![picture alt](http://i.imgur.com/RyLyWNR.png)  

Heres a list of the biggest states in US by population:  

| top 10 homicides state    	| Population 	| In Top 10 state by population  	| Homicides per 100 	|  Rank in population 	|
|-------------------	|------------	|---	|--------	|----	|
| 1. California     	| 39,250,017 	| ✔ 	| 393.3 	| 1  	|
| 2. Texas          	| 27,862,596 	| ✔ 	| 448.7 	| 2	|
| 3. New York       	| 19,745,289 	| ✔ 	| 400.7 	| 4 	|
| 4. Florida        	| 20,612,439 	| ✔ 	| 554.6 	| 3 	|
| 5.Michigan       	| 9,928,301  	| ✔ 	| 348.9 	|  10 	|
| 6. Illinois       	| 12,801,539 	| ✔ 	| 494.8	|  6 	|
| 7. Pennsylvania   	| 12,802,503 	| ✔ 	| 528.2 	|  5 	|
| 8. Georgia        	| 10,310,371 	| ✔ 	| 488.9 	|  8 	|
| 9. North Carolina 	| 10,146,788 	| ✔ 	| 497.6 	|  9 	|
| 10. Louisiana     	| 4,681,666  	|  	| 238.5 | 25 	|   


![picture alt](http://i.imgur.com/9DFnS5P.png)

## 8. Are younger perpetrators (age 15-25) more likely to get caught then older ones (25+)?
The % of people not getting caught has so little a difference. Age doesn't affect chances of getting caught statistically.  
![picture alt](http://i.imgur.com/Gh4JYa5.png)
![picture alt](http://i.imgur.com/DFmFyuv.png)

Authors
-------
#### David Shmilowitz  
#### Jonathan Szigethy
