# <center>第五届空间语义理解评测（SpaCE2025）任务申请书</center>


- 任务组织者：詹卫东、穗志方（北京大学）
- 任务负责人/联系人：肖力铭 
- 联系方式：[lmxiao@stu.pku.edu.cn]()


> - <a href="#content">任务内容</a>
> - <a href="#data">评测数据</a>
>     - <a href="#ziduan">数据字段</a>
>     - <a href="#example">数据样例</a>
>     - <a href="#distribution">数据规模</a>
> - <a href="#eval">评价标准</a>
> - <a href="#time">评测赛程</a>
> - <a href="#award">奖项设置</a>
> - <a href="#otherinfo">其他信息</a>
> - <a href="#committee">评测委员会</a>

### <center>1.  <span id="content">任务内容</span></center>

#### 1.1  任务简介

空间表达描述了物体之间的空间方位关系，是自然语言中的高频现象。实现空间语义理解不仅依赖语言知识，还需要调用空间认知能力，准确构建文本表征的空间场景。空间语义理解评测（Spatial Cognition Evaluation，简称 SpaCE）以测试机器的空间语义理解水平为目标，自2021年开始连续举办了四届赛事1，发布了一系列评测任务，包括（1）空间信息正误判断；（2）空间信息异常识别；（3）空间参照实体识别；（4）空间语义角色识别；（5）空间异形同义判别；（6）空间方位关系推理，等等。大语言模型在SpaCE2024的评测结果显示，大语言模型的空间语义理解水平与普通人类的平均水平相比，在对空间认知加工要求较高的任务上，存在较大差距。空间语义理解对大语言模型来说仍然是一项挑战性任务。 
第五届空间语义理解评测（SpaCE2025）继续开展针对大语言模型的空间语义理解能力测试，关注大语言模型在以下任务上的表现： 

（1）空间信息正误判断。空间信息正确的文本可以构造出合乎常理的空间场景，而错误的文本不能，本任务要求机器判断文本的空间信息是否正确。 

（2）空间参照实体识别。确定实体方位依赖参照物，但文本中存在方位词前省略参照物的现象，本任务要求机器在这类文本中找出提供方位参照的实体。 

（3）空间异形同义判别。两个有方位词语差异的空间表达存在描述相同空间场景的可能，有异形同义和异形异义两种情况，本任务要求机器找出符合对应情况的词语对。 

（4）空间方位关系推理。给定一个空间场景和若干已知的实体间方位关系，本任务要求机器推理出实体在空间场景中的位置，以及未知的方位关系。 


#### 1.2  与SpaCE2024的比较

 SpaCE2025 与 SpaCE2024 相比，有以下变化和特色： 

（1）舍弃依赖语言形式标记作答的评测任务。根据SpaCE2024的评测结果，大语言模型在形式特征明显、形义对应关系简单的语义角色识别任务上已经达到了与人类相当的水平，但在需要调动认知能力进行深层语义理解的任务上，仍然有较大的提升空间。为了进一步了解大语言模型的空间认知能力，SpaCE2025专注于具有较高认知加工难度的评测任务。 

（2）提升评测数据的多样性和平衡性。为了更加全面、准确地评估大语言模型的空间语义理解能力，SpaCE2025覆盖了过去未曾考察的空间表达，并提升了数据规模，确保不同考察项目的题量分布更加均衡，力求使评测结果具有统计意义。 

（3）关注跨语言的空间语义理解能力。SpaCE2025在空间方位关系推理任务中提供中英文对照的评测数据，旨在考察大语言模型的空间语义理解能力是否具有语言相关性，同时探索语言能力与推理能力之间的关系。 

> 第一届中文空间语义理解评测（SpaCE2021）的相关资源：
> - Github仓库： https://github.com/2030NLP/SpaCE2021
> - 评测网站： http://ccl.pku.edu.cn:8084/SpaCE2021/
> 
> 第二届中文空间语义理解评测（SpaCE2022）的相关资源：
> - Github仓库： https://github.com/2030NLP/SpaCE2022
> - 评测网站： https://2030nlp.github.io/SpaCE2022/
> 
> 第三届中文空间语义理解评测（SpaCE2023）的相关资源：
> - Github仓库： https://github.com/2030NLP/SpaCE2023
> - 评测网站： https://2030nlp.github.io/SpaCE2023/
>
> 第四届中文空间语义理解评测（SpaCE2024）的相关资源：
> - Github仓库： https://github.com/2030NLP/SpaCE2024
> - 评测网站： https://2030nlp.github.io/SpaCE2024/


