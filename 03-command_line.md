# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
'mkdir -p': this will make a path of directories even if they don't previously exist
'ls -lr': more details on contents of a directory (size, author, date, etc.)\n
'pushd': brings you to the chosen directory; with no arguemnt will go to last directory pushed
'popd': brings you back to previous directory
'cp -r [dir] [dir]': copies and directory AND ITS CONTENTS (this is what the '-r' stands for) to another directory 
'mv [old name] [new name]': moves/renames a file or directory 
'more': display contents of file; use up and down arrow key or w to page through
'rm -rf [dir]': removes a directory and its files
'*': wildcard re
'grep -i [key word or phrase] [file/s]': this will look up the word or phrase in the files that match, ignoring case


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > `ls` lists the contents of the current working directory. `ls -a` lists all the directorys and all their contents. `ls -l` lists extra details including size, author, date, etc. `ls -lh` adds labels to the columns, such as size to make it more readable. 

---


---

What does `xargs` do? Give an example of how to use it.

> > `xargs` will take an input from STDIN and then feed this to another command. Its usefulness comes with its combination with other commands, such as `find` and `grep`. 

---

