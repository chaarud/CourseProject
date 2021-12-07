# Link to video presentation

# Documentation

## 1. Overview of code function

This is a script to make content-based recommendations about companies. The data set is taken from the publicly available descriptions of companies on the site Crunchbase (www.crunchbase.com). This script can be used to explore the top 2000 most popular companies on Crunchbase - it allows the user to designate a few companies they are interested in, and uses that information to make recommendations.

Furthermore, a user can indicate whether the recommendations they are viewing are useful or not, and this information is accounted for when making future recommendations by augmenting the user's preferences.

## 2. Documentation of implementation

The script builds off of a metapy search engine (set up similarly to the one we used in MP2). 

## 3. Documentation of usage

In order to get metapy to work, I had to use python 3.5 (similar to the setup for MP2). I ran this code on a mac, and found [this post on campuswire](https://campuswire.com/c/G0A3AA370/feed/1856) helpful for setting up an environment for python 5.3.7.

To use, simply invoke `python recommender.py`. There aren't any command-line arguments to pass - I've hardcoded some of the things that would have made sense as command line arguments to make running the script as simple as possible.

## 4. Description of contribution of each team member

Not applicable - I was the only person on my team.

# Proposal and progress report

The project proposal pdf can be found in the file "project_proposal.pdf"

The progress report pdf can be found in the file "progress_report.pdf"