### <center>2.  <span id="data">评测数据</span></center>

#### 2.1  <span id="ziduan">数据字段</span>

（1）text：文本材料。字符串。机器需要阅读理解text后回答问题。 
    
（2）question：机器需要回答的问题。字符串。形式上是一个句中有括号的陈述句。 
    
（3）option：题目选项。字典，键-值对为“选项字母-选项内容”。最少有两个键-值对，最多有四个键-值对。选项字母为A、B、C、D。 
    
（4）answer：题目答案。数组，元素是选项字母。例如，["A"]表示机器选择option的A选项作为答案。测试集没有answer字段。 
    
（5）inference：空间方位关系推理题的参考推理过程。字符串。仅空间方位关系推理任务的微调集有inference字段。 


#### 2.2  <span id="example">数据样例</span>


##### 2.2.1  <span id="task1">空间信息正误判断</span>

```json
{
    text：孟某驾驶一辆未悬挂法定号牌的电动自行车从小区西门出发，后座载着同事何某。驶出西门后，孟某右转凉城路由南向北行驶至车站南路路口附近，随后右转进入车站南路。此时，谈某正驾驶电动自行车在前方同向骑行，孟某从右侧超越谈某的过程中，孟某的电动自行车右侧与谈某的电动自行车左侧发生碰擦，致谈某向右倒地。孟某加速往东逃逸，后被前方水电路路口的交警拦停抓获。 
    question：text 的空间信息(  )。 
    option：{A:正确, 
             B:错误} 
    answer：[B]
}
```

说明：

- 样例的文本存在异常的空间信息：“孟某从右侧超越谈某的过程中，孟某的电动自行车右侧与谈某的电动自行车左侧生碰擦”。根据空间方位常识可知，孟某如果从右侧超越谈某，只能是孟某的左侧与谈某的右侧发生碰擦，不可能孟某的右侧与谈某的左侧发生碰擦。所以文本的空间信息是错误的。
  
##### 2.2.2  <span id="task2">空间参照实体识别</span>


```json
{
    text：孟某驾驶一辆未悬挂法定号牌的电动自行车从小区西门出发，后座载着同事何某。驶出西门后，孟某右转沿凉城路由南向北行驶至车站南路路口附近，随后右转进入车站南路。此时，谈某正驾驶电动自行车在前方同向骑行，孟某从左侧超越谈某的过程中，孟某的电动自行车右侧与谈某的电动自行车左侧发生碰擦，致谈某向右倒地。孟某加速往东逃逸，后被前方水电路路口的交警拦停抓获。 
    question：“谈某正驾驶电动自行车在前方同向骑行”指的是“谈某正驾驶电动自行车在孟某前方同向骑行”。该陈述(  )。 
    option：{A:正确, 
             B:错误} 
    answer：[A] 
}
```
说明：

- 样例中，“谈某……在前方同向行驶”指的是谈某在孟某之前，而相应地，孟某则是在谈某的后方骑行。

##### 2.2.3  <span id="task3">空间异形同义判别</span>


```json
{
    text：晚上，桑桑在花园里循声捉蟋蟀，就听见荷塘边的草地上有笛子声，隔水看，白雀正在笛子声里做动作。今晚的月亮不耀眼，一副迷离恍惚的神气。桑桑看不清蒋一轮与白雀，但又分明看得清他们的影子。蒋一轮倚在柳树下，用的是让桑桑最着迷的姿势:两腿微微交叉着。白雀的动作在这样的月光笼罩下，显得格外的柔和。桑桑坐在塘边，呆呆地看着，捉住的几只蟋蟀从盒子里趁机逃跑了。 
    question：“蒋一轮倚在柳树下”中的“下”替换为(  )形成的新句可以与原句表达相同的空间场景。 
    option：{A:内, 
             B:中, 
             C:旁, 
             D:边} 
    answer：[C, D] 
}
```


说明：

- 样例中，把“下”替换为“旁”和“边”，形成的新句与原句都能描述蒋一轮在地面上且身体与树干接触的空间场景。

##### 2.2.4  <span id="task4">空间方位关系推理</span>

【中文样例】

