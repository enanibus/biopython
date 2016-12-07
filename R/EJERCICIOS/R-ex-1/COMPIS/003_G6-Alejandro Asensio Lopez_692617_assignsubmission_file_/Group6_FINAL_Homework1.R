## My_Group: Group6 (Alejandro Asensio, Marina Gonzalo, Mª Jose Jimenez, 
## Jaime Quesada)

## 1. Scripts

## 1.1 Creating the script

## ----------- 1.1.1 -----------

  rm(list = ls())

## ----------- 1.1.2 -----------

  x <- seq(123, 297, 3.5)

## ----------- 1.1.3 -----------

  summary(x)

## 1.2 Running the script

## ----------- 1.2.1 -----------

## First select the lines you want to run, then go to Code/Run Selected Line(s) 
## Keyboard shortcut is command + enter.

## ----------- 1.2.2 -----------

## First we have to save the current script in the same directory where R is 
## running. 
## For example, we will name our script "MyScript.R"
## Second, we open an R session and write:

  source("MyScript.R", echo = TRUE, max.deparse.length = 9999999999999)

## ----------- 1.2.3 -----------

## Operating System: Mac OS
## Enter the terminal and write 

                        R --vanilla < MyScript.R

## Make sure your current pathway is the directory where the script is. 
## Otherwise, write the complete pathway of the file, instead of only its name.

## ============================================================================

## 2. Some read.table operations

## ----------- 2.1 -----------

  read.table("d1.txt", header = TRUE)

## ----------- 2.2 -----------

  read.table("d2.txt", header = TRUE, sep = "\t", na.strings = " ")

## ----------- 2.3 -----------

  read.table("d3.txt", sep = "\t", na.strings = " ")

## ----------- 2.4 -----------

  read.table("d4.txt", header = TRUE, comment.char = "@")

## ============================================================================

## 3. Packages

## ----------- 3.1 -----------

## Version 2.4.0

## ----------- 3.2 -----------

## Version 2.1-3

## ----------- 3.3 -----------

## In addition to install the package, you have to load it. Then you can call 
## the function:

   library("OncoSimulR")
   oncoSimulIndiv(fp)
   
## You need the argument fp, which is either a poset or a fitnessEffects object

## ============================================================================
  
## 4. The help

## ----------- 4.1 -----------

## character(0)

## ----------- 4.2 -----------

## Help pages:
##             car::scatter3d		Three-Dimensional Scatterplots and Point 
## Identification

## ----------- 4.3 -----------

## > apropos("scatter3d")
## [1] "scatter3d"

## > help.search("scatter3d")
## Help pages:
##             car::scatter3d		Three-Dimensional Scatterplots and Point 
## Identification

## ----------- 4.4 -----------

## apropos("something") is a function that returns a character vector giving 
## the names of all functions matching "something". 

## Before loading the package car there was no function called "scatter3d", so 
## apropos("scatter3d") return an empty vector. The car package includes the 
## fuction scatter3d(), so after loading this package, the expression 
## apropos("scatter3d") return a vector with one element: the name of this 
## fuction.

## ----------- 4.5 -----------

## apropos() returns a vector with all the fuctions in the current R session 
## that contain the given argument as part of their names, while help.search() 
## returns all functions (including those that are part of packages installed 
## in your library) that contain the given argument as part of their names, 
## alias (if specified), title or concept.
   
## ----------- 4.6 -----------
   
## apropos("scatter") is more helpful, because it returns less matches. 
## Nevertheless, if you only use apropos("scatter") you may miss functions that 
## contain scatter in their names, that are installed in your library but that 
## have not been imported to the current R session. 
## The solution for this problem is use help.search("scatter").
   
## ----------- 4.7 -----------

## By default, the fields argument of help.search() function is a vector 
## containing "name", "concept" and "title", so it will return all the fuctions
## with the given argument in its concept, name or title. If we wont only the 
## functions that contain "scatter3d" in its name, we should write:
   
   help.search("scatter3d", fields = "name")
   
## ============================================================================
## 5. Saving objects

## ----------- 5.1 -----------

x <- 97
y <- 95
save(x, file = "oneObject.RData")

## ----------- 5.2 -----------

## save.image(file = "oneObject.RData") would have saved x and y

