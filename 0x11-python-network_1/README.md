# 0x11. Python - Network #1
## Project Requirements
### Python Scripts
- Formatted with PEP8 style standards
- Compiled with `python3`
- All files must be executable
- All modules should have a documentation `python3 -c 'print(__import__("my_module").__doc__)'`
- Must use `get` to access to dictionary value by key (it won't throw an exception if the key doesn't exist in the dictionary)
- Code should not be executed when imported

## File Descriptions
**0-hbtn_status.py:** a Python script that fetches `https://intranet.hbtn.io/status` using `urllib`

**1-hbtn_header.py:** a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response

**2-post_email.py:** a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

**3-error_code.py:** a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`)

**4-hbtn_status.py:** a Python script that fetches `https://intranet.hbtn.io/status` using `requests`

**5-hbtn_header.py:** a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

**6-post_email.py:** a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response

**7-error_code.py:** a Python script that takes in a URL, sends a request to the URL and displays the body of the response

**8-json_api.py:** a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter

**9-starwars.py:** a Python script that takes in a string and sends a search request to the Star Wars API

**10-my_github.py:** a Python script that takes your Github credentials (username and password) and uses the Github API to display your `id`

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)