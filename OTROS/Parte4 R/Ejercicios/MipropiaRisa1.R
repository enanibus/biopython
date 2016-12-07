##Ejercicio 5
x <- 97
y <- 95
save(x, file = "oneObject.RData")
#with save.image() we would have saved the whole objects in the global env.
load("oneObject.RData")

##Ejercicio 6
hr <- c(87, 78, 86, 62, 69, 69, 68, 67, 75, 76)
age <- rep(c(11, 63, 40, 47), times = c(3, 2, 4, 1))
hr45 <- hr[(age < 45)]
hr2 <- c(Juan = hr[age == 63][1], 
         Ana = hr[age == 63][2], Carmen = hr[age == 47][3])