## ============================================================================
## 6. Vectors, data frames, etc.

hr <- c(87, 78, 86, 62, 69, 69, 68, 67, 75, 76)

## ----------- 6.1 -----------

age <- c(rep(c(11, 63, 40, 47), c(3, 2, 4, 1)))

## ----------- 6.2 -----------

hr[age < 45]

## ----------- 6.3 -----------

hr2 <- c("Juan" = hr[age == 63][1] , "Ana" = hr[age == 63][2] , 
         "Carmen" = hr[age == 47])

## ----------- 6.4 -----------

hr2["Juan"]; hr2["Ana"]

## ----------- 6.5 -----------

The_Matrix <- matrix(data = c(hr2, c(age[age == 63 | age == 47])), nrow = 3, 
                     ncol = 2, dimnames = list(names(hr2)))
## ----------- 6.6 -----------

Data_Frame <- data.frame(HeartRate = hr2, Age = c(age[age == 63 | age == 47]))

## ----------- 6.7 -----------

Data_Frame_Names <- data.frame(HeartRate = hr2, 
                               Age = c(age[age == 63 | age == 47]),
                               Name = names(hr2))
## ----------- 6.8 -----------

The_Matrix["Juan", 1]

## ----------- 6.9 -----------

The_Matrix["Juan", ]

## ----------- 6.10 -----------

Data_Frame["Ana", "HeartRate"]

## ----------- 6.11 -----------

Data_Frame_Names[2, 1]

## ----------- 6.12 -----------

Data_Frame_Names["Ana", ]

## ----------- 6.13 -----------

y <- which(Data_Frame_Names[ , "Age"] > 60)
New_Data_Frame_Names <- data.frame(Age = Data_Frame_Names[y, "Age"])

## ----------- 6.14 -----------

x <- which(Data_Frame[, "Age"] > 60)
New_Data_Frame <- data.frame(Age = Data_Frame[x, "Age"])

## ----------- 6.15 -----------

All_People_Matrix <- matrix(data = c(hr, age), nrow = 10, ncol = 2)
Older_Than_15 <- which(All_People_Matrix[ , 2] > 15)
HeartRates_And_Ages <- matrix(data = All_People_Matrix [Older_Than_15, ], 
                              ncol = 2, nrow = length(Older_Than_15))

## ----------- 6.16 -----------

## The length of the sex vector is longer than the number of subjects. We can 
## think that the last value is an error and eliminate it. In this situation, 
## those sexes can correspond to the subjects, since the sexes of Juan, Ana 
## and Carmen are correct.

## ----------- 6.17 -----------

sex1 <- c("M", "F")[c(2, 2, 1, 1, 2, 2, 1)]
combined_matrix <- cbind(HeartRates_And_Ages, sex1)



## ----------- 6.18 -----------

Sex <-  c("M", "F")[c(1, 2, 1)]
Combined_data_frame <- cbind(Data_Frame, Sex)




## ============================================================================
## 7. Sort and order
## ----------- 7.1 -----------
## CHECK ALL THE VARIABLES IN EXERCISE 6.15!!
## We establish the specific order of the numbers in the age column, in order 
## to apply it to the hr column.
Correct_Order <- order(HeartRates_And_Ages[,2])

## We define the hr column.
MyHRColumn <- All_People_Matrix [Older_Than_15, ][,1]

## We apply the order of the age column to the hr one.
MyData <- c(MyHRColumn[Correct_Order[1]], MyHRColumn[Correct_Order[2]], 
            MyHRColumn[Correct_Order[3]], MyHRColumn[Correct_Order[4]],
            MyHRColumn[Correct_Order[5]], MyHRColumn[Correct_Order[6]],
            MyHRColumn[Correct_Order[7]])

## Since we have 4 people that are 40 years old, we order the first 4 numbers
## in the hr column.
MyDataOrdered <- sort(MyData[1:4])

## And now this is the final data of the hr column.
MyDataFinal <- c(MyDataOrdered, MyData[5:7])

## We just create the matrix and it is done!
New_HeartRates_And_Ages <- 
  matrix(data = c(MyDataFinal, sort(HeartRates_And_Ages[,2])),
         ncol = 2, nrow = length(Older_Than_15))

