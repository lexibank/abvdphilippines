# Notes

## Download

```shell
cldfbench download lexibank_abvdphilippines.py
```

## Make CLDF

```shell
cldfbench lexibank.makecldf lexibank_abvdphilippines.py --clts-version=v2.2.0 --glottolog-version=v4.5 --concepticon-version=v2.5.0 
```

## Making a Nexus File

You will need to have the lexibank dataset installed. Probably best outside the directory:

```shell
# set up and install a virtual environment
python -m venv env
source ./env/bin/activate

# clone git repository
git clone https://github.com/lexibank/abvdphilippines

# or update repository
cd abvdphilippines
git checkout main
git pull
cd ..

# install dataset
cd abvdphilippines
pip install -e .
cd ..
```

To make a nexus file, use the custom `abvdphilippines.nexus` in cldfbench. The parameters are:

* --output=/path/to/filename.nex = the output file to write.
* --ascertainment = add BEASTs ascertainment correction if you want.
** --ascertainment=overall - one ascertainment character added for overall correction.
** --ascertainment=word - per word ascertainment correction.
* --removecombined=<int> - set level at which to filter combined cognates.

```shell
# make a nexus file, with combined cognates removed above level 2:
cldfbench abvdphilippines.nexus --removecombined 2 --output abvd_philippines.nex

# ...with per-word ascertainment correction:
cldfbench abvdphilippines.nexus --ascertainment=word --removecombined 2 --output abvd_philippines.nex
```
