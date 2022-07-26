# Python課題00

Pythonの基本的文法を身につける課題です。
この課題をクリアするとIFやForを含む、基本文法とコマンドライン引数についての理解ができます。

## 採点ツールの使い方

```
> python3 check.py
<ファイル名> <引数> <ステータス>
```

ステータスには以下があります。
```
OK					テストがクリアできました。
>> KO <<			テストがクリアできませんでした。もう一度プログラムを見直しましょう。
file does not exist	該当するファイルがありません。
```

## 課題

課題はそれぞれのエクササイズ名でフォルダーを作り、その中にファイルを格納してください。

```
./
|
|-ex00
| |-print.py
|
...
|-ex07
| |-put_sqare.py
```


### ex00

|提出するファイル|使う関数|
|----|----|
|print.py|print()|

`print.py`
```
print("hello")
```
このように書いて実行すると、以下の様な出力が得られます。

```
> python3 print.py
hello
>
```

この様な出力をさせてください。

```
> python3 print.py
HELLO
>
```

### ex01

|提出するファイル|使う関数|
|----|----|
|print_some.py|print(), type()|

`print.py`
```
print(type("HELLO"))
```

この様なファイルを作ると、出力は以下のようになります。
```
> python3 print_some.py
<class 'str'>
>
```

これを利用して、以下のような出力を作ってください。

```
> python3 print_some.py
hello <class 'str'>
HELLO <class 'str'>
123 <class 'str'>
123 <class 'int'>
>
```

### ex02

|提出するファイル|使う関数|
|----|----|
|type.py|print(), type()|

`1, 2, 3`が格納されたリストを作りましょう。
さらに、リストとそれぞれの要素の型も出力してください。

```
> python3 type.py
[1, 2, 3] <class 'list'>
1 <class 'int'>
2 <class 'int'>
3 <class 'int'>
> 
```

### ex03

|提出するファイル|使う関数等|
|----|----|
|arg.py|print(), sys.args|

コマンドライン引数を出力して下さい。
（ただし、コマンドライン引数は必ず１つ与えられるとして、エラー処理はしなくて良い）

```
> python3 arg.py hello
hello
> python3 arg.py 1
1
>
```

### ex04

|提出するファイル|使う関数等|
|----|----|
|if.py|print(), sys.args, int()|

コマンドライン引数がゼロだった場合に「`数字は0です`」、負だった場合に「`数字は負です`」、正だった場合に「`数字は正です`」と出力してください。
（ただし、コマンドライン引数は必ず１つ与えられるとして、エラー処理はしなくて良い）

```
> python3 if.py 1
数字は正です
>
```

### ex05

|提出するファイル|使う関数等|
|----|----|
|while.py|print()|

必要に応じて`str()`を使います。使いたくない場合は`print()`の引数に注目してみてください。
`while()`文を使用して、以下のような出力を得てください。

```
> python3 while.py
Hello 0
Hello 1
Hello 2
```

### ex06

|提出するファイル|使う関数等|
|----|----|
|for.py|print(), sys.args|

for文を使ってください。（ファイル名を除く）与えられた引数をすべて出力してください。

ヒント：自身のファイル名は`__file__`で確認できます！

```
> python3 for.py 1 2 3
1
2
3
> 
```

### ex07

|提出するファイル|使う関数等|
|----|----|
|put_sqare.py|print(), sys.args, str(), int()|

第1引数に与えられた文字列を第2引数分出力するのを第2引数分行出力します。
つまり、以下のような例です。

```
> python3 put_sqare.py "#" 2
##
##
> python3 put_sqare.py aa 2
aaaa
aaaa
```

（ただし、コマンドライン引数は必ず2つ与えられるとして、エラー処理はしなくて良い）
