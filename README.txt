README
Project 3 - Search


Names of Group Members:
Angela Li, Patrick Li


Descriptions of any Known Bugs with the Program:
None that are known


Instructions for Use:
1. The user will first index a particular XML/wiki file by typing the following command into the terminal:


python3 index.py <XML filepath> <titles filepath> <docs filepath> <words filepath>


Doing this will parse, tokenize, remove stop words, and stem all the text in the XML file. Additionally, the term relevances are calculated for each word in the text and the authority of each page in the wiki/XML is calculated.


2. Next, the user will run the following command into the terminal which will prompt the user to enter in a query.:


python3 query.py [--pagerank] <titleIndex filepath> <documentIndex filepath> <wordIndex filepath>


After entering in their query, the user will see the results of the 10 results of the pages with the highest combined PageRank and term relevance scores from that wiki/XML unless there are less than 10 results, then all results will be ranked. 


3. The user can continue to type in queries into the search engine until they type in ":quit" in which the REPL will terminate.


Description of how the Pieces of the Program Fit Together:


Indexer:
* In our program, the indexer file is the first file to be run. Upon calling the main method, an instance of an Index object is created and the parseXML function is called. 
* This method executes the parsing, stemming, removing stop words, and tokenizing processes and then calls the calculate_term_relevance and page_rank functions. 
* Calling these methods populates dictionaries that are used to store the corresponding values. 
* This data is written to outside files to be passed into the query. This pre-storage of data helps query search faster.


Querier:
* Next, after the user runs the querier in the terminal, the main method in query.py is run. 
* The main method extracts the user’s input from the terminal and inputs it into the REPL function, which then runs every word in the query against every document in the corpus and calculates its combined PageRank (if applicable) and term relevance score using the score_terms and score_terms_with_page_rank functions. 
* Lastly, the find_final_rankings function is called which prints to the terminal the 10 (or fewer) pages with the highest combined scores.
* The REPL (which uses a while loop) then continues to prompt the user for additional queries until the user types “:quit” into the terminal.


Description of Features that Failed to be Implemented:
N/A


Description of Extra Features that were Implemented:
N/A


Description of how the Program was Tested:


Unit Tests:
* We’ve written unit tests (including both general and edge cases) for all sections of the indexer which are listed below:
   * Parsing/tokenizing (i.e. making sure that the ids_to_titles, titles_to_ids, and page_to_links are populated correctly)
   * Stemming and removing stop words
   * Calculating term relevances (indirectly testing term frequency and inverse document frequency)
   * Calculating weights from a page to another page, Euclidean distances, and PageRanks 


Error Testing:
* We’ve also written tests for the following errors/exceptions:
   * Testing Invalid Filepath for Indexer: When we enter a file that is not in the same folder as the indexer and the querier, we get a message saying “File was not found”
   * Testing for a query that is not found in the chosen wiki: When we enter in a bogus query that is not located in the corpus, we get the following message: “No search results were found”

System Tests:
   * Lastly, in order to test the querier, we’ve conducted the following system general tests/searches:
   * DocProcessingExample1.xml: 
   * When searching the query “Liverpool,” we get the results “Liverpool” and “EPL” (in that order)
   * When searching the query “Manchester City,” we get the results “Manchester City” and “EPL” (in that order)
   * When searching the query “EPL,” we get the result “EPL”
   * DocProcessingExample2.xml: 
   * When searching the query “Embiid,” we get the results “Joel Embiid” and “Philadelphia 76ers” (in that order)
   * When searching the query “Scottie Barnes,” we get the results “Scottie Barnes” and “Toronto Raptors” (in that order)
   * When searching the query “ScOtTiE BArnES,” we get the results “Scottie Barnes” and “Toronto Raptors” (in that order)
   * We’ve also conducted the following edge cases:
   * tf_idf_example_6.xml: 
   * When searching the query “!,” we get the following message: “No search results were found” (punctuation)
   * When searching the query “is,” we get the following message: “No search results were found” (stop word)
   * tf_idf_example_4.xml: 
   * When searching the query “is,” we get the following message: “No search results were found” (no text on pages)
   * When searching the query “page,” we get the following message: “No search results were found” (“page” occurs on 4 documents and there are 4 pages in the corpus)
   * We’ve tested our indexer and querier against the outlined queries (with and without PageRank) in the MediumWiki Google Doc and all the results in our terminal appeared in the Google Doc.


--------------------------------------------SRC CONTENT---------------------------------------------

Search Engines and Social Responsibility


Design check task 4-a: Listen to or read the transcript of this short podcast segment of an interview with Charlton McIlwain, author of Black Software: The Internet and Racial Justice, from the AfroNet to Black Lives Matter, on Black engineers in the early days of the internet.


Design check task 4-b: Consider these examples of early internet community building and information sharing (AfroLink, NetNoir, Universal Black Pages). Which type of information distribution (search engines vs community pages) performs better according to different values, such as scalability, diversity, accessibility, security, and power? Pick two of these values and for each one you choose, argue which distribution method better achieves it and why. (2 - 4 sentences)


Diversity: We believe that search engines perform better according to diversity because it allows users to connect with a wider range of people than a community page. In the podcast, the speaker mentions that “I had myself encountered a whole group of people whom our internet, computing, and media histories had never known,” inferring that search engines and other computing technologies had allowed him to meet a lot of different people. Additionally, search engines can aggregate large amounts of data and information, which can allow users to be exposed to a variety of different viewpoints on the web.


