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

### Rendering and Metrics
I use [Nerfstudio](https://docs.nerf.studio/quickstart/installation.html) and [Hloc](https://github.com/cvg/Hierarchical-Localization) for rendering the gaussian splats, and use original GS repo code for evaluating metrics. For rendering and evaluation, run:

```bash
cd rendering_and_metrics
python gs_schedule.py --dir <folder containing images to render (which can be blurr)> --gt_dir <ground truths for those images, especially if they are blurr>
```
The results are stored in "args.dir"+"_gs" folder as renderings and metrics (.txt) file.
## Some Results

| Original Gaussian Splatting | Preprocessed-Gaussian Splatting (Strategy-1) | Preprocessed-Gaussian Splatting (Strategy-3) |
|:--:|:--:|:--:|
| ![GIF 1](some_results/original_gs.gif) | ![GIF 2](some_results/strategy-1.gif) | ![GIF 3](some_results/strategy-3.gif) |

| BAD-Gaussians | Deblur-NeRF |
|:--:|:--:|
| ![GIF 4](some_results/bad_gaussian.gif) | ![GIF 5](some_results/deblur-nerf.gif) |





