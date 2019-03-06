#violin
p <- ggplot(data = RegionalData, aes(factor(Region), log2(RT)))
p + geom_violin(aes(fill = as.character(Region)))

#four graphs, log points
ggplot(data = RegionalData) +
  geom_point (mapping = aes(y = log2(RT), x = LengthofRegion, color = Region)) +
  facet_grid(. ~ Level1)

#four graphs, non-log points
ggplot(data = RegionalData) +
  geom_point (mapping = aes(y = RT, x = LengthofRegion, color = Region)) +
  facet_grid(. ~ Level1)

#four groups X five regions graph, log points
ggplot(data = RegionalData) +
  geom_point (mapping = aes(y = log2(RT), x = LengthofRegion, color = as.character(Region))) +
  facet_grid(Region ~ Level1)

#boxplot --> regions X four groups, shows condensing RRTs at increasing proficiencies
ggplot(data = RegionalData) + 
  geom_boxplot (mapping = aes(y = Residual, color = as.character(Region)), show.legend = FALSE) +
  facet_grid(Level1 ~ Region)

#boxplot --> advanced in 3 conditions
ggplot(data = filter(RegionalData3cond, Level1 == 4)) + 
     geom_boxplot (mapping = aes(y = Residual, color = as.character(Region)), show.legend = FALSE) +
     facet_grid(Condition ~ Region)

#Regional Analysis of Variation (Boxplot by level -- Region 3)
analysis.df <- RegionalData3cond
analysis.df$Level1 = factor(analysis.df$Level1, 
            labels = c("Intermediate", "Advanced", "Post-Advanced", "Native"))
ggplot(filter(analysis.df, Region == 3), aes(x = Level1, y = Residual))+
  geom_boxplot(fill = "cyan")+
  scale_x_discrete() + xlab ("Proficiency Level") + ylab("Residual Reaction Times")



#Regional Analysis of Variation (Boxplot by level -- Grid of Regions)    
ggplot(analysis.df, aes(x = Level1, y = Residual))+
  geom_boxplot(fill = "cyan")+
  facet_grid(.~ Region)
  scale_x_discrete() + xlab ("Proficiency Level") + ylab("Residual Reaction Times")
  
  

#ANOVA REGION 1
Anova_Reg1 <- aov(Residual ~ Level1 + Condition, data = filter(analysis.df, Region == 1, ComprehensionCheckCorrect == 1, PercentCorrect >= .6))
ggplot(filter(analysis.df, Region == 1, ComprehensionCheckCorrect == 1, PercentCorrect >= .6), aes(x = Level1, y = Residual))+
  geom_boxplot(mapping = aes(fill = Level1))+
  scale_x_discrete() + xlab ("Proficiency Level") + ylab("Residual Reaction Times")
summary(Anova_Reg1)
TukeyHSD(Anova_Reg1, "Level1")


#ANOVA REGION 2 
Anova_Reg2 <- aov(Residual ~ Level1 + Condition, data = filter(analysis.df, Region == 2, ComprehensionCheckCorrect == 1, PercentCorrect >= .6))
ggplot(filter(analysis.df, Region == 2, ComprehensionCheckCorrect == 1, PercentCorrect >= .6), aes(x = as.factor(Level1), y = Residual))+
  geom_boxplot(mapping = aes(fill = Level1))+
  scale_x_discrete() + xlab ("Proficiency Level") + ylab("Residual Reaction Times")
summary(Anova_Reg2)
TukeyHSD(Anova_Reg2, "Level1")



#ANOVA REGION 3
Anova_Reg3 <- aov(Residual ~ Level1 + Condition, data = filter(analysis.df, Region == 3, ComprehensionCheckCorrect == 1, PercentCorrect >= .6))
ggplot(filter(analysis.df, Region == 3, ComprehensionCheckCorrect == 1, PercentCorrect >= .6), aes(x = Level1, y = Residual))+
  geom_boxplot(mapping = aes(fill = Level1))+
  scale_x_discrete() + xlab ("Proficiency Level") + ylab("Residual Reaction Times")
summary(Anova_Reg3)
TukeyHSD(Anova_Reg3, "Level1")


#ANOVA REGION 4 
Anova_Reg4 <- aov(Residual ~ Level1 + Condition, data = filter(analysis.df, Region == 4, ComprehensionCheckCorrect == 1, PercentCorrect >= .6))
ggplot(filter(analysis.df, Region == 4, ComprehensionCheckCorrect == 1, PercentCorrect >= .6), aes(x = Level1, y = Residual))+
  geom_boxplot(mapping = aes(fill = Level1))+
  scale_x_discrete() + xlab ("Proficiency Level") + ylab("Residual Reaction Times")
summary(Anova_Reg4)



#ANOVA REGION 5
Anova_Reg5 <- aov(Residual ~ Level1 + Condition, data = filter(analysis.df, Region == 5, ComprehensionCheckCorrect == 1, PercentCorrect >= .6))
ggplot(filter(analysis.df, Region == 5, ComprehensionCheckCorrect == 1, PercentCorrect >= .6), aes(x = Level1, y = Residual))+
  geom_boxplot(mapping = aes(fill = Level1))+
  scale_x_discrete() + xlab ("Proficiency Level") + ylab("Residual Reaction Times")
summary(Anova_Reg5)





voweldata <- select(Vowel_Data_Final, Level, Speaker, f1, f2)
kmeans(voweldata, 5)
results <- kmeans(voweldata, 5)
results


results_Lev1 <- kmeans(filter(voweldata, Level == 1), 5)
results_Lev1

results_Lev2 <- kmeans(filter(voweldata, Level == 2), 5)
results_Lev3 <- kmeans(filter(voweldata, Level == 3), 5)

Lev1 <- filter(Vowel_Data_Final, Level == 1)
Lev2 <- filter(Vowel_Data_Final, Level == 2)
Lev3 <- filter(Vowel_Data_Final, Level == 3)

table(Lev1$Vowel, results_Lev1$cluster)
table(Lev2$Vowel, results_Lev2$cluster)
table(Lev3$Vowel, results_Lev3$cluster)



ggplot(data = Vowel_Data_Final)+ 
       geom_point(mapping = aes (x = f2, y = -f1, color = Vowel))+
       facet_wrap(Level ~. )
