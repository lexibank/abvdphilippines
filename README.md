# CLDF dataset derived from Greenhill et al.'s "Austronesian Basic Vocabulary Database" from 2020 focusing on Philippine languages

[![CLDF validation](https://github.com/SimonGreenhill/abvd_philippines/workflows/CLDF-validation/badge.svg)](https://github.com/SimonGreenhill/abvd_philippines/actions?query=workflow%3ACLDF-validation)

## How to cite

If you use these data please cite
- the original source
  > Greenhill, S.J., Blust. R, & Gray, R.D. (2008). The Austronesian Basic Vocabulary Database: From Bioinformatics to Lexomics. Evolutionary Bioinformatics, 4:271-283.
- the derived dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


This dataset is licensed under a CC-BY-4.0 license

Available online at https://abvd.shh.mpg.de/austronesian/


Conceptlists in Concepticon:
- [Blust-2008-210](https://concepticon.clld.org/contributions/Blust-2008-210)
## Notes

# Notes:

## Download

```
cldfbench download lexibank_abvdphilippines.py
```

## Make CLDF:

```
$ cldfbench lexibank.makecldf lexibank_abvdphilippines.py --clts-version=v2.2.0 --glottolog-version=v4.5 --concepticon-version=v2.5.0 
```


## Making a Nexus File:

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
cldfbench abvdphilippines.nexus --removecombined 2 --output abvdoceanic.nex

# ...with per-word ascertainment correction:
cldfbench abvdphilippines.nexus --ascertainment=word --removecombined 2 --output abvdoceanic.nex
````






## Statistics


[![CLDF validation](https://github.com/SimonGreenhill/abvd_philippines/workflows/CLDF-validation/badge.svg)](https://github.com/SimonGreenhill/abvd_philippines/actions?query=workflow%3ACLDF-validation)
![Glottolog: 100%](https://img.shields.io/badge/Glottolog-100%25-brightgreen.svg "Glottolog: 100%")
![Concepticon: 100%](https://img.shields.io/badge/Concepticon-100%25-brightgreen.svg "Concepticon: 100%")
![Source: 100%](https://img.shields.io/badge/Source-100%25-brightgreen.svg "Source: 100%")
![BIPA: 80%](https://img.shields.io/badge/BIPA-80%25-yellow.svg "BIPA: 80%")
![CLTS SoundClass: 80%](https://img.shields.io/badge/CLTS%20SoundClass-80%25-yellow.svg "CLTS SoundClass: 80%")

- **Varieties:** 210
- **Concepts:** 210
- **Lexemes:** 46,360
- **Sources:** 92
- **Synonymy:** 1.24
- **Cognacy:** 43,389 cognates in 4,758 cognate sets (201 singletons)
- **Cognate Diversity:** 0.10
- **Invalid lexemes:** 0
- **Tokens:** 264,765
- **Segments:** 249 (50 BIPA errors, 50 CTLS sound class errors, 199 CLTS modified)
- **Inventory size (avg):** 34.04

# Contributors

Name               | GitHub user     | Description                          | Role
---                | ---             | ---                                  | ---
Simon J. Greenhill | @SimonGreenhill | maintainer                           | Author
Johann-Mattis List | @lingulist  | orthography profiles | Other




## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [Wordlist](https://github.com/cldf/cldf/tree/master/modules/Wordlist) at [cldf/cldf-metadata.json](cldf/cldf-metadata.json)