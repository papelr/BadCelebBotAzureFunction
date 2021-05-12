# BadCelebBotAzureFunction

1) Custom built Azure Function in a Docker container
2) Custom written python scripts that create a new last name (randomly combined syllables from a spreadsheet), select a celebrity from a spreadsheet, craft a Tweet, scrape an image of the celeb from the web using Selenium (hence, custom Docker image), and posts a Tweet giving the celeb's "real name" and tagging them. 
3) Of course, the "real name" is a bogus and ridiculous concoction - but that's the point, isn't it? (Also the main point = creating an Azure Function with a custom Docker container running on a timer trigger with Selenium failing every other firing!)
4) There is one python script missing - the one with the Twitter API keys & my Slack hook. Obviously that's intentional (if it's not obvious, that's on you, not me!) 
5) I build the Docker image in VS Code, push to Docker Hub, and then set the WebApp settings in Azure to the latest image push. It's clunky, I know - but how else am I supposed to get Selenium running when Azure only offers one or two base Docker images?
6) Let's not forget some of these spectacularly clunky python scripts (and one very, very mangled class). So, sorry 'bout that, gotta learn somehow, ya know?


## Twitter Account: https://twitter.com/bad_celeb_names
## Handle: @bad_celeb_names


Follow at your own risk! Just kidding, the account actually looks somewhat professional (?!)