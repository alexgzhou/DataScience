

# 关于两百行实现的超简单区块链
## 区块结构（block structure）
这里使用了最简单的区块结构，即只由最必须的内容构成：区块高度，区块内的数据，区块哈希，前一个区块的哈希，时间戳；
## 区块哈希
区块需要其哈希值来保证数据的完整性，这里使用了SHA-256 函数  
具体是对区块号+上一区块的哈希值+时间戳+数据进行哈希计算得出的
## 区块确认
为了确认一个区块我们必须知道上一个区块的哈希值，然后创造剩下的所需内容，区块数据是由终端用户提供的
## 区块储存
一个内存中的js数组被用来储存区块链，第一个区块也就是创世区块，是被硬件写入的
## 验证区块完整性
这里做了几个判断
1. 区块编号的校验
2. 验证上一区块的哈希
3. 验证新区块的哈希校验
## 选择最长链
同样的这里也是通过几个简单的判断来操作的
1. 新的区块链有效并且长度大于当前的区块链
2. 使用新的区块链替换当前的区块链
3. 广播新的区块链
## 节点之间的沟通
利用node.js使得每一个节点都建立一个网页服务器，而其它节点访问该服务器可以提出一些特定的指令来获得
# 对于文章这一部分的总结
1. 这里提供了一个非常简单的区块链的构成，是由一些简单的函数和类实现的，而区块链本身就是一个区块变量的数组。
2. 关于更多的工作量证明算法；交易；以及钱包这里都没有提及，但在之后的文章中还有更详细的内容。
# 对目前工作的总结
1. 本周细细的读了一遍node.js 开发加密货币，由于很多内容已经变得非常复杂了所以理解起来略困难
2. 读了200行开发一个非常简单的区块链，将该文章的源代码读懂了并整理清楚了，并阅读了后续文章
3. 花了一天的时间看JavaScript和node.js 还没看完。
# 对接下来工作的安排
1. 熟悉JavaScript与node.js并按照上文提到的200行开发区块链实现并建立一份中文开发文档
2. 按照200行教程的后续即在typescript中实现工作量证明算法；交易；钱包；交易池。理解使用typescript的原因，是否重写或者照搬先实现并制作一份中文开发文档。
3. 在下周二之前争取实现一个较为基础的新型“比特币”，能够实现基本的生成新的区块链，创建交易钱包，交易，挖矿功能并且对其中各部分实现与修改较为熟练。
4. 如果还有时间那么去亿书币的源码中查看dpos机制的实现代码并尝试注释重现或者重写。

# 关于200行教程后续文章的概述
在定义的类中逐渐加入新的函数，新的变量或者加入新的类来实现挖矿、工作量难度证明、交易脚本、钱包实现等功能，钱包的交互界面也大多数是基于网页端。关于这些内容未来基本上会保持每日翻译实现注释的进度进行更新。