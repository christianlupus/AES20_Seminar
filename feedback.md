# Feedback on Code

## General

- Documentation how to use the files is missing.
    - What requirements are to be satisfied?
    - Where to put the files?
    - How to start/call the files?
- How to generate certificates? -> documentation/report
- Settting `verify=false` on `requests.get()` function call renders SSL obsolete -> man in the middle attack (both in client as well as login)
- How to set up MySQL? At least a initialization file (SQL file) would be needed to define the tables
- Maybe putting everything into a venv allows for more flexibility?
- Overview of the whole process/access procedure would be benefical
- `.gitignore` file?

## File __init__.py

- Make the configuration configurable (at least put them in separate variables to allow for an overview and simple way of changing thiongs like mysql host/user/....
- Why allowing generally POST for `/access` but not granting access at all?
- The route `/access` allows for bruteforcing the tag id
    - Implications unknown (-> documentation)
    - Potential option for DoS attack
- The `cursor.close()` on l. 33 is never reached
- Card number is stored as varchar/char in DB, right? In l. 22/51 the quotes are missing
- The SQL command in l. 22 can be hacked: both parameters `rfid_tag` and `door_id` are used unchecked and coming from the user/client/attacker (SQL injections)
- The `/register` route has POST support but is generally not granted.
- The SQL command in l. 45 allows injections
- Password is stored in plain text in DB
- Success in API (both routes) is distinguished only by context/content, better might be [status codes](https://stackoverflow.com/a/46199430/882756)
- Let the framework do the work for you: Split the `/register` route into two (one for registering **new** and one for unregisterung **obsolete** card numbers. The authorization and authentication can be extracted into a separate function that is called
- Curors are not closed on `register()` function (multiple times)
- Split methods in a clear pattern, e.g. MVC/MVVM
    - The controller just manages the interaction of the other parts
    - The model contains all code to interact with the DB only, it serves as a DB abstraction layert and simplifies access
    - The view just handles the return values to the client/user/...
    - The business logic can go to the view or the controller or separately into a helper
    - This is just a rough suggestion, alternatives might be existing, for such a small program it might be a bit too much
- Is `db.commit()` required in l. 61/66? Was a transaction started? Would bee a good thing to avoid issues with synchronization (locks/locked transactions might be needed)

## File login.py

- Why a relay call to `/register` and not calling directly `/register`?
- URL is fixed, make it configurable
- Why a new app for the login part?

## File login.html

- action of the form is empty. By intention?