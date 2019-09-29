# SBBSurprise

## Inspiration

People generally tend to be lazy. Even if we'd like to go outside and do some interesting stuff, the barrier of organising something often scares us away. So, what if we can provide a way of finding interesting day trips, without having to be concerned about every train connection and location? But the best part for those who seek adventures is the surprise, when you finally get to know your plans only minutes before your train leaves…


## What it does

The Application provides you with tickets for daytrips all around switzerland. First you enter your starting location and the date, afterwards you can choose some categories if you'd like your day to be something in a specific direction. Or by not telling any categorie information you might get to a place where you'd never expected to spend an amazing day. 

With only entering this low amount of information you'll get an offer for a surprise trip. No clue where it's going to be, you're in for an adventure.

While you don't have to do any organisation, the application checks for every train-, bus- and boat station in switzerland whether there are some interesting things around and if they fit your chosen categories. It then evaluates different offers with discounts up to 70% to find you a nice and not expensive day off.

## How we built it
SBB offered some APIs with a lot of data about their trains, stations, tickets, etc. Once we had some information about the stations we needed to find some activities to do there. That's why we used the Google API to categorize the station based on the reachable interesting things around them. 

After we had our categorized data, we could start to filter and work with it. Also we needed the SBB API again to find the best price offers for the trips.



## Challenges we ran into
The first steps for the frontend views could be done quite easily. But we run into some bigger problems with the Vue Materials not being adaptable to our ideas. Also for the data management there was some more work to do but it turned out fine.  

Some major problems with setting up the development environment occured. These were quite frustrating and took away a lot of time.

We worked with some languages that we weren't that familiar with before. So the lack of experience with python or vue was a burden but we also gained a lot from it.

With SBBs APIs we had some problems because it produced errors for some stations that weren't supported.

Also the location was so huge we had difficulties finding the showers

## Accomplishments that we're proud of
Actually managing to create a working prototype. 

Planning the product before diving into work so we had a way to go and all worked together well.

Finding the showers.

## What we learned
Not everyone was familiar with all the languages so we could profit a lot from the different levels of knowledge.

Another important lesson was that even if the challenge seems quite clear, there are still millions of ways to interpret and to discuss what to do. So you should never underestimate a challenge that seems clear.


## What's next for SBB Surprise

Integration in the SBB environment. Riddles/Hints to keep the customers interested and engaged, improvement of the algorithm, add some additional features.

## Built With
The Frontend - Webapplication is built with VueJS. Additionally we used Vuex and Vue Material.
The Backend consists of Python used with Flask. 
