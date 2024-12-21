# Search

## Background
Search engines are powerful tools that allow users to retrieve information from vast datasets. Modern search engines process user queries to return highly relevant results within milliseconds. This efficiency is achieved through preprocessing (indexing) and intelligent ranking algorithms.

This project replicates the functionality of a simplified search engine, working with Wikipedia datasets in XML format. The search engine preprocesses this data, builds efficient data structures to interpret it, and uses the PageRank algorithm to rank documents.

## Indexer
The indexer is responsible for the following things:
- Parsing XML documents to extract terms, titles, and document IDs
- Creating data structures to map terms to documents
- Storing preprocessed data for efficient query handling

### Steps in Indexing

1. Parse the XML Dataset: Extract pages, titles, IDs, and text using Python's XML libraries.
2. Create Mappings:
  - Titles: Map document IDs to titles
  - Words: Map terms to documents
  - Ranks: Calculate and store PageRank values

3. Write Outputs:
  - Store mappings and rankings in files (titles.txt, docs.txt, words.txt) for later use by the querier.

### Command Line Inputs and Outputs
The indexer will take the following as input to the program:

`<XML filepath> <titles filepath> <docs filepath> <words filepath>`

The indexer takes in these inputs in this exact order and print an error message if there are fewer or more than four arguments.

#### Inputs
1. `<XML filepath>`: The name of the input XML file that the Indexer will read and parse.
2. `<titles filepath>`: The name of the output file where document IDs are mapped to document titles.
3. `<docs filepath>`: The name of the output file that stores the rankings computed by PageRank.
4. `<words filepath>`: The name of the output file that stores the relevance of documents to words.

#### Outputs
- **titles filepath:** Maps document IDs to document titles, facilitating user-friendly query results
- **docs filepath:** Stores PageRank values to rank documents by importance
- **words filepath:** Maps terms to document relevance scores, enabling efficient query processing

### Pages and Links

#### Pages
Each Wiki file consists of a single XML element tagged `xml`, within which there are a number of pages (also referred to as _documents_). Each page is enclosed by opening and closing `page` tags. Within each page, there is a `title`, a unique non-negative integer `id`, and some `text`, all enclosed by their respective tags.

For example, consider the following 2-page wiki:

```
<xml>
    <page>
        <title>A</title>
        <id>1</id>
        <text>[[C]]</text>
    </page>
    <page>
        <title>B</title>
        <id>2</id>
        <text>[[D]]</text>
    </page>
</xml>
```

#### Links
Page text may include links formatted in a specific way, which is critical for parsing text and understanding the relationships between pages. Links have two components: the text that is displayed and the address of the page it links to. In the wikis, the address corresponds to the title of the linked page. Links can be categorized as follows:

1. Direct Links: When the link text matches the linked page title, it appears as:

`[[Hammer]]`

Here, "Hammer" is both the text and the title of the linked page. In such cases, "Hammer" is treated as a word in the wiki text and contributes to parsing.

2. Links with Different Display Text: When the displayed text differs from the linked page title, the two are separated by a pipe (|):

`[[Presidents|Washington]]`

In this case, the page links to "Presidents" but displays "Washington" in the text. Only the displayed text ("Washington") is included in parsing for relevance; the page title ("Presidents") is excluded unless it appears elsewhere in plaintext.

3. Meta-Page Links: Links to meta-pages, such as categories, follow the same format. For instance:

`[[Category:Computer Science]]`

This links to the page "Category:Computer Science" and includes "Category", "Computer", and "Science" as individual words for parsing.

## Querier
The querier takes a user query and returns the most relevant results using preprocessed data. It focuses on the following items:
- Parsing user queries
- Finding documents containing the queried terms
- Sorting results based on relevance and PageRank

Here is an example run of the querier:

<img width="620" alt="Screenshot 2024-12-21 at 5 53 26 PM" src="https://github.com/user-attachments/assets/56ea5026-c3e3-42a9-af3d-fbb1b294a342" />

## PageRank Algorithm
The PageRank algorithm evaluates the importance of web pages based on their link structures. Pages with more inbound links from high-quality pages receive higher ranks.

### Steps Taken to Implement PageRank
1. Build a Graph: Represents documents as nodes and links as edges
2. Iterative Calculation:
  - Assign an initial rank to each document
  - Update ranks based on the ranks of linking documents
  - Repeat until ranks converge

3. Store Results: Save PageRank values for use by the querier

## Search Engine Architecture
The following diagram summarizes the components of the search engine. The orange blocks are the inputs (the web pages and the query). The blue boxes are different components of the solution (which you will write). The white boxes are files of intermediate data that get produced and read by the blue boxes. The components split into two main parts (the indexer and the querier) that were developed independently.

<img width="747" alt="Screenshot 2024-12-21 at 5 57 36 PM" src="https://github.com/user-attachments/assets/7c2615ba-61fb-46f2-904c-e339d0d5b229" />









