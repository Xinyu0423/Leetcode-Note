# Resume Question

## SQL
1. 选择--Select
   1. 表连接--想要的数据在多张表里，想取多个字段
   ```
    -- table_1中有id,age; table_2中有id，sex。想取出id,age,sex 三列信息
    -- 将table_1,table_2 根据主键id连接起来
    select a.id,a.age,b.sex from 
    (select id,age from table_1) a --将select之后的内容存为临时表a
    join 
    (select id, sex from table_2) b --将select之后的内容存为临时表b
    on a.id =b.id
   ```
2. 表连接--Join,Left join, right join, union
   1. join : hive的join默认是inner join，找出左右都可匹配的记录；
   2. left join: 左连接，以左表为准，逐条去右表找可匹配字段，如果有多条会逐次列出，如果没有找到则是NULL；
   3. right join：右连接，以右表为准，逐条去左表找可匹配字段，如果有多条会逐次列出，如果没有找到则是NULL；
   4. full outer join: 全连接，包含两个表的连接结果，如果左表缺失或者右表缺失的数据会填充NULL。
   5. 每种join 都有on , on的是左表和右表中都有的字段。join 之前要确保关联键是否去重，是不是刻意保留非去重结果。


3. 去重--distinct
4. 聚合函数和group by
   1. 聚合函数帮助我们进行基本的数据统计，例如计算最大值、最小值、平均值、总数、求和
5. 筛选--having, where
6. 聚合--max, min, sum, count+group by
7. 排序--order by, sort by
8. 条件--case when...end
9.  字符串--substr, concat, split
10. 日期函数--to_date, datediff
11. 分组排序--row_number()
    1.  分组排序 
    2.  rank(), dense_rank()。
    3.  rank()排序相同时会重复，总数不会变 ，意思是会出现1、1、3这样的排序结果；
    4.  dense_rank() 排序相同时会重复，总数会减少，意思是会出现1、1、2这样的排序结果。
    5. row_number() 则在排序相同时不重复，会根据顺序排序。  
12. 取百分比--percentile

Reference: https://zhuanlan.zhihu.com/p/61805956

## Bert
1. 整体架构
   1. 基础架构-tranformer的encoder
      1. Encode可以分为3个部分，输入部分，注意力机制，前馈神经网络
      2. Bert使用多个encoder堆叠在一起，bert base使用12层，bert launch使用24层encoder
      3. 6个encoder堆叠形成编码端，6个decoder堆叠形成解码端
      4. word embedding使用随机初始化或者word_to_vertex
      5. position encoding中使用token embedding+segement emb+position emb
2. Bert输入部分
   1. NSP(next sentence prediction)二分类任务，处理两个句子之间的关系
   2. Token Embedding进行随机初始化
   3. Segment Embedding区分两个/多个句子
   4. Position Embedding使用随机初始化后由模型去学习出来
   5. Transform中使用的是正余弦函数
3. 如何做预训练: MLM(mask language model)+NSP
   1. bert在预训练时使用的是大量的无标注的语料（无监督模型）
   2. 对于无监督，有两种目标函数
      1. AR(autoregressive)
         1. 自回归模型，只能考虑单侧的信息，比如GPT
      2. AE(Autoencoding)
         1. 自编码模型：从损坏的输入数据中预测重建原始数据，Bert使用的就是AE模型
         2. Mask的概率问题
            1. 随机mast15%的单词
               1. 10%替换成其他
               2. 10%原封不动
               3. 80%替换成mask
   3. NSP任务
      1. NSP训练样本
         1. 从训练语料库中抽取两个连续的段落作为正样本
         2. 从不同的文档中随机创建一对段位作为负样本
         3. 缺点：主题预测和连贯性预测合并成单项任务
