# fancy-repos  
  
1. [termtosvg](#termtosvg)  
1. [lolcat](#lolcat)  
1. [spider for Beijing rent](#spider-rent)  
1. [d3.js](#d3js)


### termtosvg  
- [termtosvg](https://github.com/nbedos/termtosvg) from github  
- a Python-based Unix terminal recorder that renders command line sessions as standalone SVG animations  
![cheat.sh](https://cdn.rawgit.com/KaiboLiu/kaiboliu.github.io/231f16fe/images/svg_cheat.sh.svg "cheat.sh")  
  
### lolcat  
- [lolcat](https://github.com/busyloop/lolcat) from github  
- a very fancy command line tool to output rainbow of colors in terminal.   
![lolcat](https://cdn.rawgit.com/KaiboLiu/fancy-repos/eb9a3d74/img/svg_lolcat.svg "lolcat")  
<!--  
<img src="https://cdn.rawgit.com/KaiboLiu/fancy-repos/eb9a3d74/img/svg_lolcat.svg">  
<img src="https://cdn.rawgit.com/KaiboLiu/kaiboliu.github.io/231f16fe/images/svg_cheat.sh.svg">  
<img src="./img/svg_cheat.sh.svg" width="50%">  
-->  
  
  
  
  
### spider-rent  
- inspired from this [post](https://mp.weixin.qq.com/s/vvZ2yBb2eMKP800LUPoAWg), to crawl Beijing/Shanghai rent information from lianjia.com  
- use `requests` and `lxml` to extract information  
- `requests`：是用来请求对链家网进行访问的包。  
- `lxml`：解析网页，用 Xpath 表达式与正则表达式一起来获取网页信息，相比 bs4 速度更快。  
- beijing: https://bj.lianjia.com/zufang  
- shanghai: https://sh.lianjia.com/zufang  
- delimiter with `;`:  
	- awk: `awk -F; '{print $4, $9'`  
	- sort: `sort -rnt$',' -k9`  
		- `-k9` means sort against the 9th column  
		- `-n` means make the 9th column as numeric instead of string.   
		- `-u` means merge all the duplicates in **9th column**.   
		- `-r` means sort reversely  
	- sed: `sed -i 'str' 's/original/new/g' file.txt`  
		- `-i` in-place(i.e. save back to the original file), while in OSX, we need to use `-i 'str'`, making `str` as extension to save the file to file**str**.txt. If `str=''` then we overwrite the original file  
		- `s` = the substitute command  
		- `original` = a regular expression describing the word to replace (or just the word itself)  
		- `new` = the text to replace it with  
		- `g` = global (i.e. replace all and not just the first occurrence)  
		- `file.txt` = the file name  
- list the results  
	```bash  
	cat -n rent_lianjia_bj.txt | sort -rnt$',' -k9|head -15| lolcat  
	# highest rent  
	cat -n rent_lianjia_bj.txt | sort -rnt$',' -k11|head -15| lolcat  
	# highest unit_rent  
	```  
- color in awk  
	```bash  
	RED='\033[01;31m'  
	GREEN='\033[01;32m'  
	YELLOW='\033[01;33m'  
	BLUE='\033[01;34m'  
	NONE='\033[0m'  
	awk '{print $1, "\033[01;31m"$2"\033[0m", $3}'  
	```  
- 34min/2070s for Beijing  (19551 items) 
- 42min/2516s for Shanghai (14051 items)
- 10min/ 636s for Shenzhen (4248 items)
- 16min/ 964s for Hangzhou (6589 items)
- 15min/ 924s for Changsha (6128 items)
- get to know a package [pyecharts](https://github.com/pyecharts/pyecharts) form the author of this project via wechat


### d3.js
wonderful [projects](https://github.com/d3/d3/wiki/Gallery) from [d3js](https://d3js.org/)
- [Chord Diagram](./d3js/chordDiagram), from online [project](https://bl.ocks.org/mbostock/1046712)
- [Streamgraph](./d3js/), from online [project](https://bl.ocks.org/mbostock/4060954)
- [Word Cloud](https://www.jasondavies.com/wordcloud/) very cool visualization tool ready to use
- [D3 Hierarchical Edge Bundling](https://beta.observablehq.com/@mbostock/d3-hierarchical-edge-bundling), and [interactive version](http://mbostock.github.io/d3/talk/20111116/#17)
- [POLITICAL INFLUENCE](http://www.brightpointinc.com/political_influence/)
- [Over the Decades, How States Have Shifted](https://archive.nytimes.com/www.nytimes.com/interactive/2012/10/15/us/politics/swing-history.html)




- fix the bug of cache line flashback in the scenario of continuous (multi-sentence) audio input.
- optimize parameters for the `eos` detection for the purpose of shorter latency.
- modified the line break strategy into a more smoother nature for dynamic scroll.

citi:
200k存60天给$1000 年化3%
50k  存60天给$600 年化7.2%
15k  存60天给$400 年化16%
hsbc:
100k存90天给$750 年化3%
10k  存90天给$350 年化14%
1.5k 存90天给$200 年化53%