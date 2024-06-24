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
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto;">
  <figure style="margin: 0; text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
    <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; min-height: 250px;">
      <img src="some_results/original_gs.gif" alt="GIF 1" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <figcaption style="margin-top: 10px;">Original Gaussian Splatting</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
    <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; min-height: 250px;">
      <img src="some_results/strategy-1.gif" alt="GIF 2" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <figcaption style="margin-top: 10px;">Preprocessed-Gaussian Splatting (Strategy-1)</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
    <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; min-height: 250px;">
      <img src="some_results/strategy-3.gif" alt="GIF 3" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <figcaption style="margin-top: 10px;">Preprocessed-Gaussian Splatting (Strategy-3)</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
    <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; min-height: 250px;">
      <img src="some_results/bad_gaussian.gif" alt="GIF 4" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <figcaption style="margin-top: 10px;">BAD-Gaussians</figcaption>
  </figure>
  <figure style="margin: 0; text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
    <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; min-height: 950px;">
      <img src="some_results/deblur-nerf.gif" alt="GIF 5" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <figcaption style="margin-top: 10px;">Deblur-NeRF</figcaption>
  </figure>
</div>





