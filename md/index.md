# <center>第五届空间语义理解评测任务（SpaCE2025）</center>

**[<center>👉 <font style=color:rgb(226,76,71)>点我立即报名</font> 👈</center>](https://docs.qq.com/form/page/DSWpBdE9FUWFOUkZa)**

- 组织者/主席：詹卫东、穗志方
- 工作人员：肖力铭，胡楠，秦宇航，邓思锐，崔香，蔡奇栩，姜秀旻，丁锦坤，张子涵，王希豪，孙春晖，邢丹，杨奕欣，马敬原，李政，王悦
- 主办单位：北京大学 
- 联系方式：[lmxiao@stu.pku.edu.cn]()


> - <a href="#content">任务内容</a>
> - <a href="#data">评测数据</a>
>     - <a href="#ziduan">数据字段</a>
>     - <a href="#example">数据样例</a>
>     - <a href="#distribution">数据概况</a>
> - <a href="#eval">评价标准</a>
> - <a href="#time">评测赛程</a>
> - <a href="#award">奖项设置</a>
> - <a href="#otherinfo">其他信息</a>
> - <a href="#rules">赛事规则</a>

### <center>1.  <span id="content">任务内容</span></center>

#### 1.1  任务简介

空间表达描述了物体之间的空间方位关系，是自然语言中的高频现象。实现空间语义理解不仅依赖语言知识，还需要调用空间认知能力，准确构建文本表征的空间场景。空间语义理解评测（Spatial Cognition Evaluation，简称 SpaCE）以测试机器的空间语义理解水平为目标，自2021年开始连续举办了四届赛事1，发布了一系列评测任务，包括（1）空间信息正误判断；（2）空间信息异常识别；（3）空间参照实体识别；（4）空间语义角色识别；（5）空间异形同义判别；（6）空间方位关系推理，等等。大语言模型在SpaCE2024的评测结果显示，大语言模型的空间语义理解水平与普通人类的平均水平相比，在对空间认知加工要求较高的任务上，存在较大差距。空间语义理解对大语言模型来说仍然是一项挑战性任务。 

第五届空间语义理解评测（SpaCE2025）继续开展针对大语言模型的空间语义理解能力测试，关注大语言模型的空间语言能力和空间推理能力。

- **空间语言能力类评测任务**，包括三个子任务：

（1）空间信息正误判断。判断题。空间信息正确的文本可以构造出合乎常理的空间场景，而错误的文本不能，本任务要求机器判断文本的空间信息是否正确。回答“正确”或“错误”。

（2）空间参照实体判断。判断题。确定实体方位依赖参照物，但文本中存在方位词前省略参照物的现象，本任务给出可能在句子中充当参照物的实体，要求机器判断该实体是否是正确的参照物。回答“正确”或“错误”。

（3）空间异形同义判断。判断题。两个有方位词语差异的空间表达存在描述相同空间场景的可能，有异形同义和异形异义两种情况，本任务要求机器判断两个文本描述的空间场景是相同还是不同。回答“相同”或“不同”。

- **空间推理能力类评测任务**，包括两个子任务：

（1）中文空间方位关系推理。选择题。给定一个空间场景和若干已知的实体间方位关系，本任务要求机器在中文文本中推理出实体在空间场景中的位置，以及未知的方位关系。

（2）英文空间方位关系推理。选择题。与中文推理文本对照的英文文本，要求机器在英文文本中推理出实体在空间场景中的位置，以及未知的方位关系。


#### 1.2  与SpaCE2024的比较

 SpaCE2025 与 SpaCE2024 相比，有以下变化和特色： 

（1）舍弃依赖语言形式标记作答的评测任务。根据SpaCE2024的评测结果，大语言模型在形式特征明显、形义对应关系简单的语义角色识别任务上已经达到了与人类相当的水平，但在需要调动认知能力进行深层语义理解的任务上，仍然有较大的提升空间。为了进一步了解大语言模型的空间认知能力，SpaCE2025专注于具有较高认知加工难度的评测任务。 

（2）提升评测数据的多样性和平衡性。为了更加全面、准确地评估大语言模型的空间语义理解能力，SpaCE2025覆盖了过去未曾考察的空间表达，并提升了数据规模，确保不同考察项目的题量分布更加均衡，力求使评测结果具有统计意义。 

（3）关注跨语言的空间推理能力。SpaCE2025在空间方位关系推理任务中提供中英文对照的评测数据，旨在考察大语言模型的空间推理能力是否具有语言相关性，同时探索语言能力与推理能力之间的关系。 

> 第一届中文空间语义理解评测（SpaCE2021）
> - 评测网站： http://ccl.pku.edu.cn:8084/SpaCE2021/
> 
> 第二届中文空间语义理解评测（SpaCE2022）
> - 评测网站： https://2030nlp.github.io/SpaCE2022/
> 
> 第三届中文空间语义理解评测（SpaCE2023）
> - 评测网站： https://2030nlp.github.io/SpaCE2023/
>
> 第四届中文空间语义理解评测（SpaCE2024）
> - 评测网站： https://2030nlp.github.io/SpaCE2024/


### <center>2.  <span id="data">评测数据</span></center>

#### 2.1  <span id="task1">空间信息正误判断</span>

##### 2.1.1  <span id="ziduan">数据字段</span>

id：题目编号。每道题目都有唯一的编号，形如“jsi-数据集-数字”。jsi为任务英文judging spatial information的缩写，demo和test分别代表示例集和测试集。

instruction：说明考题目标的引导语。仅供参考，参赛队伍可自行设计提示词。

text：包含空间语言表达的文本材料。

interpretation：空间信息正误判断结果的释义文本。仅供参赛队伍参考。测试集没有此字段。

answer：对text的空间信息是否正确的判断结果。取值为“正确”或“错误”。

##### 2.1.2  <span id="ziduan">数据样例</span>

```json
{
    id: jsi-demo-1
    instruction: 判断text的空间语言表达是否正确。请只回答“正确”或“错误”。
    text: 碰撞发生后，“VANMANILA”轮船长迅速跑去驾驶台左侧外部的桥翼查看情况，当班三副杰哈尔跟在后面看见“XIANGZHOU”轮甲板以下已没入水上，就迅速跑回驾驶台发布全船广播，船长回驾驶室见其在进行减速操作，下令恢复原速继续航行。
    interpretation: 文本存在异常的空间表达：【没入水上】。“没入”指在水面之下，即水中，与“水上”矛盾。
    answer: 错误
}
```

#### 2.2  <span id="task2">空间参照实体判断</span>

##### 2.2.1  <span id="ziduan">数据字段</span>

id：题目编号。每道题目都有唯一的编号，形如“rsr-数据集-数字”。rsr为任务英文retrieving spatial referents的缩写，demo和test分别代表示例集和测试集。

instruction：说明考题目标的引导语。仅供参考，参赛队伍可自行设计提示词。

text：包含参照缺失句的文本材料。

interpretation：取text中的一个实体作为可能的参照物来解释方位参照的文本

answer：对interpretation是否正确的判断结果。取值为“正确”或“错误”。

##### 2.2.2  <span id="ziduan">数据样例</span>

```json
{
    id: rsr-demo-1
    instruction: 判断interpretation是否正确。请只回答“正确”或“错误”。
    text: 李国秀熟练地用左脚夹起水瓢，从桶里舀起水，开始浇灌院子里的盆栽。不远处，丈夫张顺东单手拿着手机，跟在妻子后面，聚精会神地录制视频。一旁的昆明市东川区电子商务公共服务中心负责人陆金云小声指导：“可以绕到侧面，拍个浇花的特写。”
    interpretation: “可以绕到侧面”是以“李国秀”为基准，确定“侧面”所指的具体方位。
    answer: 正确
}
```

#### 2.3  <span id="task3">空间异形同义判断</span>

##### 2.3.1  <span id="ziduan">数据字段</span>

id：题目编号。每道题目都有唯一的编号，形如“rse-数据集-数字”。rse为任务英文recognizing synonymous expression的缩写，demo和test分别代表示例集和测试集。

instruction：说明考题目标的引导语。仅供参考，参赛队伍可自行设计提示词。

text1：与text2形成对照的文本材料。

text2：与text1形成对照的文本材料。

interpretation：空间异形同义判断结果的释义文本。仅供参赛队伍参考。测试集没有此字段。

answer：对text1和text2描述的空间场景是否相同的判断结果。取值为“相同”或“不同”。

##### 2.3.2  <span id="ziduan">数据样例</span>

```json
{
    id: rse-demo-3
    instruction: 判断text1和text2描述的空间场景是否相同。请只回答“相同”或“不同”。
    text1: 他穿街过巷，来到段公馆的后花园外，只听从高墙后飘出一阵笙、管、笛、萧的乐声和缠绵柔婉的《长生殿》歌声。
    text2: 他穿街过巷，来到段公馆的后花园外，只听从高墙里飘出一阵笙、管、笛、萧的乐声和缠绵柔婉的《长生殿》歌声。
    interpretation: 两个文本的形式差异部分是“从高墙后飘出一阵笙、管、笛、萧的乐声和缠绵柔婉的《长生殿》歌声”和“从高墙里飘出一阵笙、管、笛、萧的乐声和缠绵柔婉的《长生殿》歌声”。在“从高墙后飘出一阵笙、管、笛、萧的乐声和缠绵柔婉的《长生殿》歌声”中，歌声来自于被高墙遮挡的位置；在“从高墙里飘出一阵笙、管、笛、萧的乐声和缠绵柔婉的《长生殿》歌声”中，歌声来自于被高墙围起来的位置，这个位置被高墙遮挡。因此，两个句子都可以表示歌声来自于被高墙遮挡的位置的空间场景，text1和text2描述的空间场景相同。答案：【相同】。
    answer: 相同
}
```

#### 2.4  <span id="task4">中文空间方位关系推理</span>

##### 2.4.1  <span id="ziduan">数据字段</span>

id：题目编号。每道题目都有唯一的编号，形如“spr-zh-数据集-数字”。spr为任务英文spatial position reasoning的缩写，train, dev, test分别代表训练集, 验证集和测试集。

instruction：说明考题目标的引导语。通过引导语可区分单选题（一个正确答案）和多选题（两个或两个以上正确答案）。仅供参考，参赛队伍可自行设计提示词。

text：包含情景描述和已知条件的文本材料。

question：机器需要回答的推理问题。形式上是一个句中有括号的陈述句。 
    
options：题目选项。字典，键-值对为“选项字母-选项内容”，有四个键-值对。选项字母为A、B、C、D。 
    
answer：推理问题的答案。数组，元素是选项字母。例如，["A"]表示机器选择option的A选项作为答案。测试集没有此字段。

##### 2.4.2  <span id="ziduan">数据样例</span>

```json
{
    id: spr-zh-train-0
    instruction: 题目是多选题，有两个或两个以上的正确答案。答案选项必须与标准答案完全一致才能得分。请逐步思考，并最终输出答案选项。
    text: 赵志敬、谭处端、郝大通、孙不二、刘处玄、王处一六位道士在终南山重阳宫内盘腿席地打坐，围成一个圆圈，修炼内功，六人的位置恰好形成一个正六边形。六人都面朝外背对圆心而坐。任意相邻两人之间的间距相等，大约为一米。已知： 
    (1)王处一在谭处端右侧紧邻位置； 
    (2)郝大通在孙不二逆时针方向第三个位置； 
    (3)刘处玄与王处一正背对；
    (4)赵志敬在孙不二右边数起第一个位置； 
    (5)从郝大通的左边数起第五个位置是谭处端。
    question: 刘处玄与()之间隔着其他实体。
    options: {A:王处一, 
             B:郝大通, 
             C:孙不二, 
             D:赵志敬} 
    answer: [A, C]
}
```

说明：

- 文本描绘了一个正六边形的围坐场景，六个实体以背对中心的状态位于正六边形的顶点。根据文本给出的已知条件，可以推理出每个实体的位置，可知：刘处玄与郝大通和赵志敬相邻。因此，刘处玄与其他三个实体之间隔着实体。


#### 2.5  <span id="task5">英文空间方位关系推理</span>

##### 2.5.1  <span id="ziduan">数据字段</span>

id：题目编号。每道题目都有唯一的编号，形如“spr-en-数据集-数字”。spr为任务英文spatial position reasoning的缩写，train, dev, test分别代表训练集, 验证集和测试集。

instruction：说明考题目标的引导语。通过引导语可区分单选题（一个正确答案）和多选题（两个或两个以上正确答案）。仅供参考，参赛队伍可自行设计提示词。

text：包含情景描述和已知条件的文本材料。

question：机器需要回答的推理问题。形式上是一个句中有括号的陈述句。 
    
options：题目选项。字典，键-值对为“选项字母-选项内容”，有四个键-值对。选项字母为A、B、C、D。 
    
answer：推理问题的答案。数组，元素是选项字母。例如，["A"]表示机器选择option的A选项作为答案。测试集没有此字段。

##### 2.5.2  <span id="ziduan">数据样例</span>

```json
{
    id: spr-en-train-0
    instruction：The question is multiple-choice with more than one correct answers. Answer choices must exactly match the gold answer to be considered correct. Please think step by step and finally output the answer choices.
    text：Michael, Mary, Jennifer, William, John, Robert, ——these six Taoist priests are seated cross-legged on the ground inside the Chongyang Palace on Zhongnan Mountain, arranged in a circle as they practice internal martial arts. The positions of the six priests form a perfect hexagon. Each person is facing outward, with their backs to the center of the circle. The distance between any two adjacent priests is equal, approximately one meter. It is known that: 
    (1)Mary is directly to the right of Robert;
    (2)Jennifer is in the third position counterclockwise from William; 
    (3)John and Robert are back-to-back;
    (4)Michael occupies the first position to the right of William;
    (5)Mary occupies the fifth position to the left of Jennifer. 
    question：There are other people between John and (). 
    option：{A:Robert, 
             B:Jennifer, 
             C:William, 
             D:Michael} 
    answer：[A, C]
}
```

说明：

- 英文例题和中文例题是对应关系，除了实体的名称不同，空间场景以及已知条件均相同。根据文本给出的已知条件，可以推理出每个实体的位置，可知：John 与 Jennifer 和 Michael 相邻。因此，John 与其他三个实体之间隔着实体。

#### 2.6  <span id="distribution">数据概况</span>

总题量约 10,000 题。空间信息正误判断、空间参照实体判断、空间异形同义判断任务划分示例集和测试集，示例集各提供约 20 条高质量代表性数据，测试集各约 1,000 题。空间方位关系推理划分训练集、验证集和测试集，训练集提供 2,000 条数据，验证集 500 题，测试集 3,500 题。 

空间信息正误判断、空间参照实体判断、空间异形同义判断任务在多种不同类型的真实语料上进行改写工作，包括：报刊语料、文学作品语料、中小学课本语料、交通事故描述文本、人体动作文本、地理百科文本。空间方位关系推理任务则是运用基于知识库的数据合成方法生成的高质量合成数据。    

### <center>3.  <span id="eval">评价标准</span></center>
参赛队伍的排名依据为两大类任务的综合得分 S ，S1 代表空间语言能力类评测任务的得分，S2 代表空间推理能力类评测任务的得分，Acc<sub>i</sub> 代表各子任务的准确率（Accuracy，Acc）。公式如下：

![](images/score.png)

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
<td>2月20日~3月31日</td>
<td>开放报名</td>
</tr>
<tr>
<td>3月26日</td>
<td>发布示例集</td>
</tr>
<tr>
<td>3月31日</td>
<td>发布训练集、验证集和测试集，开放结果提交</td>
</tr>
<tr>
<td>5月11日</td>
<td>测试结果提交截止</td>
</tr>
<tr>
<td>5月15日</td>
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

一等奖拟定 0-1名 ，奖金池共 12,000。

二等奖拟定 0-2名 ，奖金池共 12,000。

三等奖拟定 0-4名 ，奖金池共 12,000。

由中国中文信息学会为本次评测获奖队伍提供荣誉证书。

### <center>6.  <span id="otherinfo">报名方式</span></center>

请仔细阅读《[第五届空间语义理解评测 SpaCE2025 参赛协议](https://github.com/PKU-SpaCE/SpaCE2025/tree/main/agreements/Agreement.md)》和《[第五届空间语义理解评测 SpaCE2025 数据集使用许可](https://github.com/PKU-SpaCE/SpaCE2025/tree/main/agreements/LICENSE.md)》，然后点击进入 [报名链接](https://docs.qq.com/form/page/DSWpBdE9FUWFOUkZa)

### <center>7.  <span id="rules">赛事规则</span></center>

一、参赛模型要求：

（1）空间语言能力类评测任务（3个子任务）：可通过设计提示词或微调的方式基于**参数量不大于7B的大语言模型**参赛。

（2）空间推理能力类评测任务（2个子任务）：**必须通过微调[DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)的方式参赛**。

二、以下行为将**取消获奖资格**：

（1）在模型训练、微调阶段使用验证集或测试集的数据。例如，用测试集生成伪标签数据进行数据增强；

（2）将验证集或测试集的数据作为提示词示例使用；

（3）测试集提交结果为人工作答结果；

（4）使用SpaCE2025以外的其他数据集；

（5）参赛模型不符合要求；

（6）最终成绩无法复现。

三、请将所有子任务的提交结果放于一个文件中。文件规定为jsonl格式，每行一个json对象，每个json对象至少包括id字段和answer字段。

四、参赛队伍每日最多可提交3次测试集结果，最终成绩取所有提交结果中的最高得分。主办方将实时返回每次提交的得分，并每日更新一次排行榜。提交通道关闭后再提交的结果不计入排名。

五、参赛队伍须向主办方提交可复现的模型、代码和提示词。鉴于大语言模型输出的不稳定性，复现结果允许在2%以内浮动。

六、最终解释权归主办方所有。
