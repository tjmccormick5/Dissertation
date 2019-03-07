#restructure Vowel_Data_Final to be 3 smaller data sheets by level, selecting relevant columns
voweldata <- select(Vowel_Data_Final, Level, Speaker, Vowel, f1, f2)
vowels_Lev1 <- filter(voweldata, Level == 1)
vowels_Lev2 <- filter(voweldata, Level == 2)
vowels_Lev3 <- filter(voweldata, Level == 3)

#select f1 and f2 for each sheet
freq_vow_Lev1 <- select(vowels_Lev1, f1, f2)
freq_vow_Lev2 <- select(vowels_Lev2, f1, f2)
freq_vow_Lev3 <- select(vowels_Lev3, f1, f2)

#kmeans for 5 clusters for each f1/f2 sheet
results_Lev1 <- kmeans(freq_vow_Lev1, 5)
results_Lev2 <- kmeans(freq_vow_Lev2, 5)
results_Lev3 <- kmeans(freq_vow_Lev3, 5)

#table for vowels by clusters
table(vowels_Lev1$Vowel, results_Lev1$cluster)
table(vowels_Lev2$Vowel, results_Lev2$cluster)
table(vowels_Lev3$Vowel, results_Lev3$cluster)

#6 figures arranged side by side
par(mfrow = c(1,2))
plot(vowels_Lev1[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_Lev1$Vowel)], main = "Vowels")
plot(vowels_Lev1[c("f2", "f1")], col = c("blue", "green", "orange", "black", "red")[results_Lev1$cluster], main = "Clusters")
plot(vowels_Lev2[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_Lev2$Vowel)], main = "Vowels")
plot(vowels_Lev2[c("f2", "f1")], col = c("blue", "green", "orange", "black", "red")[results_Lev2$cluster], main = "Clusters")
plot(vowels_Lev3[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_Lev3$Vowel)], main = "Vowels")
plot(vowels_Lev3[c("f2", "f1")], col = c("blue", "green", "orange", "black", "red")[results_Lev3$cluster], main = "Clusters")



par(mfrow = c(1, 1))
#END 5 VOWEL SYSTEM, Select participants



#BEGIN 5 VOWEL SYSTEM, Select participants   
#restructure Vowel_Data_Final to be 3 smaller data sheets by level, selecting relevant columns
voweldataspeaker <- select(Vowel_Data_Final, Level, Speaker, Vowel, f1, f2)
vowels_L1_S13 <- filter(voweldata, Level == 1, Speaker == 13)
vowels_L2_S5 <- filter(voweldata, Level == 2, Speaker == 5)
vowels_L3_S18 <- filter(voweldata, Level == 3, Speaker == 18)

#select f1 and f2 for each sheet
freq_vow_L1_S13 <- select(vowels_L1_S13, f1, f2)
freq_vow_L2_S5 <- select(vowels_L2_S5, f1, f2)
freq_vow_L3_S18 <- select(vowels_L3_S18, f1, f2)

#kmeans for 5 clusters for each f1/f2 sheet
results_L1_S13 <- kmeans(freq_vow_L1_S13, 5)
results_L2_S5 <- kmeans(freq_vow_L2_S5, 5)
results_L3_S18 <- kmeans(freq_vow_L3_S18, 5)

#table for vowels by clusters
table(vowels_L1_S13$Vowel, results_L1_S13$cluster)
table(vowels_L2_S5$Vowel, results_L2_S5$cluster)
table(vowels_L3_S18$Vowel, results_L3_S18$cluster)

par(mfrow = c(1, 2))    
#plot clusters/vowels Lev1
plot(vowels_L1_S13[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_L1_S13$Vowel)], main = "Vowels")
plot(vowels_L1_S13[c("f2", "f1")], col = c("red", "blue", "green", "orange", "black")[results_L1_S13$cluster], main = "Clusters")


#plot clusters/vowels Lev2
plot(vowels_L2_S5[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_L2_S5$Vowel)], main = "Vowels")
plot(vowels_L2_S5[c("f2", "f1")], col = c("blue", "green", "orange", "black", "red")[results_L2_S5$cluster], main = "Clusters")

#plot clusters/vowels Lev3
plot(vowels_L3_S18[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_L3_S18$Vowel)], main = "Vowels")
plot(vowels_L3_S18[c("f2", "f1")], col = c("blue", "black", "red", "orange", "green")[results_L3_S18$cluster], main = "Clusters")


par(mfrow = c(1, 1))
#END 5 VOWEL SYSTEM, Select participants



#BEGIN 4 VOWEL SYSTEM, All participants, NO U
#restructure Vowel_Data_Final to be 3 smaller data sheets by level, selecting relevant columns
voweldata <- select(Vowel_Data_Final, Level, Speaker, Vowel, f1, f2)
voweldata_NoU <- filter(voweldata, Vowel != "u")
vowels_Lev1 <- filter(voweldata_NoU, Level == 1)
vowels_Lev2 <- filter(voweldata_NoU, Level == 2)
vowels_Lev3 <- filter(voweldata_NoU, Level == 3)

#select f1 and f2 for each sheet
freq_vow_Lev1 <- select(vowels_Lev1, f1, f2)
freq_vow_Lev2 <- select(vowels_Lev2, f1, f2)
freq_vow_Lev3 <- select(vowels_Lev3, f1, f2)

