# Contributing

Mobius is designed to stay compact and predictable.
Follow these quick steps to submit your assignment:

## Working locally
Follow these quick steps to submit your assignment:

- Clone the forked repo:
 ```sh
  git clone git@github.com:{your_username}/mobius.git

  or

  git clone https://github.com/{your_username}/mobius.git
 ```

 - Set your repo as origin:

 ```sh
   git remote add origin git@github.com:{your_username}/mobius.git

   or

   git remote add origin https://github.com/{your_username}/mobius.git
 ```

  - Set the main repo as upstream:

  ```sh
    git remote add upstream git@github.com:Aaryan-Dadu/mobius.git

    or

    git remote add upstream https://github.com/Aaryan-Dadu/mobius.git
  ```

1. Create a virtual environment and install the project.
2. Run `mobius build` to generate the site.
3. Run `pytest` before opening a change.

## The Work
Open the repository in your editor and start contributing:

Add and commit this change:

```sh
  git add .
  git commit -m "your commit message"
```

*(Reminder: 100% human-written content only. AI generation = Disqualification.)*

## Submit

Push your changes to origin
```bash
git push origin main
```
Go to **github -> your repository -> create a PR** to the main upstream repository.

## Style

- keep modules small and focused
- prefer explicit data flow through page metadata
- keep template changes consistent with the reference output
- update tests when page structure changes intentionally

## Pull requests

Changes should include:

- code updates
- matching tests when behavior changes
- documentation updates when commands or layout change