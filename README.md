web-scraper
===========

A simple script that scrapes a website, extracting texts in a CSV file with the format below, and saving images.

| Page      | Tag                             | Text         | Link              | Image                  |
|-----------|---------------------------------|--------------|-------------------|------------------------|
| page path | element tag (h{1,6}, a, p, etc) | text content | link url (if any) | image address (if any) |

## Usage
First, install dependencies (python3):

```
pip install -r requirements
```

Then create a file containing urls of the websites you want to scrape, one line for each website, for example (I'll call this file `test_websites`):

```
https://theread.me
https://theguardian.com
```

Now you are ready to execute the script:

```
python index.py test_websites
                # ^ path to your file
```

To see available options, try `python index.py -h`.
