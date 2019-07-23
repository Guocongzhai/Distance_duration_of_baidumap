#library(tidyverse)
library(readxl)

#input the data resource
data1 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\1.xlsx')
data2 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\2.xlsx')
data3 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\3.xlsx')
data4 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\4.xlsx')
data5 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\5.xlsx')
data6 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\6.xlsx')
data7 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\7.xlsx')
data8 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\8.xlsx')
data9 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\9.xlsx')
data10 <- read_excel('C:\\Users\\LAYZ\\Desktop\\Survery\\10.xlsx')

#data9$`订单产生时间`<-as.numeric(data9$`订单产生时间`)
#merge all the datasets
data2$`问卷编号` <- data2$`问卷编号` + 49
data3$`问卷编号` <- data3$`问卷编号` + 79
data4$`问卷编号` <- data4$`问卷编号` + 110
data5$`问卷编号` <- data5$`问卷编号` + 162
data6$`问卷编号` <- data6$`问卷编号` + 204
data7$`问卷编号` <- data7$`问卷编号` + 238
data8$`问卷编号`<-data8$`问卷编号`+283
data9$`问卷编号` <- data9$`问卷编号` + 327
data10$`问卷编号` <- data10$`问卷编号` + 357

traveldata <- rbind(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10)
#summary(traveldata)
traveldata$`问卷编号` <- as.factor(traveldata$`问卷编号`)

traveldata$`出行目的` <- as.factor(traveldata$`出行目的`-1)

# library(lubridate)
# traveldata$`订单产生时间` <- hour(traveldata$`订单产生时间`)
# traveldata<-subset(traveldata,traveldata$`订单产生时间`!=' ')
# for (i in 1:nrow(traveldata)) {
#   if ((9  > traveldata[i, 6] & traveldata[i, 6] > 6)||(19 > traveldata[i, 6] & traveldata[i, 6] > 16 )) { traveldata[i, 6] <-1 }
#   else { traveldata[i, 6] <-0}
# }
# traveldata$`订单产生时间`<-as.factor(traveldata$`订单产生时间`)
#traveldata$`订单产生时间`[(traveldata$`订单产生时间` >6 & traveldata$`订单产生时间` < 9) | (traveldata$`订单产生时间` > 16 & traveldata$`订单产生时间` < 19)] <- 2

traveldata$`问题1` <- as.factor(traveldata$`问题1`)
#traveldata$`问题2`[traveldata$`问题2`==1]<-2
traveldata$`问题2` <- as.factor(traveldata$`问题2`)
traveldata$`问题3`<-as.factor(traveldata$`问题3`)
traveldata$`问题4` <- as.factor(traveldata$`问题4`)
traveldata$`问题5` <- as.factor(traveldata$`问题5`)
traveldata$`问题6` <- as.factor(traveldata$`问题6`)

traveldata$`性别` <-as.factor(traveldata$`性别`-1)
traveldata$`婚姻状况` <- as.factor(traveldata$`婚姻状况`-1)
traveldata$`职业` <- as.factor(traveldata$`职业`-1)
traveldata$`已完成最高学历` <- as.factor(traveldata$`已完成最高学历`-1)
traveldata$`未成年人数`[is.na(traveldata$`未成年人数`)]<-1
traveldata$`汽车`[is.na(traveldata$`汽车`)] <- 1
traveldata$`摩托车`[is.na(traveldata$`摩托车`)] <- 0
traveldata$`非机动车·`[is.na(traveldata$`非机动车·`)] <- 1
traveldata$`驾照`[is.na(traveldata$`驾照`)]<-1
traveldata$`驾照` <- as.factor(traveldata$`驾照`-1)

