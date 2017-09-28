# 0x15. Javascript - Web JQuery
## Project Requirements
### Javascript Scripts
- All files will be interpreted on Chrome (version 57.0)
- Code should be semistandard compliant with the flag `--global $`: `semistandard *.js --global $`
- Must use jQuery version 3.x
- Not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data...

## File Descriptions
**0-script.js:** a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`)
- Must use `document.querySelector` to select the HTML tag
- Can't use the jQuery API

**1-script.js:** a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`)
- Must use `document.querySelector` to select the HTML tag
- Must use the jQuery API

**2-script.js:** a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`
- Can't use `document.querySelector` to select the HTML tag
- Must use the jQuery API

**3-script.js:** a Javascript script that adds the class red to the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`
- Can't use `document.querySelector` to select the HTML tag
- Must use the jQuery API

**4-starwars_count.js:** a Javascript script that toggles the class of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#toggle_header`
- The `HEADER` tag must always have one class: `red` or `green`, never both in the same time, never empty.
- If the current class is `red`, when the user clicks on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
- Can't use `document.querySelector` to select the HTML tag
- Must use the jQuery API

**5-script.js:** a Javascript script that adds a `LI` element to a list when the user clicks on the tag `DIV#add_item`
- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- Can't use `document.querySelector` to select the HTML tag
- Must use the jQuery API

**6-script.js:** a Javascript script that updates the text of the HTML tag `HEADER` to "New Header!!!" when the user clicks on `DIV#update_header`
- Can't use document.querySelector to select the HTML tag
- Must use the jQuery API

**7-script.js:** a Javascript script that fetches and replaces the `name` of this URL: `http://swapi.co/api/people/5/?format=json`
- The name must be displayed in the HTML tag `DIV#character`
- Can't use `document.querySelector` to select the HTML tag
- Must use the jQuery API

**8-script.js:** a Javascript script that fetches and lists all movies `title` by using this URL: `http://swapi.co/api/films?format=json`
- All movie titles must be list in the HTML tag UL#list_movies
- Can't use `document.querySelector` to select the HTML tag
- Must use the jQuery API

**9-script.js:** a Javascript script that fetches and prints the San Francisco wind speed by using this URL: `https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json`
- The wind speed must be display in the HTML tag `DIV#sf_wind_speed`
- Can't use `document.querySelector` to select the HTML tag
- Must use the jQuery API You script must be work when it imported from the `HEAD` tag

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)