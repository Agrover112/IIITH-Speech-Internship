# IIITH-Speech-Internship

The following repository contains all the work I have done during my internship at Speech Lab , LTRC, IIIT-H. Since it is virtually impossible to showcase it in one repository,  will use this as a vault for future work as well. 
The initial  work (1 year back) was on Speech analysis(Week-1-Week-5) and running an ASR system on Kaldi (GMM-HMM using LDA features) which I deleted (wasn't using git)

Since most of the work is using Open Source tools, they are present as forks .The main work,changes are however contained within my [Kaldi fork](https://github.com/Agrover112/kaldi)
grapheme to phoneme conversion using [1] [g2p-sequitur],  , 

- Lexicon FST generation : Rendered PDFs present [here.](https://github.com/Agrover112/kaldi/tree/current/egs/yesno/s5)
- [1][2] G2P: Grapheme to phoneme conversion using Sequitur G2P [here](https://github.com/Agrover112/sequitur-g2p)
- [3]Vocab and lexicon generation (& validation) : Scripts for automatic lexicon generation present [here](https://github.com/Agrover112/kaldi/tree/current/egs/librispeech/s5)
- Forced Alignment and GoP:  Forced alignment and Goodness of Pronounciation(probability score) generation using DNN,GMM/HMM Acoustic models as .ctm files and also into Textgrid format, for Praat [here](https://github.com/Agrover112/kaldi-dnn-ali-gop/tree/aligop)
- Pipeline for Modified GoP score calculation: A pipeline for automatic calculation  Posteriors, Alignments and thus calculation of modified GoP scores [here](https://github.com/Agrover112/lex)


# Blogs:

- [Understanding Kaldi Part-1](https://medium.com/@agrover112/understanding-kaldi-part-1-c869980b1cbf)
: I wrote a blog explaining the process of creating Librispeech dictionary.

# Resources
- [Kaldi Resources](https://github.com/Agrover112/Kaldi-resources)
: Resources related to Kaldi.


# Notes

[1]It is recommended to use some other grapheme to phoneme convertor such as Phonitisaurus as they might be state of the art, but this is best for Kaldi-like workflow.

[2] The Sequitur G2P probably would fail for everyone attempting to use Python2.7 [(fixed by a PR #90)](https://github.com/sequitur-g2p/sequitur-g2p/pull/90)

[3] Documenting really helps especially if a rogue git pull suddenly is merged wierdly removing a commit that's worth 1 months work. Thx `git reflog`

[4] The decoding graph is pretty important and consists of HoCoLoG components. 
