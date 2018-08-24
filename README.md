About
-----

OMDB API client in python, this repository contain a tiny wrapper around OMDB
in order to search(string), and retrieve content get_by_id(string) /
get_by_tite(string). Based in https://github.com/dgilland/omdb.py

See full instructions in README.pdf

Usage
-----

    $ echo 'OMDB_APIKEY="your-api-key' > .env
    $ ./setup.sh

The above script will build/run a minimalist python container with the test
results, it also creates a dist/ folder where the omdb module is saved.

Dependencies
------------

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
