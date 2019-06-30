# plant data tool

Source main.py into python or ipython in order to more easily analyze plant genomic data from the GLDS-7 dataset. Make sure the rest of these files are also in the same directory when the file is loaded.

```
# load file
> exec(open('main.py').read())

# input a list of genes into an array
> genelist = gene_input()
CEV1
FAD3
FAD7
ETR1
ERS1
CTR1
COI1
JAR1
EIN2
EIN3
ERF1
Thi1
Thi2
VSP1
PDF1
PDF2
^D

# search in all gene lists with lax requirements on biological and statistical significance
> search(genelist, semistrict)
---SHOOT---
ctr1   FP:  0.04181615464389932   FC:  1.3107387065931944
erf1   FP:  0.14522020473344033   FC:  1.2696163060555106
ers1   FP:  0.020548776037499383   FC:  1.3612900717945409
pdf1   FP:  0.10593473206112458   FC:  1.1972316427261593
---ROOT---
pdf2   FP:  0.10650910262844282   FC:  1.1459810908232937
---HYPOCOTYL---
ein2   FP:  0.09624827422814496   FC:  1.159931075849986
ctr1   FP:  0.08996938052495372   FC:  1.1461526184057065
---WHOLE PLANT---

```

Learn more by reading the source code, it's pretty straightforward.

GeneLab data are courtesy of the NASA GeneLab Data Repository (https://genelab-data.ndc.nasa.gov/genelab/projects/).
