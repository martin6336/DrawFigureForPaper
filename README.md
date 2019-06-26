# DrawFigureForPaper
This repo stores some python scripts for drawing figures in scientific papers, i.e., "[Microblog Hashtag Generation via Encoding Conversation Contexts
](https://www.aclweb.org/anthology/N19-1164)" and "[Topic-Aware Neural Keyphrase Generation for Social Media Language](https://arxiv.org/pdf/1906.03889.pdf)". 

Here I do not intend to give detailed tutorials on how to draw figures using python, but just share some examples, including _heatmap_, _histogram with error bar_, and _line figure_. This repo will be kept updating:)

## Dependencies
* Python 3.6
* matplotlib
* pickle
* numpy

## Heatmap 
Heatmap is a kind of common figures for visualizing attention scores. The inputs for drawing one heatmap would be column labels, row labels, and the weights to decide the darkness of color in each grid.
Here I give two examples below: (plotted by `heatmap.py` and `double_heatmap.py`)

<p align="center">
  <img src="https://github.com/yuewang-cuhk/DrawFigureForPaper/blob/master/heatmap.PNG" alt="blue heatmap" width="500"/>
</p>


As the attention weights may be in large size, you can dump it in the format of csv (e.g., `bi_attn.csv`) and read it as input in the program later.

<p align="center">
  <img src="https://github.com/yuewang-cuhk/DrawFigureForPaper/blob/master/double_heatmap.PNG" alt="red heatmap" width="500"/>
</p>


## Histogram
Histogram with error bar is a very good choice for demonstrating your model performance. Here I give two examples: (plotted by `hist_error_bar.py` and `frequency_hist.py`). Acknowledge [Wang Chen](https://github.com/Chen-Wang-CUHK) for his help.

<p align="center">
  <img src="https://github.com/yuewang-cuhk/DrawFigureForPaper/blob/master/hist_error_bar.PNG" alt="double vertical histogram with error bar" width="500"/>
</p>

<p align="center">
  <img src="https://github.com/yuewang-cuhk/DrawFigureForPaper/blob/master/frequency_hist.PNG" alt="double horizontal histogram" width="500"/>
</p>

## Line Figure
Here I show two examples on line figures: (plotted by `dist_line.py` and `absent_rate_lines.py`)

<p align="center">
  <img src="https://github.com/yuewang-cuhk/DrawFigureForPaper/blob/master/dist_line.PNG" alt="line figure for distributions" width="500"/>
</p>

To compute the distributions for each bin, you can first prepare the data statistics in the a `collections` python object and dump them as pickle object, e.g., `tw_seg_data.pickle` and `wb_seg_data.pickle`. `dist_line.py` reads these pickle data as input and compute its distribution for each bin. 

<p align="center">
  <img src="https://github.com/yuewang-cuhk/DrawFigureForPaper/blob/master/absent_rate_lines.PNG" alt="lline figure for absent rates" width="500"/>
</p>
