# Project Pokedex
## Task
Given a csv file, make a porgram to query Pokemon stats based on:
- display selected number of Pokemon with their types and statistics\
*(In what order?)*
- display the first Pokemon of a Type of the trainer’s choice\
*(again, what is first?)*
- display all Pokemon with Total Base stat of the trainer’s choice.\
*(There's only 800 entry I dont' plan to use B-search)*
- display all Pokemon with a minimum set of stats
*(obviusly b search but 800 no need)*
- display all legendary Pokemon of Types of the trainer’s choice\
*(Tough...)*


*It's a school project so I can't really share the task file, copyright, you know＼（〇_ｏ）／*

The original task is a Command Line Interface(CLI) programme, but **Who want to use a CLI programme ?**
Also, the queries are weird, e.g. (no name query)

## So Here's the ideas of additional features:
1. "Guess The pokemon" mini game\
<img src="./ASSETS/readme_assets/Guess the pokemon.png" alt="Guess the pokemon"  height="200">
2. Star Plot \
<img src="./ASSETS/readme_assets/Dirty Deeds Done Dirt Cheap.jpg" alt="JOJO REFERENCE!!!" height="200">
3. Name query with levenstein distance for spelling aids\
<img src="./ASSETS/readme_assets/Search%20%20Hint%20Example.png" alt="JOJO REFERENCE!!!" height="200">
4. A UI
5. Export as a packaged software with no dependency issue

...But, I'm a JC student who scored 3/15 for physics, so **It is time-wise impossible to deliver all the features**\
**If you are keen on turing these into reality, feel free to contribute to this repo.*

# Devlog
## Day -8
Before I open this repo, I alrd implimented a web scraping script to download the pokemon images, and defined the basic Pokemon object.\
<img src="./ASSETS/readme_assets/Webscrap.png" alt="JOJO REFERENCE!!!" height="200">

The name in the csv is not the same as the name for image link, so some data filtering had to be done.

*It was done on 7/3/2025*

## Day 1
The 25 that still doesnt work is done manually. (by hard-coding their URL)

800 file seems to be a bit fat for Github, so I ignored the folder. **⭐PLEASE run the web scraping file to get the image assets, before you run the programme!**

After Checking the video, heres the better defined problem statement:

>#### Given a csv file, make a porgram to query Pokemon stats based on:
>- *display the first N row of CSV, with tabs*
>- *display the first pokemon of type S, full type name, case sensitive*
>- *display all pokemon with total stat N*
>- *display all pokemon with Special attack, special defense, and speed all greater or equal to the user's input.*
>- *input two types, letter for letter, and find legerndary pokemon*\
>
>program need to be input-robust\
>(ironically, the queries are not so robust, a UI can easily avoid these problems...)

After getting interrupted by some other tasks, which took unexpectedly long, I think Ill stop here for tdy.

*Done on 15/3/2025*

## Day 9
After a looooooooooooooooooooooooooooooooooooooooooooooooooooooooooong while, now NOI had finished and I wanna chill.\
So lets get back to this! q(≧▽≦q)\
---
#### Reorganised UI idea
It would be both easier & user friendlier to impliment the features in the following manners
- A "**Filter**" Manual with following
    - Two "**Type**" option dropdown
    - A bar for "**Base stat**" with a min and max value
        - A "**Advanced**" Query option for min. specific stats
    - A "**Legendary**" switch
    - A small "**Clear**" button to clear filter
- A "**Name**" field where user can search for pokemon
- If you type "Guess My Name" in the name bar, A New window with one round of "Guess my name" pops up

But welp, Im definitely *not* gonna code all these myself. ╮(╯-╰)╭\
To prevent anyone from accusing me for using AI, I'm gonna make the base version tdy.
---
Welp, It's 11pm and I feel like just doing a more advanced version of the Command Line interface and thats it\
╮（╯＿╰）╭\
I'll summarise Functionality and user guide in the next Devlog.
*Done on 24/3/2025*