Accessibility: We believe that the information distribution provided by search engines give more accessibility to certain types of information because it was incorporated into the World Wide Web, which people were already using at the time. After its development, people all around the world were able to access a multitude of sites containing various information. In fact, the podcast mentions how this innovation became “very public” and “very open.”


Security: We believe that community pages provide more security to its users because it is a relatively small platform for people to interact with and there aren’t many cybersecurity issues when dealing with community forums because not many people will try to hack them or exploit them. However, large search engines have a higher risk of being attacked due to people wanting certain information to be prioritized or more accessible to the world.


Design check task 4-c: Mcllwain argues that Google (or more broadly, search) “makes assumptions about what the user wants” which “can create a wide-scale gap.” Based on what you’ve read and learned so far about the inner workings of search:


What assumptions does the PageRank algorithm you are implementing make about the relative importance of web pages and what the user is searching for?


We think that the PageRank algorithm makes the assumption that websites that have many other websites linked to it are more important than other websites that don’t have many links connecting to it (1). Because of this, it assumes that the user is searching for information that has the highest “authority” on a particular topic, which may not always fit what the user is interested in (for example, maybe the user is interested in novel, less popular, or more controversial viewpoints about a particular subject). (2) Additionally, this approach may favor older web pages that have had many links connected to them rather than more current pages that the user could be searching for. (3)


Do you think Mcllwain’s statement is fair and accurate or do you think he’s missing something? Why?


Recall what you’ve learned earlier in the course about bias, stakeholders, power dynamics, filter-bubbles, and comparators to inform your answer to the two questions above. (6-8 sentences)


We think that McIlwain’s statement is not really accurate because it does seem to guide searchers towards the most relevant or most supported web pages/information about a topic (which is usually what people want). (4) As a result, this allows everyone who has access to the internet the ability to receive information that is strongly supported and backed up (i.e. has the highest authority) and thus it is in fact narrowing the gap in society and allowing less privileged individuals to gain access to the same information as everyone else. (5) However, I do also believe that search engines benefit the developers and engineers who work to create it, as they have access to a wealth of information about people’s search preferences and can use it to maximize certain costs and control what information people can view around the world. (6) This can have a negative impact in regards to a filter bubble because controlling what results a certain search can have can impact what a person thinks about the world and can limit them in their knowledge. (7) As a result, it can skew a person’s preferences in terms of locations, past-click behavior, search history, and website recommendations. (8)


Neutrality, Bias, and Monopolization:


Design check task 5-a: Read Algorithms of Oppression: How Search Engines Reinforce Racism by Safiya Umoja Noble (pages 15-26, up to the paragraph that begins with “There is an important and growing movement of scholars.”)


Design check task 5-b: Read How does Google’s monopoly hurt you? by Geoffrey Fowler.


Design check task 5-c: Navigate to google.com and try out these searches!
Search for “jeans.”
Search for “climate change is fake”
Search for “buy zofran” (Note: Zofran is a anti-nausea/vomiting medication)


Design check task 5-d: Reflect on the search results. Does anything surprise you? Which of Noble’s or Fowler’s arguments are supported or complicated by these results? (2 - 4 sentences)


Upon searching for “jeans,” we noticed that many ads were shown at the very top, followed by popular retailers that sell jeans. This supports Fowler’s viewpoint that Google is trying to make the search feature more lucrative for them and its stakeholders rather than for the users themselves. There were similar results when we searched “buy zofran”


Upon searching the phrase “climate change is fake,” we found that the first article that popped up was one that was titled “10 Myths about Climate Change,” which makes me think that Google is trying to help provide people with more factual information about important environmental crises and rather mitigate the spread of disinformation. This somewhat complicates Noble’s viewpoint, which asserts that Google needs to do more to protect the dissemination of dangerous assumptions and perspectives.


Design check task 5-e: For each of the three theories, do you think the theory prioritizes the user’s perspective, the website’s perspective, or the search engine’s perspective? (3 short sentences, one per theory)


We think that the first theory prioritizes the website’s perspective. This is because they have the assurance that they will be able to display information freely without being censored. This can lead to more users being attracted to their sites and visiting them, possibly increasing revenue for that company.


We think that the second theory prioritizes the search engine’s perspective. This is because this approach allows the search engine company to rank and control how information is ordered and thus can rank and place certain ads very high to increase revenue. Since the theory postulates that ranking is “innately biased,” it leaves it up to the company’s discretion and they can ultimately develop their search results to benefit their own users.


We think that the third theory prioritizes the user’s perspective. We feel this way because the theory states that search should be personalized towards their preferences and goals, making searching for items easier for them. This in turn allows them to benefit more from a search experience than websites or the search engine company itself.


Design check task 5-f: Which theory do you think best describes the aims and execution of search engines today? Which theories do you think that Noble and Fowler would most support? Which theory do you think search engines should aim for? (4 - 6 sentences)

We think that the third theory is the one that best describes the aims and execution of search engines today. Nowadays, many companies try to make themselves appeal to the user and have features that can make their search experience much easier. They achieve that through user-specific location settings, shopping preferences, ad/website recommendations, and more. Doing so allows the search engine company to attract more users and thus boost revenue. I think that Noble would most support the Conduit theory because she advocates for tailoring search results that don’t discriminate or create biased views against minorities. I think that Fowler would most support the second theory because it aligns with his views that search engines can rank information and search results themselves that most benefit their stakeholders and engineers. In our opinion, we believe that search engines should aim for the third theory, which would help users find the information they need, which is the main goal of people using a search engine in the first place.