## Goal
Add zsh functions to compile and monitor changes of latex papers on MacOS

## Dependencies

 - [MacTex](http://www.tug.org/mactex/)
 - [fswatch](https://emcrisostomo.github.io/fswatch/)

## Usage

source this script into `~./zshrc`

e.g 

```
source $HOME/compile_latex.sh
```

To compile paper run 

```
paper_compile main.tex
```

To Watch any changes in LaTex and Bibtex

```
paper_monitor main.tex
```


To compile a LaTex document without Bibtex

```
latex_monitor main.tex
```
