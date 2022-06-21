# Blog Application
This is a blog application built with Python(Django), HTML and CSS.

## Installation
- Fork the project to your account then clone it.
- Create a virtual environment and install all the dependencies from requirements.txt

```bash
$ pip install -r requirements.txt
```
NB: 
- The project uses a PotsgreSQL Database.
- The App uses trigram similarity so create the extenstion in your db.
```bash
$ psql <db_name>;
$ CREATE EXTENSION pg_trgm;
```

## Features
- Admin can post, update, delete blogs.
- The app comes with a sitemap framework to help with search engine rankings.
- Users/reader can search for blogs using the search bar which has been optimized to search words with similarities(trigram).

![alt text for screen readers](./static/images/search.png "Search Module").


## Contributing
Pull requests are welcome.

Please make sure to update tests as appropriate.

## License
&copy; [MIT](https://choosealicense.com/licenses/mit/)
