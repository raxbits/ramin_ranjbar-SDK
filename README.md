# LOTR Python SDK

This package provides functionality to work with [Lord of the Ring API](https://the-one-api.dev/).

## Documentation

* SDK Documentation will be hosted online soon.

## Installation

The package can be installed with `pip`:

```bash
pip install --upgrade lotr
```

Install from source:

```bash
pip install .
```

### Requirements

- Python 3.8+

## Quick Start

To use this library, you must have an API key and specify it as a string when creating the client object. To get your API key, signup here : https://the-one-api.dev/account

Below is simple example to use the sdk client:

```python
import lotr

# initialize the Client with an API Key or set env variable LOTR_API_KEY=<YOUR_API_KEY>
client = lotr.Client('<YOUR_API_KEY>')

# get the list of available movies with meta data
movies = client.get_movies()

# get information about specific movie by id (identified by _id in data returned by client.get_movies())
movie_info = client.get_movie_info(_id='5cd95395de30eff6ebccde5d')

#get movie information by full movie title
movie_info = client.get_movie_info(name='The Lord of the Rings Series')

#get movie information by key word in the movie title 
movie_info = client.get_movie_info(name='Unexpected') #returns detail of movies with 'Unexpected' in their title

# get information about specific movie by id (identified by _id in data returned by client.get_movies())
movie_info = client.get_movie_info(_id='5cd95395de30eff6ebccde5d')

# get quote for a specific movie
movie_quote = client.get_movie_quote(_id='5cd95395de30eff6ebccde5d')
```