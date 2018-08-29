# fancy-repos

1. [termtosvg](#termtosvg)
1. [lolcat](#lolcat)  
1. [spider for Beijing rent](#spider-rent)

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
- inspired from this [post](http://bigdata.51cto.com/art/201808/582085.htm), to crawl Beijing/Shanghai rent information from lianjia.com
- use `requests` and `lxml` to extract information
- `requests`：是用来请求对链家网进行访问的包。
- `lxml`：解析网页，用 Xpath 表达式与正则表达式一起来获取网页信息，相比 bs4 速度更快。
- beijing: https://bj.lianjia.com/zufang
- shanghai: https://sh.lianjia.com/zufang
- delimiter with `;`:
	- awk: `awk -F; '{print $4, $9'`
	- sort: `sort -rnt$',' -k9`
		- `-k9` means sort against the 9th column
		- `-n` means make the 9th column as numeric instead of string
		- `-u` means merge all the duplicates in **9th column**
		- `-r` means sort reversely
- list the result with highest rent
	```bash
	cat -n rent_lianjia_bj_0.txt | sort -rnt$',' -k9|head -15| lolcat
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
- 34min for Beijing
- ?min for Shanghai