traveldata$`家庭收入`[is.na(traveldata$`家庭收入`)] <- 2
traveldata$`家庭收入` <- as.factor(traveldata$`家庭收入`)
traveldata$`个人月收入`[is.na(traveldata$`个人月收入`)] <- 1
traveldata$`个人月收入` <- as.factor(traveldata$`个人月收入`)
traveldata$`工作时制`[is.na(traveldata$`工作时制`)]<-2
traveldata$`工作时制` <- as.factor(traveldata$`工作时制`-1)
traveldata$`购车意愿` <- as.factor(traveldata$`购车意愿`)
traveldata$`原因一` <- as.factor(traveldata$`原因一`)
traveldata$`原因二` <- as.factor(traveldata$`原因二`)
traveldata$`原因三`<-as.factor(traveldata$`原因三`)

traveldata$`等待时间`[is.na(traveldata$`等待时间`)] <- 2
traveldata$`出行耗时`<-traveldata$`行驶时间`+traveldata$`等待时间`
#traveldata <- subset(traveldata, traveldata$`行驶里程` != ' ' & traveldata$`行驶时间` != ' ')
#traveldata$`问题2`[is.na(traveldata$`问题2`)] <- 1

names(traveldata) <- c('peopleid', 'trippurpose', 'O', 'D', 'ordertype', 'ordertime', 'distance', 'waitingtime', 'drivingtime', 'totaltime', 'expense', 'question1',
                       'question2', 'question3', 'question4', 'question5', 'question6', 'age', 'gender', 'marriage', 'homeaddress', 'occupation', 'educationdegree', 'educationyear',
                       'adultnumber', 'employedadults', 'youngpeople', 'vehicle', 'motorcycle', 'nonautomible', 'driverlicence', 'homeincome', 'personalincome', 'workingtimetype',
                       'frequencyofcar-hailing','willingtobuyavehicle','reason1','reason2','reason3')


#summary(traveldata$trippurpose)
#waitgroup <- cut(traveldata$waitingtime, c(0, 5,10,15, Inf))
#table(traveldata$ordertime, waitgroup)
write.csv(traveldata, file = 'C:\\Users\\LAYZ\\Desktop\\traveldata.csv')
#traveldata$`问题2` <- as.character(traveldata$`问题2`)
#distance estimation
#ibrary(baidumap)
#library(REmap)

#traveldata$`起点位置`<-gsub("[(.*)]","",traveldata$`起点位置`)
#traveldata$`起点位置`<-as.numeric(traveldata$`起点位置`)
#options(baidumap.key = 'G0iK9REEnCpHAqBXG3vi1QTHvPNw1C7A')
#getBaiduMap(traveldata$`起点位置`, width = 400, height = 400, zoom = 10, scale = 2, color = "color", messaging = TRUE)



#model establishment
index <- duplicated(traveldata$peopleid)
uniquedata <- traveldata[!index,]

agegroup <- cut(uniquedata$age, c(15, 25, 35, 45, 55, Inf))
summary(agegroup)

summary(uniquedata$gender)
table(uniquedata$vehicle)
table(uniquedata$marriage)
table(uniquedata$personalincome)
table(uniquedata$homeincome)
table(uniquedata$educationdegree)
table(uniquedata$driverlicence)
table(uniquedata$workingtimetype)
summary(uniquedata$adultnumber)
summary(uniquedata$employedadults)
summary(uniquedata$youngpeople)
summary(uniquedata$vehicle)
summary(uniquedata$motorcycle)
summary(uniquedata$nonautomible)

table(uniquedata$`frequencyofcar-hailing`)


table(traveldata$question1)

library(nnet)
modeldata1 <- traveldata[(traveldata$question1 == '7')&(traveldata$question2=='6'|traveldata$question2=='1'), - c(1:12, 14:17, 21, 35:39)]
model1 <- multinom(question2 ~ ., data = modeldata1)
stepmodel1<- step(model1, trace = FALSE)
summary(stepmodel1)
#stepmodelpre <- predict(stepmodel, type = "p")
#stepmodelpre
model2 <- multinom(question2 ~ trippurpose +waitingtime+ drivingtime + expense + age + gender + marriage + educationyear
                   + employedadults + youngpeople + vehicle + driverlicence + personalincome, data = modeldata)
stepmodel2 <- step(model2, trace = FALSE)
summary(stepmodel2)


