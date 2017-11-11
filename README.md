# AE and VAE Playground

**Disclaimer**: VAE coming soon...

#### Remarks

It seems the traditional normalization scheme (`mean=0.1307`, `std=0.3081`) leads to extremely poor performance (i.e. blurry white-ish blobs). I ended up using the `0.5` normalization which shifts the range of pixel values to [-1, 1]. I got the idea from [SherlockLiao](https://github.com/SherlockLiao/pytorch-beginner/tree/master/08-AutoEncoder) so do check out his repository!

A `tanh` activation right after the decoder layer really helps with the reconstructions. I assume that since tanh's range is [-1, 1], we are in a way "cheating" and helping the autoencoder's output match the initial normalization distribution.

#### Simple fully-connected autoencoder

<p align="center">
 <img src="./plots/simple_no_regularization.png" alt="Drawing">
</p>

#### Simple fully-connected autoencoder with `tanh`

<p align="center">
 <img src="./plots/simple_no_regularization_tanh.png" alt="Drawing">
</p>

#### Simple fully-connected autoencoder with `tanh` and L1 regularization

<p align="center">
 <img src="./plots/simple_l1_regularization_tanh.png" alt="Drawing">
</p>

#### Stacked 6 layer autoencoder

<p align="center">
 <img src="./plots/stacked_ae.png" alt="Drawing">
</p>

#### Stacked 6 layer autoencoder with `tanh`

<p align="center">
 <img src="./plots/stacked_ae_tanh.png" alt="Drawing">
</p>

#### Convolutional autoencoder with `tanh`

<p align="center">
 <img src="./plots/conv_ae_tanh.png" alt="Drawing">
</p>