#kmeans for 5 clusters for each f1/f2 sheet
results_Lev1 <- kmeans(freq_vow_Lev1, 4)
results_Lev2 <- kmeans(freq_vow_Lev2, 4)
results_Lev3 <- kmeans(freq_vow_Lev3, 4)

#table for vowels by clusters
table(vowels_Lev1$Vowel, results_Lev1$cluster)
table(vowels_Lev2$Vowel, results_Lev2$cluster)
table(vowels_Lev3$Vowel, results_Lev3$cluster)

# figures arranged side by side
par(mfrow = c(1,2))
plot(vowels_Lev1[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_Lev1$Vowel)], main = "Vowels")
plot(vowels_Lev1[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[results_Lev1$cluster], main = "Clusters")
plot(vowels_Lev2[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_Lev2$Vowel)], main = "Vowels")
plot(vowels_Lev2[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[results_Lev2$cluster], main = "Clusters")
plot(vowels_Lev3[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[as.factor(vowels_Lev3$Vowel)], main = "Vowels")
plot(vowels_Lev3[c("f2", "f1")], col = c("orange", "red", "blue", "green", "black")[results_Lev3$cluster], main = "Clusters")


par(mfrow = c(1, 1))
#END 4 VOWEL SYSTEM, All participants, No U



#BEGIN 4 VOWEL SYSTEM, Select participants
#restructure Vowel_Data_Final to be 3 smaller data sheets by level, selecting relevant columns
voweldataspeaker <- select(Vowel_Data_Final, Level, Speaker, Vowel, f1, f2)
voweldataspeaker_NoU <- filter(voweldataspeaker, Vowel != "u")
vowels_L1_S13 <- filter(voweldataspeaker_NoU, Level == 1, Speaker == 13)
vowels_L2_S5 <- filter(voweldataspeaker_NoU, Level == 2, Speaker == 5)
vowels_L3_S8 <- filter(voweldataspeaker_NoU, Level == 3, Speaker == 8)

#select f1 and f2 for each sheet
freq_vow_L1_S13 <- select(vowels_L1_S13, f1, f2)
freq_vow_L2_S5 <- select(vowels_L2_S5, f1, f2)
freq_vow_L3_S8 <- select(vowels_L3_S8, f1, f2)

#kmeans for 5 clusters for each f1/f2 sheet
results_L1_S13 <- kmeans(freq_vow_L1_S13, 4)
results_L2_S5 <- kmeans(freq_vow_L2_S5, 4)
results_L3_S8 <- kmeans(freq_vow_L3_S8, 4)

#table for vowels by clusters
table(vowels_L1_S13$Vowel, results_L1_S13$cluster)
table(vowels_L2_S5$Vowel, results_L2_S5$cluster)
table(vowels_L3_S8$Vowel, results_L3_S8$cluster)

par(mfrow = c(1,2))
#plot clusters/vowels Lev1
plot(vowels_L1_S13[c("f2", "f1")], col = c("red", "blue", "green", "orange", "black")[as.factor(vowels_L1_S13$Vowel)], main = "Vowels")
plot(vowels_L1_S13[c("f2", "f1")], col = c("red", "blue", "green", "orange", "black")[results_L1_S13$cluster], main = "Clusters")

#plot clusters/vowels Lev2
plot(vowels_L2_S5[c("f2", "f1")], col = c("red", "blue", "green", "orange", "black")[as.factor(vowels_L2_S5$Vowel)], main = "Vowels")
plot(vowels_L2_S5[c("f2", "f1")], col = c("red", "blue", "green", "orange", "black")[results_L2_S5$cluster], main = "Clusters")

#plot clusters/vowels Lev3
plot(vowels_L3_S8[c("f2", "f1")], col = c("red", "blue", "green", "orange", "black")[as.factor(vowels_L3_S8$Vowel)], main = "Vowels")
plot(vowels_L3_S8[c("f2", "f1")], col = c("red", "blue", "green", "orange", "black")[results_L3_S8$cluster], main = "Clusters")


par(mfrow = c(1, 1))
#END 4 VOWEL SYSTEM, Select participants




#Results Beginner
#Kappa with Linear Weighting
#0.8051 == ObservedKappa
#0.0094 == StandardError	 
#.95 Confidence Interval 
#Lower Limit	== 0.7868
#Upper Limit  == 0.8234

# 0.9471 == maximum possible linear-weighted kappa, given the observed marginal frequencies
# 0.8501 == observed as proportion of maximum possible


#Results intermediate
#Kappa with Linear Weighting
#0.8275 == ObservedKappa
#0.0087 == StandardError	 
#.95 Confidence Interval 
#Lower Limit	== 0.8105
#Upper Limit  == 0.8445

# 0.9444 == maximum possible linear-weighted kappa, given the observed marginal frequencies
# 0.8762 == observed as proportion of maximum possible



#Results advanced
#Kappa with Linear Weighting
#0.8137 == ObservedKappa
#0.0092 == StandardError	 
#.95 Confidence Interval 
#Lower Limit	== 0.7957
#Upper Limit  == 0.8317

# 0.9384 == maximum possible linear-weighted kappa, given the observed marginal frequencies
# 0.8671 == observed as proportion of maximum possible
