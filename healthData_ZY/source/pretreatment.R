## 清空列表
rm(list=ls())
gc()
options(scipen = 200)

## 读取数据
data_result<-read.csv(file.choose(), stringsAsFactors = F)

## 数据框名字
# names(data_result)

## 加载sqldf包
library(sqldf)

# df1 <- sqldf("select * from data_result where XIANGMUBM in(760,761,2161,762,2399,2328,9,10,2330,2520,29,23,48,79,2328,2329)")  

head(data_result,8)
## 利用sql语句查询数据，并且行转列
df2 <- sqldf("select  
             
             TIJIANBM,
             MAX(case when XIANGMUBM=760 then TIJIANJG end) as 'HT',
             MAX(case when XIANGMUBM=761 then TIJIANJG  end) as 'WT',
             MAX(case when XIANGMUBM=2161 then TIJIANJG end) as 'DBP',
             MAX(case when XIANGMUBM=762 then TIJIANJG end) as 'SBP',
             MAX(case when XIANGMUBM=2300 then TIJIANJG end) as 'FBG',
             MAX(case when XIANGMUBM=2328 then TIJIANJG end) as 'TG1',
             MAX(case when XIANGMUBM=9 then TIJIANJG end) as 'TG',
             MAX(case when XIANGMUBM=10 then TIJIANJG end) as 'HDL',
             MAX(case when XIANGMUBM=2330 then TIJIANJG end) as 'TC',
             MAX(case when XIANGMUBM=2520 then TIJIANJG end) as 'LDL',
             MAX(case when XIANGMUBM=29 then TIJIANJG end) as 'TLDL',

             MAX(case when XIANGMUBM=23 then TIJIANJG end) as 'Past1',
             MAX(case when XIANGMUBM=48 then TIJIANJG end) as 'Past2',
             MAX(case when XIANGMUBM=79 then TIJIANJG end) as 'Past3',
             MAX(case when XIANGMUBM=90 then TIJIANJG end) as 'Past4',
             MAX(case when XIANGMUBM=102 then TIJIANJG end) as 'Past5',
             MAX(case when XIANGMUBM=109 then TIJIANJG end) as 'Past6',

             MAX(case when XIANGMUBM=2032 then TIJIANJG end) as 'Style',
             MAX(case when XIANGMUBM=2169 then TIJIANJG end) as 'Medicine',
             MAX(case when XIANGMUBM=2170 then TIJIANJG end) as 'Family',
             MAX(case when XIANGMUBM=2856 then TIJIANJG end) as 'Screen',
             MAX(case when XIANGMUBM=1590 then TIJIANJG end) as 'BP24'
             from data_result 
             
             group by TIJIANBM")

df2 <- df2[,-7]
rm(data_result)
gc()

## 读取数据
data_peopleInfo<-read.csv(file.choose(), stringsAsFactors = F)
head(data_peopleInfo,2)

## 筛选数据
library(dplyr)
data_peopleInfo2 <- subset(data_peopleInfo,data_peopleInfo$TIJIANBM %in% df2$TIJIANBM)

rm(data_peopleInfo)
gc()

## 去重
# data_peopleInfo3 <- distinct(data_peopleInfo2[,c(2,4,5,6)])
data_peopleInfo3 <- data_peopleInfo2[!duplicated(data_peopleInfo2$TIJIANBM), ]

## 合并，左连接
head(data_peopleInfo2,1)
df3 <- merge(df2,data_peopleInfo3,by.x = "TIJIANBM")
head(df3,1)
rm(df2)
rm(data_peopleInfo2)
rm(data_peopleInfo3)
gc()

### 标准1开始 ###
df3p1 <- sqldf("select *,WT*100*100/(HT*HT) as BMI from df3")

# df3p11 <- sqldf("select *,case when BMI>=25 then 1 else 0 end as p1,
#                case when FBG>=5.6 then 1 else 0 end as p2,
#                case when DBP>=85 or SBP>=130 then 1 else 0 end as p3,
#                case when TG1>=1.7 or TG2>=1.7 then 1 else 0 end as p4,
#                case when (HDL<1  and XINGBIE==1) or (HDL<1.3  and XINGBIE==2) then 1 else 0 end as p5
#                from df3P1
#                ")
# 
# df3p1<-df3
# for( i in 1:length(df3p1$TIJIANBM)) {
#   if (!is.na(df3p1[i,"TG1"])){
#     df3p1[i,"TG2"]<-df3p1[i,"TG1"]
#   }
# }

for(i in 2:11){
  df3p1[, i] <- as.numeric(df3p1[, i])
}

df3p1$p1 <- ifelse(df3p1$BMI >= 25, 1, 0)
df3p1$p2 <- ifelse(df3p1$FBG >= 5.6, 1, 0)
df3p1$p3 <- ifelse(df3p1$DBP>=85 | df3p1$SBP>=130, 1, 0)
df3p1$p4 <- ifelse(df3p1$TG >=1.7, 1, 0)
df3p1$p5 <- ifelse((df3p1$HDL<1 & df3p1$XINGBIE==1) | (df3p1$HDL<1.3 & df3p1$XINGBIE==2), 1, 0)
df3p1$p <- df3p1$p1 + df3p1$p2+ df3p1$p3+ df3p1$p4+ df3p1$p5
df3p1$y <- ifelse(df3p1$p >= 3, 1, 0)
# table(df3p1$p1)
df3p1 <- df3p1[, -(32:37)]
# summary(df3p1$y)
df3p1 <- df3p1[which(!is.na(df3p1$y)), ]
df4 <- df3p1
# table(df4$y)
### 标准1结束 ###

## 姓名正则处理,去掉首字为非数字的姓名的数字
df4p1 <- df4
rm(df4)
df4p1$name <- unlist(lapply(df4p1$XINGMING, function(x){
  if(grepl("\\d", substr(x, 1, 1))){
    x
  } else {
    gsub("\\d", "", x)
  }
}))

## 取年份,增加patientId
df4p1$birthyear <- substr(df4p1$CHUSHENGRQ,1,4)
df4p1t1 <- sqldf("select distinct name, XINGBIE, birthyear from df4p1")
df4p1t1$patientId <- seq(1:length(df4p1t1$name))

df4p2 <- sqldf("select a.*,b.patientId from df4p1 a left join df4p1t1 b on a.name=b.name
                       and a.XINGBIE=b.XINGBIE and a.birthyear =b.birthyear")
rm(df4p1t1)

df4p2_order <- df4p2[with(df4p2, order(df4p2[,"patientId"], as.Date(df4p2[, "TIJIANRQ"]))), ]
# df4p2$y2 <- 5 #随意值
# for (i in 2:length(df4p2_order$TIJIANBM)){
#   first <- df4p2_order[i-1,]
#   second <- df4p2_order[i,]
#   if((first$patientId == second$patientId) && (as.double(as.Date(second$TIJIANRQ)) -  as.double(as.Date(first$TIJIANRQ))  < 730  ) && (as.double(as.Date(second$TIJIANRQ)) -  as.double(as.Date(first$TIJIANRQ))  >180  )){
#     df4p2_order[i-1,]$y2 <- second$Y
#   }
# }
# df5 <- df4p2_order[which((df4p2_order$y2!=5)), ]

for (i in 2:length(df4p2_order$TIJIANBM)){
  if((df4p2_order[i-1, "patientId"] == df4p2_order[i, "patientId"]) && (as.double(as.Date(df4p2_order[i, "TIJIANRQ"])) -  as.double(as.Date(df4p2_order[i-1, "TIJIANRQ"]))  < 730  ) && (as.double(as.Date(df4p2_order[i, "TIJIANRQ"])) -  as.double(as.Date(df4p2_order[i-1, "TIJIANRQ"]))  >180  )){
    df4p2_order[i-1, "y2"] <- df4p2_order[i, "y"]
    df4p2_order[i-1, "BMI2"] <- df4p2_order[i, "BMI"]
    df4p2_order[i-1, "DBP2"] <- df4p2_order[i, "DBP"]
    df4p2_order[i-1, "SBP2"] <- df4p2_order[i, "SBP"]
  }
}

## 换方法验证y2
# df4p2_order$y3 <- c(unlist(lapply(2:nrow(df4p2_order), function(x){
#   if((df4p2_order[x-1, "patientId"] == df4p2_order[x, "patientId"]) && (as.double(as.Date(df4p2_order[x, "TIJIANRQ"])) -  as.double(as.Date(df4p2_order[x-1, "TIJIANRQ"]))  < 730  ) && (as.double(as.Date(df4p2_order[x, "TIJIANRQ"])) -  as.double(as.Date(df4p2_order[x-1, "TIJIANRQ"]))  >180  )){
#     df4p2_order[x, "y"]
#   }else {
#     NA
#   }
# })),NA)
# df4p2_order<-df4p2_order[,-37]

df5 <- df4p2_order[which(!is.na(df4p2_order$y2)), ]
# t1<- sqldf("select * from df5 where (y=0 and y2=1)")
# t2<- sqldf("select * from df5 where (y=0 and y2=0)")
# t3<- sqldf("select * from df5 where (y=1 and y2=0)")
# t4<- sqldf("select * from df5 where (y=1 and y2=1)")
# sum(is.na(df5$TC))

df6 <- df5[,c(35,24,26,34,1,31,2:8,11:20,32,36)]
df6Y <- df6[which(df6$y == 1), ]
df6N <- df6[which(df6$y == 0), ]

df7 <- df5[,c(35,24,26,34,1,31,2:8,37:39,11:20,32,36)]

## 写出数据
write.csv(df6N,"D:/chromeDownload/df6N.csv",row.names = F)
