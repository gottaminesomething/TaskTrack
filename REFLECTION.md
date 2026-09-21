# ICA04 Reflection

## 1. Local and Remote Repositories

What is the difference between the local TaskTrack repository and the repository hosted on GitHub?

the difference between a local repository is that it cannot be pulled and edited from multiple devices, it is limited to the one folder it was created in. a repository hosted on github allows for pulling and pushing from any device with a clone and editing permissions


## 2. Connecting and Pushing

Why did adding `origin` not immediately place the project files on GitHub?

origin connects your local git repository to the github repo, it does not upload anything automatically, that only happens when you run the push command

## 3. Cloning

How is cloning a repository different from downloading its files as a ZIP archive?

it is a clone of the repository in its entirety, and has its own push and pull capability, as well as giving you all of the repo's commit history

## 4. Fetching and Pulling

What information did `git fetch` update, and what additional action did `git pull` perform?
fetch gets the information changed but does not change your own working environment
pull downloads it and applies it to your branch

## 5. Focused Commits

Why is it useful to commit the Python feature, sample task data, and README documentation separately?

because it allows for more specific commit names without them getting overly long