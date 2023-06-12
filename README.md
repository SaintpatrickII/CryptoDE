# CryptoDE
Data Engineering project Utilising Coinmarketcap API

Expanding on my previous DE Project I wanted to explore further into DE by bringing my own API, Throughout this project new issues will come into play with using this new API.
For this project I have a few main aims to expand on my last project:
- Data wrangle with a live API
- Introduce Databricks for data warehousing
- Introduce more AWS services to gain exposure to cloud infrastrucure for DE

# 1. What are we pipelining?

- For this I've utilised the coinmarketcap API, the documentation gives a good basis to start bringing in data
- 
- However from first glance there isnt too much usable data avaliable
- 
- the default 'v1/cryptocurrency/listings/latest' api_call is full of well... not great data, until we get to the 'quote' key, this has useful information alike the volume, market cap etc.
- 
- The only problem with this however is the data is all held as a key-value pair for USD conversion
- 
- to make my dataframe useful I will need, the each coins name, its symbol & some nested dict KV pairs