```json
{
    text：赵志敬、谭处端、郝大通、孙不二、刘处玄、王处一六位道士在终南山重阳宫内盘腿席地打坐，围成一个圆圈，修炼内功，六人的位置恰好形成一个正六边形。六人都面朝外背对圆心而坐。任意相邻两人之间的间距相等，大约为一米。已知： 
    (1)王处一在谭处端右侧紧邻位置。 
    (2)郝大通在孙不二逆时针方向第三个位置。 
    (3)刘处玄与王处一正背对。 
    (4)赵志敬在孙不二右边数起第一个位置。 
    (5)从郝大通的左边数起第五个位置是谭处端。 
    question：刘处玄与(  )之间隔着其他实体。 
    option：{A:王处一, 
             B:郝大通, 
             C:孙不二, 
             D:赵志敬} 
    answer：[A, C] 
    inference： 
    因为王处一在谭处端右侧紧邻位置，所以谭处端的右边起第一个就是王处一。 
    因为谭处端的右边起第一个就是王处一，所以王处一在谭处端顺时针方向第一个位置。 
    因为从郝大通的左边数起第五个位置是谭处端，所以郝大通的右边起第一个就是谭处端。 
    因为郝大通的右边起第一个就是谭处端，所以谭处端在郝大通顺时针方向第一个位置。 
    因为郝大通在孙不二逆时针方向第三个位置，所以孙不二在郝大通顺时针方向第三个位置。 
    因为孙不二在郝大通顺时针方向第三个位置，所以孙不二在谭处端顺时针方向第二个位置。 
    因为孙不二在谭处端顺时针方向第二个位置，所以孙不二在王处一顺时针方向第一个位置。 
    因为赵志敬在孙不二右边数起第一个位置，所以赵志敬在孙不二顺时针方向第一个位置。 
    因为刘处玄与王处一正背对，所以刘处玄在王处一顺时针方向第三个位置。 
    因为刘处玄在王处一顺时针方向第三个位置，所以刘处玄在孙不二顺时针方向第二个位置。 
    因为刘处玄在孙不二顺时针方向第二个位置，所以刘处玄在赵志敬顺时针方向第一个位置。 
    因为王处一在谭处端顺时针方向第一个位置，所以刘处玄在谭处端顺时针方向第四个位置。 
    因为谭处端在郝大通顺时针方向第一个位置，所以刘处玄在郝大通顺时针方向第五个位置。 
    因为刘处玄在郝大通顺时针方向第五个位置，所以刘处玄在郝大通逆时针方向第一个位置。 
    因此，刘处玄与王处一之间隔着其他实体，刘处玄与谭处端之间隔着其他实体，刘处玄与
    孙不二之间隔着其他实体。
}
```

【英文样例】

```json
{
    text：Six Taoist priests——Michael, Mary, Jennifer, William, John, Robert——are sitting cross-legged on the ground inside the Chongyang Palace on Zhongnan Mountain, forming a circle as they practice internal martial arts. The positions of the six individuals form a perfect hexagon. Each person is facing outward, with their backs to the center of the circle. The distance between any two adjacent individuals is equal, approximately one meter. It is known that: 
    (1)Mary is directly to the right of Robert. 
    (2)Jennifer is in the third position counterclockwise from William. 
    (3)John and Robert are back-to-back. 
    (4)Michael occupies the first position to the right of William. 
    (5)Mary occupies the fifth position to the left of Jennifer. 
    question：There are other entities between John and (). 
    option：{A:Robert, 
             B:Jennifer, 
             C:William, 
             D:Michael} 
    answer：[A, C] 
    inference： 
    Because Robert is directly to the right of Mary, Robert is the first to the right of Mary. 
    Because Robert is the first to the right of Mary, Robert is in the first position clockwise from Mary. 
    Because Mary occupies the fifth position to the left of Jennifer, Mary is the first to the right of Jennifer. 
    Because Mary is the first to the right of Jennifer, Mary is in the first position clockwise from Jennifer. 
    Because Jennifer is in the third position counterclockwise from William, William is in the third position clockwise from Jennifer. 
    Because William is in the third position clockwise from Jennifer, William is in the second position clockwise from Mary. 
    Because William is in the second position clockwise from Mary, William is in the first position clockwise from Robert. 
    Because Michael occupies the first position to the right of William, Michael is in the first position clockwise from William. 
    Because John and Robert are back-to-back, John is in the third position clockwise from Robert. 
    Because John is in the third position clockwise from Robert, John is in the second position clockwise from William. 
    Because John is in the second position clockwise from William, John is in the first position clockwise from Michael. 
    Because Robert is in the first position clockwise from Mary, John is in the fourth position clockwise from Mary. 
    Because Mary is in the first position clockwise from Jennifer, John is in the fifth position clockwise from Jennifer. 
    Because John is in the fifth position clockwise from Jennifer, John is in the first position counterclockwise from Jennifer. 
    Therefore, there are other entities between John and Robert, between John and Mary, and between John and William.
}
```

