# Intro to version control

## Useful references

- [the git book](https://git-scm.com/book/en/v2) is available free online and is an extremely thorough resource for all things `git`.
- [the Mastering Git](https://thoughtbot.com/upcase/mastering-git) course by thoughtbot is a great way to learn some more advanced `git`.

## Why use version control?

- facilitates collaboration
- allows rollback to earlier working versions
- allows devs to look back at the project history

## Version control systems

There are a couple of version control systems you might hear about:

- `git`
- `mercurial`
- `subversion`
- `perforce`

But at this point `git` is the most popular (and best!).

## Basic concepts

- branches
- commits
- snapshots

## Exercises

1. Make sure you have `git` installed locally
2. Check out the repository locally and have a look around the files
3. Install a python virtual environment and try and run the tests locally
4. Now let's write a new test! Add in the optional `last_name` parameter and write a test (bonus points for doing it TDD)
5. Check out a branch and commit that change
6. Push that branch up to the remote repo and create a PR
7. Merge that in after approval
8. Clean up - pull down the new main branch and delete your local feature branch
9. Tada! You've added a new feature like a pro!

## Extra exercises

1. Add a new failing test for the `salutation` feature
2. Ahh it's lunchtime, but we don't want to leave our code uncommited. Just create a wip commit and push it up
3. We've come back from lunch let's finish the feature and push it up
4. Create a PR
5. Before merging this, we want to clean up our history (we don't want messy wip commits). We can do an interactive rebase to squash our two commits into one
6. Push that up (we'll need to do a force push)
7. Merge that in and do the same clean up as before
8. Tada! Another feature - and we made sure to maintain a clean git history in the process too!
