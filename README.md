# pygbdx: Simple CLI for GBDX
This is a simple cli to Digital Globe's GBDX platform, this was designed from the perspective of community user (the freely available tier). This platform allows you to access all of DG's Open data and also open Ikonos data along with Landsat and Sentinel datasets. You can create a [notebook acccount here](https://notebooks.geobigdata.io). I realized that the gbdx python libraries could be wrapped in a simple CLI and include additional features to serve as a functional CLI and this project is an attempt at doing that. The notebook setup offers additional tools, a GUI and interactive framework while CLI simplifies some of the operational needs of batch processing and performing calls using your own local machine.

## Table of contents
* [Installation](#installation)
* [Getting started](#getting-started)
* [pygbdx Simple CLI for GBDX](#pygbdx-simple-cli-for-gbdx)
	* [init](#init)
    * [info](#info)
    * [simple search](#simple-search)

## Installation
This assumes that you have native python & pip installed in your system, you can test this by going to the terminal (or windows command prompt) and trying

```python``` and then ```pip list```

If you get no errors and you have python 2.7.14 or higher you should be good to go. Please note that I have tested this only on python 2.7.15 but it should run on python 3.

**This also needs gbdxtools to be [installed on your system](https://gbdxtools.readthedocs.io/en/latest/)**

To install **pygbdx: Simple CLI for GBDX** you can install using two methods

```pip install pygbdx```

or you can also try

```
git clone https://github.com/samapriya/pygbdx.git
cd pygbdx
python setup.py install
```
For linux use sudo.

Installation is an optional step; the application can be also run directly by executing pygbdx.py script. The advantage of having it installed is being able to execute ppipe as any command line tool. I recommend installation within virtual environment. If you don't want to install, browse into the pygbdx folder and try ```python pygbdx.py``` to get to the same result.


## Getting started

As usual, to print help:

```
usage: pygbdx.py [-h] {init,info,simple_search} ...

GBDX Simple CLI

positional arguments:
  {init,info,simple_search}
    init                Initialize GBDX
    info                Prints account info for GBDX
    simple_search       Simple search to look for DG assets that intersect
                        your AOI handles KML/SHP/GEOJSON

optional arguments:
  -h, --help            show this help message and exit
```

To obtain help for a specific functionality, simply call it with _help_ switch, e.g.: `pygbdx simple_search -h`. If you didn't install pygbdx, then you can run it just by going to *pygbdx* directory and running `python pygbdx.py [arguments go here]`

## pygbdx Simple CLI for Earth Engine Uploads
The tool is designed to act as simple CLI for gbdx using the gbdxtools and more functionality will be added as the project evolves over time. All tools are designed keeping in mind the free community edition only.

### init
Just a simple tool to initalize and save config and access tokens.

```
usage: pygbdx init [-h]

optional arguments:
  -h, --help  show this help message and exit
```

### info
This prints info about your gbdx accounts, and prints information such as username,user id,account account id,id,role,client_id and account level.

```
usage: pygbdx info [-h]

optional arguments:
  -h, --help  show this help message and exit
```

### simple search
The script searches and summaries results for DG assets that intersect with your geometry or geometries depending on whether you pass a file or a folder. For now the script can handle GeoJSON, KML or Shapefile. It allows you to pass geometry but also startdate, enddate and limit for the number of items to look for.

```
usage: pygbdx simple_search [-h] [--local LOCAL] [--start START]
                               [--end END] [--limit LIMIT]

optional arguments:
  -h, --help     show this help message and exit
  --local LOCAL  full path for folder or file with SHP/KML/GEOJSON
  --start START  start date YYYY-MM-DD
  --end END      end date YYYY-MM-DD
  --limit LIMIT  Limit the number of items to search
```