说明：

- 中文样例和英文样例是对应关系，除了实体的名称不同，空间场景以及已知条件均相同。文本描绘了一个正六边形的围坐场景，六个实体以背对中心的状态位于正六边形的顶点。根据文本给出的已知条件，可以推理出每个实体的位置，可知刘处玄与郝大通和赵志敬相邻、John 与 Jennifer 和 Michael 相邻。由此可知，刘处玄、John 与其他三个实体之间隔着实体。

#### 2.3  <span id="distribution">数据概况</span>

总题量约13,000 题。空间信息正误判断、空间参照实体识别、空间异形同义判别任务划分示例集和测试集，示例集各提供约50条代表性数据，测试集各约800题。空间方位关系推理划分微调集、验证集和测试集，微调集提供约3,000条带推理过程的数据，验证集约1000 题，测试集约6000题。 

空间信息正误判断、空间参照实体识别、空间异形同义判别任务在多种不同类型的真实语料上进行改写工作，包括：报刊语料、文学作品语料、中小学课本语料、交通事故描述文本、人体动作文本、地理百科文本。空间方位关系推理任务则是运用基于知识库的数据合成方法生成的高质量合成数据。 

测试集中设置约3%的干扰题，不计入比赛成绩，仅用于衡量大语言模型的稳定性。干扰题是在比赛题上进行复制或形式扰动形成的题目，扰动前后答案不变，包括直接复制题目、改变选项顺序、改变问题括号的位置等操作。“稳定”的意思是大语言模型在比赛题及其对应的干扰题上都给出了一致的答案。     

### <center>3.  <span id="eval">评价标准</span></center>
SpaCE2025 使用准确率（Accuracy，Acc）作为评价指标和排名依据，公式如下：
```python
Acc = 命中正确答案的题数 / 题目总数
```

稳定性用于衡量机器表现的稳定程度，不作为排名依据。以比赛题及其对应的干扰题为一组，公式如下：
```python
稳定性 = 组内答案完全一致的组数 / 总组数
```



### <center>4.  <span id="time">评测赛程</span></center>
目前拟定的赛程安排如下：
<table class="table table-bordered">
<thead>
<tr>
<th>时间</th>
<th>事项</th>
</tr>
</thead>
<tbody>
<tr>
<td>2月20日~4月15日</td>
<td>开放报名</td>
</tr>
<tr>
<td>3月1日</td>
<td>发布训练集</td>
</tr>
<tr>
<td>4月15日</td>
<td>发布验证集和测试集，开放结果提交</td>
</tr>
<tr>
<td>5月15日</td>
<td>测试结果提交截止</td>
</tr>
<tr>
<td>5月21日</td>
<td>参赛模型提交截止</td>
</tr>
<tr>
<td>5月30日</td>
<td>评测论文初稿提交截止</td>
</tr>
<tr>
<td>5月31日</td>
<td>公布最终排名和获奖名单</td>
</tr>
<tr>
<td>6月15日</td>
<td>评测论文终稿提交截止</td>
</tr>
<tr>
<td>6月20日</td>
<td>评测论文录用通知</td>
</tr>
<tr>
<td>8月</td>
<td>评测研讨会</td>
</tr>
</tbody></table>


### <center>5.  <span id="award">奖项设置</span></center>

评测奖金由华为公司赞助。本次评测将评选出如下奖项：

一等奖拟定 0-1名 ，奖金待定。

二等奖拟定 0-2名 ，奖金待定。

三等奖拟定 0-4名 ，奖金待定。

由中国中文信息学会为本次评测获奖队伍提供荣誉证书。

### <center>6.  <span id="otherinfo">其他信息</span></center>
本次评测的官方网址、报名方式等信息将在评测发布时一同公布。

### <center>7.  <span id="committee">评测委员会</span></center>
单位：北京大学 

主席：詹卫东、穗志方 

工作人员：肖力铭，胡楠，秦宇航，邓思锐，崔香，蔡奇栩，姜秀旻，丁锦坤，张子涵，王希豪，孙春晖，邢丹，杨奕欣，马敬原，李政，王悦
