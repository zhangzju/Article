好久没有技术贴的更新，随着备受关注的个人所得税法修正案草案19日提请十三届全国人大常委会第三次会议审议，我也来蹭一波热度，使用Python来写一个简单的小脚本计算一下当前的工资能够在新的个税起征点下多拿到多少钱。

这次税法修正案主要有四处调整：

1. 个税起征点提高，从原先的3500元提高至5000元；
2. 实行综合征税，工资薪金、劳务报酬、稿酬和特许权使用费四项劳动性所得首次实行综合征税；
3. 首次增加子女教育支出、继续教育支出、大病医疗支出、住房贷款利息和住房租金等专项附加扣除；
4. 优化调整税率结构，扩大较低档税率级距

对于我们小伙伴来说，最直观的应该就是个税起征点的变化了，由于税率并没有发生变化，因此我们交的税是变少了，对于已经很艰难的我们来说，算是一丢丢好处吧。

在上次的只制作头像的教程中，我们已经安装好了Python的执行环境，不再赘述了，首先看看我们要完成的程序需要干点什么：

1. 接受一个来自命令行的输入，输入的值是我们的月薪
2. 根据月薪计算起征点为3500和起征点为5000情况下的纳税总额
3. 将新旧起征点下的纳税总额相减，打印出我们多拿的几块钱

当我们编写好Python代码的文件之后，会在命令行中运行这个文件，而在运行文件的时候，我们可以附加一些参数，然后在代码中获取这些参数并处理，例如：
```javascript
python XXX.py 5000
```
其中的python是运行命令，XXX.py是我们需要运行的文件，而5000则是我们传递给程序的参数，不同于前面两个，参数是可以变的，这也就决定了我们可以改变参数来获得不同月薪的数据.如何在代码中获取到输入的参数呢？这部分的内容，科科，还是比较难以理解的，因为牵扯到模块的调用，建议还是直接拿来用就好了，代码如下：

```python
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <salary>".format(sys.argv[0]))
        sys.exit(1)

    salary = float(sys.argv[1])
    dec = tax_dec(salary)
    print("工资总额: {}, 多拿: {}".format(salary, dec))
```

然后我们需要计算纳税总额，尽管起征点变化，但是税率还是没有改变，目前的税率如下图：

这个图也很好理解，他把需要纳税的金额分成了很多个区间，处于1500以下的这部分薪酬需要按照0.03的比例来纳税，以此类推，所以我们需要有一个函数来实现一个这样的功能"输入需要纳税的金额，输出纳税总额"，这部分的代码如下：

```python
def tax_indeed(salary):
    if salary <= 1500:
        return salary * 0.03
    elif salary > 1500 and salary <= 4500:
        return 0.03*1500 + (salary-1500)*0.1
    elif salary > 4500 and salary <= 9000:
        return 0.03*1500 + 0.1*3000 + (salary-4500)*0.2
    elif salary > 9000 and salary <= 35000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + (salary-9000)*0.25
    elif salary > 35000 and salary <= 55000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + (salary-35000)*0.30
    elif salary > 55000 and salary <= 80000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + 0.30*20000 + (salary-55000)*0.35
    else:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + 0.30*20000 + 0.35*25000 + (salary-80000)*0.45
```

最后我们需要一个计算出在新旧的个税起征点下纳税总额相差多少的函数，这个比较简单，只需要我们将月薪传入函数，然后分别减去3500和5000的个税起征点，并且用上面已经完成的根据纳税金额计算出纳税额的函数进行运算即可，这部分的函数如下：

```python
def tax_dec(salary):
    former_tax = tax_indeed(salary-3500)
    latter_tax = tax_indeed(salary-5000)
    return former_tax-latter_tax
```

新建一个后缀为.py的文件，例如SelfTax.py，然后使用打开这个文件进行编辑，我们把已经完成的代码写入文件，不要忘记添加第一行的引入sys系统标准库的语句，所有的代码如下：

```python
import sys

def tax_indeed(salary):
    if salary <= 1500:
        return salary * 0.03
    elif salary > 1500 and salary <= 4500:
        return 0.03*1500 + (salary-1500)*0.1
    elif salary > 4500 and salary < 9000:
        return 0.03*1500 + 0.1*3000 + (salary-4500)*0.2
    elif salary > 9000 and salary < 35000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + (salary-9000)*0.25
    elif salary > 35000 and salary < 55000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + (salary-35000)*0.30
    elif salary > 55000 and salary < 80000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + 0.30*20000 + (salary-55000)*0.35
    else:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + 0.30*20000 + 0.35*25000 + (salary-80000)*0.45

def tax_dec(salary):
    former_tax = tax_indeed(salary-3500)
    latter_tax = tax_indeed(salary-5000)
    return former_tax-latter_tax


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <salary>".format(sys.argv[0]))
        sys.exit(1)

    salary = float(sys.argv[1])
    dec = tax_dec(salary)
    print("工资总额: {}, 多拿: {}".format(salary, dec))
```
