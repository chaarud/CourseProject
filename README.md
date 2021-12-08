# Link to video presentation

# Documentation

## 1. Overview of code function

This is a script to make content-based recommendations about companies. The data set is taken from the publicly available descriptions of companies on the site Crunchbase (www.crunchbase.com). This script can be used to explore the top 2000 most popular companies on Crunchbase - it allows the user to designate a few companies they are interested in, and uses that information to make recommendations.

Furthermore, a user can indicate whether the recommendations they are viewing are useful or not, and this information is accounted for when making future recommendations by augmenting the user's preferences.

## 2. Documentation of implementation

Since content-based filtering builds largely off of a search engine, this script uses metapy. This is set up similarly to the one used by the class for MP2. This means there is a corpus of "documents" describing a company's name and some general-purpose descriptions. This can be found in the `companies` directory, in the file `companies.dat`. Each line represents a distinct company, and there is information about 2000 companies in the file. The file `companies/line.toml` also includes an option for the entire body of the company description to be preserved after the metapy index is built, because the script needs to read from that to display a useful recommendation.

The script itself can be divided into three portions. The first is setup - the metapy index is built from the data file, and an Okapi BM25 ranker is instantiated. Then, all of the company descriptions are broken down and keyed by the company name, so that there is a simple and efficient lookup method available later in the script to map from a company's name to its description.

The second part is the user's setup of their initial preferences. This repeatedly asks the user to input names of companies in the data set/corpus they find interesting (case-sensitive and exact). These are saved to a list, and after the user is finished inputting their initial preferences, the list is transformed into a query document. The contents of the query document are simply the concatenated descriptions of all the initial preferences (which means they'll all contribute equally to the eventual recommendations).

The third part is the actual recommendation loop.

## 3. Documentation of usage

In order to get metapy to work, I had to use python 3.5 (similar to the setup for MP2). I ran this code on a mac, and found [this post on campuswire](https://campuswire.com/c/G0A3AA370/feed/1856) helpful for setting up an environment for python 5.3.7.

To use, simply invoke `python recommender.py`. There aren't any command-line arguments to pass - I've hardcoded some of the things that would have made sense as command line arguments to make running the script as simple as possible.

The script will ask for companies as initial user preferences. This input is exact match and case-sensitive - in order for the initial preferences to be constructed effectively, you must pick companies that are in the data set. Lots of large tech companies are here - for a full list of company names acceptable for the initial preferences phase, consult the file `possible_companies.txt`.

## 4. Description of contribution of each team member

Not applicable - I was the only person on my team.

# Proposal and progress report

The project proposal pdf can be found in the file "project_proposal.pdf"

The progress report pdf can be found in the file "progress_report.pdf"
