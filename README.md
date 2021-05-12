# BadCelebBotAzureFunction

1) Custom built Azure Function in a Docker container
2) Custom written python scripts that create a new last name (randomly combined syllables from a spreadsheet), select a celebrity from a spreadsheet, craft a Tweet, scrape an image of the celeb from the web using Selenium (hence, custom Docker image), and posts a Tweet giving the celeb's "real name" and tagging them. 
3) Of course, the "real name" is a bogus and ridiculous concoction - but that's the point, isn't it? (Also the main point = creating an Azure Function with a custom Docker container running on a timer trigger with Selenium failing every other firing!)
4) There is one python script missing - the one with the Twitter API keys & my Slack hook. Obviously that's intentional (if it's not obvious, that's on you, not me!) 
5) I build the Docker image in VS Code, push to Docker Hub, and then set the WebApp settings in Azure to the latest image push. It's clunky, I know - but how else am I supposed to get Selenium running when Azure only offers one or two base Docker images?

6) Let's not forget some of these spectacularly clunky python scripts (and one very, very mangled class). So, sorry 'bout that, but gotta learn somehow, ya know?


# Twitter Account Info

- Twitter Account: https://twitter.com/bad_celeb_names
- Handle: @bad_celeb_names

# Copy the GitHub, Build the Image (not sure why you'd want to, but whatever!)
1) Download the files (though you'll need your own Twitter API script & Slack hook - or delete the Slack notification script and take out the requisite lines in `__init__.py`

2) You need Docker Hub downloaded and running (and create a repo online)
3) `docker build --tag <YOUR_DOCKER_HUBB_ID>/whateveryourrepoiscalled:v1.0.0 .`
4) `docker push <YOUR_DOCKER_HUB_ID>/whateveryourrepoiscalled:v1.0.0`
5) Then there's a whole bunch of Azure Portal configuration, which I'm **not** going to go into: 

    * https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#python-version-and-package-management

    * https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=python

    * https://medium.com/@omerfarooqali/docker-container-on-azure-functions-with-python-33ad1a1166a4

    * https://towardsdatascience.com/how-to-create-a-selenium-web-scraper-in-azure-functions-f156fd074503

    *  https://www.shanebart.com/azure-cron-cheat-sheet/

    *  https://faun.pub/running-azure-functions-in-a-docker-container-a-beginners-guide-f921c150eab4 

6) There's a few things you need in the Portal; a function app, storage account, application insights, setting your storage account key correctly in the Portal and in local.settings.json (it's a goddamn pain) - but the above links account for all of that. 

# Disclaimer
Follow at your own risk! Just kidding, the account actually looks somewhat professional (?!)