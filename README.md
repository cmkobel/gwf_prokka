# gwf wrapper for prokka
This is a trivial package, that I seem to find myself using all over the place. Thus it is nice to have it lying in a repo.

## Usage
place fasta files in the `fasta/` dir

run the workflow:
```
# install dependencies
conda install -c gwforg gwf
conda install -c bioconda prokka

# check that everything is OK
gwf status

# run it
gwf run
```

The output can be found in `output/`


