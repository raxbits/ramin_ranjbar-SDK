
# Philosophy
LOTR sdk has the following design goals:
- To enable access to the sdk endpoints designated in the challenge
- To be easy to use
- To be easy to test and debug

## Overall Thoughts
- API Key can be passed through Client constructor or using env vars to ease secrete rotations in prod if needed 
- API key is verified before any other operations are possible, saving user time and headache if this was evaluated lazely later.
- Code is re-used as much as possible, for example _request function handles all http communication
- Using docstring and linting to ensure good code readability.
- Pytest to test some aspects of functionality
- This pacakge can be uploaded to pypi, since it carries almost all metadata needed to do so.

## Key Classes
- Client - Encapsulates underlying operations needed to make things work reliably.
- CustomError - Raises error with custom message, flagging the user what has gone astray

