# 0x0F. Python - Object-relational mapping
## Project Requirements
### Python Scripts
- Formatted with PEP8 style standards
- Compiled with `python3`
- All files must be executable
- All modules should have a documentation `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All functions should have a documentation `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- Not allowed to use `execute` with sqlalchemy

## File Descriptions
**0-select_states.py:** a script that lists all states from the database `hbtn_0e_0_usa`

**1-filter_states.py:** a script that lists all states with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`

**2-my_filter_states.py:** a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument

**3-my_safe_filter_states.py:** a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument and is safe from MySQL injections

**4-cities_by_state.py:** a script that lists all cities from the database `hbtn_0e_4_usa`

**5-filter_cities.py:** a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

**model_state.py:** a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`

**7-model_state_fetch_all.py:** a script that lists all `State` objects from the database `hbtn_0e_6_usa`

**8-model_state_fetch_first.py:** a script that prints the first `State` object from the database `hbtn_0e_6_usa`

**9-model_state_filter_a.py:** a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

**10-model_state_my_get.py:** a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

**11-model_state_insert.py:** a script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`

**12-model_state_update_id_2.py:** a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

**13-model_state_delete_a.py:** a script that deletes all `State` objects with a name containing the letter a from the database `hbtn_0e_6_usa`

**model_city.py, 14-model_city_fetch_by_state.py:** a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City` and a script that prints all `City` objects from the database `hbtn_0e_14_usa`

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)