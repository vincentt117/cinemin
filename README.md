# Cinemin

Python script for checking whether tickets for a given movie can be bought.
Currently only works for http://cineplex.com/

## Running

Run in command line with python3. Use the following format
```
>> python3 tickets_ava.py MOVIE-NAME1 MOVIE-NAME2 ...
```

For example:
```
>> python3 tickets_ava.py avengers-endgame green-book
2019-03-15 13:46:31
avengers-endgame: ❌   https://www.cineplex.com/Movie/avengers-endgame
green-book: ✅   https://www.cineplex.com/Movie/green-book

```