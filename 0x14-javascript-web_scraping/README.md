# 0x14. Javascript - Web scraping
## Project Requirements
### Javascript Scripts
- First line of all files should be `#!/usr/bin/node`
- Code should be `semistandard` compliant (version 11.0.0)
- All files must be executable
- Not allowed to use `var`

## File Descriptions
**0-readme.js:** a script that reads and prints the content of a file
- The first argument is the file path
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the error object

**1-writeme.js:** a script that writes a string to a file.
- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in `utf-8`
- If an error occurred during while writing, print the error object

**2-statuscode.js:** a script that display the status code of a `GET` request.
- The first argument is the URL to request (`GET`)
- The status code must be printed like this: `code: <status code>`
- You must use the module `request`

**3-starwars_title.js:** a script that prints the title of a Star Wars movie where the episode number matches a given integer
- The first argument is the episode number
- You must use the Star wars API with the endpoint `http://swapi.co/api/films/:episode_id`
- You must use the module `request`

**4-starwars_count.js:** a script that prints the number of movies where the character "Wedge Antilles" is present
- The first argument is the API URL of the Star wars API: `http://swapi.co/api/films/`
- Wedge Antilles is character ID `18`
- You must use the module `request`

**5-request_store.js:** a script that gets the contents of a webpage and stores it in a file
- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be UTF-8 encoded
- You must use the module `request`

**6-completed_tasks.js:** a script that computes the number of tasks completed by user id
- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
- You must use the module `request`

**100-starwars_characters.js:** a script that prints all characters of a Star Wars movie
- The first argument is the Movie ID - example: `3` = "Return of the Jedi"
- Display one character name by line
- You must use the Star Wars API
- You must use the module `request`

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)