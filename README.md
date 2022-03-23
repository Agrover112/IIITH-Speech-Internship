# IIITH-Speech-Internship

The following repository contains all the work I have done during my internship at Speech Lab , LTRC, IIIT-H. Since it is virtually impossible to showcase it in one repository,  will use this as a vault for future work as well. 
The initial  work (1 year back) was an ASR system on Kaldi (GMM-HMM using LDA features) which I deleted (wasnt using git)

Since most of the work is using Open Source tools, they are present as forks in following repositories.
[kaldi dnn and gmm alignment](https://github.com/Agrover112/kaldi-dnn-ali-gop/tree/aligop) which generates alignments using gmm/hmm into a Textgrid format, grapheme to phoneme conversion using [1] [g2p-sequitur](https://github.com/Agrover112/sequitur-g2p),  , rest of the work as of present in  [kaldi]()

- Lexicon FST generation : Rendered PDFs present [here.](https://github.com/Agrover112/kaldi/tree/current/egs/yesno/s5)
- [3]Vocab and lexicon generation (& validation) : Scripts for automatic lexicon generation present [here](https://github.com/Agrover112/kaldi/tree/current/egs/librispeech/s5)


# Blogs:

- [Understanding Kaldi Part-1](https://medium.com/@agrover112/understanding-kaldi-part-1-c869980b1cbf)
: I explain how the prepare_dict.sh works line by line




# Notes

[1]It is recommended to use some other grapheme to phoneme convertor such as Phonitisaurus as they might be state of the art, but this is best compatible with Kaldi imo.

[2] The Sequitur G2P probably would fail for everyone attempting to use Python2.7 [(fixed by a PR #90)](https://github.com/sequitur-g2p/sequitur-g2p/pull/90)

[3] Documenting really helps especially if a rogue git pull suddenly is merged wierdly removing a commit that's worth 1 months work. Thx git reflog
