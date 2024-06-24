#  Improved 3D Gaussian Splatting


## Installation

**Platform**: Ubuntu 22+


## Running Commands
```bash
chmod +x run_strategy_1.sh
./run_strategy_1 <path to images folder>
```


```bash
chmod +x run_strategy_2.sh
./run_strategy_2 <path to images folder>
```


```bash
chmod +x run_strategy_3.sh
./run_strategy_3 <path to images folder>
```


## Some Results
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 900px; margin: 0 auto;">
  <figure style="margin: 0; text-align: center;">
    <img src="some_results/original_gs.gif" alt="GIF 1" style="width: 100%; height: auto;">
    <figcaption style="margin-top: 10px;">Original Gaussian Splatting</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center;">
    <img src="some_results/strategy-1.gif" alt="GIF 2" style="width: 100%; height: auto;">
    <figcaption style="margin-top: 10px;">Preprocessed-Gaussian Splatting (Strategy-1)</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center;">
    <img src="some_results/strategy-3.gif" alt="GIF 3" style="width: 100%; height: auto;">
    <figcaption style="margin-top: 10px;">Preprocessed-Gaussian Splatting (Strategy-3)</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center;">
    <img src="some_results/bad_gaussian.gif" alt="GIF 4" style="width: 100%; height: auto;">
    <figcaption style="margin-top: 10px;">BAD-Gaussians</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center;">
    <img src="some_results/deblur-nerf.gif" alt="GIF 5" style="width: 100%; height: auto;">
    <figcaption style="margin-top: 10px;">Deblur-NeRF</figcaption>
  </figure>
</div>





