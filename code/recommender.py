import sys

import metapy
import pytoml

NUM_DOCS = 2000

def input_yes(input):
    return input.lower().startswith("y") or input.lower().startswith("yes")

def input_no(input):
    return input.lower().startswith("n") or input.lower().startswith("no")

def fetch_unique(idx, query, already_recommended, page_size):
    if (page_size > NUM_DOCS):
        print("No unique recommendations left!")
        sys.exit(1)

    results = ranker.score(idx, query, page_size)
    for result in results:
        result_content = idx.metadata(result[0]).get("content")
        result_split = result_content.split(',', 1)
        result_company_name = result_split[0]
        result_company_desc = result_split[1]
        if result_company_name not in already_recommended:
            return (result_company_name, result_company_desc)

    fetch_unique(idx, query, already_recommended, page_size * 2)

if __name__ == '__main__':

    cfg = "config.toml"
    idx = metapy.index.make_inverted_index(cfg)
    ranker = metapy.index.OkapiBM25(1.9, 0.75, 200)

    with open(cfg, 'r') as fin:
        cfg_d = pytoml.load(fin)

    query = metapy.index.Document()

    companies = {}
    for i in range(NUM_DOCS):
        record = idx.metadata(i).get("content")
        record_split = record.split(',', 1)
        company_name = record_split[0]
        company_desc = record_split[1]
        companies[company_name] = company_desc

    print("Welcome to a company recommendation system!\n"
          "To get started, you will need to initialize your profile with some preferences.\n"
          "Please enter the names of some companies that are interesting to you: ")

    preference_inputs = []
    while True:
        preference_input = input("Please enter a single company name: ")

        if preference_input in companies:
            preference_inputs.append(preference_input)
        else:
            print("Didn't find company in list of companies indexed. Please make sure case-sensitive spelling is correct.")

        proceed = input("Would you like to enter another? Y/N: ")
        if input_no(proceed) and not preference_inputs:
            print("You need to indicate at least one preference.")
        if input_no(proceed):
            break
        elif not input_yes(proceed):
            print("Please input either Y or N. Completing initial preferences input.")
            break

    preference_contents = [companies[company] for company in preference_inputs]
    query.content(" ".join(preference_contents))

    already_recommended = preference_inputs
    while True:
        print("\nHere's a recommendation for you, based on the companies you have already indicated preferring: ")
        (result_company_name, result_company_desc) = fetch_unique(idx, query, already_recommended, 10)

        already_recommended.append(result_company_name)

        print("Recommendation: {}".format(result_company_name))
        print("\t{}".format(result_company_desc))

        feedback = input("Was your recommendation interesting? Please indicate Y/N: ")
        if input_yes(feedback):
            query.content(query.content() + " " + result_company_desc)
        elif not input_no(feedback):
            print("Please input either Y or N. Considering recommendation uninteresting and proceeding.")

        proceed = input("Would you like to see more recommendations? Y/N: ")
        if input_no(proceed):
            print("Goodbye!")
            break
        elif not input_yes(proceed):
            print("Please input either Y or N. Completing recommendations.")
            break


