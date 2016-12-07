
# EXERCICE 1-----------------------------------------------------------------------------
#1.1.1
rm (list = ls())
ls()

#1.1.2
x <- seq ( from = 193, to = 297, by = (3.5) )

#1.1.3
summary (x)


#1.2 
#After saving the script with the name "SCRIPT1_G8.R", for instance:

#1.2.1 From RStudio:

  #Using RStudio, under File menu, choose the Open File option, or press Ctrl+O.
  #It allows you to select the directory where the file is and load it into the
  #top left window. From there, you can select the specific lines you want to 
  #send to the console and, therefore, execute them.

#1.2.2 From an R session: 

   # source ("SCRIPT1_G8.R", echo = TRUE, max.deparse.length = 999999)
   # With echo = True we can see the lines after parsing.

#1.2.3 From the command line or console: 

   # R.exe -- vanilla < SCRIPT1_G8.R


#EXERCICE 2---------------------------------------------------------------------------

setwd("~/R-ex-1")
# We set the directory to R-ex-1, so that it can be run from the same directory
# from any other machine. It only works if the directory R-ex-1 is in Documents, 
# due to the fact that "~" leads to Documents. 
# If this doens't work, you can always set the Directory manually from Session,
# -> Set working directory -> choose directory. 

#2.1.
read.table ("d1.txt", header = TRUE)

#2.2.
read.table ("d2.txt", header = TRUE, sep = "\t")

#2.3. 
read.table ("d3.txt", sep = '\t')

#2.4. 
read.table ("d4.txt", header = TRUE, comment.char = '@')


# EXERCICE 3------------------------------------------------------------------------

#3.1. You can check your package version by looking the list of packages
# on the bottom right corner. Here, on the user library, you can see a
# description and the version
        # version number: 2.4.0

#3.2. You can check your package version by looking the list of packages
# on the bottom right corner. Here, on the user library, you can see a
# description and the version
        #version number: 2.1-3

#3.3. Installing the package (install.package("OncoSimulR")) is not enough;
# you have to "call" the function to this session by using library('OncoSimulR')


#EXERCICE 4------------------------------------------------------------------------------

#4.1. The only output you get is "character(0)"

#4.2. This links to the function scatter3d (inside car package) help: 
# Three-Dimensional Scatterplots and Point Identification
    # Description,
    # Usage
    # Value
    # Arguments
    # Note
    # Author(s)
    # References
    # See Also
    # Examples

#4.3. The output is different from the one in 4.1: [1] "scatter3d"

#4.4. Before loading the car package, apropos couldn't find any function named
# "scatter3d", therefore the vector returned is empty (you get "character(0)". 
# However, after loading the car package, apropos finds the requested function
# and returns one element inside the vector.

#4.5. apropos() returns a vector that contains the names of the functions 
# which have a match with the string "scatterd3d". 
# However, help.search() looks for the same string in the whole body of the 
# help pages.

#4.6. If you want to find functions with "scatter" in their names, apropos 
# is much more useful. 
# In this example, apropos returns a vector of length = 6, but help.search 
# returns a series of many more links and gives you more information 
# about the functions, so sometimes it could be really useful.
# Yes, you can miss it, as in this example we just made. Before having loaded
# the car package,  apropos couldn't find scatter3d function, even though it 
# was already installed.

#4.7. Yes, help.search finds functions with "scatter" in their names, 
# regardless of their packages being loaded. In order to show only those
# functions with the query word in their names, fields = "name" has to be
# specified. If not, it will search in all the description.


#EXERCICE 5---------------------------------------------------------------------------

#5.1. 

x <- 97
y <- 95
save (x, file = "oneObject.RData")

#5.2. save.image() function would have created a binary file with the whole
# working environment (in this case, it would have saved the "x" object as 
# well as "y" object). In fact, if no file name would have been especified, 
# this binary file would simply be ".RData": a hidden file that could be 
# loaded during the next R session by default.


# EXERCICE 6--------------------------------------------------------------------------

X <- read.table("AnotherDataSet.txt")
hr <- c (87, 78, 86, 62, 69, 69, 68, 67, 75, 76)
hr

#6.1
age <- rep (c (11, 63, 40, 47), c(3, 2, 4, 1))
age

#6.2
condition1 <- (age < 45)
hr[condition1]

