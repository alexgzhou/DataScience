# 健康体检数据周报20180326--xgboost建模gbtree

## 建模
* 选取决定代谢综合征的指标作为feature，次年结果y2作为label
* 根据y2，按照2:1选取训练集和测试集
* xgboost（booster = "gbtree",eta = 0.1,objective = "reg:logistic"），其他参数默认，建模。nrounds选取200。

## 结果
* auc=0.925

## 计划（必做）
* feature增加性别、年龄
* 增加其他参数输出，如error
* 模型调参
* 将数据分组建模

## 后面计划（选做）
* 尝试xgboost线模型
* 尝试lightGbm建模