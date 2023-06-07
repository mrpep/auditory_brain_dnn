## Many but not all deep neural network audio models capture brain responses and exhibit correspondence between model stages and brain regions

This repository contains code and data accompanying: Greta Tuckute*, Jenelle Feather*, Dana Boebinger, Josh H. McDermott (2023): Many but not all deep neural network audio models capture brain responses and exhibit correspondence between model stages and brain regions.

## Environment
The environment does not require any sophisticated packages and would run in most Python 3.6 environments with [pandas](https://pandas.pydata.org/), [scikit-learn](https://scikit-learn.org/stable/), [statsmodels](https://www.statsmodels.org/stable/index.html), [seaborn](https://seaborn.pydata.org/) and [matplotlib](https://matplotlib.org/). However, to use the exact Python 3.6.10 environment used in the paper, install it as:

```
conda env create -f env_auditory_brain_dnn.yml
```

## Obtaining predictivity scores for DNNs
We used to common model-brain evaluation metrics, namely regression and representational similarity analysis (RSA), as demonstrated in the figure below.

<img src="./illustrations/fig1.png" width="600"/>


### Regression
To perform regression from DNN activations (regressors) to brain/component responses, run [/aud_dnn/AUD_main.py](https://github.com/gretatuckute/auditory_brain_dnn/blob/main/aud_dnn/AUD_main.py). This script 1. Loads a DNN unit activations from a given model (*source_model*) and layer (*source_layer*), 2. Loads the target (*target*) of interest (either neural data: *NH2015* (Norman-Haignere et al., 2015; 7,694 voxels across 8 participants) or *B2021* (Boebinger et al., 2021; 26,792 voxels across 20 participants), or component data *NH2015comp* (Norman-Haignere et al., 2015; 6 components), 3. Runs a ridge-regression across 10 splits of the data (165 sounds; 83 sounds in train and 82 sounds in test) and stores the outputs in /results/ in subfolders with an identifier corresponding to the DNN name.

#### Note on how DNN unit activations are organized
In the study we used either in-house models (trained by us, in lab) or external models (publicly available models). Both types of model activations are loaded using the function [get_source_features](https://github.com/gretatuckute/auditory_brain_dnn/blob/main/aud_dnn/utils.py#L211) which for in-house models will load the activations stored in a single h5 file (see e.g., /model-actv/Kell2018word/natsound_activations.h5). For external models, the model activations are stored as a single pickle file per sound using each sound's identifier (see e.g., /model-actv/S2T/stim5_alarm_clock_activations.pkl) which contains the activations across layers for the sound "stim5_alarm_clock" according to the sound nomenclature (see /data/stimuli/ -- the corresponding sound file would be named "stim5_alarm_clock.wav"). The [PytorchWrapper class](https://github.com/gretatuckute/auditory_brain_dnn/blob/main/aud_dnn/utils.py#L104) loads and concatenates these individual pickle files according to the specified sound order.
For both in-house and external models, we denote model activations obtained using a permuted network architecture with "_randnetw", e.g. /model-actv/Kell2018word/natsound_activations_randnetw.h5 or /model-actv/S2T/stim5_alarm_clock_activations_randnetw.pkl).


## Generating plots

TODO
(In notebooks, mention aggregation, e.g. for fig 7 and fig 2)


## DNN activations

### In-house models
TO-DO

### External models (publicly available)
The following repositories were used to extract DNN representations from the external DNN models:

[AST](https://github.com/gretatuckute/ast)<br>
[DCASE2020](https://github.com/gretatuckute/dcase-2020-baseline)<br>
[DeepSpeech2](https://github.com/gretatuckute/deepspeech.pytorch)<br>
[MetricGAN](https://github.com/gretatuckute/speechbrain_activation_extraction)<br>
[SepFormer](https://github.com/gretatuckute/speechbrain_activation_extraction)<br>
[S2T](https://github.com/gretatuckute/asr)<br>
[VGGish](https://github.com/gretatuckute/torchvggish)<br>
[wav2vec](https://github.com/gretatuckute/asr)<br>
[VQ-VAE (ZeroSpeech)](https://github.com/gretatuckute/ZeroSpeech)<br>

We thank the authors and developers for making these weights publicly available!
