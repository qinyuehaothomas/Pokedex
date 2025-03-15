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

The original task is a Command Line Interface(CLI) programme, but **Who on earth uses a CLI programme ?** (except those VIM/Linux gigachads.)

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

...But, I'm a JC student who scored 3/15 for physics, so **It is time-wise impossible, and not meaningful to deliver all the features**\
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
