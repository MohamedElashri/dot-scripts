function paper_compile() {
	if [ "$1" != "" ]
	then
		if [[ "$1" == *.tex ]]
		then
			project_name="${1%.*}"
		else
			project_name="$1"
		fi
		latex_file="$project_name".tex

		pdflatex $latex_file
		bibtex $project_name
		pdflatex $latex_file
		pdflatex $latex_file
	else
		echo "Please specify main latex file name"
	fi
}

# Watch any changes in LaTex and Bibtex
# It automatically triggers the above paper_compile function whenever *.tex or *.bib files changed.
# e.g. latex_dir> paper_monitor main.tex
function paper_monitor(){
	if [ "$1" != "" ]
	then
		if [[ "$1" == *.tex ]]
		then
			project_name="${1%.*}"
		else
			project_name="$1"
		fi

		paper_compile $project_name

		# Open the compiled PDF file with default PDF viewer
		# If you want to specify a viewer you can add -a flag
		# e.g. open -a Preview "$1".pdf
		open "$project_name".pdf

		fswatch **/*.tex **/*.bib | (while read; do paper_compile $1; done)
	else
		echo "Please specify main latex file name"
	fi
}

# Keep compiling a LaTex document without Bibtex
function latex_monitor(){
	if [ "$1" != "" ]
	then
		pdflatex $1
		fswatch $1 | (while read; do pdflatex $1; done)
	else
		echo "Please specify tex file"
	fi
}

