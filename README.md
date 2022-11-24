# leaving_twitter
python script to grab the list of followers or following to a csv

heavily based on https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/0d1587147d3bf8338b5fea2b4e5bb56d37f5c2b6/Follows-Lookup/followers_lookup.py

- added csv writer 
- pagination

# usage

- add your twitter Bearer Token: https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens
- bring in your user_id, easily done through https://tweeterid.com/
- comment or uncomment lines 13/14 and 21/22 depending on whether you are grabbing the following list or the followers