#6.3
data <- hr [c (age == 63)| (age == 47)]     
names <- c ("Juan", "Ana", "Carmen")
hr2 <- c ("Juan" = data[1], "Ana" = data[2], "Carmen" = data[3])
hr2

#6.4
z <- c (hr2["Juan"], hr2["Ana"])
z

#6.5
y <- (age == 63)| (age == 47)
Results_matrix <- cbind (hr2, age[y])
colnames (Results_matrix) <- c ("HR", "Age")
Results_matrix

#6.6
(Results_data_frame <- data.frame (HR = c(hr2), Age = c(age[y])))

#6.7
(Results_data_frame2 <- data.frame(Name = names(hr2), HR = c(hr2), 
                        Age = c(age[y]), row.names = NULL))

# We could do the same with a matrix: 

Results_Matrix2 <- cbind (c (names(hr2) ), hr2, age[y] )
colnames(Results_Matrix2) <- c("Names", "HR", "Age")
row.names (Results_Matrix2) <- NULL
Results_Matrix2

#6.8
#Combining indices and row names
Results_matrix [1, 1]
Results_matrix ["Juan", "HR"]
Results_matrix ["Juan", 1]
Results_matrix [1, "HR"]

#6.9
#Using indices
Results_matrix ["Juan",]
#Using row names
Results_matrix [1, ]

#6.10
Results_data_frame ["Ana", "HR"]
Results_data_frame [2, 1]
Results_data_frame ["Ana", 1]
Results_data_frame [2, "HR"]

#6.11
Results_data_frame2 [2, "HR"]
Results_data_frame2 ["2", "HR"]
Results_data_frame2 [2, 2]
Results_data_frame2 ["2", 2]

#6.12
Results_data_frame2 ["2", ]
Results_data_frame2 [2, ]


#6.13
Results_data_frame2 [which (Results_data_frame2[ , 3] > 60), ]


#6.14
Results_data_frame[which (Results_data_frame[ , 2] > 60), ]

#6.15
Matrix_all <- cbind (hr, age)
(Matrix_older_15 <- Matrix_all [which (Matrix_all[ ,2] > 15), ])

#6.16
sex <- c("M", "F")[c(1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1)]
# In this case, we have 11 data for sex, but only 10 individuals. 
# If we consider that the last one is the spare one, those sexes
# could perfectly correspond to the individuals above: 
    # Juan: M
    # Ana: F
    # Carmen: F
# As the vector sex is 1 element longer than hr and age, it returns
# a Warning Message. However, it uses the recycling rule and also returns
# the matrix. 
Matrix_Sex <-  cbind(hr, age, sex)
Matrix_NameSex <- cbind ((Matrix_Sex [which ( Matrix_Sex [ ,2] > 40 ), ]),
                         names)
colnames(Matrix_NameSex) <- c("HR", "Age", "Sex", "Names")
Matrix_NameSex
#Prints a matrix with sex and names in order to see if they match.

#6.17
# To do this exercice, we created the vector sex2, which only has 
# 10 elements (we deleted the last one). We will work with this vector
# from now on, instead of sex. 

sex2 <- c("M", "F")[c(1, 2, 1, 1, 2, 2, 1, 1, 2, 2)]

Matrix_older_15v2 <- cbind (Matrix_older_15, cbind (age, sex2) 
                            [ which(age > 15), 2])
colnames(Matrix_older_15v2) <- c("HR", "Age", "Sex")
Matrix_older_15v2


#6.18 
Data_frame_Final <- cbind (Results_data_frame, 
                           Sex = cbind (age, sex2)[(age == 63) | (age == 47), 2])
Data_frame_Final


# EXERCICE 7-------------------------------------------------------------------------
Matrix_ordered <- Matrix_older_15 [order (Matrix_older_15[ , 2],
                                        Matrix_older_15[ , 1]), ]
colnames(Matrix_ordered) <- c("HR", "Age")
Matrix_ordered

# In this case, we use order. 
# Order returns a permutation which rearranges its first argument into 
# ascending or descending order, breaking ties by further arguments.
# As we wan it to be sorted by age, and secondly by HR, we firstly write
# the argument age, and secondly the argument HR. 
# This way, it will show the youngest individuals on top and, for people
# with the same age, it will show the one with the slowest heart rate on top. 

