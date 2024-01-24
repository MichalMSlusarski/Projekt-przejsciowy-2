### Użyte biblioteki

library(tidyverse)
library(ggplot2)
library(ggpubr)
library(knitr)

## Załadowanie pliku i sprawdzenie reczne korelacji

site_db <- read.csv("C:/Users/mikdo/Downloads/lighthouse-output-full.csv")

kor_perf_av <- cor.test(site_db$average_position, site_db$performance_score, method = "pearson")
kor_best_av <- cor.test(site_db$average_position, site_db$best_practices_score, method = "pearson")
kor_acc_av <- cor.test(site_db$average_position, site_db$accessibility_score, method = "pearson")
kor_seo_av <- cor.test(site_db$average_position, site_db$seo_score, method = "pearson")

kor_perf_we <- cor.test(site_db$weighted_position, site_db$performance_score, method = "pearson")
kor_best_we <- cor.test(site_db$weighted_position, site_db$best_practices_score, method = "pearson")
kor_acc_we <- cor.test(site_db$weighted_position, site_db$accessibility_score, method = "pearson")
kor_seo_we <- cor.test(site_db$weighted_position, site_db$seo_score, method = "pearson")

## stworzenie wykresów
av1 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = performance_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = average_position, y = performance_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.60"),x=50,y=0.4,size=4)

av1.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = performance_score)) +
  geom_smooth(mapping = aes(x = average_position, y = performance_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.60"),x=50,y=0.4,size=4)

av2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = best_practices_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = average_position, y = best_practices_score)) +
  annotate(geom="text",label=("R = -0.19 p = 0.04451"),x=50,y=0.5,size=4)

av2.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = best_practices_score)) +
  geom_smooth(mapping = aes(x = average_position, y = best_practices_score)) +
  annotate(geom="text",label=("R = -0.19 p = 0.04451"),x=50,y=0.5,size=4)

av3 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = accessibility_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = average_position, y = accessibility_score)) +
  annotate(geom="text",label=("R = -0.091 p = 0.3389"),x=50,y=0.5,size=4)

av3.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = accessibility_score)) +
  geom_smooth(mapping = aes(x = average_position, y = accessibility_score)) +
  annotate(geom="text",label=("R = -0.091 p = 0.3389"),x=50,y=0.5,size=4)


av4 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = seo_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = average_position, y = seo_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.6"),x=50,y=0.5,size=4)

av4.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = average_position, y = seo_score)) +
  geom_smooth(mapping = aes(x = average_position, y = seo_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.6"),x=50,y=0.5,size=4)

we1 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = performance_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = weighted_position, y = performance_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.60"),x=50,y=0.4,size=4) +
  coord_cartesian(xlim = c(1, 300))

we1.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = performance_score)) +
  geom_smooth(mapping = aes(x = weighted_position, y = performance_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.60"),x=50,y=0.4,size=4) +
  coord_cartesian(xlim = c(1, 300))

we2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = best_practices_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = weighted_position, y = best_practices_score)) +
  annotate(geom="text",label=("R = -0.19 p = 0.04451"),x=50,y=0.5,size=4) +
  coord_cartesian(xlim = c(1, 300))

we2.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = best_practices_score)) +
  geom_smooth(mapping = aes(x = weighted_position, y = best_practices_score)) +
  annotate(geom="text",label=("R = -0.19 p = 0.04451"),x=50,y=0.5,size=4) +
  coord_cartesian(xlim = c(1, 300))

we3 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = accessibility_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = weighted_position, y = accessibility_score)) +
  annotate(geom="text",label=("R = -0.091 p = 0.3389"),x=50,y=0.5,size=4) +
  coord_cartesian(xlim = c(1, 300))

we3.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = accessibility_score)) +
  geom_smooth(mapping = aes(x = weighted_position, y = accessibility_score)) +
  annotate(geom="text",label=("R = -0.091 p = 0.3389"),x=50,y=0.5,size=4) +
  coord_cartesian(xlim = c(1, 300))

we4 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = seo_score)) +
  geom_smooth(method = 'lm', mapping = aes(x = weighted_position, y = seo_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.6"),x=50,y=0.5,size=4) +
  coord_cartesian(xlim = c(1, 300))

we4.2 <- ggplot(data = site_db) +
  geom_point(mapping = aes(x = weighted_position, y = seo_score)) +
  geom_smooth(mapping = aes(x = weighted_position, y = seo_score)) +
  annotate(geom="text",label=("R = -0.05 p = 0.6"),x=50,y=0.5,size=4) +
  coord_cartesian(xlim = c(1, 300))

info <- data.frame(
  Zmienna = c("Performance Score", "Best Practises", "Accessibility Score", "Seo Score"),
  Average_Position = c("p = 0.6", "p = 0.04", "p = 0.33", "p = 0.6"),
  Korelacja_zachodzi = c("NIE", "TAK", "NIE", "NIE"),
  Weighted_Position = c("p = 0.77", "p = 0.01", "p = 0.6", "p = 0.6"),
  Korelacja_zachodzi = c("NIE", "TAK", "NIE", "NIE")
)
kable(info)
