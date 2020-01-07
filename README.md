# for-each-commit
you can create gif **call-graph** animation.  
![](./graph/call-aimation.gif)  

I used [bxcodec/go-clean-arch](https://github.com/bxcodec/go-clean-arch) program to create this animation.

## Prepare
- [Go](https://golang.org/)
- [Python3](https://www.python.org/)
- [Graphvis](https://www.graphviz.org/)
- [ImageMagick](https://imagemagick.org/index.php)

## Usage
### 0. clean graph directory
remove all files in your graph directory. `rm graph/*`
### 1. checkout branch
not to break your program I recommend you to change the branch of your program.
### 2. run python to create dot and gif files of each commit.
`python main.py /path/to/your/program/dir/`
### 3. resize all gif files
`mogrify -resize (height)x(width)! graph/*.gif`  
ex) `mogrify -resize 530x120! graph/*.gif`
### 4. create a gif animation
`convert -delay 50 -loop 0 graph/*.gif call-aimation.gif`