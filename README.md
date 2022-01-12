# scrapping-metrics

## Setup
- Fork this repo
- Update `metrics.json` to be:
```
{}
```
- On Github, go to Setting > Secrets and create (follow the steps [here](https://github.com/vintasoftware/github-metrics#project-variables-setup)):
    - LOGIN
    - ORG_NAME
    - REPOSITORY_NAME
    - TOKEN
    - EXCLUDE_AUTHORS
- To fill the data retroactively you should run:
    - The script considers sprints of 2 weeks and 2019-12-30 as the start date

```
python retroactive.py
```

- To deploy run:
```
$ heroku create my-dash-app # change my-dash-app to a unique name
$ git add . # add all files to git
$ git commit -m 'Initial app boilerplate'
$ git push heroku main # deploy code to heroku
$ heroku ps:scale web=1  # run the app with a 1 heroku "dyno"
```
- On heroku, configure a pipeline deploy for every new push to main

## Local Setup
```
- pyenv virtualenv 3.9.0 kpis
- pip install -r requirements.txt
- ipython kernel install --name "kpis" --user
- jupyter lab
```

## Running the notebook
- https://mybinder.org/


## TODO
- Improve code
- Open a PR for github metrics. Why is the repo private?
- Separate metrics per squad
- Include hotfixes metrics


## Resources
- https://simonwillison.net/2021/Dec/7/git-history/
- https://simonwillison.net/2020/Oct/9/git-scraping/
