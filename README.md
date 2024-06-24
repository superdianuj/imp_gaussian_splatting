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

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; text-align: center;">
  <figure style="margin: 0; padding: 10px;">
    <img src="some_results/original_gs.gif" alt="GIF 1" style="width: 200px; height: auto; display: block; margin: 0 auto;">
    <figcaption style="margin-bottom: 10px;">GS</figcaption>
  </figure>
  <figure style="margin: 0; padding: 10px;">
    <img src="some_results/strategy-1.gif" alt="GIF 2" style="width: 200px; height: auto; display: block; margin: 0 auto;">
    <figcaption style="margin-top: 10px;">P-GS (Strategy-1)</figcaption>
  </figure>
  <figure style="margin: 0; padding: 10px;">
    <img src="some_results/strategy-3.gif" alt="GIF 3" style="width: 200px; height: auto; display: block; margin: 0 auto;">
    <figcaption style="margin-top: 10px;">P-GS (Strategy-3)</figcaption>
  </figure>
  <figure style="margin: 0; padding: 10px;">
    <img src="some_results/bad_gaussian.gif" alt="GIF 4" style="width: 200px; height: auto; display: block; margin: 0 auto;">
    <figcaption style="margin-top: 10px;">BAD-Gaussians</figcaption>
  </figure>
  <figure style="margin: 0; padding: 10px;">
    <img src="some_results/deblur-nerf.gif" alt="GIF 5" style="width: 200px; height: auto; display: block; margin: 0 auto;">
    <figcaption style="margin-top: 10px;">Deblur-NeRF</figcaption>
  </figure>
</div>