4. 如何提升Bert下游任务的表现
   1. 在大量通用语料中训练一个language model（一般用已经训练好的）
   2. 在相同领域继续训练LM(Domain transfer)
      1. 使用动态mask：每次epoch去训练的时候使用mask，而不是一直使用同一个
   3. 在任务相关的小数据上继续训练LM（task transfer）
   4. 在任务相关数据上做具体任务（fine-tune）
   5. Batch size：16，32
   6. Learning rate：尽量小一点避免灾难性遗忘
   7. Number of epochs：3，4
5. 脱敏数据中如何使用Bert
   1. 如果数据很大，可以直接训练一个新的bert
   2. 数据很小，会导致欠拟合
   3. 

## Machine Learning
1. 朴素贝叶斯
   1. 公式: P(B|A)=P(A|B)P(B)/P(A)
   2. 朴素贝叶斯采用 属性条件独立性 的假设。
   3. 优点:计算复杂度小，时间空间开销小
   4. 缺点：前提假设限制性太强，分类任务中的各个特征很少满足。
2. 决策树(Reference:https://blog.csdn.net/Datawhale/article/details/102878758)
   1. 1.决策树和条件概率分布的关系？
      1. 决策树可以表示成给定条件下类的条件概率分布. 决策树中的每一条路径都对应是划分的一个条件概率分布. 每一个叶子节点都是通过多个条件之后的划分空间，在叶子节点中计算每个类的条件概率，必然会倾向于某一个类，即这个类的概率最大.
   2. 决策树怎么剪枝？
      1. 一般算法在构造决策树的都是尽可能的细分，直到数据不可划分才会到达叶子节点，停止划分. 因为给训练数据巨大的信任，这种形式形式很容易造成过拟合，为了防止过拟合需要进行决策树剪枝. 一般分为预剪枝和后剪枝，预剪枝是在决策树的构建过程中加入限制，比如控制叶子节点最少的样本个数，提前停止. 后剪枝是在决策树构建完成之后，根据加上正则项的结构风险最小化自下向上进行的剪枝操作. 剪枝的目的就是防止过拟合，是模型在测试数据上变现良好，更加鲁棒.
   3. 决策树的优点？
      1. 优点: 决策树模型可读性好，具有描述性，有助于人工分析；效率高，决策树只需要一次性构建，反复使用，每一次预测的最大计算次数不超过决策树的深度。
      2. 缺点: 对中间值的缺失敏感；可能产生过度匹配的问题，即过拟合。
3. 随机森林(Reference:https://blog.csdn.net/Heitao5200/article/details/103758643)
   1. 多次随机取样，多次随机取属性，选取最优分割点，构建多个(CART)分类器，投票表决
   2. 随机森林的随机性体现在哪里？
      1. 多次有放回的随机取样，多次随机取属性
   3. 随机森林为什么不容易过拟合？
      1. 随机森林中的每一颗树都是过拟合的，拟合到非常小的细节上
      2. 随机森林通过引入随机性，使每一颗树拟合的细节不同
      3. 所有树组合在一起，过拟合的部分就会自动被消除掉。
   4. 随机森林的优缺点
      1. 优点
         1. 训练可以高度并行化，对于大数据时代的大样本训练速度有优势。个人觉得这是的最主要的优点。
         2. 由于可以随机选择决策树节点划分特征，这样在样本特征维度很高的时候，仍然能高效的训练模型。
         3. 在训练后，可以给出各个特征对于输出的重要性
         4. 由于采用了随机采样，训练出的模型的方差小，泛化能力强。
         5. 相对于Boosting系列的Adaboost和GBDT， RF实现比较简单。
         6. 对部分特征缺失不敏感。
      2. 缺点
         1. 在某些噪音比较大的样本集上，RF模型容易陷入过拟合。
         2. 取值划分比较多的特征容易对RF的决策产生更大的影响，从而影响拟合的模型的效果。
5. 逻辑回归(Reference：https://zhuanlan.zhihu.com/p/34670728)
   1. 怎么防止过拟合？
      1. 通过正则化方法。正则化方法是指在进行目标函数或代价函数优化时，在目标函数或代价函数后面加上一个正则项，一般有L1正则与L2正则等。
   2. 为什么正则化可以防止过拟合？
      1. 过拟合表现在训练数据上的误差非常小，而在测试数据上误差反而增大。其原因一般是模型过于复杂，过分得去拟合数据的噪声。正则化则是对模型参数添加先验，使得模型复杂度较小，对于噪声扰动相对较小。
   3. L1正则和L2正则有什么区别？
      1. L2与L1的区别在于，L1正则是拉普拉斯先验，而L2正则则是高斯先验。L1可以产生稀疏解,可以让一部分特征的系数缩小到0，从而间接实现特征选择。所以L1适用于特征之间有关联的情况。L2让所有特征的系数都缩小，但是不会减为0，它会使优化求解稳定快速。所以L2适用于特征之间没有关联的情况
   4. 逻辑回归为什么一般性能差？
      1. LR是线性的，不能得到非线性关系，实际问题并不完全能用线性关系就能拟合。
   5. 如何用LR解决非线性问题？
      1. 将特征离散成高维的01特征可以解决分类模型的非线性问题
   6. 优缺点
      1. 优点：
         1. （模型）模型清晰，背后的概率推导经得住推敲。
         2. （输出）输出值自然地落在0到1之间，并且有概率意义（逻辑回归的输出是概率么？https://www.jianshu.com/p/a8d6b40da0cf）。
         3. （参数）参数代表每个特征对输出的影响，可解释性强。
         4. （简单高效）实施简单，非常高效（计算量小、存储占用低），可以在大数据场景中使用。
         5. （可扩展）可以使用online learning的方式更新轻松更新参数，不需要重新训练整个模型。
         6. （过拟合）解决过拟合的方法很多，如L1、L2正则化。
         7. （多重共线性）L2正则化就可以解决多重共线性问题。
      2. 缺点：
         1. 缺点：
            1. （特征相关情况）因为它本质上是一个线性的分类器，所以处理不好特征之间相关的情况。
            2. （特征空间）特征空间很大时，性能不好。
            3. （精度）容易欠拟合，精度不高。
6. SVM(Reference:https://zhuanlan.zhihu.com/p/43827793)
   1. SVM 是一种二类分类模型。它的基本模型是在特征空间中寻找间隔最大化的分离超平面的线性分类器。
      1. 当训练样本线性可分时，通过硬间隔最大化，学习一个线性分类器，即线性可分支持向量机.
      2. 当训练数据近似线性可分时，引入松弛变量，通过软间隔最大化，学习一个线性分类器，即线性支持向量机；
      3. 当训练数据线性不可分时，通过使用核技巧及软间隔最大化，学习非线性支持向量机。
   2.  SVM 为什么采用间隔最大化
       1.  当训练数据线性可分时，存在无穷个分离超平面可以将两类数据正确分开。感知机利用误分类最小策略，求得分离超平面，不过此时的解有无穷多个。线性可分支持向量机利用间隔最大化求得最优分离超平面，这时，解是唯一的。另一方面，此时的分隔超平面所产生的分类结果是最鲁棒的，对未知实例的泛化能力最强。可以借此机会阐述一下几何间隔以及函数间隔的关系。
   3. 为什么 SVM 要引入核函数
      1. 当样本在原始空间线性不可分时，可将样本从原始空间映射到一个更高维的特征空间，使得样本在这个特征空间内线性可分。而引入这样的映射后，所要求解的对偶问题的求解中，无需求解真正的映射函数，而只需要知道其核函数。核函数的定义：K(x,y)=<ϕ(x),ϕ(y)>，即在特征空间的内积等于它们在原始样本空间中通过核函数 K 计算的结果。一方面数据变成了高维空间中线性可分的数据，另一方面不需要求解具体的映射函数，只需要给定具体的核函数即可，这样使得求解的难度大大降低。
   4. 为什么SVM对缺失数据敏感
      1. 这里说的缺失数据是指缺失某些特征数据，向量数据不完整。SVM 没有处理缺失值的策略。而 SVM 希望样本在特征空间中线性可分，所以特征空间的好坏对SVM的性能很重要。缺失特征数据将影响训练结果的好坏。
   5. 优缺点：
      1. 优点：
         1. 解决高维特征的分类问题和回归问题很有效,在特征维度大于样本数时依然有很好的效果。
         2. 仅仅使用一部分支持向量来做超平面的决策，无需依赖全部数据。
         3. 有大量的核函数可以使用，从而可以很灵活的来解决各种非线性的分类回归问题。
         4. 样本量不是海量数据的时候，分类准确率高，泛化能力强。
      2. 缺点：
         1. 如果特征维度远远大于样本数，则SVM表现一般。
         2. SVM在样本量非常大，核函数映射维度非常高时，计算量过大，不太适合使用。
         3. 非线性问题的核函数的选择没有通用标准，难以选择一个合适的核函数。
         4. SVM对缺失数据敏感。


## 高频面试题
1. 解决过拟合（overfitting的方法）
   1. early stopping、数据集扩增（Data augmentation）、正则化（Regularization）、Dropout，BN
2. 解决欠拟合（underfitting的方法）
   1. 增加新特征，考虑加入特征组合，高次特征来增大假设空间
   2. 减少正则化参数。
   3. 使用非线性模型:比如核SVM，决策树，深度学习等模型
   4. 容量低的模型很难拟合训练集，使用集成学习方法，







## Machine Learning高频面试题
Reference: https://www.dataapplab.com/machine-learning-interview-questions/
1.  什么是偏差（bias）、方差（variable）之间的均衡？
    1.  Bias 是由于你使用的学习算法过度简单地拟合结果或者错误地拟合结果导致的错误。它反映的是模型在样本上的输出与真实值之间的误差，即模型本身的精准度，即算法本身的拟合能力。Bias 可能会导致模型欠拟合，使其难以具有较高的预测准确性，也很难将你的知识从训练集推广到测试集。
    2.  Variance 是由于你使用的学习算法过于复杂而产生的错误。它反映的是模型每一次输出结果与模型输出期望之间的误差，即模型的稳定性。反应预测的波动情况。Variance 过高会导致算法对训练数据的高纬度变化过于敏感，这样会导致模型过度拟合数据。从而你的模型会从训练集里带来太多噪音，这会对测试数据有一定的好处。
    3.  Bias-Variance 的分解，本质上是通过在基础数据集中添加偏差、方差和一点由噪声引起的不可约误差，来分解算法上的学习误差。从本质上讲，如果你使模型更复杂并添加更多变量，你将会失去一些 Bias 但获得一些 Variance，这就是我们所说的权衡（tradeoff）。这也是为什么我们在建模的过程中，不希望这个模型同时拥有高的偏差和方差。
   
2. 监督学习和非监督学习有什么不同？
   1. 监督学习需要train有label的数据。例如，为了进行classification（一项受监督的学习任务），您需要首先标记将用于培训模型的数据，以便将数据分类到标记的组中。相反的，无监督学习不需要明确标记数据。

3. KNN和 k-means 聚类由什么不同？
   1. K-Nearest Neighbors是一种监督分类算法，而 k-means聚类是一种无监督的聚类算法。 虽然这些机制起初可能看起来相似，但这实际上意味着为了使K-Nearest Neighbors工作，你需要标记数据，以便将未标记的点分类（因此是最近邻居部分）。 K均值聚类仅需要一组未标记的点和阈值：算法将采用未标记的点并逐渐学习如何通过计算不同点之间的距离的平均值将它们聚类成组。
   2. 这里的关键区别在于，KNN需要标记点，因此是有监督的学习，而k-means不是，因此是无监督学习。

4. 解释一下ROC曲线的原理
   1. ROC曲线是真阳率与各种阈值下的假阳率之间的对比度的图形表示。 它通常用作代表模型灵敏度（真阳性）与跌落之间的平衡或它将触发误报（假阳性）的概率。
5. 定义精度和召回率
   1. 召回（率）也称为真阳性率：您的模型声称的阳性数量与整个数据中的实际阳性数量相比。 精确度也称为阳性预测值，它衡量的是您的模型声称与实际声称的阳性数量相比的准确阳性数量。 在您预测在10个苹果的情况下有10个苹果和5个橙子的情况下，可以更容易地想到回忆和精确度。 你有完美的召回（实际上有10个苹果，你预测会有10个），但66.7％的精度，因为在你预测的15个事件中，只有10个（苹果）是正确的。
6. 什么是贝叶斯定理？它在机器学习环境中如何有用?
   1. 贝叶斯定理描述了当你不能准确知悉一个事物的本质时，你可以依靠与事物特定本质相关的事件出现的多少去判断其本质属性的概率。 它给出了已知先验知识下事件的后验概率。
   2. 在数学上，它表示为条件样本的真阳性率除以总体的假阳性率和条件的真阳性率之和。假设你在流感测试后有60%的机会真的感染了流感，但是在感染了流感的人中，50%的测试都是错误的，总人口只有5%的机会感染了流感。在做了阳性测试后，你真的有60%的机会患上流感吗？
   3. 贝叶斯定理说不，它说你有一个（0.6*0.05）（条件样本的真阳性率）/（0.6*0.05）（条件样本的真阳性率）+（0.5*0.95）（人群的假阳性率）= 5.94%的机会感染流感。
7. 为什么我们要称“朴素”贝叶斯？
   1. 尽管 Naive Bayes 具有实际应用，特别是在文本挖掘中，但它被认为是“天真的”，因为它假设在实际数据中几乎不可能看到：条件概率被计算为组件个体概率的纯乘积。 这意味着特征的绝对独立性 – 这种情况在现实生活中可能永远不会遇到。
8. L1、L2正则之间有什么不同？
   1. L2正则，对应的是加入2范数，使得对权重进行衰减，从而达到惩罚损失函数的目的，防止模型过拟合。保留显著减小损失函数方向上的权重，而对于那些对函数值影响不大的权重使其衰减接近于0。相当于加入一个gaussian prior。
   2. L1正则 对应得失加入1范数，同样可以防止过拟合。它会产生更稀疏的解，即会使得部分权重变为0，达到特征选择的效果。相当于加入了一个laplacean prior。
9. 如何对决策树进行剪枝？
   1.  剪枝是在决策树中，为了降低模型的复杂度，提高决策树模型的预测精度，去除预测能力较弱的分支后所发生的现象。修剪可以自下而上和自上而下进行，方法包括减少错误修剪和成本复杂度修剪。
   2.  减少错误修剪可能是最简单的版本：替换每个节点。如果不降低预测精度，则保持修剪。虽然很简单，但这种启发式方法实际上非常接近于一种可以最大限度地优化准确性的方法。
10. 什么是F1数，怎么使用它？
    1.  F1分数是衡量模型性能的指标。它是模型精度和召回的加权平均值，结果趋向于1是最好的，结果趋向于0是最差的。你可以在分类测试中使用它，而真正的否定并不重要。
11. 什么时候你应该使用分类而不是回归？
    1.  分类产生离散值并将数据集转换为严格的类别，而回归则提供连续的结果，使您能够更好地区分各个点之间的差异。如果您希望结果反映数据集中数据点对某些明确类别的归属性（例如：如果您希望知道某个名称是男性还是女性，而不仅仅是它们与男性和女性名称之间的关联性），则可以使用分类而不是回归。
12. 你如何确保你的模型没有过拟合？
    1.  过度拟合的训练数据以及数据携带的噪音，对于测试数据会带来不确定的推测。有如下三种方法避免过拟合：
    2.  保持模型尽可能地简单：通过考量较少的变量和参数来减少方差，达到数据中消除部分噪音的效果。
    3.  使用交叉检验的手段如：k-folds cross-validation。
    4.  使用正则化的技术如：LASSO方法来惩罚模型中可能导致过拟合的参数。
13. 什么是梯度下降法？
    1.  梯度下降法简单来说就是一种寻找目标函数最小化的方法。
14. 损失函数
    1.  损失函数用来评价模型的预测值和真实值不一样的程度，损失函数越好，通常模型的性能越好。不同的模型用的损失函数一般也不一样。

## Operating System操作系统高频面试题
1. 请分别简单说一说进程和线程以及它们的区别。
   1. 进程(process)与线程(thread)最大的区别是进程拥有自己的地址空间，某进程内的线程对于其他进程不可见，即进程A不能通过传地址的方式直接读写进程B的存储区域。进程之间的通信需要通过进程间通信(Inter-process communication，IPC)。与之相对的，同一进程的各线程间之间可以直接通过传递地址或全局变量的方式传递信息。
   2. 此外，进程作为操作系统中拥有资源和独立调度的基本单位，可以拥有多个线程。通常操作系统中运行的一个程序就对应一个进程。在同一进程中，线程的切换不会引起进程切换。在不同进程中进行线程切换，如从一个进程内的线程切换到另一个进程中的线程时，会引起进程切换。相比进程切换，线程切换的开销要小很多。线程于进程相互结合能够提高系统的运行效率。
   3. 线程可以分为两类：
      1. 一类是用户级线程(user level thread)。对于这类线程，有关线程管理的所有工作都由应用程序完成，内核意识不到线程的存在。在应用程序启动后，操作系统分配给该程序一个进程号，以及其对应的内存空间等资源。应用程序通常先在一个线程中运行，该线程被成为主线“程。在其运行的某个时刻，可以通过调用线程库中的函数创建一个在相同进程中运行的新线程。 用户级线程的好处是非常高效，不需要进入内核空间，但并发效率不高。
      2. 另一类是内核级线程(kernel level thread)。对于这类线程，有关线程管理的所有工作由内核完成，应用程序没有进行线程管理的代码，只能调用内核线程的接口。内核维护进程及其内部的每个线程，调度也由内核基于线程架构完成。内核级线程的好处是，内核可以将不同线程更好地分配到不同的CPU，以实现真正的并行计算。
   4. 事实上，在现代操作系统中，往往使用组合方式实现多线程，即线程创建完全在用户空间中完成，并且一个应用程序中的多个用户级线程被映射到一些内核级线程上，相当于是一种折中方案。


2. 线程同步的方式有哪些？
   1. 互斥量：采用互斥对象机制，只有拥有互斥对象的线程才有访问公共资源的权限。因为互斥对象只有一个，所以可以保证公共资源不会被多个线程同时访问。
   2. 信号量：它允许同一时刻多个线程访问同一资源，但是需要控制同一时刻访问此资源的最大线程数量。
   3. 事件（信号）：通过通知操作的方式来保持多线程同步，还可以方便的实现多线程优先级的比较操作。
3. 进程的通信方式有哪些？
   1. 主要分为：管道、系统IPC（包括消息队列、信号量、共享存储）、SOCKET
   2. 管道主要分为：普通管道PIPE 、流管道（s_pipe）、命名管道（name_pipe）
   3. 管道是一种半双工的通信方式，数据只能单项流动，并且只能在具有亲缘关系的进程间流动，进程的亲缘关系通常是父子进程
   4. 命名管道也是半双工的通信方式，它允许无亲缘关系的进程间进行通信
   5. 信号量是一个计数器，用来控制多个进程对资源的访问，它通常作为一种锁机制。
   6. 消息队列是消息的链表，存放在内核中并由消息队列标识符标识。
   7. 信号是一种比较复杂的通信方式，用于通知接收进程某个事件已经发生。
   8. 共享内存就是映射一段能被其它进程访问的内存，这段共享内存由一个进程创建，但是多个进程可以访问。
4. 什么是缓冲区溢出？有什么危害？其原因是什么？
   1. 缓冲区溢出是指当计算机向缓冲区填充数据时超出了缓冲区本身的容量，溢出的数据覆盖在合法数据上。
   2. 危害有以下两点：
      1. 程序崩溃，导致拒绝额服务
      2. 跳转并且执行一段恶意代码
      3. 造成缓冲区溢出的主要原因是程序中没有仔细检查用户输入。
5. 什么是死锁？死锁产生的条件？
   1. 在两个或者多个并发进程中，如果每个进程持有某种资源而又等待其它进程释放它或它们现在保持着的资源，在未改变这种状态之前都不能向前推进，称这一组进程产生了死锁。通俗的讲就是两个或多个进程无限期的阻塞、相互等待的一种状态。
   2. 死锁产生的四个条件（有一个条件不成立，则不会产生死锁）
      1. 互斥条件：一个资源一次只能被一个进程使用
      2. 请求与保持条件：一个进程因请求资源而阻塞时，对已获得资源保持不放
      3. 不剥夺条件：进程获得的资源，在未完全使用完之前，不能强行剥夺
      4. 循环等待条件：若干进程之间形成一种头尾相接的环形等待资源关系
6. 进程有哪几种状态？
   1. 就绪状态：进程已获得除处理机以外的所需资源，等待分配处理机资源
   2. 运行状态：占用处理机资源运行，处于此状态的进程数小于等于CPU数
   3. 阻塞状态： 进程等待某种条件，在条件满足之前无法执行
7. 分页和分段有什么区别？
   1. 段是信息的逻辑单位，它是根据用户的需要划分的，因此段对用户是可见的 ；页是信息的物理单位，是为了管理主存的方便而划分的，对用户是透明的。
   2. 段的大小不固定，有它所完成的功能决定；页大大小固定，由系统决定
   3. 段向用户提供二维地址空间；页向用户提供的是一维地址空间
   4. 段是信息的逻辑单位，便于存储保护和信息的共享，页的保护和共享受到限制。
8. 操作系统中进程调度策略有哪几种？
   1. FCFS(先来先服务)，优先级，时间片轮转，多级反馈
9. 说一说进程同步有哪几种机制。
   1.  原子操作、信号量机制、自旋锁管程、会合、分布式系统
10. 说一说死锁的处理基本策略和常用方法。
    1.  解决死锁的基本方法如下：
        1.  预防死锁、避免死锁、检测死锁、解除死锁
    2. 解决四多的常用策略如下：
       1. 忽略该问题。例如鸵鸟算法，该算法可以应用在极少发生死锁的的情况下。为什么叫鸵鸟算法呢，因为传说中鸵鸟看到危险就把头埋在地底下，可能鸵鸟觉得看不到危险也就没危险了吧。跟掩耳盗铃有点像。
       2. 检测死锁并且恢复。
       3. 仔细地对资源进行动态分配，以避免死锁。
       4. 通过破除死锁四个必要条件之一，来防止死锁产生。
11. 请问死锁的条件是什么？
    1.  互斥条件(Mutual exclusion)：
        1.  资源不能被共享，只能由一个进程使用。
    2. 请求与保持条件(Hold and wait)：已经得到资源的进程可以再次申请新的资源。
    3. 非剥夺条件(No pre-emption)：已经分配的资源不能从相应的进程中被强制地剥夺。
    4. 循环等待条件(Circular wait)：系统中若干进程组成环路，该环路中每个进程都在等待相邻进程正占用的资源。












